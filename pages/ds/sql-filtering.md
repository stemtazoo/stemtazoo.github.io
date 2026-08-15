---
layout: page
title: SQLのフィルタリング処理とは？（WHERE句によるデータ抽出）【DS検定】
description: "SQLのフィルタリング処理とは、条件を指定して必要なデータだけを抽出する操作です。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。初学者が迷いやすい判断ポイントも確認します。"
permalink: /ds/sql-filtering/
categories: [data-engineering]
tags: [ds, data-processing, sql]
prev: /ds/sql-exists/
next: /ds/sql-groupby/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**SQLのフィルタリング処理とは、条件を指定して必要な行だけを抽出する操作**です。

DS検定では、**「条件に合うデータだけを取り出す = `WHERE`」**と判断できることが重要です。

## 直感的な説明

例えば、次の売上データがあるとします。

| 日付 | 店舗 | 売上 |
|---|---|---:|
| 4/1 | 東京 | 80万円 |
| 4/2 | 東京 | 120万円 |
| 4/3 | 大阪 | 90万円 |
| 4/4 | 東京 | 150万円 |

「売上が100万円以上の日だけ知りたい」なら、必要な行は次の2件です。

| 日付 | 店舗 | 売上 |
|---|---|---:|
| 4/2 | 東京 | 120万円 |
| 4/4 | 東京 | 150万円 |

このように、**条件に合う行だけを残す**のがフィルタリングです。

SQLでは `WHERE` 句を使います。

```sql
SELECT *
FROM sales
WHERE 売上 >= 1000000;
```

## 定義・仕組み

基本形は次の通りです。

```sql
SELECT 列名
FROM テーブル名
WHERE 条件;
```

### よく使う条件指定

| 演算子 | 意味 |
|---|---|
| `AND` | 複数条件をすべて満たす |
| `OR` | 複数条件のどれかを満たす |
| `IN` | 指定した値の集合に含まれる |
| `LIKE` | 文字列パターンを指定する |
| `BETWEEN` | 範囲を指定する |

例えば、東京店舗かつ売上100万円以上なら、

```sql
SELECT *
FROM sales
WHERE 店舗 = '東京'
  AND 売上 >= 1000000;
```

となります。

## どんな場面で使う？

フィルタリングは、分析対象を絞るほぼすべての場面で使います。

- **売上分析**：高額売上だけを見る、特定店舗だけを見る
- **顧客分析**：30代だけを見る、購入回数が多い顧客を抽出する
- **ログ分析**：エラーログだけを見る、特定期間だけを見る

データ分析では、

> **抽出 → 集計 → 可視化**

という流れになることが多く、フィルタリングはその最初の段階です。

## よくある誤解・混同

### ❌ フィルタリング = データ削除

フィルタリングは、**対象となる行を選ぶ操作**です。

元データそのものを削除する `DELETE` とは役割が違います。

### ❌ フィルタリング = 集計

違います。

| 操作 | 役割 |
|---|---|
| フィルタリング（`WHERE`） | 必要な行を選ぶ |
| 集計（`GROUP BY` + 集計関数） | データをまとめて計算する |

### ❌ `WHERE` はテーブル結合に使う

テーブルを結合するのは `JOIN` です。

`WHERE` は、**条件によって行を絞る**ために使います。

## まとめ（試験直前用）

- **フィルタリング = 条件に合う行を抽出**
- SQLでは **`WHERE`** を使う
- **`WHERE` = 抽出 / `GROUP BY` = 集計 / `JOIN` = 結合**
- データ削除とは別の操作

DS検定では、**「条件を指定して必要なデータだけを取り出す」なら `WHERE`** と判断しましょう。

## 対応スキル項目（データエンジニアリング力シート）

- データ加工
- フィルタリング処理
- ★ 数十万レコードのデータに対して、条件を指定してフィルタリングできる（特定値に合致する・もしくは合致しないデータの抽出、特定範囲のデータの抽出、部分文字列の抽出など）

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
