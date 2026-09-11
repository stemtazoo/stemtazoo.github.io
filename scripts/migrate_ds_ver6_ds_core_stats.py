#!/usr/bin/env python3
"""Migrate reviewed DS statistics, visualization, and evaluation pages to ver.6 ★1."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

DIRECT = {
    "bayes-theorem.md": ("statistics", "datascience-0024"),
    "design-of-experiments.md": ("data-preparation", "datascience-0102"),
    "correlation-and-causation.md": ("statistics", "datascience-0017"),
    "correlation-vs-causation.md": ("statistics", "datascience-0017"),
    "covariance-and-correlation.md": ("statistics", "datascience-0019"),
    "covariance-correlation.md": ("statistics", "datascience-0019"),
    "coefficient-of-determination-contribution.md": ("modeling", "datascience-0158"),
    "boxplot.md": ("visualization", "datascience-0014"),
    "power-law.md": ("statistics", "datascience-0023"),
    "chart-types.md": ("visualization", "datascience-0141"),
    "chi-square-distribution.md": ("statistics", "datascience-0020"),
    "discrete-continuous-distribution.md": ("statistics", "datascience-0020"),
    "evaluation-metrics-comparison.md": ("modeling", "datascience-0173"),
    "interpret-statistics.md": ("statistics", "datascience-0033"),
    "point-interval-estimation.md": ("statistics", "datascience-0050"),
    "type1-type2-error.md": ("statistics", "datascience-0052"),
    "student-t-test.md": ("statistics", "datascience-0054"),
    "welch-t-test.md": ("statistics", "datascience-0054"),
    "z-test.md": ("statistics", "datascience-0054"),
    "f-test.md": ("statistics", "datascience-0054"),
    # Individually reviewed multi-item legacy blocks retain only items supported by the article body.
    "paired-vs-independent-data.md": ("statistics", "datascience-0054"),
    "sample-variance-unbiased-variance.md": ("statistics", "datascience-0015"),
    "pearson-correlation.md": ("statistics", "datascience-0019"),
    "r-squared-adjusted-r-squared.md": ("modeling", "datascience-0159"),
    "spearman-rank-correlation.md": ("statistics", "datascience-0022"),
}

HEADING_RE = re.compile(r"^## 対応スキル項目（データ(?:サイエンス|エンジニアリング)力シート）\s*$", re.MULTILINE)


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
    lines = ["## 対応スキル項目（ver.6 データサイエンス）", ""]
    for key, label in (("section", "分類"), ("category", "スキルカテゴリ"), ("subcategory", "サブカテゴリ")):
        value = row.get(key, "").strip()
        if value:
            lines.append(f"- **{label}**：{value}")
    required = row.get("required_skill", "").strip() or "—"
    lines.extend([
        f"- **必須スキル**：{required}",
        f"- ★ {row['item'].strip()}",
        "- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rows = json.loads(DATA.read_text(encoding="utf-8"))
    by_id = {row["item_id"]: row for row in rows}
    changed: list[str] = []
    already: list[str] = []

    for filename, (section, item_id) in DIRECT.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        if meta.get("ds_area") != "datascience" or meta.get("ds_section") != section:
            raise SystemExit(f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')}")
        row = by_id.get(item_id)
        if not row or row.get("area") != "datascience":
            raise SystemExit(f"{filename}: official item mismatch {item_id}")
        match = HEADING_RE.search(text)
        if not match:
            if "## 対応スキル項目（ver.6 データサイエンス）" in text and row["item"] in text:
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: legacy DS skill block not found")
        start, end = bounds(text, match)
        new_text = text[:start] + canonical_block(row) + text[end:]
        changed.append(filename)
        if args.write:
            path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: changed={len(changed)}, already={len(already)}")
    for filename in changed:
        print(f"CHANGE {filename} -> {DIRECT[filename][1]}")
    for filename in already:
        print(f"ALREADY {filename} -> {DIRECT[filename][1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
