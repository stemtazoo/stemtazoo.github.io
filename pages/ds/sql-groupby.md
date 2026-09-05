---
layout: page
title: GROUP BYとは？データ集計の基本を理解する【DS検定】
description: "SQLのGROUP BYをデータ集計の基本として整理します。指定した列で行をグループ化し、COUNTやSUMなどの集計関数と組み合わせる考え方、WHEREやHAVINGとの違いを確認できます。本文では、用語の定義、具体例、似た概念との違い、試験で迷いやすい選択肢の見分け方まで、短時間で復習できるようにまとめています。"
permalink: /ds/sql-groupby/
categories: [data-engineering]
tags: [ds, data-processing, sql]
ds_area: dataengineering
ds_section: data-processing
prev: /ds/sql-filtering/
next: /ds/sql-having/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**GROUP BYとは、指定した列の値ごとに行をグループ化し、集計するSQLの仕組み**です。

DS検定では、次の切り分けが重要です。

| SQL | 役割 |
|---|---|
| `WHERE` | 条件に合う行を絞る |
| `GROUP BY` | 同じ値の行をグループ化する |

## 直感的な説明

例えば、次の売上データがあるとします。

| 顧客 | 商品 | 売上 |
|---|---|---:|
| 田中 | ノートPC | 120000 |
| 佐藤 | マウス | 3000 |
| 田中 | キーボード | 8000 |
| 佐藤 | モニター | 30000 |

「顧客ごとの売上合計」を知りたい場合、同じ顧客の行をまとめます。

| 顧客 | 売上合計 |
|---|---:|
| 田中 | 128000 |
| 佐藤 | 33000 |

このように、**同じ値を持つ行をグループ化して集計する**のが `GROUP BY` です。

## 定義・仕組み

基本形は次の通りです。

```sql
SELECT 列, 集計関数
FROM テーブル
GROUP BY 列;
```

例えば、顧客ごとの売上合計を求める場合は、

```sql
SELECT customer, SUM(sales)
FROM orders
GROUP BY customer;
```

とします。

### よく使う集計関数

| 関数 | 意味 |
|---|---|
| `COUNT` | 件数 |
| `SUM` | 合計 |
| `AVG` | 平均 |
| `MAX` | 最大値 |
| `MIN` | 最小値 |

例えば、顧客ごとの注文数なら次のようになります。

```sql
SELECT customer, COUNT(*)
FROM orders
GROUP BY customer;
```

## どんな場面で使う？

GROUP BYは、カテゴリごとに数値をまとめたい場面で使います。

- **売上分析**：商品別売上、顧客別売上
- **マーケティング分析**：地域別顧客数、年齢層別購入数
- **業務分析**：担当者別売上、部門別コスト

## よくある誤解・混同

### ❌ `WHERE` と `GROUP BY` は同じ

違います。

- `WHERE` → **集計前に行を絞る**
- `GROUP BY` → **行をグループ化する**

### ❌ `GROUP BY` は並び替え

並び替えは `ORDER BY` です。

`GROUP BY` の役割は、**集計の単位を作ること**です。

### ❌ `GROUP BY` だけで集計値が自動計算される

`GROUP BY` はグループを作る構文です。合計や平均などを求めるときは、通常 `SUM` や `AVG` などの集計関数と組み合わせます。

## まとめ（試験直前用）

| 判断したいこと | SQL |
|---|---|
| 条件に合う行を絞る | `WHERE` |
| 同じ値の行をまとめる | `GROUP BY` |
| 合計・平均などを求める | `SUM` / `AVG` など |

覚えるポイントは次の3つです。

- **WHERE = 行を絞る**
- **GROUP BY = グループ化**
- **集計関数と組み合わせる**

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
