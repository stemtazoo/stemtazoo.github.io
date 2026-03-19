#!/usr/bin/env python3
"""Build versioned skill-check datasets from the official XLSX source.

Outputs:
- data/skillcheck/versions/<version>/skillcheck.csv                     (normalized canonical table)
- data/skillcheck/versions/<version>/skillcheck.json                    (same rows in JSON)
- data/skillcheck/versions/<version>/skilllevel_definition_2023.csv     (raw skill-level table)
- data/skillcheck/versions/<version>/skilllevel_definition_2023.json    (same rows in JSON)
- data/skillcheck/exports/latest.json                                   (latest-version alias)
- data/skillcheck/exports/skilllevel_definition_2023_latest.json        (latest skill-level alias)
- data/skillcheck/exports/index.json                                    (version manifest)
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile

DEFAULT_SOURCE_URL = "https://www.datascientist.or.jp/common/docs/skillcheck_ver5.00_simple.xlsx"
ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = ROOT / "data" / "skillcheck"
RAW_DIR = DATA_ROOT / "raw"
VERSIONS_DIR = DATA_ROOT / "versions"
EXPORTS_DIR = DATA_ROOT / "exports"
TARGET_SKILLCHECK_SHEETS = [
    "ビジネス力",
    "データサイエンス力",
    "データエンジニアリング力",
    "AI利活用スキル",
]
SHEET_SLUGS = {
    "ビジネス力": "business",
    "データサイエンス力": "datascience",
    "データエンジニアリング力": "dataengineering",
    "AI利活用スキル": "ai",
    "スキルレベル定義2023": "skilllevel-definition-2023",
}
SKILLLEVEL_SHEET = "スキルレベル定義2023"
HEADER_ROW_INDEX = 2
DATA_START_ROW_INDEX = 3

N = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pkg": "http://schemas.openxmlformats.org/package/2006/relationships",
}

CANONICAL_COLUMNS = [
    "version",
    "sheet",
    "section",
    "category",
    "subcategory",
    "item_id",
    "item",
    "notes",
    "source_url",
]


@dataclass
class Row:
    version: str
    sheet: str
    section: str
    category: str
    subcategory: str
    item_id: str
    item: str
    notes: str
    source_url: str

    def as_dict(self) -> dict[str, str]:
        return {
            "version": self.version,
            "sheet": self.sheet,
            "section": self.section,
            "category": self.category,
            "subcategory": self.subcategory,
            "item_id": self.item_id,
            "item": self.item,
            "notes": self.notes,
            "source_url": self.source_url,
        }


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-._]", "", text)
    return text or "unknown"


def normalize_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return re.sub(r"\s+", " ", value).strip()
    return str(value).strip()


def infer_version(path_or_url: str, override: str | None = None) -> str:
    if override:
        return override
    m = re.search(r"ver([0-9]+(?:\.[0-9]+)*)", path_or_url, re.IGNORECASE)
    if m:
        return m.group(1)
    return "unknown"


def download_if_needed(source_url: str, out_path: Path) -> Path:
    if out_path.exists():
        return out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(source_url) as r:
            out_path.write_bytes(r.read())
    except Exception as e:
        raise SystemExit(
            f"Failed to download source xlsx: {source_url}. "
            "You can download it manually and run with --xlsx <path>. "
            f"details={e}"
        ) from e
    return out_path


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def col_index(cell_ref: str) -> int:
    letters = re.match(r"([A-Z]+)", cell_ref)
    if not letters:
        return 0
    s = letters.group(1)
    n = 0
    for ch in s:
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n - 1


def parse_shared_strings(zf: ZipFile) -> list[str]:
    name = "xl/sharedStrings.xml"
    if name not in zf.namelist():
        return []
    root = ET.fromstring(zf.read(name))
    out: list[str] = []
    for si in root.findall("main:si", N):
        texts = [t.text or "" for t in si.findall(".//main:t", N)]
        out.append(normalize_text("".join(texts)))
    return out


def workbook_sheets(zf: ZipFile) -> list[tuple[str, str]]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))

    rel_map: dict[str, str] = {}
    for rel in rels.findall("pkg:Relationship", N):
        rid = rel.get("Id")
        target = rel.get("Target")
        if rid and target:
            rel_map[rid] = target.lstrip("/")

    out: list[tuple[str, str]] = []
    for sh in wb.findall("main:sheets/main:sheet", N):
        name = sh.get("name") or "sheet"
        rid = sh.get(f"{{{N['rel']}}}id")
        if not rid or rid not in rel_map:
            continue
        target = rel_map[rid]
        if not target.startswith("xl/"):
            target = f"xl/{target}"
        out.append((name, target))
    return out


def sheet_rows(zf: ZipFile, sheet_path: str, shared: list[str]) -> list[list[str]]:
    root = ET.fromstring(zf.read(sheet_path))
    rows: list[list[str]] = []

    for row in root.findall("main:sheetData/main:row", N):
        cells: dict[int, str] = {}
        for c in row.findall("main:c", N):
            ref = c.get("r", "A1")
            idx = col_index(ref)
            cell_type = c.get("t")

            v = c.find("main:v", N)
            is_node = c.find("main:is", N)
            raw = ""
            if cell_type == "s" and v is not None and v.text is not None:
                si = int(v.text)
                raw = shared[si] if 0 <= si < len(shared) else ""
            elif cell_type == "inlineStr" and is_node is not None:
                parts = [t.text or "" for t in is_node.findall(".//main:t", N)]
                raw = "".join(parts)
            elif v is not None and v.text is not None:
                raw = v.text
            cells[idx] = normalize_text(raw)

        if not cells:
            rows.append([])
            continue

        max_idx = max(cells)
        ordered = [cells.get(i, "") for i in range(max_idx + 1)]
        rows.append(ordered)

    return rows


def trim_trailing_empty(values: list[str]) -> list[str]:
    trimmed = list(values)
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    return trimmed


def normalize_headers(values: list[str]) -> list[str]:
    headers: list[str] = []
    for idx, value in enumerate(values, start=1):
        header = normalize_text(value)
        headers.append(header or f"column_{idx}")
    return trim_trailing_empty(headers)


def row_to_record(headers: list[str], values: list[str], *, version: str, source_url: str, sheet_name: str) -> dict[str, str]:
    padded = list(values) + [""] * max(0, len(headers) - len(values))
    record = {header: normalize_text(padded[idx]) for idx, header in enumerate(headers)}
    record["version"] = version
    record["sheet"] = sheet_name
    record["source_url"] = source_url
    return record


def notes_from_record(record: dict[str, str], headers: list[str]) -> str:
    parts = [f"{header}: {record[header]}" for header in headers if record.get(header)]
    return " | ".join(parts)


def extract_skillcheck_rows(rows: list[list[str]], sheet_name: str, version: str, source_url: str) -> list[Row]:
    if len(rows) <= HEADER_ROW_INDEX:
        return []

    headers = normalize_headers(rows[HEADER_ROW_INDEX])
    out: list[Row] = []
    item_seq = 0

    for cells in rows[DATA_START_ROW_INDEX:]:
        values = trim_trailing_empty(cells)
        if not any(values):
            continue

        record = row_to_record(headers, values, version=version, source_url=source_url, sheet_name=sheet_name)
        item_text = record.get("チェック項目", "")
        if not item_text:
            continue

        item_seq += 1
        category = record.get("スキルカテゴリ", "")
        if sheet_name == "データエンジニアリング力":
            subcategory = record.get("サブカテゴリ", "")
        elif sheet_name == "AI利活用スキル":
            subcategory = record.get("AI区分 LLM、Diffusion、両方", "")
        else:
            subcategory = record.get("サブカテゴリ", "")

        out.append(
            Row(
                version=version,
                sheet=sheet_name,
                section="",
                category=category,
                subcategory=subcategory,
                item_id=f"{SHEET_SLUGS.get(sheet_name, slugify(sheet_name))}-{item_seq:04d}",
                item=item_text,
                notes=notes_from_record(record, headers),
                source_url=source_url,
            )
        )

    return out


def extract_skilllevel_rows(rows: list[list[str]], sheet_name: str, version: str, source_url: str) -> list[dict[str, str]]:
    if len(rows) <= HEADER_ROW_INDEX:
        return []
    headers = normalize_headers(rows[HEADER_ROW_INDEX])
    out: list[dict[str, str]] = []
    for cells in rows[DATA_START_ROW_INDEX:]:
        values = trim_trailing_empty(cells)
        if not any(values):
            continue
        out.append(row_to_record(headers, values, version=version, source_url=source_url, sheet_name=sheet_name))
    return out


def enumerate_workbook_data(xlsx_path: Path, version: str, source_url: str) -> tuple[list[Row], list[dict[str, str]]]:
    skillcheck_rows: list[Row] = []
    skilllevel_rows: list[dict[str, str]] = []

    with ZipFile(xlsx_path) as zf:
        shared = parse_shared_strings(zf)
        for sheet_name, sheet_path in workbook_sheets(zf):
            if sheet_name not in TARGET_SKILLCHECK_SHEETS and sheet_name != SKILLLEVEL_SHEET:
                continue
            rows = sheet_rows(zf, sheet_path, shared)
            if sheet_name in TARGET_SKILLCHECK_SHEETS:
                skillcheck_rows.extend(extract_skillcheck_rows(rows, sheet_name, version, source_url))
            elif sheet_name == SKILLLEVEL_SHEET:
                skilllevel_rows.extend(extract_skilllevel_rows(rows, sheet_name, version, source_url))

    return skillcheck_rows, skilllevel_rows


def write_csv(path: Path, rows: list[Row]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CANONICAL_COLUMNS)
        writer.writeheader()
        for r in rows:
            writer.writerow(r.as_dict())


def write_json(path: Path, rows: list[Row]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [r.as_dict() for r in rows]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_records_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_records_json(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_manifest(version: str, source_url: str, raw_file: Path, row_count: int, skilllevel_row_count: int) -> None:
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = EXPORTS_DIR / "index.json"
    existing: dict[str, object] = {"versions": []}
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))

    versions = existing.get("versions", [])
    if not isinstance(versions, list):
        versions = []

    entry = {
        "version": version,
        "source_url": source_url,
        "raw_file": str(raw_file.relative_to(ROOT)),
        "sha256": digest_file(raw_file),
        "rows": row_count,
        "skilllevel_rows": skilllevel_row_count,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    versions = [v for v in versions if isinstance(v, dict) and v.get("version") != version]
    versions.append(entry)
    versions.sort(key=lambda v: str(v.get("version", "")))

    out = {"latest": version, "versions": versions}
    manifest_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-url", default=DEFAULT_SOURCE_URL)
    parser.add_argument("--xlsx", help="Use local xlsx file path")
    parser.add_argument("--version", help="Override version, e.g. 5.00")
    parser.add_argument("--min-rows", type=int, default=20)
    args = parser.parse_args()

    version = infer_version(args.xlsx or args.source_url, override=args.version)

    if args.xlsx:
        xlsx_path = Path(args.xlsx).resolve()
        if not xlsx_path.exists():
            raise SystemExit(f"xlsx not found: {xlsx_path}")
        source_url = args.source_url
    else:
        filename = Path(args.source_url).name
        xlsx_path = RAW_DIR / filename
        source_url = args.source_url
        download_if_needed(source_url, xlsx_path)

    rows, skilllevel_rows = enumerate_workbook_data(xlsx_path=xlsx_path, version=version, source_url=source_url)
    if len(rows) < args.min_rows:
        raise SystemExit(f"Parsed rows too small: {len(rows)} (min {args.min_rows})")

    version_dir = VERSIONS_DIR / version
    csv_path = version_dir / "skillcheck.csv"
    json_path = version_dir / "skillcheck.json"
    skilllevel_csv_path = version_dir / "skilllevel_definition_2023.csv"
    skilllevel_json_path = version_dir / "skilllevel_definition_2023.json"
    latest_path = EXPORTS_DIR / "latest.json"
    skilllevel_latest_path = EXPORTS_DIR / "skilllevel_definition_2023_latest.json"

    write_csv(csv_path, rows)
    write_json(json_path, rows)
    write_json(latest_path, rows)
    write_records_csv(skilllevel_csv_path, skilllevel_rows)
    write_records_json(skilllevel_json_path, skilllevel_rows)
    write_records_json(skilllevel_latest_path, skilllevel_rows)
    update_manifest(version, source_url, xlsx_path, len(rows), len(skilllevel_rows))

    print(f"Generated: {csv_path.relative_to(ROOT)}")
    print(f"Generated: {json_path.relative_to(ROOT)}")
    print(f"Generated: {skilllevel_csv_path.relative_to(ROOT)}")
    print(f"Generated: {skilllevel_json_path.relative_to(ROOT)}")
    print(f"Generated: {latest_path.relative_to(ROOT)}")
    print(f"Generated: {skilllevel_latest_path.relative_to(ROOT)}")
    print(f"Rows: {len(rows)}")
    print(f"Skill level rows: {len(skilllevel_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
