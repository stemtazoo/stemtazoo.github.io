#!/usr/bin/env python3
"""Migrate reviewed AI-utilization technology/social-trend pages to DS ver.6."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"
ITEM_ID = "value-creation-0001"
FILES = (
    "cps.md",
    "cps-iot-digitaltwin-cheatsheet.md",
    "digital-twin.md",
    "industry4-0.md",
    "society5.md",
)
HEADING_RE = re.compile(r"^## 対応スキル項目（AI利活用スキルシート）\s*$", re.MULTILINE)


def front_matter(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return data
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


def block(row: dict[str, str]) -> str:
    lines = ["## 対応スキル項目（ver.6 価値創造）", ""]
    for key, label in (("phase", "フェーズ"), ("section", "分類"), ("category", "スキルカテゴリ"), ("subcategory", "サブカテゴリ")):
        value = row.get(key, "").strip()
        if value:
            lines.append(f"- **{label}**：{value}")
    required = row.get("required_skill", "").strip() or "—"
    lines.extend([
        f"- **必須スキル**：{required}",
        f"- ★ {row['item'].strip()}",
        "- [ver.6 ★1スキルチェックで確認する](/ds/value-creation-skillcheck/)",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rows = json.loads(DATA.read_text(encoding="utf-8"))
    row = next((x for x in rows if x.get("item_id") == ITEM_ID), None)
    if not row or row.get("area") != "value-creation":
        raise SystemExit(f"official item not found or area mismatch: {ITEM_ID}")

    changed: list[str] = []
    already: list[str] = []
    for filename in FILES:
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        if meta.get("ds_area") != "value-creation" or meta.get("ds_section") != "technology-social-trends":
            raise SystemExit(f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')}")

        match = HEADING_RE.search(text)
        if not match:
            if "## 対応スキル項目（ver.6 価値創造）" in text and row["item"] in text:
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: legacy AI-utilization block not found")

        start, end = bounds(text, match)
        new_text = text[:start] + block(row) + text[end:]
        changed.append(filename)
        if args.write:
            path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: changed={len(changed)}, already={len(already)}")
    for filename in changed:
        print(f"CHANGE {filename} -> {ITEM_ID}")
    for filename in already:
        print(f"ALREADY {filename} -> {ITEM_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
