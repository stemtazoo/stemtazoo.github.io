#!/usr/bin/env python3
"""Migrate a reviewed batch of remaining legacy AI-utilization DS pages to ver.6."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

DIRECT = {
    "bias-variance-tradeoff.md": ("datascience", "modeling", "datascience-0183"),
    "sigmoid-function.md": ("datascience", "modeling", "datascience-0190"),
}

SUPPLEMENTAL = {
    "analytics-4types.md": ("datascience", "data-understanding", "分析目的・意思決定タイプの補助学習"),
    "inheritance.md": ("dataengineering", "programming", "オブジェクト指向プログラミングの補助学習"),
    "polymorphism.md": ("dataengineering", "programming", "オブジェクト指向プログラミングの補助学習"),
    "weak-strong-ai.md": ("foundation", "ai-fundamentals", "AIの概念整理の補助学習"),
    "llm-temperature.md": ("foundation", "ai-fundamentals", "生成AIの出力制御の補助学習"),
}

LEGACY_HEADING = re.compile(r"^## 対応スキル項目（AI利活用スキルシート）\s*$", re.MULTILINE)
AREA_LABEL = {
    "foundation": "基盤",
    "datascience": "データサイエンス",
    "dataengineering": "データエンジニアリング",
}
AREA_PAGE = {
    "foundation": "/ds/foundation-skillcheck/",
    "datascience": "/ds/datascience-skillcheck/",
    "dataengineering": "/ds/engineering-skillcheck/",
}


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
    return match.start(), (after + nxt.start() if nxt else len(text))


def canonical_block(row: dict[str, str]) -> str:
    area = row["area"]
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]
    for key, label in (("phase", "フェーズ"), ("section", "分類"), ("category", "スキルカテゴリ"), ("subcategory", "サブカテゴリ")):
        value = normalize(row.get(key, ""))
        if value:
            lines.append(f"- **{label}**：{value}")
    required = normalize(row.get("required_skill", "")) or "—"
    lines.extend([
        f"- **必須スキル**：{required}",
        f"- ★ {normalize(row['item'])}",
        f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})",
        "",
    ])
    return "\n".join(lines)


def supplemental_block(area: str, position: str) -> str:
    return "\n".join([
        f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）",
        "",
        f"- **位置づけ**：{position}",
        "- **★1直接対応**：なし",
        "- ver.6の★1一覧にはこの用語自体の直接項目はありません。関連する試験テーマの理解を補う学習内容として整理します。",
        f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})",
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
        match = LEGACY_HEADING.search(text)
        if not match:
            if f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）" in text and normalize(row["item"]) in text:
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
        match = LEGACY_HEADING.search(text)
        if not match:
            if f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）" in text and "**★1直接対応**：なし" in text:
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: legacy AI-utilization block not found")
        start, end = bounds(text, match)
        new_text = text[:start] + supplemental_block(area, position) + text[end:]
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
