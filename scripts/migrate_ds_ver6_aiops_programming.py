#!/usr/bin/env python3
"""Migrate reviewed legacy AI-utilization AIOps/MLOps and programming pages.

AIOps/MLOps pages are mapped to official ver.6 ★1 items. Constructor and
encapsulation remain useful programming background but do not have same-theme
★1 items in the ver.6 exam list, so they are marked as supplemental learning.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

DIRECT: dict[str, tuple[str, str, tuple[str, ...]]] = {
    "aiops.md": ("dataengineering", "environment-setup", ("dataengineering-0169",)),
    "mlops.md": ("dataengineering", "environment-setup", ("dataengineering-0162",)),
    "aiops-mlops-cheatsheet.md": (
        "dataengineering",
        "environment-setup",
        ("dataengineering-0162", "dataengineering-0169"),
    ),
}

SUPPLEMENTAL: dict[str, tuple[str, str, str]] = {
    "constructor.md": ("dataengineering", "programming", "オブジェクト指向プログラミングの補助学習"),
    "encapsulation.md": ("dataengineering", "programming", "オブジェクト指向プログラミングの補助学習"),
}

LEGACY_HEADING = re.compile(r"^## 対応スキル項目（AI利活用スキルシート）\s*$", re.MULTILINE)
AREA_LABEL = {"dataengineering": "データエンジニアリング"}
AREA_PAGE = {"dataengineering": "/ds/engineering-skillcheck/"}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


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


def canonical_block(rows: list[dict[str, str]]) -> str:
    area = rows[0]["area"]
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]
    for key, label in (("section", "分類"), ("category", "スキルカテゴリ"), ("subcategory", "サブカテゴリ")):
        values = {normalize(row.get(key, "")) for row in rows if normalize(row.get(key, ""))}
        if len(values) == 1:
            lines.append(f"- **{label}**：{next(iter(values))}")
    if len(rows) == 1:
        required = normalize(rows[0].get("required_skill", "")) or "—"
        lines.extend([f"- **必須スキル**：{required}", f"- ★ {normalize(rows[0]['item'])}"])
    else:
        for row in rows:
            required = normalize(row.get("required_skill", "")) or "—"
            lines.append(f"- ★ {normalize(row['item'])}（必須スキル：{required}）")
    lines.extend([f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})", ""])
    return "\n".join(lines)


def supplemental_block(position: str) -> str:
    return "\n".join([
        "## 対応スキル項目（ver.6 データエンジニアリング）",
        "",
        f"- **位置づけ**：{position}",
        "- **★1直接対応**：なし",
        "- ver.6の★1一覧にはこの用語自体の直接項目はありません。プログラミング基礎の理解を補う学習テーマとして整理します。",
        "- [ver.6 ★1スキルチェックで確認する](/ds/engineering-skillcheck/)",
        "",
    ])


def replace_block(text: str, block: str, filename: str) -> str | None:
    match = LEGACY_HEADING.search(text)
    if not match:
        return None
    start, end = bounds(text, match)
    return text[:start] + block + text[end:]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rows = json.loads(DATA.read_text(encoding="utf-8"))
    by_id = {row["item_id"]: row for row in rows}
    changed: list[str] = []
    already: list[str] = []

    for filename, (area, section, item_ids) in DIRECT.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        if meta.get("ds_area") != area or meta.get("ds_section") != section:
            raise SystemExit(f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')}")
        mapped = []
        for item_id in item_ids:
            row = by_id.get(item_id)
            if not row or row.get("area") != area:
                raise SystemExit(f"{filename}: official item mismatch {item_id}")
            mapped.append(row)
        new_text = replace_block(text, canonical_block(mapped), filename)
        if new_text is None:
            heading = f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）"
            if heading in text and all(normalize(row["item"]) in text for row in mapped):
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: legacy block not found")
        changed.append(filename)
        if args.write:
            path.write_text(new_text, encoding="utf-8")

    for filename, (area, section, position) in SUPPLEMENTAL.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        if meta.get("ds_area") != area or meta.get("ds_section") != section:
            raise SystemExit(f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')}")
        new_text = replace_block(text, supplemental_block(position), filename)
        if new_text is None:
            if "## 対応スキル項目（ver.6 データエンジニアリング）" in text and "**★1直接対応**：なし" in text:
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: legacy block not found")
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
