#!/usr/bin/env python3
"""Migrate manually reviewed near-match legacy DS skill blocks to ver.6.

Mappings are explicit filename -> official ver.6 item_id pairs. Before writing, the
script verifies the article's ds_area matches the official item area and that the
legacy block still contains exactly one ★ item. This avoids broad fuzzy auto-editing.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

REVIEWED = {
    "nosql.md": "dataengineering-0069",
    "spark.md": "dataengineering-0068",
    "yarn.md": "dataengineering-0068",
    "visualization-basic-perspectives.md": "datascience-0153",
    "malware.md": "foundation-0032",
}

LEGACY_LABELS = (
    "ビジネス力シート",
    "AI利活用スキルシート",
    "データサイエンス力シート",
    "データエンジニアリング力シート",
)
AREA_LABEL = {
    "foundation": "基盤",
    "value-creation": "価値創造",
    "datascience": "データサイエンス",
    "dataengineering": "データエンジニアリング",
}
AREA_PAGE = {
    "foundation": "/ds/foundation-skillcheck/",
    "value-creation": "/ds/value-creation-skillcheck/",
    "datascience": "/ds/datascience-skillcheck/",
    "dataengineering": "/ds/engineering-skillcheck/",
}
HEADING_RE = re.compile(
    r"^## 対応スキル項目（(?:" + "|".join(map(re.escape, LEGACY_LABELS)) + r")）\s*$",
    re.MULTILINE,
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def bounds(text: str, match: re.Match[str]) -> tuple[int, int]:
    after = match.end()
    nxt = re.search(r"^##\s+", text[after:], re.MULTILINE)
    end = after + nxt.start() if nxt else len(text)
    return match.start(), end


def canonical_block(row: dict[str, str]) -> str:
    area = row["area"]
    required = normalize(row.get("required_skill", "")) or "—"
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]
    if row.get("phase"):
        lines.append(f"- **フェーズ**：{row['phase']}")
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rows = json.loads(DATA.read_text(encoding="utf-8"))
    by_id = {row["item_id"]: row for row in rows}
    changed: list[str] = []

    for filename, item_id in REVIEWED.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        match = HEADING_RE.search(text)
        if not match:
            raise SystemExit(f"{filename}: legacy skill heading not found")
        start, end = bounds(text, match)
        block = text[start:end]
        stars = re.findall(r"^-\s*★\s*(.+?)\s*$", block, re.MULTILINE)
        if len(stars) != 1:
            raise SystemExit(f"{filename}: expected exactly one legacy ★ item, got {len(stars)}")
        row = by_id.get(item_id)
        if not row:
            raise SystemExit(f"{filename}: official item not found: {item_id}")
        meta = front_matter(text)
        if meta.get("ds_area") != row.get("area"):
            raise SystemExit(
                f"{filename}: ds_area mismatch {meta.get('ds_area')} != {row.get('area')}"
            )
        new_text = text[:start] + canonical_block(row) + text[end:]
        if new_text != text:
            changed.append(filename)
            if args.write:
                path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: reviewed similar migrations={len(changed)}")
    for filename in changed:
        print(f"CHANGE {filename} -> {REVIEWED[filename]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
