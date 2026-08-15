---
layout: page
title: クリティカルパスとは？プロジェクト遅延を左右する重要な経路【DS検定】
description: "クリティカルパス（Critical Path）とは、プロジェクト全体の完了時間を決める最も長い作業経路のことです。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。"
permalink: /ds/critical-path/
categories: [business]
tags: [ds, design]
prev: /ds/agile-development/
next: /ds/pdca-cycle/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**クリティカルパス（Critical Path）とは、プロジェクト全体の完了時間を決める最も長い作業経路**です。

DS検定では、**この経路上の作業が遅れると、プロジェクト全体の完了も遅れる**という点が重要です。

## 直感的な説明

例えば、データ分析プロジェクトに次の工程があるとします。

> データ取得 → 前処理 → 分析 → モデル評価 → レポート作成

すべての作業が同じように納期へ影響するわけではありません。

複数の作業ルートがある中で、**合計所要時間が最も長く、遅れがそのまま全体の遅れにつながる経路**がクリティカルパスです。

> **判断ポイント：** 「重要そうな作業」ではなく、**時間的に最も長い経路**を見るのがポイントです。

## 定義・仕組み

### ① 最も長い作業経路

例えば、次の2つの経路があるとします。

- A → B → C
- A → D → E

各作業の所要時間を合計し、**最も時間がかかる経路**がクリティカルパスになります。

### ② 遅れるとプロジェクト全体が遅れる

クリティカルパス上の作業には、通常ほとんど余裕時間がありません。

そのため、

- 作業が遅れる
- トラブルが発生する

と、プロジェクト全体の納期に影響します。

### ③ 重点的に管理する

プロジェクト管理では、クリティカルパス上のタスクを優先して監視します。

## どんな場面で使う？

### ① プロジェクトスケジュール管理

- どの作業が納期に直結するか
- どこが遅れると危険か

を把握するために使います。

### ② システム開発

要件定義、設計、開発、テストなどの工程の中から、**全体の完了時間を決める経路**を確認します。

### ③ データ分析プロジェクト

データ取得や前処理が後工程の前提になっている場合、その遅れが分析全体へ影響することがあります。

## よくある誤解・混同

### ❌ 重要な作業 = クリティカルパス

クリティカルパスは重要度ではなく、**所要時間と依存関係**で決まります。

### ❌ WBSやガントチャートと同じ

| 手法 | 主な役割 |
|---|---|
| WBS | 作業を分解する |
| ガントチャート | 作業の時間を可視化する |
| クリティカルパス | 全体納期を決める経路を把握する |

### ❌ すべての作業がクリティカル

余裕時間がある作業は、多少遅れてもプロジェクト全体の完了日に影響しない場合があります。

## まとめ（試験直前用）

- **クリティカルパス = プロジェクト完了時間を決める経路**
- **最も所要時間が長い経路**
- その経路上の作業が遅れると全体も遅れる
- WBS・ガントチャートとの役割の違いに注意

DS検定では、**「最も長い作業経路」「遅れると全体が遅れる」ならクリティカルパス**と判断しましょう。

## 対応スキル項目（ビジネス力シート）

- プロジェクト推進
- リソースマネジメント
- ★ 指示に従ってスケジュールを守り、チームリーダーに頼まれた自分の仕事を完遂できる

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

<hr>

<div style="margin-top: 16px;">
  🏠 <a href="/ds/">DS検定トップに戻る</a>
</div>

<div style="display:flex;justify-content:space-between;margin-top:12px;">

  {% if page.previous.url %}
    <a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url }}">{{ page.next.title }} →</a>
  {% endif %}

</div>
