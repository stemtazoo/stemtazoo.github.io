#!/usr/bin/env python3
"""Migrate legacy DS/DE skill blocks using the official ver.6 change-mapping sheets.

Safety conditions:
- article still has a legacy Data Science or Data Engineering skill-sheet heading
- legacy block contains exactly one ★ item
- that legacy text exactly matches one 2023 item in the corresponding official change map
- the mapped ver.6 item is still ★1
- the mapped ver.6 item exists uniquely in exam_star1_latest.json
- article ds_area matches that official ver.6 item area

Run without --write for a dry run.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
EXAM = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"
MAP_DS = ROOT / "data" / "skillcheck" / "versions" / "6.00" / "change_mapping_datascience.json"
MAP_DE = ROOT / "data" / "skillcheck" / "versions" / "6.00" / "change_mapping_dataengineering.json"

SOURCE_CONFIG = {
    "データサイエンス力シート": (MAP_DS, "datascience"),
    "データエンジニアリング力シート": (MAP_DE, "dataengineering"),
}
AREA_LABEL = {
    "datascience": "データサイエンス",
    "dataengineering": "データエンジニアリング",
}
AREA_PAGE = {
    "datascience": "/ds/datascience-skillcheck/",
    "dataengineering": "/ds/engineering-skillcheck/",
}
EXCLUDED = {
    "index.md", "optional-math-algorithm.md", "business-skillcheck.md",
    "engineering-skillcheck.md", "skillcheck.md", "ai-utilization-skillcheck.md",
    "foundation-skillcheck.md", "value-creation-skillcheck.md",
    "datascience-skillcheck.md", "model-curriculum-summary.md",
    "skilllevel-2023-summary.md", "skilllevel-2023-assistant-ds-business.md",
    "skilllevel-2023-assistant-ds-dataengineering.md",
    "skilllevel-2023-assistant-ds-datascience.md", "file-transfer-protocol.md",
}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def bounds(text: str, start: int, heading: str) -> tuple[int, int]:
    after = start + len(heading)
    nxt = re.search(r"^##\s+", text[after:], re.MULTILINE)
    end = after + nxt.start() if nxt else len(text)
    return start, end


def canonical_block(row: dict[str, str]) -> str:
    area = row["area"]
    required = normalize(row.get("required_skill", "")) or "—"
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]
    if row.get("section"):
        lines.append(f"- **分類**：{row['section']}")
    if row.get("category"):
        lines.append(f"- **スキルカテゴリ**：{row['category']}")
    if row.get("subcategory"):
        lines.append(f"- **サブカテゴリ**：{row['subcategory']}")
    lines.extend([
        f"- **必須スキル**：{required}",
        f"- ★ {normalize(row['item'])}",
        f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})",
        "",
    ])
    return "\n".join(lines)


def build_mapping(path: Path, expected_area: str, exam_by_text: dict[str, list[dict[str, str]]]) -> dict[str, dict[str, str]]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, dict[str, str]] = {}
    ambiguous: set[str] = set()
    for row in rows:
        old = normalize(row.get("チェック項目_2023", ""))
        new = normalize(row.get("チェック項目", ""))
        if not old or not new:
            continue
        if normalize(row.get("スキルレベル_2023", "")) != "★":
            continue
        if normalize(row.get("スキルレベル", "")) != "★":
            continue
        candidates = [r for r in exam_by_text.get(new, []) if r.get("area") == expected_area]
        if len(candidates) != 1:
            continue
        if old in out and out[old].get("item_id") != candidates[0].get("item_id"):
            ambiguous.add(old)
            continue
        out[old] = candidates[0]
    for old in ambiguous:
        out.pop(old, None)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    exam_rows = json.loads(EXAM.read_text(encoding="utf-8"))
    exam_by_text: dict[str, list[dict[str, str]]] = {}
    for row in exam_rows:
        exam_by_text.setdefault(normalize(row.get("item", "")), []).append(row)

    mappings = {
        heading: build_mapping(path, area, exam_by_text)
        for heading, (path, area) in SOURCE_CONFIG.items()
    }

    changed: list[tuple[str, str]] = []
    skipped: list[tuple[str, str]] = []

    for path in sorted(DS_DIR.glob("*.md")):
        if path.name in EXCLUDED:
            continue
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)

        matched_heading = None
        for label in SOURCE_CONFIG:
            heading = f"## 対応スキル項目（{label}）"
            if heading in text:
                matched_heading = (label, heading)
                break
        if not matched_heading:
            continue

        label, heading = matched_heading
        start = text.find(heading)
        block_start, block_end = bounds(text, start, heading)
        block = text[block_start:block_end]
        stars = [normalize(x) for x in re.findall(r"^-?\s*★\s*(.+?)\s*$", block, re.MULTILINE)]
        if len(stars) != 1:
            skipped.append((path.name, f"legacy ★ item count={len(stars)}"))
            continue

        row = mappings[label].get(stars[0])
        if not row:
            skipped.append((path.name, "no unique official 2023→ver.6 ★1 mapping"))
            continue
        if meta.get("ds_area") != row.get("area"):
            skipped.append((path.name, f"area mismatch {meta.get('ds_area')}!={row.get('area')}"))
            continue

        new_text = text[:block_start] + canonical_block(row) + text[block_end:]
        if new_text != text:
            changed.append((path.name, row["item_id"]))
            if args.write:
                path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: official change-map migrations={len(changed)}")
    for filename, item_id in changed:
        print(f"CHANGE {filename} -> {item_id}")
    print(f"Skipped legacy DS/DE blocks={len(skipped)}")
    for filename, reason in skipped[:60]:
        print(f"SKIP {filename}: {reason}")
    if len(skipped) > 60:
        print(f"... {len(skipped)-60} more skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
