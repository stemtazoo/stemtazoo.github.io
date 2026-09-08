#!/usr/bin/env python3
"""Migrate reviewed legacy AI-utilization ML/NLP pages to DS ver.6.

Direct mappings use official ver.6 ★1 item IDs when the article theme clearly
matches. Closely related concepts without a direct ★1 item are retained as
supplemental learning instead of being forced onto a different official item.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

DIRECT = {
    "cnn.md": ("datascience", "modeling", "datascience-0220"),
    "random-forest.md": ("datascience", "modeling", "datascience-0191"),
    "activation-functions-hidden-layer.md": ("datascience", "modeling", "datascience-0190"),
    "annotation.md": ("datascience", "modeling", "datascience-0185"),
    "nltk.md": ("datascience", "unstructured-data", "datascience-0289"),
    "japanese-morphological-analysis-tools.md": ("datascience", "unstructured-data", "datascience-0289"),
    "dependency-parsing.md": ("datascience", "unstructured-data", "datascience-0289"),
    "nlp-cleaning.md": ("datascience", "unstructured-data", "datascience-0288"),
    "digital-image-representation.md": ("datascience", "unstructured-data", "datascience-0301"),
    "image-filter-processing.md": ("datascience", "unstructured-data", "datascience-0302"),
    "convolution.md": ("datascience", "modeling", "datascience-0302"),
}

SUPPLEMENTAL = {
    "kernel.md": ("datascience", "modeling", "画像処理・CNN理解の補助学習"),
    "entropy.md": ("datascience", "statistics", "決定木・情報量理解の補助学習"),
    "impurity.md": ("datascience", "modeling", "決定木の分岐基準の補助学習"),
    "gini-vs-entropy.md": ("datascience", "modeling", "決定木の分岐基準比較の補助学習"),
}

HEADING_RE = re.compile(r"^## 対応スキル項目（AI利活用スキルシート）\s*$", re.MULTILINE)
AREA_LABEL = {"datascience": "データサイエンス"}
AREA_PAGE = {"datascience": "/ds/datascience-skillcheck/"}


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


def canonical_block(row: dict[str, str]) -> str:
    area = row["area"]
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]
    for key, label in (("section", "分類"), ("category", "スキルカテゴリ"), ("subcategory", "サブカテゴリ")):
        value = row.get(key, "").strip()
        if value:
            lines.append(f"- **{label}**：{value}")
    required = row.get("required_skill", "").strip() or "—"
    lines.extend([
        f"- **必須スキル**：{required}",
        f"- ★ {row['item'].strip()}",
        f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})",
        "",
    ])
    return "\n".join(lines)


def supplemental_block(position: str) -> str:
    return "\n".join([
        "## 対応スキル項目（ver.6 データサイエンス）",
        "",
        f"- **位置づけ**：{position}",
        "- **★1直接対応**：なし",
        "- ver.6の★1一覧にはこの用語自体の直接項目はありません。関連するモデル・分析手法の理解を補う学習テーマとして整理します。",
        "- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)",
        "",
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rows = json.loads(DATA.read_text(encoding="utf-8"))
    by_id = {row["item_id"]: row for row in rows}
    changed: list[str] = []
    already: list[str] = []

    for filename, (area, section, item_id) in DIRECT.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        if meta.get("ds_area") != area or meta.get("ds_section") != section:
            raise SystemExit(f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')}")
        row = by_id.get(item_id)
        if not row or row.get("area") != area:
            raise SystemExit(f"{filename}: official item mismatch {item_id}")
        match = HEADING_RE.search(text)
        if not match:
            if f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）" in text and row["item"] in text:
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: legacy AI-utilization block not found")
        start, end = bounds(text, match)
        new_text = text[:start] + canonical_block(row) + text[end:]
        changed.append(filename)
        if args.write:
            path.write_text(new_text, encoding="utf-8")

    for filename, (area, section, position) in SUPPLEMENTAL.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        if meta.get("ds_area") != area or meta.get("ds_section") != section:
            raise SystemExit(f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')}")
        match = HEADING_RE.search(text)
        if not match:
            if "## 対応スキル項目（ver.6 データサイエンス）" in text and "**★1直接対応**：なし" in text:
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: legacy AI-utilization block not found")
        start, end = bounds(text, match)
        new_text = text[:start] + supplemental_block(position) + text[end:]
        changed.append(filename)
        if args.write:
            path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: changed={len(changed)}, already={len(already)}")
    for filename in changed:
        print(f"CHANGE {filename}")
    for filename in already:
        print(f"ALREADY {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
