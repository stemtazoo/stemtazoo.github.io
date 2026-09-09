#!/usr/bin/env python3
"""Migrate the final legacy AI-utilization skill blocks to DS skillcheck ver.6."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

DIRECT = {
    "feature-importance.md": "datascience-0191",
    "logistic-regression.md": "datascience-0160",
    "machine-learning-algorithms-cheatsheet.md": "datascience-0181",
    "machine-learning-methods.md": "datascience-0181",
    "overfitting-tree-depth.md": "datascience-0183",
}

SUPPLEMENTAL = {
    "data-augmentation.md": ("datascience", "unstructured-data", "画像データ拡張の補助学習"),
    "image-metadata.md": ("datascience", "unstructured-data", "画像データ理解の補助学習"),
    "information-gain.md": ("datascience", "modeling", "決定木・情報利得の補助学習"),
    "jupyter-r-usage.md": ("dataengineering", "environment-setup", "分析環境・実行環境の補助学習"),
    "predictive-analytics.md": ("datascience", "modeling", "予測分析の補助学習"),
    "stemming-vs-lemmatization.md": ("datascience", "unstructured-data", "テキスト前処理の補助学習"),
}

AREA_LABEL = {
    "datascience": "データサイエンス",
    "dataengineering": "データエンジニアリング",
}
AREA_PAGE = {
    "datascience": "/ds/datascience-skillcheck/",
    "dataengineering": "/ds/engineering-skillcheck/",
}
HEADING = re.compile(r"^## 対応スキル項目（AI利活用スキルシート）\s*$", re.MULTILINE)


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


def block_bounds(text: str, match: re.Match[str]) -> tuple[int, int]:
    after = match.end()
    nxt = re.search(r"^##\s+", text[after:], re.MULTILINE)
    return match.start(), after + nxt.start() if nxt else len(text)


def direct_block(row: dict[str, str]) -> str:
    area = row["area"]
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]
    for key, label in (("phase", "フェーズ"), ("section", "分類"), ("category", "スキルカテゴリ"), ("subcategory", "サブカテゴリ")):
        value = normalize(row.get(key, ""))
        if value:
            lines.append(f"- **{label}**：{value}")
    required = normalize(row.get("required_skill", "")) or "—"
    lines += [
        f"- **必須スキル**：{required}",
        f"- ★ {normalize(row['item'])}",
        f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})",
        "",
    ]
    return "\n".join(lines)


def supplemental_block(area: str, position: str) -> str:
    return "\n".join([
        f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）",
        "",
        f"- **位置づけ**：{position}",
        "- **★1直接対応**：なし",
        "- ver.6の★1一覧にはこのテーマと同一の直接項目がないため、試験理解を補う関連テーマとして整理します。",
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

    for filename in list(DIRECT) + list(SUPPLEMENTAL):
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        match = HEADING.search(text)

        if filename in DIRECT:
            row = by_id.get(DIRECT[filename])
            if not row:
                raise SystemExit(f"{filename}: missing official item {DIRECT[filename]}")
            area = row["area"]
            if meta.get("ds_area") != area:
                raise SystemExit(f"{filename}: ds_area mismatch {meta.get('ds_area')} != {area}")
            replacement = direct_block(row)
            expected_heading = f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）"
            expected_item = f"★ {normalize(row['item'])}"
            if not match:
                if expected_heading in text and expected_item in text:
                    already.append(filename)
                    continue
                raise SystemExit(f"{filename}: legacy block not found")
        else:
            area, section, position = SUPPLEMENTAL[filename]
            if meta.get("ds_area") != area or meta.get("ds_section") != section:
                raise SystemExit(
                    f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')} != {area}/{section}"
                )
            replacement = supplemental_block(area, position)
            if not match:
                if f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）" in text and "**★1直接対応**：なし" in text:
                    already.append(filename)
                    continue
                raise SystemExit(f"{filename}: legacy block not found")

        start, end = block_bounds(text, match)
        new_text = text[:start] + replacement + text[end:]
        if new_text != text:
            changed.append(filename)
            if args.write:
                path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: changed={len(changed)}, already={len(already)}")
    for name in changed:
        target = DIRECT.get(name, "supplemental-no-direct-star1")
        print(f"CHANGE {name} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
