#!/usr/bin/env python3
"""Migrate the legacy privacy-law skill group to official ver.6 foundation-0008.

The legacy Business-skill item
`個人情報保護やプライバシー保護に関する法制度を理解している`
appears in multiple privacy/legal articles. In ver.6 these topics are consolidated
into foundation-0008 (行動規範 / コンプライアンス).

Only files satisfying all safety checks are changed:
- ordinary pages/ds/*.md article
- legacy Business-skill heading is still present
- exactly one legacy ★ item exists and equals LEGACY_ITEM
- ds_area is foundation
- official target item foundation-0008 exists and is foundation

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
TARGET_ID = "foundation-0008"
LEGACY_ITEM = "個人情報保護やプライバシー保護に関する法制度を理解している"
LEGACY_HEADING = "## 対応スキル項目（ビジネス力シート）"

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
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip().strip('"')
    return out


def block_bounds(text: str, start: int) -> tuple[int, int]:
    after = start + len(LEGACY_HEADING)
    nxt = re.search(r"^##\s+", text[after:], re.MULTILINE)
    end = after + nxt.start() if nxt else len(text)
    return start, end


def canonical_block(row: dict[str, str]) -> str:
    required = normalize(row.get("required_skill", "")) or "—"
    lines = ["## 対応スキル項目（ver.6 基盤）", ""]
    if row.get("section"):
        lines.append(f"- **分類**：{row['section']}")
    if row.get("category"):
        lines.append(f"- **スキルカテゴリ**：{row['category']}")
    if row.get("subcategory"):
        lines.append(f"- **サブカテゴリ**：{row['subcategory']}")
    lines.extend([
        f"- **必須スキル**：{required}",
        f"- ★ {normalize(row['item'])}",
        "- [ver.6 ★1スキルチェックで確認する](/ds/foundation-skillcheck/)",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rows = json.loads(DATA.read_text(encoding="utf-8"))
    by_id = {row["item_id"]: row for row in rows}
    target = by_id.get(TARGET_ID)
    if not target or target.get("area") != "foundation":
        raise SystemExit(f"Official target invalid: {TARGET_ID}")

    changed: list[str] = []
    for path in sorted(DS_DIR.glob("*.md")):
        if path.name in EXCLUDED:
            continue
        text = path.read_text(encoding="utf-8-sig")
        if LEGACY_ITEM not in text:
            continue
        heading_pos = text.find(LEGACY_HEADING)
        if heading_pos < 0:
            raise SystemExit(f"{path.name}: legacy item found but Business heading missing")
        meta = front_matter(text)
        if meta.get("ds_area") != "foundation":
            raise SystemExit(f"{path.name}: expected ds_area foundation, got {meta.get('ds_area')}")
        start, end = block_bounds(text, heading_pos)
        block = text[start:end]
        stars = [normalize(x) for x in re.findall(r"^-\s*★\s*(.+?)\s*$", block, re.MULTILINE)]
        if stars != [LEGACY_ITEM]:
            raise SystemExit(f"{path.name}: unexpected legacy ★ items: {stars}")
        new_text = text[:start] + canonical_block(target) + text[end:]
        if new_text != text:
            changed.append(path.name)
            if args.write:
                path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: privacy-law migrations={len(changed)}")
    for name in changed:
        print(f"CHANGE {name} -> {TARGET_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
