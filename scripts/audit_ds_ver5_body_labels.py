#!/usr/bin/env python3
"""Audit legacy ver.5 skill-sheet labels remaining in DS article bodies.

This script does not modify articles. It reports ordinary DS articles that still
contain legacy sheet labels so ver.6 replacements can be reviewed safely.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
OUT = ROOT / "docs" / "audits" / "ds-ver5-body-labels.md"

LEGACY_LABELS = {
    "ビジネス力シート": "old-business",
    "AI利活用スキルシート": "old-ai-utilization",
    "データサイエンス力シート": "old-datascience",
    "データエンジニアリング力シート": "old-dataengineering",
}

EXCLUDED = {
    "index.md",
    "optional-math-algorithm.md",
    "business-skillcheck.md",
    "engineering-skillcheck.md",
    "skillcheck.md",
    "ai-utilization-skillcheck.md",
    "foundation-skillcheck.md",
    "value-creation-skillcheck.md",
    "datascience-skillcheck.md",
    "model-curriculum-summary.md",
    "skilllevel-2023-summary.md",
    "skilllevel-2023-assistant-ds-business.md",
    "skilllevel-2023-assistant-ds-dataengineering.md",
    "skilllevel-2023-assistant-ds-datascience.md",
    "file-transfer-protocol.md",
}


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


def main() -> int:
    rows = []
    counts = {key: 0 for key in LEGACY_LABELS}

    for path in sorted(DS_DIR.glob("*.md")):
        if path.name in EXCLUDED:
            continue
        text = path.read_text(encoding="utf-8-sig")
        matched = [label for label in LEGACY_LABELS if label in text]
        if not matched:
            continue
        meta = front_matter(text)
        for label in matched:
            counts[label] += 1
        rows.append(
            (
                path.name,
                meta.get("title", ""),
                meta.get("ds_area", ""),
                meta.get("ds_section", ""),
                " / ".join(matched),
            )
        )

    lines = [
        "# DS検定 ver.5 本文表記監査",
        "",
        "> `scripts/audit_ds_ver5_body_labels.py` により自動生成。通常記事本文に残る旧ver.5スキルシート名を検出します。",
        "",
        "## 集計",
        "",
        f"- 旧表記が残る通常記事: **{len(rows)}**",
    ]
    for label, count in counts.items():
        lines.append(f"- `{label}`: **{count}記事**")

    lines.extend([
        "",
        "## 修正方針",
        "",
        "旧見出しだけを機械的に名称変更しない。本文に列挙された旧チェック項目自体がver.6で移動・統合されている可能性があるため、`ds_area` / `ds_section` と公式ver.6の★1データを照合して記事単位で更新する。",
        "",
        "優先順は **基盤・価値創造（旧ビジネス/AI利活用からの再編）→ データサイエンス → データエンジニアリング** とする。",
        "",
        "## 対象記事",
        "",
        "| ファイル | title | ds_area | ds_section | 旧表記 |",
        "|---|---|---|---|---|",
    ])
    for filename, title, area, section, matched in rows:
        title = title.replace("|", "\\|")
        lines.append(f"| `{filename}` | {title} | `{area}` | `{section}` | {matched} |")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Legacy body-label articles: {len(rows)}")
    for label, count in counts.items():
        print(f"{label}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
