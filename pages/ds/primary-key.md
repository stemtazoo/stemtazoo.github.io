---
layout: page
title: 主キー（Primary Key）とは？データベースの基本ルールを理解【DS検定】
description: "主キー（Primary Key）とは、テーブルの中で1つのレコードを一意に識別するための列（または列の組み合わせ）です。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。"
permalink: /ds/primary-key/
categories: [data-engineering]
tags: [ds, database]
ds_area: dataengineering
ds_section: database
prev: /ds/olap/
next: /ds/rdb-vs-nosql/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**主キー（Primary Key）とは、テーブルの中で1つのレコードを一意に識別するための列（または列の組み合わせ）**です。

DS検定では、**「重複しない」「NULLにならない」識別子**として理解できるかが重要です。

## 直感的な説明

例えば顧客テーブルを考えてみます。

| 顧客ID | 名前 |
|---:|---|
| 1001 | 田中 |
| 1002 | 鈴木 |
| 1003 | 田中 |

「田中」という名前は複数存在します。

名前だけで管理すると、

- どの田中さんなのか
- どの注文に紐づくのか

が分からなくなります。

そこで、**必ず1人だけを識別できる値**を用意します。それが主キーです。

## 定義・仕組み

主キーとは、

> **テーブル内の各行（レコード）を一意に識別する列**

です。

### ① 重複してはいけない

同じ主キー値が2つあると、レコードを区別できません。

**NG例**

| 顧客ID | 名前 |
|---:|---|
| 1001 | 田中 |
| 1001 | 鈴木 |

### ② NULLになってはいけない

主キーがNULLでは、どのレコードなのかを識別できません。

### ③ 1テーブルにつき主キーは1つ

1つのテーブルに設定する主キーは1つです。

ただし、**複数列を組み合わせて1つの主キーにする「複合主キー（Composite Key）」**はあります。

例えば、

| 注文ID | 商品ID | 数量 |
|---:|---:|---:|
| 100 | 10 | 2 |
| 100 | 20 | 1 |

のようなテーブルでは、`注文ID + 商品ID` の組み合わせで1行を識別する場合があります。

## どんな場面で使う？

主キーは、テーブル内のレコードを安定して識別し、他テーブルとの関係を作るために使います。

### 顧客テーブル

| 顧客ID（PK） | 名前 |
|---:|---|
| 1001 | 田中 |

### 注文テーブル

| 注文ID（PK） | 顧客ID（FK） |
|---:|---:|
| 5001 | 1001 |

この場合、

- **主キー（PK）** → そのテーブルのレコードを識別
- **外部キー（FK）** → 他テーブルのレコードを参照

という役割になります。

## よくある誤解・混同

### ❌ 主キー = 一意制約

似ていますが同じではありません。

| 概念 | 重複 | NULL | 主な役割 |
|---|---|---|---|
| 主キー | 不可 | 不可 | レコードの識別 |
| 一意制約 | 不可 | DBMSの仕様による | 値の重複防止 |

DS検定では、まず**主キーは「重複不可 + NULL不可」**と押さえると判断しやすくなります。

### ❌ 主キーと外部キーは同じ

| 用語 | 役割 |
|---|---|
| 主キー | 自分のテーブルのレコードを識別 |
| 外部キー | 他テーブルを参照 |

**主キー = 識別、外部キー = 関係**と整理すると切り分けやすいです。

### ❌ 「主キーはNULLを許可できる」

これは誤りです。

主キーは、

- **NULL不可**
- **重複不可**

です。

## まとめ（試験直前用）

- **主キー** = レコードを一意に識別する列
- **NULL不可・重複不可**
- 1テーブルにつき主キーは1つ
- 複数列をまとめた**複合主キー**はあり得る
- **外部キー**は他テーブルとの関係を作る

DS検定では、**「主キー = 識別」**を軸に選択肢を判断しましょう。

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
