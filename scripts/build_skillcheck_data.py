#!/usr/bin/env python3
"""Build versioned skill-check datasets from the official XLSX source.

ver.6 is normalized to one row per skill level. The value-creation sheet stores
three level descriptions in one source row, so it is expanded to three canonical
rows. ver.5 remains supported for reproducibility.

Outputs:
- data/skillcheck/versions/<version>/skillcheck.csv
- data/skillcheck/versions/<version>/skillcheck.json
- data/skillcheck/versions/<version>/exam_star1.json
- data/skillcheck/versions/<version>/skilllevel_definition_<year>.csv/json
- data/skillcheck/versions/<version>/change_mapping_*.csv/json (when present)
- data/skillcheck/exports/latest.json
- data/skillcheck/exports/exam_star1_latest.json
- data/skillcheck/exports/skilllevel_definition_latest.json
- data/skillcheck/exports/index.json
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

DEFAULT_SOURCE_URL = "https://www.datascientist.or.jp/common/docs/skillcheck_ver6.00.xlsx"
ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = ROOT / "data" / "skillcheck"
RAW_DIR = DATA_ROOT / "raw"
VERSIONS_DIR = DATA_ROOT / "versions"
EXPORTS_DIR = DATA_ROOT / "exports"

VER6_SHEETS = ["基盤", "価値創造力", "データサイエンス力", "データエンジニアリング力", "融合"]
VER5_SHEETS = ["ビジネス力", "データサイエンス力", "データエンジニアリング力", "AI利活用スキル"]
AREA_MAP = {
    "基盤": "foundation",
    "価値創造力": "value-creation",
    "データサイエンス力": "datascience",
    "データエンジニアリング力": "dataengineering",
    "融合": "fusion",
    "ビジネス力": "business",
    "AI利活用スキル": "ai-utilization",
}
SHEET_SLUGS = {
    "基盤": "foundation",
    "価値創造力": "value-creation",
    "データサイエンス力": "datascience",
    "データエンジニアリング力": "dataengineering",
    "融合": "fusion",
    "ビジネス力": "business",
    "AI利活用スキル": "ai",
}
VALID_LEVELS = {"★": 1, "★★": 2, "★★★": 3}

N = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pkg": "http://schemas.openxmlformats.org/package/2006/relationships",
}

CANONICAL_COLUMNS = [
    "version", "area", "sheet", "no", "subno", "phase", "section",
    "category", "subcategory", "skill_level", "skill_level_rank",
    "vc", "ds", "de", "bz", "required_skill", "old_division",
    "skill_definition", "ai_utilization", "ai_utilization_type",
    "ai_category", "item_id", "item", "notes", "source_url",
]


@dataclass
class Row:
    version: str
    area: str
    sheet: str
    no: str
    subno: str
    phase: str
    section: str
    category: str
    subcategory: str
    skill_level: str
    skill_level_rank: str
    vc: str
    ds: str
    de: str
    bz: str
    required_skill: str
    old_division: str
    skill_definition: str
    ai_utilization: str
    ai_utilization_type: str
    ai_category: str
    item_id: str
    item: str
    notes: str
    source_url: str

    def as_dict(self) -> dict[str, str]:
        return {name: getattr(self, name) for name in CANONICAL_COLUMNS}


def normalize_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return re.sub(r"\s+", " ", value).strip()
    return str(value).strip()


def compact_key(value: str) -> str:
    return re.sub(r"\s+", "", normalize_text(value)).lower()


def record_get(record: dict[str, str], *keys: str) -> str:
    wanted = {compact_key(k) for k in keys}
    for key, value in record.items():
        if compact_key(key) in wanted:
            return normalize_text(value)
    return ""


def infer_version(path_or_url: str, override: str | None = None) -> str:
    if override:
        return override
    m = re.search(r"ver([0-9]+(?:\.[0-9]+)*)", path_or_url, re.IGNORECASE)
    return m.group(1) if m else "unknown"


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
    m = re.match(r"([A-Z]+)", cell_ref)
    if not m:
        return 0
    n = 0
    for ch in m.group(1):
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n - 1


def parse_shared_strings(zf: ZipFile) -> list[str]:
    name = "xl/sharedStrings.xml"
    if name not in zf.namelist():
        return []
    root = ET.fromstring(zf.read(name))
    out = []
    for si in root.findall("main:si", N):
        # Exclude phonetic guide runs (rPh). Collect only visible text/rich-text.
        parts = []
        direct = si.find("main:t", N)
        if direct is not None:
            parts.append(direct.text or "")
        for run in si.findall("main:r", N):
            t = run.find("main:t", N)
            if t is not None:
                parts.append(t.text or "")
        out.append(normalize_text("".join(parts)))
    return out


def workbook_sheets(zf: ZipFile) -> list[tuple[str, str]]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_map = {}
    for rel in rels.findall("pkg:Relationship", N):
        rid, target = rel.get("Id"), rel.get("Target")
        if rid and target:
            rel_map[rid] = target.lstrip("/")
    out = []
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
    rows = []
    for row in root.findall("main:sheetData/main:row", N):
        cells: dict[int, str] = {}
        for c in row.findall("main:c", N):
            idx = col_index(c.get("r", "A1"))
            cell_type = c.get("t")
            v = c.find("main:v", N)
            is_node = c.find("main:is", N)
            raw = ""
            if cell_type == "s" and v is not None and v.text is not None:
                si = int(v.text)
                raw = shared[si] if 0 <= si < len(shared) else ""
            elif cell_type == "inlineStr" and is_node is not None:
                parts = []
                direct = is_node.find("main:t", N)
                if direct is not None:
                    parts.append(direct.text or "")
                for run in is_node.findall("main:r", N):
                    t = run.find("main:t", N)
                    if t is not None:
                        parts.append(t.text or "")
                raw = "".join(parts)
            elif v is not None and v.text is not None:
                raw = v.text
            cells[idx] = normalize_text(raw)
        if not cells:
            rows.append([])
        else:
            rows.append([cells.get(i, "") for i in range(max(cells) + 1)])
    return rows


def trim(values: list[str]) -> list[str]:
    out = list(values)
    while out and not out[-1]:
        out.pop()
    return out


def normalize_headers(values: list[str]) -> list[str]:
    headers = [normalize_text(v) or f"column_{i+1}" for i, v in enumerate(values)]
    return trim(headers)


def row_to_record(headers: list[str], values: list[str]) -> dict[str, str]:
    padded = list(values) + [""] * max(0, len(headers) - len(values))
    return {header: normalize_text(padded[i]) for i, header in enumerate(headers)}


def notes_from_record(record: dict[str, str], headers: list[str], exclude: set[str] | None = None) -> str:
    exclude = {compact_key(x) for x in (exclude or set())}
    parts = []
    for header in headers:
        if compact_key(header) in exclude:
            continue
        value = record.get(header, "")
        if value:
            parts.append(f"{header}: {value}")
    return " | ".join(parts)


def find_header_row(rows: list[list[str]], required_headers: set[str]) -> tuple[int, list[str]]:
    wanted = {compact_key(x) for x in required_headers}
    for idx, cells in enumerate(rows[:12]):
        headers = normalize_headers(cells)
        compact = {compact_key(h) for h in headers}
        if wanted.issubset(compact):
            return idx, headers
    raise ValueError(f"header row not found; required={sorted(required_headers)}")


def make_row(
    *, record: dict[str, str], headers: list[str], sheet_name: str,
    version: str, source_url: str, item_id: str, skill_level: str,
    item: str, required: str = "", skill_definition: str = "",
) -> Row:
    area = AREA_MAP.get(sheet_name, "")
    return Row(
        version=version,
        area=area,
        sheet=sheet_name,
        no=record_get(record, "No", "NO"),
        subno=record_get(record, "SubNo", "Sub No", "SubN", "SubNo."),
        phase=record_get(record, "フェーズ"),
        section=record_get(record, "分類"),
        category=record_get(record, "スキルカテゴリ"),
        subcategory=record_get(record, "サブカテゴリ"),
        skill_level=skill_level,
        skill_level_rank=str(VALID_LEVELS.get(skill_level, "")),
        vc=record_get(record, "VC"),
        ds=record_get(record, "DS"),
        de=record_get(record, "DE"),
        bz=record_get(record, "BZ"),
        required_skill=required or record_get(record, "必須スキル", "必須 スキル", "必須"),
        old_division=record_get(record, "旧区分"),
        skill_definition=skill_definition or record_get(record, "スキル定義"),
        ai_utilization=record_get(record, "AI活用"),
        ai_utilization_type=record_get(record, "AI活用タイプ"),
        ai_category=record_get(record, "AI区分", "AI区分 LLM、Diffusion、両方"),
        item_id=item_id,
        item=item,
        notes=notes_from_record(
            record, headers,
            {"チェック項目", "スキル定義", "★（見習い）", "★★（一人前）", "★★★（棟梁）"},
        ),
        source_url=source_url,
    )


def extract_standard_rows(rows: list[list[str]], sheet_name: str, version: str, source_url: str) -> list[Row]:
    if not rows:
        return []
    header_idx, headers = find_header_row(rows, {"スキルカテゴリ", "チェック項目"})
    out = []
    seq = 0
    for cells in rows[header_idx + 1:]:
        values = trim(cells)
        if not any(values):
            continue
        record = row_to_record(headers, values)
        item = record_get(record, "チェック項目")
        level = record_get(record, "スキルレベル")
        if not item:
            continue
        # ver.6 fusion has one explanatory reference row with level "–"; it is
        # not one of the 845 skill items.
        if sheet_name == "融合" and level not in VALID_LEVELS:
            continue
        seq += 1
        out.append(make_row(
            record=record, headers=headers, sheet_name=sheet_name,
            version=version, source_url=source_url,
            item_id=f"{SHEET_SLUGS.get(sheet_name, 'skill')}-{seq:04d}",
            skill_level=level, item=item,
        ))
    return out


def extract_value_creation_rows(rows: list[list[str]], version: str, source_url: str) -> list[Row]:
    if not rows:
        return []
    header_idx, headers = find_header_row(rows, {"スキルカテゴリ", "スキル定義", "★（見習い）"})
    out = []
    seq = 0
    levels = [
        ("★", "★（見習い）", "★ 必須"),
        ("★★", "★★（一人前）", "★★ 必須"),
        ("★★★", "★★★（棟梁）", "★★★ 必須"),
    ]
    for cells in rows[header_idx + 1:]:
        values = trim(cells)
        if not any(values):
            continue
        record = row_to_record(headers, values)
        definition = record_get(record, "スキル定義")
        if not definition:
            continue
        for level, item_col, required_col in levels:
            item = record_get(record, item_col)
            if not item:
                continue
            seq += 1
            out.append(make_row(
                record=record, headers=headers, sheet_name="価値創造力",
                version=version, source_url=source_url,
                item_id=f"value-creation-{seq:04d}",
                skill_level=level, item=item,
                required=record_get(record, required_col),
                skill_definition=definition,
            ))
    return out


def raw_records(rows: list[list[str]], sheet_name: str, version: str, source_url: str) -> list[dict[str, str]]:
    if not rows:
        return []
    header_idx = None
    headers: list[str] = []
    for idx, cells in enumerate(rows[:12]):
        candidate = normalize_headers(cells)
        keys = {compact_key(h) for h in candidate}
        if (
            "スキルカテゴリ" in {normalize_text(h) for h in candidate}
            or compact_key("専門1：価値創造（Value Creation）力") in keys
            or compact_key("NO") in keys
        ):
            header_idx, headers = idx, candidate
            break
    if header_idx is None:
        for idx, cells in enumerate(rows[:12]):
            candidate = normalize_headers(cells)
            if len(candidate) >= 4 and sum(bool(x) for x in candidate) >= 3:
                header_idx, headers = idx, candidate
                break
    if header_idx is None:
        return []

    out = []
    for cells in rows[header_idx + 1:]:
        values = trim(cells)
        if not any(values):
            continue
        record = row_to_record(headers, values)
        record["version"] = version
        record["sheet"] = sheet_name
        record["source_url"] = source_url
        out.append(record)
    return out


def enumerate_workbook_data(xlsx_path: Path, version: str, source_url: str) -> tuple[list[Row], list[dict[str, str]], str, dict[str, list[dict[str, str]]]]:
    skill_rows: list[Row] = []
    skilllevel_rows: list[dict[str, str]] = []
    skilllevel_year = ""
    mappings: dict[str, list[dict[str, str]]] = {}

    with ZipFile(xlsx_path) as zf:
        shared = parse_shared_strings(zf)
        sheets = workbook_sheets(zf)
        sheet_names = {name for name, _ in sheets}
        is_ver6 = "価値創造力" in sheet_names and "基盤" in sheet_names
        targets = set(VER6_SHEETS if is_ver6 else VER5_SHEETS)
        skilllevel_sheet = "スキルレベル定義2025" if "スキルレベル定義2025" in sheet_names else "スキルレベル定義2023"
        skilllevel_year = "2025" if skilllevel_sheet.endswith("2025") else "2023"

        mapping_names = {
            "新旧対応（データサイエンス力）": "datascience",
            "新旧対応（エンジニアリング力）": "dataengineering",
        }

        for sheet_name, sheet_path in sheets:
            if sheet_name not in targets and sheet_name != skilllevel_sheet and sheet_name not in mapping_names:
                continue
            rows = sheet_rows(zf, sheet_path, shared)
            if sheet_name == "価値創造力":
                skill_rows.extend(extract_value_creation_rows(rows, version, source_url))
            elif sheet_name in targets:
                skill_rows.extend(extract_standard_rows(rows, sheet_name, version, source_url))
            elif sheet_name == skilllevel_sheet:
                skilllevel_rows = raw_records(rows, sheet_name, version, source_url)
            elif sheet_name in mapping_names:
                mappings[mapping_names[sheet_name]] = raw_records(rows, sheet_name, version, source_url)

    return skill_rows, skilllevel_rows, skilllevel_year, mappings


def write_rows_csv(path: Path, rows: list[Row]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CANONICAL_COLUMNS)
        writer.writeheader()
        writer.writerows(r.as_dict() for r in rows)


def write_rows_json(path: Path, rows: list[Row]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([r.as_dict() for r in rows], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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
        writer.writerows(rows)


def write_records_json(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_manifest(
    version: str, source_url: str, raw_file: Path, rows: list[Row],
    skilllevel_year: str, skilllevel_count: int, mapping_counts: dict[str, int],
) -> None:
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = EXPORTS_DIR / "index.json"
    existing: dict[str, object] = {"versions": []}
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
    versions = existing.get("versions", [])
    if not isinstance(versions, list):
        versions = []

    by_area: dict[str, int] = {}
    star1_by_area: dict[str, int] = {}
    for row in rows:
        by_area[row.area] = by_area.get(row.area, 0) + 1
        if row.skill_level == "★":
            star1_by_area[row.area] = star1_by_area.get(row.area, 0) + 1

    entry = {
        "version": version,
        "source_url": source_url,
        "raw_file": str(raw_file.relative_to(ROOT)) if raw_file.is_relative_to(ROOT) else str(raw_file),
        "sha256": digest_file(raw_file),
        "rows": len(rows),
        "exam_star1_rows": sum(r.skill_level == "★" and r.area != "fusion" for r in rows),
        "rows_by_area": by_area,
        "star1_rows_by_area": star1_by_area,
        "skilllevel_definition_year": skilllevel_year,
        "skilllevel_rows": skilllevel_count,
        "mapping_rows": mapping_counts,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    versions = [v for v in versions if isinstance(v, dict) and v.get("version") != version]
    versions.append(entry)
    versions.sort(key=lambda v: str(v.get("version", "")))
    manifest_path.write_text(
        json.dumps({"latest": version, "versions": versions}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-url", default=DEFAULT_SOURCE_URL)
    parser.add_argument("--xlsx", help="Use local xlsx file path")
    parser.add_argument("--version", help="Override version, e.g. 6.00")
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

    rows, skilllevel_rows, skilllevel_year, mappings = enumerate_workbook_data(xlsx_path, version, source_url)
    if len(rows) < args.min_rows:
        raise SystemExit(f"Parsed rows too small: {len(rows)} (min {args.min_rows})")

    version_dir = VERSIONS_DIR / version
    write_rows_csv(version_dir / "skillcheck.csv", rows)
    write_rows_json(version_dir / "skillcheck.json", rows)
    write_rows_json(EXPORTS_DIR / "latest.json", rows)

    exam_star1 = [
        r for r in rows
        if r.skill_level == "★" and r.area in {"foundation", "value-creation", "datascience", "dataengineering"}
    ]
    write_rows_json(version_dir / "exam_star1.json", exam_star1)
    write_rows_json(EXPORTS_DIR / "exam_star1_latest.json", exam_star1)

    skilllevel_csv = version_dir / f"skilllevel_definition_{skilllevel_year}.csv"
    skilllevel_json = version_dir / f"skilllevel_definition_{skilllevel_year}.json"
    write_records_csv(skilllevel_csv, skilllevel_rows)
    write_records_json(skilllevel_json, skilllevel_rows)
    write_records_json(EXPORTS_DIR / "skilllevel_definition_latest.json", skilllevel_rows)

    mapping_counts = {}
    for slug, records in mappings.items():
        write_records_csv(version_dir / f"change_mapping_{slug}.csv", records)
        write_records_json(version_dir / f"change_mapping_{slug}.json", records)
        mapping_counts[slug] = len(records)

    update_manifest(
        version, source_url, xlsx_path, rows, skilllevel_year,
        len(skilllevel_rows), mapping_counts,
    )

    by_area = {}
    for r in rows:
        by_area[r.area] = by_area.get(r.area, 0) + 1
    print(f"Rows: {len(rows)}")
    print(f"By area: {json.dumps(by_area, ensure_ascii=False, sort_keys=True)}")
    print(f"Exam ★1 rows: {len(exam_star1)}")
    print(f"Skill level definition: {skilllevel_year} ({len(skilllevel_rows)} rows)")
    print(f"Mappings: {json.dumps(mapping_counts, ensure_ascii=False, sort_keys=True)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
