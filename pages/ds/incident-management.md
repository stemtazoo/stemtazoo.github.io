---
layout: page
title: インシデント管理とは？障害対応と報告の基本【DS検定】
description: "インシデント管理とは、システム障害・セキュリティ問題・業務トラブルなど、発生した問題を早期に把握し、報告・対応・復旧へつなげる管理活動です。リスクマネジメントとの違い、レポートライン、DS検定での判断基準を整理します。"
permalink: /ds/incident-management/
categories: [business]
tags: [ds, design]
ds_area: value-creation
ds_section: governance-risk
prev: /ds/compliance-risk/
next: /ds/internal-control/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**インシデント管理とは、発生した問題を早く把握し、報告・対応・復旧へつなげる管理活動**です。

DS検定では、**問題が起きる前のリスク管理**と、**起きた後のインシデント対応**を切り分けられることが重要です。

## 直感的な説明

例えば、次のような出来事が起きたとします。

- サーバが停止した
- データ処理に失敗した
- 情報漏えいの疑いがある
- 分析結果に重大な誤りが見つかった

このとき重要なのは、個人で抱え込まず、**正式な報告経路で共有し、組織として対応すること**です。

## 定義・仕組み

### インシデントとは

業務やサービスへ悪影響を与える、または与える可能性がある出来事です。

重大事故だけでなく、早期対応が必要な小さな異常も対象になります。

### 基本的な対応の流れ

1. インシデントを発見する
2. レポートラインへ報告する
3. 影響範囲を確認する
4. 対応・復旧する
5. 原因を確認する
6. 必要に応じて再発防止へつなげる

DS検定では、特に**「まず報告する」**という行動が重要です。

### リスクマネジメントとの違い

| 概念 | 主なタイミング | 役割 |
|---|---|---|
| リスクマネジメント | 問題が起きる前 | リスクを特定・評価・低減する |
| インシデント管理 | 問題が起きた後 | 報告・対応・復旧する |

## どんな場面で使う？

### ITシステム

- サーバ障害
- ネットワーク障害
- データベース停止

### 情報セキュリティ

- 不正アクセス
- 情報漏えい
- マルウェア感染

### データ分析

- データ欠損
- バッチ処理失敗
- モデル異常
- 分析結果の誤り

## よくある誤解・混同

### ❌ 重大事故だけがインシデント

小さな異常でも、業務へ影響する可能性があれば早期報告の対象になります。

### ❌ 自分で解決してから報告する

問題を抱え込むと対応が遅れます。**発見した時点で適切に報告する**ことが基本です。

### ❌ インシデント管理 = リスクマネジメント

| 用語 | 判断基準 |
|---|---|
| リスクマネジメント | まだ起きていない問題を事前に管理 |
| インシデント管理 | 起きた問題へ対応 |

### ❌ IT部門だけの仕事

インシデントは、IT・データ分析・業務プロセスなど組織全体で発生します。

## まとめ（試験直前用）

- **インシデント = 業務やサービスに影響する問題・異常**
- **インシデント管理 = 発生後の報告・対応・復旧**
- 問題を発見したら、まず適切なレポートラインへ報告する
- 小さな異常も早期対応する
- **事前の管理 = リスクマネジメント / 発生後の対応 = インシデント管理**

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
