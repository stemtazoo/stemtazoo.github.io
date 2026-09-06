#!/usr/bin/env python3
"""Migrate multi-item legacy DS/DE skill blocks with official ver.6 change maps.

A block is changed only when all legacy ★ items:
- map uniquely through the official 2023 -> ver.6 mapping sheet,
- remain ★1 in ver.6,
- belong to the article's current ds_area, and
- resolve to the same ver.6 skill category + subcategory.

Duplicate ver.6 targets are collapsed. Run without --write for a dry run.
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
AREA_LABEL = {"datascience": "データサイエンス", "dataengineering": "データエンジニアリング"}
AREA_PAGE = {"datascience": "/ds/datascience-skillcheck/", "dataengineering": "/ds/engineering-skillcheck/"}
EXCLUDED = {
    "index.md", "optional-math-algorithm.md", "business-skillcheck.md", "engineering-skillcheck.md",
    "skillcheck.md", "ai-utilization-skillcheck.md", "foundation-skillcheck.md",
    "value-creation-skillcheck.md", "datascience-skillcheck.md", "model-curriculum-summary.md",
    "skilllevel-2023-summary.md", "skilllevel-2023-assistant-ds-business.md",
    "skilllevel-2023-assistant-ds-dataengineering.md", "skilllevel-2023-assistant-ds-datascience.md",
    "file-transfer-protocol.md",
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
    return start, after + nxt.start() if nxt else len(text)


def build_mapping(path: Path, expected_area: str, exam_by_text: dict[str, list[dict[str, str]]]) -> dict[str, dict[str, str]]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, dict[str, str]] = {}
    ambiguous: set[str] = set()
    for row in rows:
        old = normalize(row.get("チェック項目_2023", ""))
        new = normalize(row.get("チェック項目", ""))
        if not old or not new:
            continue
        if normalize(row.get("スキルレベル_2023", "")) != "★" or normalize(row.get("スキルレベル", "")) != "★":
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


def canonical_block(rows: list[dict[str, str]]) -> str:
    area = rows[0]["area"]
    category = rows[0].get("category", "")
    subcategory = rows[0].get("subcategory", "")
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]
    sections = {normalize(r.get("section", "")) for r in rows if normalize(r.get("section", ""))}
    if len(sections) == 1:
        lines.append(f"- **分類**：{next(iter(sections))}")
    if category:
        lines.append(f"- **スキルカテゴリ**：{category}")
    if subcategory:
        lines.append(f"- **サブカテゴリ**：{subcategory}")
    required_values = [normalize(r.get("required_skill", "")) or "—" for r in rows]
    if len(set(required_values)) == 1:
        lines.append(f"- **必須スキル**：{required_values[0]}")
    lines.append("- **★1チェック項目**：")
    for row in rows:
        required = normalize(row.get("required_skill", "")) or "—"
        suffix = "" if len(set(required_values)) == 1 else f"（必須: {required}）"
        lines.append(f"  - ★ {normalize(row['item'])}{suffix}")
    lines.extend([f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    exam_rows = json.loads(EXAM.read_text(encoding="utf-8"))
    exam_by_text: dict[str, list[dict[str, str]]] = {}
    for row in exam_rows:
        exam_by_text.setdefault(normalize(row.get("item", "")), []).append(row)
    mappings = {label: build_mapping(path, area, exam_by_text) for label, (path, area) in SOURCE_CONFIG.items()}

    changed: list[tuple[str, list[str]]] = []
    skipped: list[tuple[str, str]] = []

    for path in sorted(DS_DIR.glob("*.md")):
        if path.name in EXCLUDED:
            continue
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        matched = None
        for label in SOURCE_CONFIG:
            heading = f"## 対応スキル項目（{label}）"
            if heading in text:
                matched = (label, heading)
                break
        if not matched:
            continue
        label, heading = matched
        start, end = bounds(text, text.find(heading), heading)
        block = text[start:end]
        stars = [normalize(x) for x in re.findall(r"^-?\s*★\s*(.+?)\s*$", block, re.MULTILINE)]
        if len(stars) < 2:
            continue

        mapped: list[dict[str, str]] = []
        failed = False
        for star in stars:
            row = mappings[label].get(star)
            if not row:
                skipped.append((path.name, "at least one ★ item has no unique official mapping"))
                failed = True
                break
            mapped.append(row)
        if failed:
            continue
        if any(r.get("area") != meta.get("ds_area") for r in mapped):
            skipped.append((path.name, "mapped area does not match article ds_area"))
            continue
        themes = {(normalize(r.get("category", "")), normalize(r.get("subcategory", ""))) for r in mapped}
        if len(themes) != 1:
            skipped.append((path.name, "mapped ★ items span multiple ver.6 themes"))
            continue

        unique: list[dict[str, str]] = []
        seen: set[str] = set()
        for row in mapped:
            if row["item_id"] not in seen:
                unique.append(row)
                seen.add(row["item_id"])
        new_text = text[:start] + canonical_block(unique) + text[end:]
        if new_text != text:
            changed.append((path.name, [r["item_id"] for r in unique]))
            if args.write:
                path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: safe multi-item migrations={len(changed)}")
    for filename, ids in changed:
        print(f"CHANGE {filename} -> {','.join(ids)}")
    print(f"Skipped multi-item blocks={len(skipped)}")
    for filename, reason in skipped[:50]:
        print(f"SKIP {filename}: {reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
