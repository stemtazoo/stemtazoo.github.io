---
layout: page
title: データリテラシーとは？データを読み解く力【DS検定】
description: "データリテラシー（Data Literacy）とは、データを理解し、正しく読み取り、意思決定に活用する能力のことです。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。"
permalink: /ds/data-literacy/
categories: [business]
tags: [ds, data-understanding, design]
ds_area: foundation
ds_section: data-understanding
next: /ds/data-literacy-practice/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**データリテラシー（Data Literacy）とは、データを理解し、正しく読み取り、意思決定に活用する能力**です。

DS検定では、単にデータを見るだけでなく、**背景や偏りまで考えて判断できること**が重要です。

## 直感的な説明

例えば売上が増えているグラフを見たとき、

- 季節要因ではないか
- 新しい施策の効果か
- 比較条件は同じか
- データに偏りはないか

まで考える必要があります。

ただ数字を見るのではなく、**意味・背景・偏りを考えて判断する力**がデータリテラシーです。

## 定義・仕組み

データリテラシーには、次のような能力が含まれます。

### データ理解

グラフ・統計・指標などの意味を読み取る力です。

### データ分析

データから傾向やパターンを見つける力です。

### 批判的思考

データをそのまま信じず、バイアスや誤解がないかを考えます。

### 意思決定

データを経営判断や業務改善へつなげます。

## どんな場面で使う？

### ビジネス

売上データや顧客データをもとに施策を判断します。

### データ分析

統計や機械学習の結果を正しく解釈する土台になります。

### 社会

誤解を招くグラフや、根拠の弱い情報を見抜くときにも必要です。

## よくある誤解・混同

### ❌ データリテラシー = ITスキル

| 概念 | 主な意味 |
|---|---|
| ITスキル | ツールやシステムを使う能力 |
| データリテラシー | データを理解し判断する能力 |

ツールが使えるだけでは、データを正しく解釈できるとは限りません。

### ❌ データリテラシー = データサイエンス

| 概念 | 主な意味 |
|---|---|
| データリテラシー | データを読み解く基礎能力 |
| データサイエンス | 統計・機械学習などを使った分析 |

データリテラシーは、より広い層に必要な基礎能力です。

## まとめ（試験直前用）

- **データリテラシー = データを理解し、判断に使う力**
- グラフや指標を読む
- 背景・偏り・条件を確認する
- データを意思決定へつなげる
- ITツールを使えることとは別

DS検定では、**「データを正しく理解し、意思決定に活用する能力」ならデータリテラシー**と判断しましょう。

## 対応スキル項目（ビジネス力シート）

- ビジネス理解
- データ活用
- ★ データに基づく意思決定を理解している

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
