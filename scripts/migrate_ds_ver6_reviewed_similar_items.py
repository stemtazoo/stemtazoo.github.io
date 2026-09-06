#!/usr/bin/env python3
"""Migrate manually reviewed legacy DS skill blocks to official ver.6 items.

Mappings are explicit filename -> official ver.6 item_id (or item_id tuple) pairs.
A small reviewed supplemental group is also supported for legacy topics that are
still useful to learn but no longer have a direct ★1 item in ver.6. Already-
migrated mappings are accepted so the script remains idempotent.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

REVIEWED: dict[str, str | tuple[str, ...] | None] = {
    "nosql.md": "dataengineering-0069",
    "spark.md": "dataengineering-0068",
    "yarn.md": "dataengineering-0068",
    "visualization-basic-perspectives.md": "datascience-0153",
    "malware.md": "foundation-0032",
    "rdb-vs-nosql.md": "dataengineering-0069",
    "analysis-approach-selection.md": "datascience-0075",
    "causal-inference.md": "datascience-0017",
    "bcp.md": "value-creation-0049",
    "risk-management.md": "value-creation-0049",
    "operational-risk.md": "value-creation-0049",
    "incident-management.md": "value-creation-0049",
    "data-mart.md": "dataengineering-0080",
    "data-warehouse-vs-datamart.md": "dataengineering-0080",
    "analysis-approach-design.md": "foundation-0002",
    "revenue-equation.md": "foundation-0016",
    "hallucination.md": ("foundation-0017", "foundation-0018"),
    "kpi-kgi.md": "foundation-0016",
    "poc-concept-proof.md": "value-creation-0037",
    "pdca-cycle.md": "value-creation-0115",
    "pest-analysis.md": "value-creation-0001",
    "five-forces-analysis.md": "value-creation-0031",
    "swot-analysis.md": "value-creation-0031",
    "internal-control.md": "value-creation-0052",
    "data-governance.md": "value-creation-0052",
    "governance.md": "value-creation-0094",
    "customer-journey.md": "value-creation-0010",
    "design-thinking.md": "value-creation-0016",
    # ver.5では「プロジェクト推進／リソースマネジメント」に紐づいていたが、
    # ver.6 ★1（238項目）には同内容の直接項目がないため補助学習として残す。
    "agile-development.md": None,
    "critical-path.md": None,
    "gantt-chart.md": None,
    "project-management.md": None,
    "scrum.md": None,
    "wbs.md": None,
}

LEGACY_LABELS = (
    "ビジネス力シート",
    "AI利活用スキルシート",
    "データサイエンス力シート",
    "データエンジニアリング力シート",
)
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
    end = after + nxt.start() if nxt else len(text)
    return match.start(), end


def canonical_block(rows: list[dict[str, str]]) -> str:
    first = rows[0]
    area = first["area"]
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]

    common_fields = (
        ("phase", "フェーズ"),
        ("section", "分類"),
        ("category", "スキルカテゴリ"),
        ("subcategory", "サブカテゴリ"),
    )
    for key, label in common_fields:
        values = {normalize(row.get(key, "")) for row in rows if normalize(row.get(key, ""))}
        if len(values) == 1:
            lines.append(f"- **{label}**：{next(iter(values))}")

    if len(rows) == 1:
        required = normalize(first.get("required_skill", "")) or "—"
        lines.extend([
            f"- **必須スキル**：{required}",
            f"- ★ {normalize(first['item'])}",
        ])
    else:
        for row in rows:
            required = normalize(row.get("required_skill", "")) or "—"
            lines.append(f"- ★ {normalize(row['item'])}（必須スキル：{required}）")

    lines.extend([
        f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})",
        "",
    ])
    return "\n".join(lines)


def supplemental_block() -> str:
    return "\n".join([
        "## 対応スキル項目（ver.6 価値創造）",
        "",
        "- **位置づけ**：プロジェクト推進の補助学習",
        "- **★1直接対応**：なし",
        "- 旧ver.5の「プロジェクト推進／リソースマネジメント」にあった内容は、ver.6の★1一覧には同一内容の項目として掲載されていません。",
        "- [ver.6 ★1スキルチェックで確認する](/ds/value-creation-skillcheck/)",
        "",
    ])


def mapping_ids(value: str | tuple[str, ...] | None) -> tuple[str, ...]:
    if value is None:
        return ()
    return (value,) if isinstance(value, str) else tuple(value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rows = json.loads(DATA.read_text(encoding="utf-8"))
    by_id = {row["item_id"]: row for row in rows}
    changed: list[str] = []
    already: list[str] = []

    for filename, mapping in REVIEWED.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)

        if mapping is None:
            if meta.get("ds_area") != "value-creation" or meta.get("ds_section") != "project-management":
                raise SystemExit(
                    f"{filename}: supplemental metadata mismatch "
                    f"{meta.get('ds_area')}/{meta.get('ds_section')}"
                )
            match = HEADING_RE.search(text)
            if not match:
                if (
                    "## 対応スキル項目（ver.6 価値創造）" in text
                    and "**★1直接対応**：なし" in text
                ):
                    already.append(filename)
                    continue
                raise SystemExit(f"{filename}: neither legacy nor supplemental ver.6 block found")
            start, end = bounds(text, match)
            new_text = text[:start] + supplemental_block() + text[end:]
            if new_text != text:
                changed.append(filename)
                if args.write:
                    path.write_text(new_text, encoding="utf-8")
            continue

        item_ids = mapping_ids(mapping)
        mapped_rows: list[dict[str, str]] = []
        for item_id in item_ids:
            row = by_id.get(item_id)
            if not row:
                raise SystemExit(f"{filename}: official item not found: {item_id}")
            mapped_rows.append(row)

        areas = {row.get("area") for row in mapped_rows}
        if len(areas) != 1:
            raise SystemExit(f"{filename}: mapped items span multiple areas: {sorted(areas)}")
        area = mapped_rows[0]["area"]

        if meta.get("ds_area") != area:
            raise SystemExit(f"{filename}: ds_area mismatch {meta.get('ds_area')} != {area}")

        match = HEADING_RE.search(text)
        if not match:
            canonical_heading = f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）"
            expected_items = [f"★ {normalize(row['item'])}" for row in mapped_rows]
            if canonical_heading in text and all(item in text for item in expected_items):
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: neither legacy nor expected ver.6 skill block found")

        start, end = bounds(text, match)
        block = text[start:end]
        stars = re.findall(r"^(?:[-*+]\s*)?★\s*(.+?)\s*$", block, re.MULTILINE)
        if len(stars) < 1:
            raise SystemExit(f"{filename}: expected at least one legacy ★ item, got 0")

        new_text = text[:start] + canonical_block(mapped_rows) + text[end:]
        if new_text != text:
            changed.append(filename)
            if args.write:
                path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: reviewed migrations={len(changed)}, already={len(already)}")
    for filename in changed:
        ids = mapping_ids(REVIEWED[filename])
        target = ",".join(ids) if ids else "supplemental-no-direct-star1"
        print(f"CHANGE {filename} -> {target}")
    for filename in already:
        ids = mapping_ids(REVIEWED[filename])
        target = ",".join(ids) if ids else "supplemental-no-direct-star1"
        print(f"ALREADY {filename} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
