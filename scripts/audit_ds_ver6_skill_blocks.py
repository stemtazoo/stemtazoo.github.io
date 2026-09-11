#!/usr/bin/env python3
"""Validate DS ver.6 skill blocks across all ordinary DS articles.

This audit is read-only. It verifies that legacy ver.5 sheet labels are gone,
canonical ver.6 headings agree with front matter, direct mappings use exact
official ★1 wording in the same area, and supplemental blocks are explicit.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

try:
    from scripts.audit_ds_ver5_body_labels import DS_DIR, EXCLUDED, LEGACY_LABELS, front_matter
except ModuleNotFoundError:
    from audit_ds_ver5_body_labels import DS_DIR, EXCLUDED, LEGACY_LABELS, front_matter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

AREA_LABEL = {
    "foundation": "基盤",
    "value-creation": "価値創造",
    "datascience": "データサイエンス",
    "dataengineering": "データエンジニアリング",
}
HEADING_RE = re.compile(r"^## 対応スキル項目（ver\.6 ([^)]+)）\s*$", re.MULTILINE)
DIRECT_RE = re.compile(r"^- ★ (.+?)\s*$", re.MULTILINE)
REQUIRED_SUFFIX_RE = re.compile(r"（必須スキル：[^）]*）$")


def block_end(text: str, start: int) -> int:
    match = re.search(r"^##\s+", text[start:], re.MULTILINE)
    return start + match.start() if match else len(text)


def main() -> int:
    official_rows = json.loads(DATA.read_text(encoding="utf-8"))
    official_by_area = {
        area: {row["item"] for row in official_rows if row["area"] == area}
        for area in AREA_LABEL
    }

    errors: list[str] = []
    direct_count = 0
    supplemental_count = 0
    block_count = 0

    for path in sorted(DS_DIR.glob("*.md")):
        if path.name in EXCLUDED:
            continue
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)

        found_legacy = [label for label in LEGACY_LABELS if label in text]
        if found_legacy:
            errors.append(f"{path.name}: legacy labels remain: {', '.join(found_legacy)}")

        matches = list(HEADING_RE.finditer(text))
        if not matches:
            if "対応スキル項目（ver.6" in text:
                errors.append(f"{path.name}: malformed ver.6 skill heading")
            continue
        if len(matches) != 1:
            errors.append(f"{path.name}: expected one ver.6 skill block, got {len(matches)}")
            continue

        block_count += 1
        match = matches[0]
        area = meta.get("ds_area", "")
        expected_label = AREA_LABEL.get(area)
        if expected_label != match.group(1):
            errors.append(
                f"{path.name}: heading area {match.group(1)!r} "
                f"does not match ds_area {area!r}"
            )

        end = block_end(text, match.end())
        block = text[match.start():end]
        direct_items = [
            REQUIRED_SUFFIX_RE.sub("", item).strip()
            for item in DIRECT_RE.findall(block)
        ]
        is_supplemental = "**★1直接対応**：なし" in block

        if direct_items and is_supplemental:
            errors.append(f"{path.name}: direct and supplemental markers are mixed")
        elif direct_items:
            direct_count += 1
            valid_items = official_by_area.get(area, set())
            for item in direct_items:
                if item not in valid_items:
                    errors.append(
                        f"{path.name}: official ★1 item not found in area {area}: {item}"
                    )
        elif is_supplemental:
            supplemental_count += 1
            if "**位置づけ**：" not in block:
                errors.append(f"{path.name}: supplemental position is missing")
        else:
            errors.append(f"{path.name}: neither direct items nor supplemental marker found")

    print(f"Validated ver.6 skill blocks: {block_count}")
    print(f"Direct-mapping articles: {direct_count}")
    print(f"Supplemental articles: {supplemental_count}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
