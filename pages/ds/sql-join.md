---
layout: page
title: JOINとは？テーブル結合の基本を理解する【DS検定】
description: "JOINを複数テーブルをキーで結合して必要なデータを取り出すSQL操作として整理します。内部結合・外部結合の違い、NULLの扱い、DS検定での見分け方を確認できます。本文では、用語の定義、具体例、似た概念との違い、試験で迷いやすい選択肢の見分け方まで短時間で復習できます。"
permalink: /ds/sql-join/
categories: [data-engineering]
tags: [ds, data-processing, sql]
ds_area: dataengineering
ds_section: data-processing
prev: /ds/sql-in-exists/
next: /ds/sql-union/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**JOINとは、複数のテーブルを共通のキーで結合してデータを取得するSQLの仕組み**です。

DS検定では、

- `JOIN` → テーブルを結合する
- `WHERE` → 行を条件で絞る

と切り分けることが重要です。

## 直感的な説明

例えば、次の2つのテーブルがあるとします。

### 顧客テーブル

| 顧客ID | 名前 |
|---:|---|
| 1 | 田中 |
| 2 | 佐藤 |

### 注文テーブル

| 注文ID | 顧客ID | 商品 |
|---:|---:|---|
| 101 | 1 | ノートPC |
| 102 | 2 | スマートフォン |

「誰が何を買ったか」を知るには、`顧客ID` を使って2つのテーブルを結合します。

| 名前 | 商品 |
|---|---|
| 田中 | ノートPC |
| 佐藤 | スマートフォン |

これがJOINの基本イメージです。

## 定義・仕組み

JOINは、**複数のテーブルを共通の列（キー）で結びつける**ために使います。

基本形は次の通りです。

```sql
SELECT 列
FROM テーブルA
JOIN テーブルB
  ON 結合条件;
```

例えば、顧客名と購入商品を取得するなら、

```sql
SELECT customers.name, orders.product
FROM customers
JOIN orders
  ON customers.id = orders.customer_id;
```

とします。

このSQLでは、`customers.id` と `orders.customer_id` を対応づけています。

## どんな場面で使う？

JOINは、情報が複数テーブルに分かれているときに使います。

- **売上分析**：顧客テーブル + 注文テーブル
- **商品分析**：商品テーブル + 注文テーブル
- **地域分析**：顧客テーブル + 地域テーブル

データベースでは情報を分けて保存することが多いため、分析ではJOINが頻繁に登場します。

## よくある誤解・混同

### ❌ `JOIN` と `WHERE` は同じ

| SQL | 役割 |
|---|---|
| `JOIN` | テーブルを結合する |
| `WHERE` | 条件に合う行を絞る |

### ❌ JOINはデータを書き換える操作

JOINは、基本的に**データを取得するときにテーブルを組み合わせる操作**です。

データを追加・更新する `INSERT` や `UPDATE` とは役割が違います。

### ❌ JOINは2テーブルまで

JOINは3つ以上のテーブルにも使えます。

```sql
FROM A
JOIN B ON ...
JOIN C ON ...
```

のように複数のテーブルを結合できます。

## まとめ（試験直前用）

- **JOIN = テーブル結合**
- 共通キーを使って情報を組み合わせる
- **WHERE = 条件抽出**
- JOINはデータ変更そのものではない

DS検定では、**「複数テーブルの情報を組み合わせる」ならJOIN**と判断しましょう。

## 対応スキル項目（ver.6 データエンジニアリング）

- **分類**：ITエンジニアリング
- **スキルカテゴリ**：プログラミング
- **サブカテゴリ**：SQL
- **必須スキル**：◯
- ★ SQLの構文を一通り知っていて、記述・実行できる（DML・DDLの理解、各種JOINの使い分け、集計関数とGROUP BY、CASE文を使用した縦横変換、副問合せやEXISTSの活用など）
- [ver.6 ★1スキルチェックで確認する](/ds/engineering-skillcheck/)
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
