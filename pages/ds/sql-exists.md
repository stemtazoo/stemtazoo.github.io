---
layout: page
title: EXISTSとは？サブクエリの存在判定を理解する【DS検定】
description: "EXISTSは、サブクエリが1行でも結果を返すかどうかでTRUE/FALSEを判定するSQL構文です。値の一致を見るINとの違い、NOT EXISTS、相関サブクエリの読み方をDS検定向けに整理します。"
permalink: /ds/sql-exists/
categories: [data-engineering]
tags: [ds, sql]
prev: /ds/sql-distinct/
next: /ds/sql-filtering/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**EXISTS**は、サブクエリが**1行でも結果を返すか**を判定するSQL構文です。

DS検定では、**値そのものを比較するのではなく「該当データが存在するか」を見る**点が重要です。

## 直感的な説明

「注文したことがある顧客だけを出したい」とします。

このとき知りたいのは、注文金額そのものではありません。

> その顧客に対応する注文が**1件でもあるか？**

を確認できれば十分です。

これがEXISTSの考え方です。

## 定義・仕組み

基本形は次の通りです。

```sql
SELECT *
FROM customers A
WHERE EXISTS (
    SELECT 1
    FROM orders B
    WHERE A.customer_id = B.customer_id
);
```

このSQLでは、各顧客について対応する注文が1件でも見つかれば、その顧客を残します。

### SELECT 1 の意味

EXISTSが見るのは、サブクエリの**返す値ではなく、行が存在するかどうか**です。

そのため、存在判定という意味では `SELECT 1` の値そのものに意味はありません。

### NOT EXISTS

該当する行が**1件も存在しない**ことを確認したい場合は `NOT EXISTS` を使います。

```sql
SELECT *
FROM customers A
WHERE NOT EXISTS (
    SELECT 1
    FROM orders B
    WHERE A.customer_id = B.customer_id
);
```

これは「注文履歴がない顧客」を探す例です。

## どんな場面で使う？

### 関連データがある行だけ残したい

- 注文がある顧客
- 在庫がある商品
- 対応履歴がある問い合わせ

### 関連データがない行を探したい

`NOT EXISTS` を使います。

- 注文がない顧客
- 未処理の案件

## よくある誤解・混同

### ❌ EXISTSとINは同じ

目的が似る場合はありますが、判断軸が違います。

| 構文 | 見ているもの |
|---|---|
| `EXISTS` | 条件を満たす行が存在するか |
| `IN` | 値が候補集合に含まれるか |

### ❌ サブクエリが返す値が重要

EXISTSでは、**行が返るかどうか**が重要です。

### ❌ EXISTSは常に全行を最後まで調べる

実装最適化はDBMSに依存しますが、EXISTSの論理上の目的は「存在確認」です。試験では、**1件でも存在すれば条件を満たす**と理解すれば十分です。

### ❌ NOT EXISTSは値の不一致を調べる

NOT EXISTSは、条件を満たす行が**存在しないこと**を確認します。

## まとめ（試験直前用）

- `EXISTS` = **存在判定**
- サブクエリが1行でも返ればTRUE
- 値ではなく「行があるか」を見る
- `NOT EXISTS` = 該当行が存在しない
- **EXISTS = 存在 / IN = 値**で切り分ける

## 対応スキル項目（データエンジニアリング力シート）

- データ基盤
- データ操作
- ★ SQLを用いた基本的なデータ操作（検索・集計・結合等）ができる

{% include ds_article_footer.html %}
