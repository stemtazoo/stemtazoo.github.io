---
layout: page
title: COUNT(*)・COUNT(列)・COUNT DISTINCTの違い【DS検定】
description: "COUNT(*)は全行、COUNT(列)はNULLを除いた件数、COUNT(DISTINCT 列)はNULLを除き重複も除いたユニーク数を数えます。NULLと重複の扱いをDS検定向けに整理します。"
permalink: /ds/sql-count-diff/
categories: [data-engineering]
tags: [ds, data-processing, sql]
prev: /ds/er-diagram/
next: /ds/sql-count-distinct/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

| 書き方 | 数えるもの |
|---|---|
| `COUNT(*)` | 全行 |
| `COUNT(列)` | その列がNULLでない行 |
| `COUNT(DISTINCT 列)` | NULLを除き、重複も除いた値の種類数 |

DS検定では、**NULLを数えるか、重複を除くか**で切り分けます。

## 直感的な説明

次の顧客IDを考えます。

| 顧客ID |
|---|
| A |
| A |
| B |
| NULL |

結果は次の通りです。

| 式 | 結果 | 理由 |
|---|---:|---|
| `COUNT(*)` | 4 | 行を全部数える |
| `COUNT(顧客ID)` | 3 | NULLを除く |
| `COUNT(DISTINCT 顧客ID)` | 2 | NULLと重複を除きA・Bを数える |

> **何をカウントしているか**で結果が変わります。

## 定義・仕組み

### COUNT(*)

行数そのものを数えます。

```sql
SELECT COUNT(*)
FROM customers;
```

### COUNT(列)

指定列がNULLでない行を数えます。

```sql
SELECT COUNT(customer_id)
FROM customers;
```

### COUNT(DISTINCT 列)

指定列について、NULLを除き、さらに重複も除いた値の種類数を数えます。

```sql
SELECT COUNT(DISTINCT customer_id)
FROM customers;
```

## どんな場面で使う？

### 全体のレコード件数を知りたい

`COUNT(*)` を使います。

### 欠損していない値の件数を知りたい

`COUNT(列)` を使います。

### ユニークな顧客数・商品数を知りたい

`COUNT(DISTINCT 列)` を使います。

## よくある誤解・混同

### ❌ COUNT(列)は全件数

NULLがあると `COUNT(*)` と結果が変わります。

### ❌ COUNT(*)とCOUNT(列)はいつも同じ

指定列にNULLがなければ同じですが、NULLがあれば異なります。

### ❌ COUNT(DISTINCT 列)は重複だけ除けばよい

NULLも数えません。

### ❌ DISTINCTは常に行全体にかかる

`COUNT(DISTINCT 列)` では、その指定列の値に対して重複を除きます。

## まとめ（試験直前用）

- `COUNT(*)` = **全行**
- `COUNT(列)` = **NULLを除く**
- `COUNT(DISTINCT 列)` = **NULLと重複を除く**
- 「NULL」と「重複」の扱いを見る
- **何を数えているか**で選択肢を切る

## 対応スキル項目（データエンジニアリング力シート）

- データ基盤
- データ操作
- ★ SQLを用いた基本的なデータ操作（検索・集計・結合等）ができる

{% include ds_article_footer.html %}
