---
layout: page
title: BCP（事業継続計画）とは？災害時でも業務を止めない仕組み【DS検定】
description: "BCP（事業継続計画）は、災害・事故・システム障害などの非常事態でも重要業務を継続し、早期復旧するための計画です。リスクマネジメントやインシデント管理との違いを整理し、DS検定での判断基準を確認します。"
permalink: /ds/bcp/
categories: [business]
tags: [ds, design]
prev: /ds/swot-analysis/
next: /ds/compliance-risk/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**BCP（Business Continuity Plan：事業継続計画）**とは、非常事態が起きても、重要な業務を継続または早期復旧するための計画です。

DS検定では、**「非常事態でも事業を続ける・早く戻す」**という目的を見抜くことがポイントです。

## 直感的な説明

企業の活動は、次のような出来事で突然止まる可能性があります。

- 地震・台風などの自然災害
- サイバー攻撃
- 大規模システム障害
- パンデミック

何の準備もなければ、サービス停止・売上減少・顧客離れにつながります。

そこで、**「止まったときに何を優先し、どう復旧するか」を事前に決めておく**のがBCPです。

## 定義・仕組み

BCPでは、非常時に備えて主に次を決めます。

| 項目 | 例 |
|---|---|
| 優先業務 | 何を最初に復旧するか |
| 代替手段 | 代替システム・代替拠点 |
| 連絡体制 | 誰が誰へ連絡するか |
| 復旧手順 | どの順番で業務を戻すか |

流れで見ると、**非常事態 → 影響確認 → BCPに基づく継続・復旧**です。

## どんな場面で使う？

### 自然災害

- 地震
- 台風
- 洪水

### IT・セキュリティ障害

- データセンター停止
- クラウド障害
- サイバー攻撃
- ランサムウェア

### 社会的な非常事態

- パンデミック
- 大規模停電

BCPはIT部門だけでなく、**経営・業務・ITを含む企業全体の計画**です。

## よくある誤解・混同

### BCPとリスクマネジメント

| 概念 | 主な役割 |
|---|---|
| リスクマネジメント | リスクを特定・評価・対応する |
| BCP | 重大な事象が起きても事業を継続・復旧する |

### BCPとインシデント管理

| 概念 | 主な役割 |
|---|---|
| インシデント管理 | 発生した問題を報告・対応・復旧する |
| BCP | 重要事業を止めない・早く戻すための事前計画 |

### ❌ BCPはITだけの計画

BCPは業務・人員・拠点・取引先なども含む、**事業全体の継続計画**です。

## まとめ（試験直前用）

- BCP = **事業継続計画**
- 非常事態でも重要業務を継続・早期復旧する
- 代替拠点・代替システム・連絡体制などを事前に決める
- リスクマネジメント = リスクを管理する活動
- **「非常時でも事業を続ける」ならBCP**

## 対応スキル項目（ビジネス力シート）

- スキルカテゴリ：活動マネジメント
- サブカテゴリ：リスクマネジメント
- ★ 担当するタスクの遅延や障害などを発見した場合、迅速かつ適切に報告ができる

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}
{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}
    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}{% assign matched = true %}{% endif %}
    {% endfor %}
    {% if matched %}
      <li style="margin-bottom: 6px;"><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% assign count = count | plus: 1 %}
    {% endif %}
    {% if count >= 5 %}{% break %}{% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>
<div style="margin-top: 16px;">🏠 <a href="/ds/">DS検定トップに戻る</a></div>
<div style="display:flex;justify-content:space-between;margin-top:12px;">
  {% if page.previous.url %}<a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>{% endif %}
  {% if page.next.url %}<a href="{{ page.next.url }}">{{ page.next.title }} →</a>{% endif %}
</div>
