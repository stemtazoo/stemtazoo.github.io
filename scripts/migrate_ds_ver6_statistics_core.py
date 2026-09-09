#!/usr/bin/env python3
"""Migrate reviewed legacy DS statistics skill blocks to skillcheck ver.6."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

DIRECT = {
    "bayes-theorem.md": "datascience-0024",
    "quartile.md": "datascience-0014",
    "variance-and-standard-deviation.md": "datascience-0014",
    "variance-standard-deviation.md": "datascience-0014",
    "normal-and-standard-normal.md": "datascience-0016",
}

SUPPLEMENTAL = {
    "bernoulli-binomial.md": "ベルヌーイ試行・二項分布の基礎補助学習",
    "binomial-bernoulli.md": "ベルヌーイ試行・二項分布の基礎補助学習",
}

HEADING = re.compile(r"^## 対応スキル項目（データサイエンス力シート）\s*$", re.MULTILINE)


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
    lines = ["## 対応スキル項目（ver.6 データサイエンス）", ""]
    for key, label in (("phase", "フェーズ"), ("section", "分類"), ("category", "スキルカテゴリ"), ("subcategory", "サブカテゴリ")):
        value = normalize(row.get(key, ""))
        if value:
            lines.append(f"- **{label}**：{value}")
    required = normalize(row.get("required_skill", "")) or "—"
    lines += [
        f"- **必須スキル**：{required}",
        f"- ★ {normalize(row['item'])}",
        "- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)",
        "",
    ]
    return "\n".join(lines)


def supplemental_block(position: str) -> str:
    return "\n".join([
        "## 対応スキル項目（ver.6 データサイエンス）",
        "",
        f"- **位置づけ**：{position}",
        "- **★1直接対応**：なし",
        "- ver.6の★1には二項分布の正規近似に関する項目がありますが、この記事はベルヌーイ試行・二項分布そのものの基礎理解が中心のため、補助学習として整理します。",
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

    for filename in list(DIRECT) + list(SUPPLEMENTAL):
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        if meta.get("ds_area") != "datascience" or meta.get("ds_section") != "statistics":
            raise SystemExit(f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')}")
        match = HEADING.search(text)

        if filename in DIRECT:
            row = by_id.get(DIRECT[filename])
            if not row:
                raise SystemExit(f"{filename}: missing official item {DIRECT[filename]}")
            replacement = direct_block(row)
            expected_item = f"★ {normalize(row['item'])}"
            if not match:
                if "## 対応スキル項目（ver.6 データサイエンス）" in text and expected_item in text:
                    already.append(filename)
                    continue
                raise SystemExit(f"{filename}: legacy block not found")
        else:
            replacement = supplemental_block(SUPPLEMENTAL[filename])
            if not match:
                if "## 対応スキル項目（ver.6 データサイエンス）" in text and "**★1直接対応**：なし" in text:
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
        print(f"CHANGE {name} -> {DIRECT.get(name, 'supplemental-no-direct-star1')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
