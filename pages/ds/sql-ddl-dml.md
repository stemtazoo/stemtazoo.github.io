---
layout: page
title: DDLとDMLの違いとは？CREATE・SELECTはどっち？【DS検定】
description: DDLはデータベースの構造を定義し、DMLはデータを検索・追加・更新・削除します。CREATE・ALTER・DROPとSELECT・INSERT・UPDATE・DELETEを一覧で比較し、DS検定での見分け方を整理します。
permalink: /ds/sql-ddl-dml/
categories: [data-engineering]
tags: [ds, sql, database]
prev: /ds/sql-count-distinct/
next: /ds/sql-distinct/
last_modified_at: 2026-07-14
---

## まず結論

DDLとDMLの違いは、**操作する対象**で判断します。

| 分類 | 何を操作する？ | 代表的なSQL |
|---|---|---|
| DDL | テーブルなどの構造 | `CREATE`、`ALTER`、`DROP` |
| DML | テーブル内のデータ | `SELECT`、`INSERT`、`UPDATE`、`DELETE` |

DS検定では、次のように切り分けると判断しやすいです。

> **入れ物を作る・変える → DDL**  
> **中のデータを扱う → DML**

---

## 直感的な説明

データベースを、Excelの表に置き換えて考えてみます。

最初に必要なのは、表の入れ物を作ることです。

- 表を新しく作る
- 列を追加する
- 表そのものを削除する

このような**表の構造を扱う操作**がDDLです。

入れ物を作った後は、中のデータを扱います。

- データを検索する
- 行を追加する
- 値を書き換える
- 行を削除する

このような**表の中身を扱う操作**がDMLです。

---

## 定義・仕組み

SQL（Structured Query Language）は、リレーショナルデータベースを操作するための言語です。

SQLは役割によっていくつかに分類され、その代表がDDLとDMLです。

### DDL（Data Definition Language）

DDLは、**データベースやテーブルの構造を定義するSQL**です。

| SQL | 主な役割 |
|---|---|
| `CREATE` | テーブルやデータベースを作成する |
| `ALTER` | テーブル構造を変更する |
| `DROP` | テーブルやデータベースを削除する |

例として、社員テーブルを作るSQLを見てみます。

```sql
CREATE TABLE employees (
  id INT,
  name VARCHAR(50)
);
```

これは、`employees`という**テーブルの構造を作る**ため、DDLです。

### DML（Data Manipulation Language）

DMLは、**テーブルに格納されたデータを操作するSQL**です。

| SQL | 主な役割 |
|---|---|
| `SELECT` | データを検索・取得する |
| `INSERT` | データを追加する |
| `UPDATE` | データを更新する |
| `DELETE` | データを削除する |

例として、社員テーブルからデータを取得するSQLを見てみます。

```sql
SELECT *
FROM employees;
```

これは、テーブルの構造ではなく、**中にあるデータを取得する**ため、DMLとして扱います。

### 一覧で比較

| 操作 | SQL | 分類 |
|---|---|---|
| テーブルを作る | `CREATE` | DDL |
| 列を追加する | `ALTER` | DDL |
| テーブルを削除する | `DROP` | DDL |
| データを検索する | `SELECT` | DML |
| データを追加する | `INSERT` | DML |
| データを書き換える | `UPDATE` | DML |
| データを削除する | `DELETE` | DML |

---

## どんな場面で使う？

### システムを作るとき

開発の初期には、テーブルや列の構造を決める必要があります。

このときは、次のようなDDLを使います。

```sql
CREATE TABLE sales (
  sale_id INT,
  amount INT
);
```

### データを分析するとき

データ分析では、テーブル内のデータを取得・集計するため、DMLをよく使います。

```sql
SELECT customer_id, SUM(amount)
FROM sales
GROUP BY customer_id;
```

`WHERE`、`JOIN`、`GROUP BY`などを含んでいても、中心となる操作が`SELECT`であれば、データを取得するDMLとして考えます。

---

## よくある誤解・混同

### 誤解1：SELECTは構造を指定するのでDDLである

`SELECT`では取得する列を指定しますが、テーブル構造そのものを変更しているわけではありません。

**既存データを検索・取得する操作**なので、DS検定ではDMLとして判断します。

### 誤解2：DELETEとDROPは同じ削除操作である

どちらも「削除」ですが、削除する対象が違います。

| SQL | 削除するもの | 分類 |
|---|---|---|
| `DELETE` | テーブル内の行 | DML |
| `DROP` | テーブルそのもの | DDL |

迷ったら、**中身を消すのか、入れ物ごと消すのか**を確認します。

### 誤解3：JOINやWHEREはDDLである

`JOIN`や`WHERE`は、データを絞り込んだり結合したりするために使います。

```sql
SELECT *
FROM sales
JOIN customers
  ON sales.customer_id = customers.customer_id
WHERE sales.amount >= 10000;
```

このSQLはデータを取得しているため、DMLの範囲です。

### 誤解4：SELECTは必ずDMLとだけ呼ばれる

分類体系によっては、`SELECT`をDQL（Data Query Language）として分ける場合もあります。

ただし、DS検定の基本的な切り分けでは、`SELECT`をデータ操作側として扱う問題が多いため、**問題文や選択肢の分類方法を確認する**ことが大切です。

---

## 確認問題（DS検定対策）

次のうち、DDLに分類されるSQLはどれか。

- ア. `SELECT`
- イ. `INSERT`
- ウ. `UPDATE`
- エ. `ALTER`

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：エ**

- `SELECT`：データを取得するDML
- `INSERT`：データを追加するDML
- `UPDATE`：データを更新するDML
- `ALTER`：テーブル構造を変更するDDL

判断ポイントは、**テーブルの構造を変える操作かどうか**です。

</details>

---

## まとめ（試験直前用）

- DDLは、データベースやテーブルの**構造を定義するSQL**
- DMLは、テーブル内の**データを操作するSQL**
- `CREATE`、`ALTER`、`DROP`はDDL
- `SELECT`、`INSERT`、`UPDATE`、`DELETE`はDMLとして整理する
- `DELETE`は行を削除し、`DROP`はテーブルそのものを削除する
- 迷ったら、**入れ物か、中身か**で切り分ける

{% include ds_article_footer.html %}
