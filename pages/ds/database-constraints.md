---
layout: page
title: データベースの制約とは？NOT NULL・一意性・外部キーを整理【DS検定】
description: "データベースの制約をデータ品質と整合性を守るルールとして整理します。NOT NULL、一意制約、主キー、外部キーの役割とDS検定での見分け方を確認できます。本文では、用語の定義、具体例、似た概念との違い、試験で迷いやすい選択肢の見分け方まで短時間で復習できます。"
permalink: /ds/database-constraints/
categories: [data-engineering]
tags: [ds, database]
ds_area: dataengineering
ds_section: database
prev: /ds/data-warehouse-vs-datamart/
next: /ds/datalake-vs-nosql/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**データベースの制約（constraint）とは、データの整合性や正しさを保つためにテーブルへ設定するルール**です。

DS検定では、**「データ型」と「制約」を混同しないこと**が重要です。

## 直感的な説明

ルールがなければ、次のような壊れたデータが登録される可能性があります。

- IDが空
- 同じIDが重複
- 存在しない顧客IDを持つ注文

そこで、

- この列は必須
- この列は重複禁止
- この値は別テーブルに存在していなければならない

といったルールを設定します。これが**制約**です。

## 定義・仕組み

代表的な制約は次の通りです。

| 制約 | 主な役割 |
|---|---|
| `NOT NULL` | NULLを禁止する |
| `UNIQUE` | 重複を禁止する |
| `FOREIGN KEY` | 参照先との整合性を保つ |
| `CHECK` | 値の条件を指定する |
| `PRIMARY KEY` | レコードを一意に識別する |

### NOT NULL制約

NULL（値なし）を禁止します。

| 顧客ID | 名前 |
|---:|---|
| 1 | 田中 |
| 2 | 鈴木 |

顧客IDを必須にしたい場合などに使います。

### 一意性制約（UNIQUE）

同じ値の重複を禁止します。

| 社員番号 | 名前 |
|---:|---|
| 1001 | 山田 |
| 1002 | 佐藤 |

社員番号やメールアドレスなど、重複させたくない列に使います。

### 外部キー制約（FOREIGN KEY）

別テーブルに存在する値だけを許可します。

| 顧客ID | 名前 |
|---:|---|
| 1 | 田中 |
| 2 | 鈴木 |

注文テーブルに `顧客ID = 99` が登録されると、存在しない顧客を参照することになります。外部キー制約はこれを防ぎます。

### CHECK制約

`年齢 >= 0` のように、値が満たすべき条件を指定します。

## どんな場面で使う？

### システム開発

- 顧客IDは必須 → `NOT NULL`
- メールアドレスは重複禁止 → `UNIQUE`

### 業務データ管理

- 注文は既存顧客だけを参照 → `FOREIGN KEY`
- 在庫数は0以上 → `CHECK`

制約は、**データが壊れる前にDB側で防ぐ仕組み**です。

## よくある誤解・混同

### ❌ 制約 = データ型

| 概念 | 役割 | 例 |
|---|---|---|
| データ型 | 値の種類を決める | `INTEGER`, `VARCHAR`, `DATE` |
| 制約 | 値のルールを決める | `NOT NULL`, `UNIQUE`, `FOREIGN KEY` |

### ❌ 主キーとUNIQUEは同じ

主キーは**レコード識別の中心となるキー**で、基本的に `NULL不可 + 重複不可` です。

### ❌ 外部キーは値を一意にする制約

外部キーの役割は、**参照先との整合性を守ること**です。重複自体は許されます。

## まとめ（試験直前用）

- **制約 = データの整合性を守るルール**
- `NOT NULL` → NULL禁止
- `UNIQUE` → 重複禁止
- `FOREIGN KEY` → 参照先との整合性
- `CHECK` → 値の条件
- **データ型と制約を混同しない**

DS検定では、**「値の種類」ならデータ型、「値のルール」なら制約**と切り分けましょう。

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
