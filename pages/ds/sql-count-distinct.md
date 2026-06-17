---
layout: page
title: COUNT DISTINCTとは？ユニーク数を数える方法【DS検定】
description: COUNT DISTINCTは、重複を除いたユニークな値の件数を数えるSQLの集計方法です。COUNT(*)、COUNT(列)、COUNT(DISTINCT 列)の違い、NULLの扱い、GROUP BYとの組み合わせ、DS検定で問われやすい判断ポイントを整理します。
permalink: /ds/sql-count-distinct/
categories: [data-engineering]
tags: [ds, data-processing, sql]
prev: /ds/sql-count-diff/
next: /ds/sql-ddl-dml/
last_modified_at: 2026-06-17
---

## まず結論
`COUNT(DISTINCT 列名)` とは、**指定した列について、重複を除いたユニークな値の件数を数えるSQLの集計方法**です。

DS検定では、`COUNT(*)`、`COUNT(列名)`、`COUNT(DISTINCT 列名)` の違いを見分けることが重要です。

| 書き方 | 数えるもの | NULLの扱い |
|---|---|---|
| `COUNT(*)` | 行数を数える | NULLを含む行も数える |
| `COUNT(列名)` | 指定列がNULLでない行数を数える | NULLは数えない |
| `COUNT(DISTINCT 列名)` | 指定列のユニークな非NULL値を数える | NULLは数えない |

試験では、**「全部の件数」なのか「ユニーク数」なのか**を見抜くのがポイントです。

---

## 直感的な説明
次のような購入履歴があるとします。

| 行 | 顧客ID |
|---|---|
| 1 | A |
| 2 | A |
| 3 | B |
| 4 | A |

このとき、購入履歴の行数は4件です。

しかし、購入した顧客の種類は `A` と `B` の2人だけです。

```sql
SELECT COUNT(*) FROM sales;
```

結果は `4` です。  
すべての行を数えます。

```sql
SELECT COUNT(DISTINCT customer_id) FROM sales;
```

結果は `2` です。  
重複した `A` を1つとして数えるため、ユニークな顧客数は2になります。

つまり、`COUNT(DISTINCT)` は**種類の数**や**ユニーク数**を知りたいときに使います。

---

## COUNT / COUNT(列) / COUNT(DISTINCT 列) の違い
COUNT系の関数は似ていますが、数える対象が違います。

### COUNT(*)
`COUNT(*)` は、条件に一致した行の数を数えます。

```sql
SELECT COUNT(*) FROM sales;
```

行そのものを数えるため、列にNULLが含まれていても、その行はカウントされます。

### COUNT(列名)
`COUNT(列名)` は、指定した列がNULLでない行の数を数えます。

```sql
SELECT COUNT(customer_id) FROM sales;
```

`customer_id` がNULLの行は数えません。

### COUNT(DISTINCT 列名)
`COUNT(DISTINCT 列名)` は、指定した列について、NULLを除いたユニークな値の数を数えます。

```sql
SELECT COUNT(DISTINCT customer_id) FROM sales;
```

同じ顧客IDが何度出てきても、1種類として数えます。

---

## 実データで確認する
次の売上テーブルを考えます。

| order_id | customer_id | product |
|---|---|---|
| 1 | A | book |
| 2 | A | pen |
| 3 | B | book |
| 4 | NULL | notebook |
| 5 | C | book |
| 6 | C | book |

このテーブルに対して、次のSQLを実行すると結果は次のようになります。

| SQL | 結果 | 意味 |
|---|---:|---|
| `COUNT(*)` | 6 | 全部の行数 |
| `COUNT(customer_id)` | 5 | `customer_id` がNULLでない行数 |
| `COUNT(DISTINCT customer_id)` | 3 | ユニークな顧客ID数（A、B、C） |
| `COUNT(DISTINCT product)` | 3 | ユニークな商品数（book、pen、notebook） |

`customer_id` のNULLは、`COUNT(customer_id)` でも `COUNT(DISTINCT customer_id)` でも数えません。

---

## NULLの扱い
`COUNT(DISTINCT 列名)` では、NULLはユニークな値として数えません。

たとえば、`customer_id` が次のようになっているとします。

| customer_id |
|---|
| A |
| A |
| B |
| NULL |
| NULL |

```sql
SELECT COUNT(DISTINCT customer_id) FROM sales;
```

結果は `2` です。

`A` と `B` だけが数えられ、NULLは除外されます。  
NULLが2行あっても、「NULLという1種類」として数えるわけではありません。

DS検定では、**COUNT(DISTINCT)はNULLを含めて数える**という選択肢が出たら誤りです。

---

## GROUP BYと組み合わせる例
`COUNT(DISTINCT)` は、`GROUP BY` と組み合わせると「グループごとのユニーク数」を求められます。

たとえば、商品ごとのユニーク顧客数を求める場合は次のように書きます。

```sql
SELECT
  product,
  COUNT(DISTINCT customer_id) AS unique_customers
FROM sales
GROUP BY product;
```

このSQLは、商品ごとに「その商品を購入した顧客の種類数」を数えます。

| product | unique_customers |
|---|---:|
| book | 3 |
| pen | 1 |
| notebook | 0 |

`notebook` の行では `customer_id` がNULLなので、ユニーク顧客数は0になります。

総購入回数を知りたいなら `COUNT(*)`、購入した顧客の種類数を知りたいなら `COUNT(DISTINCT customer_id)` を使います。

---

## SELECT DISTINCTとの違い
`SELECT DISTINCT` と `COUNT(DISTINCT)` は、どちらも重複を除くという点では似ています。

ただし、目的が違います。

| 書き方 | 目的 | 返すもの |
|---|---|---|
| `SELECT DISTINCT 列名` | 重複を除いた値の一覧を出す | 値の一覧 |
| `COUNT(DISTINCT 列名)` | 重複を除いた値の件数を出す | 件数 |

たとえば、顧客IDの一覧を見たい場合は次のように書きます。

```sql
SELECT DISTINCT customer_id FROM sales;
```

ユニークな顧客数だけを知りたい場合は次のように書きます。

```sql
SELECT COUNT(DISTINCT customer_id) FROM sales;
```

DS検定では、**一覧を出すのか、件数を出すのか**を区別します。

---

## どんな場面で使う？
`COUNT(DISTINCT)` は、重複を除いた数を知りたい場面でよく使います。

- ユニークユーザー数（UU）
- 商品の種類数
- 購入した顧客数
- 利用された店舗数
- アクセスした端末の種類数
- アンケート回答者数

一方で、総件数や回数を知りたい場合に `COUNT(DISTINCT)` を使うと、意味が変わってしまいます。

たとえば「購入回数」を知りたいなら `COUNT(*)` が適切です。  
「購入した顧客数」を知りたいなら `COUNT(DISTINCT customer_id)` が適切です。

---

## DS検定ひっかけポイント

### よくある誤り1：COUNTとCOUNT DISTINCTを同じと考える
`COUNT(*)` は行数を数えます。

`COUNT(DISTINCT 列名)` は、指定列の重複を除いた値の数を数えます。

両者は同じではありません。

### よくある誤り2：NULLも1種類として数える
`COUNT(DISTINCT 列名)` はNULLを数えません。

NULLが複数行あっても、NULLを1種類としてカウントするわけではありません。

### よくある誤り3：総件数とユニーク数を混同する
アクセスログで `user_id` が同じ人が10回アクセスした場合、行数は10件ですが、ユニークユーザー数は1人です。

総件数とユニーク数は別の指標です。

### よくある誤り4：SELECT DISTINCTとCOUNT(DISTINCT)を混同する
`SELECT DISTINCT` は重複を除いた一覧を返します。

`COUNT(DISTINCT)` は重複を除いた件数を返します。

### 選択肢の判断基準
- 「全行数」→ `COUNT(*)`
- 「NULL以外の件数」→ `COUNT(列名)`
- 「重複を除いた件数」→ `COUNT(DISTINCT 列名)`
- 「値の一覧」→ `SELECT DISTINCT 列名`
- 「グループごとのユニーク数」→ `GROUP BY` と `COUNT(DISTINCT)`

---

## 確認問題（DS検定対策）

次の `customer_id` 列について、`COUNT(DISTINCT customer_id)` の結果として正しいものはどれか。

| customer_id |
|---|
| A |
| A |
| B |
| NULL |
| C |
| C |

- ア. 6
- イ. 5
- ウ. 4
- エ. 3

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：エ**

### 解説
`COUNT(DISTINCT customer_id)` は、重複を除いた非NULLの値を数えます。

この列に含まれる非NULLのユニーク値は、`A`、`B`、`C` の3種類です。

- `A` は2回出ていますが、1種類として数えます。
- `C` も2回出ていますが、1種類として数えます。
- NULLは数えません。

したがって、答えは `3` です。

</details>

## まとめ（試験直前用）
- `COUNT(DISTINCT 列名)` は、重複を除いたユニークな値の件数を数える
- `COUNT(*)` は行数を数える
- `COUNT(列名)` は指定列がNULLでない行数を数える
- `COUNT(DISTINCT 列名)` はNULLを数えない
- `SELECT DISTINCT` は一覧、`COUNT(DISTINCT)` は件数
- `GROUP BY` と組み合わせると、グループごとのユニーク数を求められる
- 総件数かユニーク数かを見分けるのがDS検定のポイント
