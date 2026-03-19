---
layout: page
title: PDCAサイクルとは？継続的改善の基本フレームワーク【DS検定】
permalink: /ds/pdca-cycle/
categories: [business]
tags: [ds, design]
prev: /ds/critical-path/
next: /ds/poc-concept-proof/
---

## まず結論

**PDCAサイクル（PDCA Cycle）**とは、計画→実行→評価→改善の4つのステップを繰り返して業務や品質を改善していくフレームワークです。

DS検定では 継続的な業務改善の基本的な考え方として出題されることが多いです。


試験では特に

PoC

KPI


などと混同させる問題が出ることがあります。



## 直感的な説明

例えばECサイトの売上を改善したいとします。

まず

Plan（計画）

新しいキャンペーンを計画する


次に

Do（実行）

実際にキャンペーンを実施する


その後

Check（評価）

売上やアクセスデータを分析する


最後に

Act（改善）

結果をもとに次の施策を改善する


このように

計画→実行→評価→改善

を繰り返すことで

業務を継続的に改善していきます。

これが PDCAサイクル です。



## 定義・仕組み

PDCAは次の4つのステップで構成されます。

Plan（計画）

改善のための目標や計画を立てます。

例

売上を10%増やす




Do（実行）

計画を実際に実行します。

例

新しい広告キャンペーンを実施




Check（評価）

結果をデータで評価します。

例

売上データ

アクセスログ




Act（改善）

評価結果をもとに改善します。

例

成功した施策を強化

効果が低い施策を修正




このサイクルを繰り返すことで

継続的な改善（Continuous Improvement）

が可能になります。



## どんな場面で使う？

品質管理

製造業では品質改善のために使われます。



データドリブン経営

データを分析しながら

改善施策

業務改善


を行うときに活用されます。



プロジェクト管理

業務やプロジェクトの改善にも使われます。



## よくある誤解・混同

PoCとの違い

DS検定では次の混同がよく出ます。

概念	内容

PoC	技術やアイデアの実現可能性を検証
PDCA	業務改善のサイクル


つまり

PoC → 実現できるか試す

PDCA → 改善を繰り返す


という違いがあります。



KPIとの関係

KPIは

**Check（評価）**の段階で

進捗を確認する指標として使われます。



## まとめ（試験直前用）

PDCAは 継続的改善のフレームワーク

Plan → Do → Check → Act

計画・実行・評価・改善のサイクル

PoCは 実現可能性の検証

KPIは 進捗管理指標


DS検定では

> 「計画→実行→評価→改善」



と書かれていたら

PDCAサイクルと判断するのがポイントです。



【対応スキル項目（ビジネス力シート）】

ビジネス理解

データ活用

★ データを活用した意思決定の重要性を理解している

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>
