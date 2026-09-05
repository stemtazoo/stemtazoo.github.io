#!/usr/bin/env python3
"""Find likely ver.6 replacements for legacy DS skill blocks after exact migration.

This is review-only: it never edits articles. For each remaining legacy article with
one ★ item, compare that text only against ver.6 ★1 items in the article's
`ds_area`, then report the best similarity candidate. High similarity is useful
for review but is not treated as an automatic mapping.
"""
from __future__ import annotations

import json
import re
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"
OUT = ROOT / "docs" / "audits" / "ds-ver6-similar-skill-candidates.md"

LEGACY_LABELS = (
    "ビジネス力シート",
    "AI利活用スキルシート",
    "データサイエンス力シート",
    "データエンジニアリング力シート",
)
EXCLUDED = {
    "index.md", "optional-math-algorithm.md", "business-skillcheck.md",
    "engineering-skillcheck.md", "skillcheck.md", "ai-utilization-skillcheck.md",
    "foundation-skillcheck.md", "value-creation-skillcheck.md",
    "datascience-skillcheck.md", "model-curriculum-summary.md",
    "skilllevel-2023-summary.md", "skilllevel-2023-assistant-ds-business.md",
    "skilllevel-2023-assistant-ds-dataengineering.md",
    "skilllevel-2023-assistant-ds-datascience.md", "file-transfer-protocol.md",
}
HEADING_RE = re.compile(
    r"^## 対応スキル項目（(?:" + "|".join(map(re.escape, LEGACY_LABELS)) + r")）\s*$",
    re.MULTILINE,
)


def normalize(value: str) -> str:
    value = re.sub(r"[\s　]+", "", value)
    value = value.replace("（", "(").replace("）", ")").replace("，", ",").replace("：", ":")
    return value.strip()


def front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def block_after_heading(text: str, match: re.Match[str]) -> str:
    after = match.end()
    nxt = re.search(r"^##\s+", text[after:], re.MULTILINE)
    end = after + nxt.start() if nxt else len(text)
    return text[match.start():end]


def main() -> int:
    rows = json.loads(DATA.read_text(encoding="utf-8"))
    by_area: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_area.setdefault(row.get("area", ""), []).append(row)

    candidates = []
    for path in sorted(DS_DIR.glob("*.md")):
        if path.name in EXCLUDED:
            continue
        text = path.read_text(encoding="utf-8-sig")
        match = HEADING_RE.search(text)
        if not match:
            continue
        block = block_after_heading(text, match)
        star = [m.group(1).strip() for m in re.finditer(r"^-\s*★\s*(.+?)\s*$", block, re.MULTILINE)]
        if len(star) != 1:
            continue
        meta = front_matter(text)
        area = meta.get("ds_area", "")
        options = by_area.get(area, [])
        if not options:
            continue
        source_norm = normalize(star[0])
        scored = []
        for row in options:
            score = SequenceMatcher(None, source_norm, normalize(row.get("item", ""))).ratio()
            scored.append((score, row))
        score, best = max(scored, key=lambda x: x[0])
        candidates.append((score, path.name, meta.get("title", ""), area, star[0], best))

    candidates.sort(reverse=True, key=lambda x: x[0])
    high = [x for x in candidates if x[0] >= 0.85]
    medium = [x for x in candidates if 0.70 <= x[0] < 0.85]

    lines = [
        "# DS検定 ver.6 類似スキル候補監査",
        "",
        "> 旧本文の★項目と、同じ `ds_area` の公式ver.6 ★1項目を文字列類似度で比較したレビュー用候補です。自動置換には使用しません。",
        "",
        "## 集計",
        "",
        f"- 1つの旧★項目を持つ残存記事: **{len(candidates)}**",
        f"- 高類似（0.85以上）: **{len(high)}**",
        f"- 中類似（0.70以上0.85未満）: **{len(medium)}**",
        "",
        "## 高類似候補",
        "",
        "| 類似度 | ファイル | ds_area | 旧★項目 | ver.6候補 | item_id |",
        "|---:|---|---|---|---|---|",
    ]
    for score, filename, title, area, old_item, best in high:
        old_item = old_item.replace("|", "\\|")
        item = best.get("item", "").replace("|", "\\|")
        lines.append(f"| {score:.3f} | `{filename}` | `{area}` | {old_item} | {item} | `{best.get('item_id','')}` |")

    lines.extend(["", "## 中類似候補", "", "| 類似度 | ファイル | ds_area | 旧★項目 | ver.6候補 | item_id |", "|---:|---|---|---|---|---|"])
    for score, filename, title, area, old_item, best in medium:
        old_item = old_item.replace("|", "\\|")
        item = best.get("item", "").replace("|", "\\|")
        lines.append(f"| {score:.3f} | `{filename}` | `{area}` | {old_item} | {item} | `{best.get('item_id','')}` |")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Candidates={len(candidates)}, high={len(high)}, medium={len(medium)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
