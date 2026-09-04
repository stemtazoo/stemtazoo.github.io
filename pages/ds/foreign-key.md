---
layout: page
title: 外部キー（Foreign Key）とは？テーブルの関係を理解【DS検定】
description: "外部キー（Foreign Key）とは、別のテーブルの主キーを参照することでテーブル同士の関係を表す列です。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。"
permalink: /ds/foreign-key/
categories: [data-engineering]
tags: [ds, database]
ds_area: dataengineering
ds_section: database
prev: /ds/datalake-vs-nosql/
next: /ds/normalization-2nf-3nf/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**外部キー（Foreign Key）とは、別テーブルの主キーなどを参照して、テーブル同士の関係を表す列**です。

DS検定では、**主キー = 識別 / 外部キー = 関係**と切り分けられることが重要です。

## 直感的な説明

顧客と注文を別テーブルで管理するとします。

### 顧客テーブル

| 顧客ID | 名前 |
|---:|---|
| 1 | 田中 |
| 2 | 鈴木 |

### 注文テーブル

| 注文ID | 顧客ID |
|---:|---:|
| 100 | 1 |
| 101 | 2 |

注文テーブルの `顧客ID` を見ると、**どの顧客の注文か**が分かります。

このように、別テーブルのレコードを参照するための列が外部キーです。

## 定義・仕組み

外部キーは、**他テーブルのキーを参照してテーブル間の関係を表現する列**です。

| テーブル | 列 | 役割 |
|---|---|---|
| 顧客テーブル | 顧客ID | 主キー（PK） |
| 注文テーブル | 注文ID | 主キー（PK） |
| 注文テーブル | 顧客ID | 外部キー（FK） |

### 参照整合性

外部キーには、参照先との整合性を守る役割があります。

例えば顧客テーブルに `顧客ID = 1, 2` しか存在しないのに、注文テーブルへ `顧客ID = 99` を登録すると、存在しない顧客を参照することになります。

外部キー制約を使うと、このような不整合を防げます。

## どんな場面で使う？

外部キーは、複数テーブルの関係を表現するために使います。

例えばECサイトでは、

- 顧客テーブル
- 注文テーブル
- 商品テーブル
- 注文明細テーブル

をそれぞれ分け、外部キーでつなぎます。

これがリレーショナルデータベースの基本的な考え方です。

## よくある誤解・混同

### ❌ 外部キー = 主キー

| 用語 | 主な役割 |
|---|---|
| 主キー | 自分のテーブルのレコードを一意に識別 |
| 外部キー | 他テーブルとの関係を表す |

### ❌ 外部キーは重複できない

外部キーは重複して構いません。

| 注文ID | 顧客ID |
|---:|---:|
| 100 | 1 |
| 101 | 1 |

1人の顧客が複数回注文することは自然なので、`顧客ID = 1` が複数行に現れても問題ありません。

### ❌ 外部キーは必ず一意な値になる

一意性が中心となるのは主キーです。外部キーの中心的な役割は**参照先との関係を示すこと**です。

## まとめ（試験直前用）

- **外部キー = 他テーブルを参照する列**
- テーブル間の関係を表す
- 参照整合性を守るために使う
- **外部キーは重複してよい**
- **主キー = 識別 / 外部キー = 関係**

DS検定では、この「識別」と「関係」の違いで選択肢を切りましょう。

## 対応スキル項目（データエンジニアリング力シート）

- データ管理
- データベース
- ★ データベースの基本概念（テーブル、主キー、外部キーなど）を理解している
- ★ データの整合性や品質を保つ仕組みを理解している

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
