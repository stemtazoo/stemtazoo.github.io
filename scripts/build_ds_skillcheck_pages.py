#!/usr/bin/env python3
"""Generate DS検定 ver.6 ★1 skill-check pages from normalized JSON.

The source of truth is data/skillcheck/exports/exam_star1_latest.json.
Generated pages preserve important legacy URLs while presenting the current
2026 exam structure: foundation, value creation, data science, data engineering.
"""

from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"
DS_DIR = ROOT / "pages" / "ds"
TODAY = "2026-09-05"

AREAS = OrderedDict([
    ("foundation", {
        "label": "基盤",
        "count": 21,
        "path": "foundation-skillcheck.md",
        "permalink": "/ds/foundation-skillcheck/",
        "description": "DS検定リテラシーのver.6「基盤」★1チェック項目を一覧で確認するページです。行動規範、論理的思考、課題定義、データ理解、ITセキュリティ、生成AIなどを公式スキルチェックリストver.6に沿って整理します。",
        "intro": "従来の『ビジネス力』の多くが移った領域です。**考え方・判断・データの扱い方の土台**を確認します。",
    }),
    ("value-creation", {
        "label": "価値創造",
        "count": 51,
        "path": "value-creation-skillcheck.md",
        "permalink": "/ds/value-creation-skillcheck/",
        "description": "DS検定リテラシーのver.6「価値創造」★1チェック項目を一覧で確認するページです。課題の再定義、事業設計、AI・データ活用企画、ガバナンス、PoC、効果測定などを整理します。",
        "intro": "ver.6で明確になった新しい試験領域です。**データやAIを事業価値につなげる判断**を確認します。",
    }),
    ("datascience", {
        "label": "データサイエンス",
        "count": 108,
        "path": "datascience-skillcheck.md",
        "permalink": "/ds/datascience-skillcheck/",
        "description": "DS検定リテラシーのver.6「データサイエンス」★1チェック項目を一覧で確認するページです。数学・統計、データ準備、可視化、モデル化、非構造化データなどを整理します。",
        "intro": "数学・統計からモデル化まで、**データを分析して意味を取り出す力**を確認します。",
    }),
    ("dataengineering", {
        "label": "データエンジニアリング",
        "count": 58,
        "path": "engineering-skillcheck.md",
        "permalink": "/ds/engineering-skillcheck/",
        "description": "DS検定リテラシーのver.6「データエンジニアリング」★1チェック項目を一覧で確認するページです。環境構築、収集、構造、蓄積、加工、共有、プログラミング、セキュリティなどを整理します。",
        "intro": "データ収集・蓄積・加工・共有など、**分析できる状態を作り、安定して扱う力**を確認します。",
    }),
])


def esc(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def frontmatter(title: str, description: str, permalink: str) -> str:
    return f'''---
layout: page
title: {title}
description: "{description.replace('"', '\\"')}"
permalink: {permalink}
categories: [business]
tags: [ds, skillcheck, ver6]
last_modified_at: {TODAY}
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a> ＞ <a href="/ds/skillcheck/">ver.6スキルチェック</a> ＞ {{{{ page.title }}}}
</div>
'''


def group_rows(rows: list[dict[str, str]], area: str):
    grouped: OrderedDict[tuple[str, str], list[dict[str, str]]] = OrderedDict()
    for row in rows:
        if area == "value-creation":
            primary = row.get("phase") or row.get("category") or "その他"
            secondary_parts = [row.get("category", ""), row.get("subcategory", "")]
        else:
            primary = row.get("section") or row.get("category") or "その他"
            secondary_parts = [row.get("category", ""), row.get("subcategory", "")]
        secondary = "｜".join(x for x in secondary_parts if x and x != primary) or primary
        grouped.setdefault((primary, secondary), []).append(row)
    return grouped


def build_area(area: str, cfg: dict[str, object], rows: list[dict[str, str]]) -> str:
    title = f"DS検定 ver.6｜{cfg['label']} ★1スキルチェック"
    out = [frontmatter(title, str(cfg["description"]), str(cfg["permalink"]))]
    out += [
        "\n## このページについて\n",
        f"公式 **スキルチェックリスト ver.6.00** のうち、2026年DS検定の対象となる **{cfg['label']}・★1（見習い） {len(rows)}項目**を一覧にしています。\n",
        f"{cfg['intro']}\n",
        "> **判断のコツ**：項目を丸暗記するより、「この説明は何を判断できればよいか」を確認してください。\n",
        "<div style=\"display:flex;gap:8px;flex-wrap:wrap;margin:16px 0 22px;\">",
    ]
    for key, other in AREAS.items():
        out.append(f'<a href="{other["permalink"]}" style="padding:8px 12px;border:1px solid #cbd5e1;border-radius:999px;text-decoration:none;">{other["label"]}（{other["count"]}）</a>')
    out += ["</div>\n", "---\n"]

    last_primary = None
    for (primary, secondary), items in group_rows(rows, area).items():
        if primary != last_primary:
            out.append(f"\n## {esc(primary)}\n")
            last_primary = primary
        if secondary != primary:
            out.append(f"\n### {esc(secondary)}\n")
        out.append("\n| 必須 | ★1 チェック項目 |\n|---|---|\n")
        for row in items:
            required = "○" if row.get("required_skill") in {"○", "〇"} else ""
            out.append(f"| {required} | {esc(row.get('item', ''))} |\n")

    out += [
        "\n---\n",
        "## 公式資料\n",
        "- [データサイエンティスト スキルチェックリスト ver.6.00](https://www.datascientist.or.jp/common/docs/skillcheck_ver6.00.xlsx)\n",
        "- [DS検定とは](https://www.datascientist.or.jp/dscertification/what/)\n",
        "\n> `○` はスキルレベル判定上の必須スキルです。DS検定の出題範囲を `○` の項目だけに限定する意味ではありません。\n",
    ]
    return "".join(out)


def build_overview(rows: list[dict[str, str]]) -> str:
    title = "DS検定 ver.6｜★1スキルチェック 4領域まとめ"
    desc = "DS検定リテラシーの2026年試験範囲を、スキルチェックリストver.6の★1全238項目に沿って、基盤、価値創造、データサイエンス、データエンジニアリングの4領域に整理します。"
    out = [frontmatter(title, desc, "/ds/skillcheck/")]
    out += [
        "\n## まず結論\n",
        "2026年のDS検定では、公式スキルチェックリスト ver.6 の **★1（見習い）** を中心に学習します。ブログでは試験対象を次の4領域、**合計238項目**として整理します。\n\n",
        "| 領域 | ★1項目 | 学習ページ |\n|---|---:|---|\n",
    ]
    for area, cfg in AREAS.items():
        actual = sum(1 for r in rows if r.get("area") == area)
        out.append(f"| {cfg['label']} | {actual} | [確認する]({cfg['permalink']}) |\n")
    out += [
        "| **合計** | **238** | |\n\n",
        "> **ver.5からの大きな変更**：旧「ビジネス力」の多くは「基盤」へ移り、「価値創造」が試験領域として加わりました。旧「AI利活用」は独立した試験領域ではなく、ver.6では複数領域に組み込まれています。\n",
        "\n## おすすめの確認順\n",
        "1. **基盤**：判断の土台を確認する\n2. **データサイエンス**：統計・分析・モデル化を確認する\n3. **データエンジニアリング**：データを扱う仕組みを確認する\n4. **価値創造**：分析やAIを事業価値につなげる判断を確認する\n",
        "\n## このページの使い方\n",
        "各領域ページでは、公式Excelの★1チェック項目をカテゴリ別に並べています。**知らない用語を探す一覧ではなく、自分が説明・判断できるかを確認する基準表**として使うのがおすすめです。\n",
        "\n---\n## 公式資料\n",
        "- [スキルチェックリスト ver.6.00](https://www.datascientist.or.jp/common/docs/skillcheck_ver6.00.xlsx)\n",
        "- [DS検定とは](https://www.datascientist.or.jp/dscertification/what/)\n",
    ]
    return "".join(out)


def build_legacy_page(kind: str) -> str:
    if kind == "business":
        title = "旧『ビジネス力』スキルチェックについて｜DS検定 ver.6"
        desc = "DS検定ver.5までのビジネス力と、ver.6の基盤・価値創造への移行関係を案内するページです。"
        permalink = "/ds/business-skillcheck/"
        body = '''\n## ver.6では「ビジネス力」は2つに分かれます\n\n旧ver.5までの「ビジネス力」は、そのまま1領域として扱われません。ver.6では主に、\n\n- **基盤**：論理的思考、行動規範、課題定義、データ理解など\n- **価値創造**：事業設計、プロジェクト推進、ガバナンス、PoC、効果測定など\n\nへ整理されています。\n\n- [基盤 ★1スキルチェック](/ds/foundation-skillcheck/)\n- [価値創造 ★1スキルチェック](/ds/value-creation-skillcheck/)\n- [ver.6 ★1スキルチェック全体](/ds/skillcheck/)\n'''
    else:
        title = "旧『AI利活用スキル』について｜DS検定 ver.6"
        desc = "DS検定ver.5までのAI利活用スキルと、ver.6で複数領域へ統合された学習範囲を案内するページです。"
        permalink = "/ds/ai-utilization-skillcheck/"
        body = '''\n## ver.6では「AI利活用」は独立した1領域ではありません\n\n旧ver.5の「AI利活用スキル」は、ver.6では**基盤・価値創造・データサイエンス・データエンジニアリングなど複数領域へ統合**されています。\n\n生成AIの基礎だけを独立して覚えるのではなく、\n\n- AIを安全・適切に使う → **基盤**\n- AIを事業へ適用する → **価値創造**\n- モデルや分析を理解する → **データサイエンス**\n- AIシステムを実装・運用する → **データエンジニアリング**\n\nという役割で切り分けて学習してください。\n\n- [ver.6 ★1スキルチェック全体](/ds/skillcheck/)\n- [基盤 ★1スキルチェック](/ds/foundation-skillcheck/)\n- [価値創造 ★1スキルチェック](/ds/value-creation-skillcheck/)\n'''
    return frontmatter(title, desc, permalink) + body


def main() -> int:
    rows = json.loads(SOURCE.read_text(encoding="utf-8"))
    if len(rows) != 238:
        raise SystemExit(f"Expected 238 ★1 rows, got {len(rows)}")
    if any(row.get("skill_level") != "★" for row in rows):
        raise SystemExit("exam_star1_latest.json contains a non-★ row")

    DS_DIR.mkdir(parents=True, exist_ok=True)
    (DS_DIR / "skillcheck.md").write_text(build_overview(rows), encoding="utf-8")

    for area, cfg in AREAS.items():
        area_rows = [row for row in rows if row.get("area") == area]
        if len(area_rows) != cfg["count"]:
            raise SystemExit(f"{area}: expected {cfg['count']}, got {len(area_rows)}")
        (DS_DIR / str(cfg["path"])).write_text(build_area(area, cfg, area_rows), encoding="utf-8")

    (DS_DIR / "business-skillcheck.md").write_text(build_legacy_page("business"), encoding="utf-8")
    (DS_DIR / "ai-utilization-skillcheck.md").write_text(build_legacy_page("ai"), encoding="utf-8")

    print("Generated DS ver.6 skillcheck pages: overview + 4 areas + 2 legacy guides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
