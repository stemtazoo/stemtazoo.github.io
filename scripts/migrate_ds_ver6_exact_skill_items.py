#!/usr/bin/env python3
"""Safely migrate DS article skill blocks when the legacy ★ item exactly matches ver.6.

Only articles satisfying all conditions are changed:
- ordinary `pages/ds/*.md` article
- contains one legacy skill-sheet heading
- legacy skill block contains exactly one `- ★ ...` item
- that text exactly matches exactly one ver.6 ★1 item
- article `ds_area` equals the matched ver.6 area

The whole legacy skill block is then replaced with canonical ver.6 metadata.
Run without --write for a dry run.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

LEGACY_LABELS = (
    "ビジネス力シート",
    "AI利活用スキルシート",
    "データサイエンス力シート",
    "データエンジニアリング力シート",
)

EXCLUDED = {
    "index.md",
    "optional-math-algorithm.md",
    "business-skillcheck.md",
    "engineering-skillcheck.md",
    "skillcheck.md",
    "ai-utilization-skillcheck.md",
    "foundation-skillcheck.md",
    "value-creation-skillcheck.md",
    "datascience-skillcheck.md",
    "model-curriculum-summary.md",
    "skilllevel-2023-summary.md",
    "skilllevel-2023-assistant-ds-business.md",
    "skilllevel-2023-assistant-ds-dataengineering.md",
    "skilllevel-2023-assistant-ds-datascience.md",
    "file-transfer-protocol.md",
}

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


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def load_index() -> dict[str, list[dict[str, str]]]:
    rows = json.loads(DATA.read_text(encoding="utf-8"))
    index: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        item = normalize(row.get("item", ""))
        if item:
            index.setdefault(item, []).append(row)
    return index


def skill_block_bounds(text: str, match: re.Match[str]) -> tuple[int, int]:
    start = match.start()
    after_heading = match.end()
    next_heading = re.search(r"^##\s+", text[after_heading:], re.MULTILINE)
    end = after_heading + next_heading.start() if next_heading else len(text)
    return start, end


def canonical_block(row: dict[str, str]) -> str:
    area = row["area"]
    required = normalize(row.get("required_skill", "")) or "—"
    lines = [
        f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）",
        "",
    ]
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

    index = load_index()
    changed: list[str] = []
    skipped: list[tuple[str, str]] = []

    for path in sorted(DS_DIR.glob("*.md")):
        if path.name in EXCLUDED:
            continue
        text = path.read_text(encoding="utf-8-sig")
        match = HEADING_RE.search(text)
        if not match:
            continue

        meta = front_matter(text)
        area = meta.get("ds_area", "")
        if area not in AREA_LABEL:
            skipped.append((path.name, "missing/invalid ds_area"))
            continue

        start, end = skill_block_bounds(text, match)
        block = text[start:end]
        star_items = [
            normalize(m.group(1))
            for m in re.finditer(r"^-\s*★\s*(.+?)\s*$", block, re.MULTILINE)
        ]
        if len(star_items) != 1:
            skipped.append((path.name, f"legacy ★ item count={len(star_items)}"))
            continue

        candidates = index.get(star_items[0], [])
        if len(candidates) != 1:
            skipped.append((path.name, f"exact ver.6 matches={len(candidates)}"))
            continue

        row = candidates[0]
        if row.get("area") != area:
            skipped.append((path.name, f"area mismatch {area}!={row.get('area')}"))
            continue

        new_text = text[:start] + canonical_block(row) + text[end:]
        if new_text == text:
            continue
        changed.append(path.name)
        if args.write:
            path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: exact ver.6 candidates={len(changed)}")
    for name in changed:
        print(f"CHANGE {name}")
    print(f"Skipped legacy blocks={len(skipped)}")
    for name, reason in skipped[:40]:
        print(f"SKIP {name}: {reason}")
    if len(skipped) > 40:
        print(f"... {len(skipped) - 40} more skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
