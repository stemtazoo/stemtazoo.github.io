#!/usr/bin/env python3
"""Generate an exact DS ver.6 classification audit from pages/ds.

The report separates ordinary article pages from known cross-area/index pages so
progress is not understated by pages that should not receive a single ds_area.
Run this script whenever reviewed mappings or exclusions change.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
OUT = ROOT / "docs" / "audits" / "ds-ver6-unclassified.md"

EXCLUDED = {
    "index.md",
    "optional-math-algorithm.md",
    "business-skillcheck.md",
    "engineering-skillcheck.md",
    "skillcheck.md",
    "ai-utilization-skillcheck.md",
    "model-curriculum-summary.md",
    "skilllevel-2023-summary.md",
    "skilllevel-2023-assistant-ds-business.md",
    "skilllevel-2023-assistant-ds-dataengineering.md",
    "skilllevel-2023-assistant-ds-datascience.md",
    "file-transfer-protocol.md",
}


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def main() -> int:
    files = sorted(p for p in DS_DIR.glob("*.md") if p.is_file())
    classified = []
    unclassified = []
    excluded_present = []

    for path in files:
        meta = front_matter(path)
        row = (path.name, meta.get("title", ""), meta.get("ds_area", ""), meta.get("ds_section", ""))
        if path.name in EXCLUDED:
            excluded_present.append(row)
        elif meta.get("ds_area") and meta.get("ds_section"):
            classified.append(row)
        else:
            unclassified.append(row)

    ordinary_total = len(classified) + len(unclassified)
    progress = (len(classified) / ordinary_total * 100) if ordinary_total else 0.0

    lines = [
        "# DS検定 ver.6 未分類監査",
        "",
        "> `scripts/audit_ds_ver6_classification.py` により自動生成。",
        "",
        "## 集計",
        "",
        f"- `pages/ds/*.md` 総数: **{len(files)}**",
        f"- 特殊ページ除外: **{len(excluded_present)}**",
        f"- 通常記事母数: **{ordinary_total}**",
        f"- 分類済み: **{len(classified)}**",
        f"- 未分類: **{len(unclassified)}**",
        f"- 通常記事の分類進捗: **{progress:.1f}%**",
        "",
        "## 未分類の通常記事",
        "",
    ]

    if unclassified:
        lines.extend(["| ファイル | title |", "|---|---|"])
        for name, title, _, _ in unclassified:
            lines.append(f"| `{name}` | {title} |")
    else:
        lines.append("未分類の通常記事はありません。")

    lines.extend(["", "## 分類母数から除外した特殊ページ", "", "| ファイル | title |", "|---|---|"])
    for name, title, _, _ in excluded_present:
        lines.append(f"| `{name}` | {title} |")

    missing_exclusions = sorted(EXCLUDED - {row[0] for row in excluded_present})
    if missing_exclusions:
        lines.extend(["", "## 除外リストにあるが現在存在しないページ", ""])
        lines.extend(f"- `{name}`" for name in missing_exclusions)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"total={len(files)} excluded={len(excluded_present)} ordinary={ordinary_total} classified={len(classified)} unclassified={len(unclassified)} progress={progress:.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
