---
layout: page
title: UNIONとUNION ALLの違いとは？重複の扱いを整理【DS検定】
description: "UNIONは複数のSELECT結果を結合するときに重複行を除き、UNION ALLは重複もそのまま残します。件数・重複・処理コストの違いをDS検定向けに整理します。"
permalink: /ds/sql-union/
categories: [data-engineering]
tags: [ds, data-processing, sql]
ds_area: dataengineering
ds_section: data-processing
prev: /ds/sql-join/
next: /ds/sql-where/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

| 構文 | 重複行 |
|---|---|
| `UNION` | 除く |
| `UNION ALL` | そのまま残す |

DS検定では、**重複を消すかどうか**が最重要ポイントです。

## 直感的な説明

2つの一覧を結合します。

| 一覧1 | 一覧2 |
|---|---|
| A | B |
| B | C |

結果は次のようになります。

- `UNION` → A, B, C
- `UNION ALL` → A, B, B, C

> **Bを1つにまとめるか、2つとも残すか**が違いです。

## 定義・仕組み

### UNION

複数のSELECT結果を縦に結合し、重複行を除きます。

```sql
SELECT name FROM customers_a
UNION
SELECT name FROM customers_b;
```

### UNION ALL

複数のSELECT結果を縦に結合し、重複行もそのまま残します。

```sql
SELECT name FROM customers_a
UNION ALL
SELECT name FROM customers_b;
```

### 結合できる条件

基本的には、対応する列について次をそろえる必要があります。

- 列数
- 対応する列のデータ型が互換であること

## どんな場面で使う？

### 重複を除いた一覧が欲しい

`UNION` を使います。

### 全データをそのまま残したい

`UNION ALL` を使います。

件数をそのまま保持したい集計では、重複削除が不要なら `UNION ALL` が適しています。

## よくある誤解・混同

### ❌ UNIONとUNION ALLは同じ

重複の扱いが違います。

### ❌ UNIONでも件数は変わらない

重複行があれば、`UNION` では件数が減ります。

### ❌ UNIONの方が常に高速

`UNION` は重複除去が必要になるため、一般に `UNION ALL` より追加処理が発生します。

### ❌ 結果の順番は保証される

並び順が必要なら `ORDER BY` を明示します。

## まとめ（試験直前用）

- `UNION` = **重複を除いて結合**
- `UNION ALL` = **重複を残して結合**
- 重複があれば件数が変わる
- 重複除去が不要なら `UNION ALL` の方が処理を減らしやすい
- **「重複を消すか？」で選択肢を切る**

## 対応スキル項目（データエンジニアリング力シート）

- データ基盤
- データ操作
- ★ SQLを用いた基本的なデータ操作（検索・集計・結合等）ができる

{% include ds_article_footer.html %}
