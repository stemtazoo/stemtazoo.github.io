---
layout: page
title: DDLとDMLの違いとは？CREATE・SELECT・DELETEを一覧で整理【DS検定】
description: DDLはテーブルなどの構造を定義し、DMLはテーブル内のデータを操作するSQLです。CREATE・ALTER・DROPとSELECT・INSERT・UPDATE・DELETEを一覧で比較し、DELETEとDROP、SELECTの扱いをDS検定の判断基準で整理します。
permalink: /ds/sql-ddl-dml/
categories: [data-engineering]
tags: [ds, sql, database]
ds_area: dataengineering
ds_section: sql
prev: /ds/sql-count-distinct/
next: /ds/sql-distinct/
last_modified_at: 2026-11-24
image:
  path: https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/ds/sql-ddl-dml.png
  width: 1734
  height: 907
  alt: "DDLはテーブルの構造を定義し、DMLはテーブル内のデータを扱う。CREATE・ALTER・DROPとSELECT・INSERT・UPDATE・DELETEを左右で比較した図"
---

## まず結論

DDLとDMLの違いは、**操作する対象**で判断します。

<table class="study-comparison study-comparison--pair" id="ddl-dml-pair" role="table" aria-label="DDLとDMLの比較">
  <thead role="rowgroup">
    <tr role="row"><th scope="col" role="columnheader">観点</th><th scope="col" role="columnheader" id="ddl-dml-pair-col-1">DDL</th><th scope="col" role="columnheader" id="ddl-dml-pair-col-2">DML</th></tr>
  </thead>
  <tbody role="rowgroup">
    <tr role="row">
      <th scope="row" role="rowheader" id="ddl-dml-pair-row-1">何を操作する？</th>
      <td role="cell" headers="ddl-dml-pair-row-1 ddl-dml-pair-col-1"><span class="study-comparison__label" aria-hidden="true">DDL</span>テーブルなどの構造</td>
      <td role="cell" headers="ddl-dml-pair-row-1 ddl-dml-pair-col-2"><span class="study-comparison__label" aria-hidden="true">DML</span>テーブル内のデータ</td>
    </tr>
    <tr role="row">
      <th scope="row" role="rowheader" id="ddl-dml-pair-row-2">代表的なSQL</th>
      <td role="cell" headers="ddl-dml-pair-row-2 ddl-dml-pair-col-1"><span class="study-comparison__label" aria-hidden="true">DDL</span><code>CREATE</code>、<code>ALTER</code>、<code>DROP</code></td>
      <td role="cell" headers="ddl-dml-pair-row-2 ddl-dml-pair-col-2"><span class="study-comparison__label" aria-hidden="true">DML</span><code>SELECT</code>、<code>INSERT</code>、<code>UPDATE</code>、<code>DELETE</code></td>
    </tr>
  </tbody>
</table>

DS検定では、次のように切り分けると判断しやすいです。

> **入れ物を作る・変える → DDL**  
> **中のデータを扱う → DML**

<figure style="margin:16px 0 20px;">
  <img src="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/ds/sql-ddl-dml.png" width="1734" height="907" alt="DDLはテーブルの構造を定義し、DMLはテーブル内のデータを操作する。DDLのCREATE・ALTER・DROPとDMLのSELECT・INSERT・UPDATE・DELETEを左右で比較した図" style="display:block;width:100%;max-width:100%;height:auto;" loading="lazy" decoding="async">
  <figcaption style="font-size:0.88em;line-height:1.5;color:#666;margin-top:8px;">DDLは構造、DMLはデータが操作対象です。空の表とデータ入りの表は違いを示す模式図であり、DDLは既存データのあるテーブルにも使えます。なお、SELECTをDQLとして別分類する場合もあります。</figcaption>
</figure>

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

### 触って覚える：SQLで「入れ物」と「中身」を変えてみる

**見るポイント：** DDLでは表の**構造**が変わり、DMLでは主に表の**データ**を扱います。SQLを選んで、テーブルの列と行のどちらが変わるか確かめましょう。

この教材は、架空の社員テーブル `employees` をブラウザ内で模擬操作します。**実際のデータベースには接続せず、SQL文字列も実行しません。**

まずは「CREATE」が選ばれた状態で「実行する（模擬操作）」を押し、できた表の列と行数を見てください。次に「INSERT」を実行すると、同じ列のまま1行増えます。DDLとDMLの予想は省略できます。

続けて SELECT → ALTER → UPDATE → DELETE → DROP の順に試し、どこが変わるか比べましょう。

<link rel="stylesheet" href="{{ '/assets/css/ds-ddl-dml-demo.css' | relative_url }}">

<div class="ds-ddl-demo" id="ds-ddl-dml-demo" aria-label="DDLとDMLによるテーブルの変化を確かめる教材">
  <div class="ds-ddl-demo__controls">
    <label for="ds-ddl-operation">① 操作するSQL
      <select id="ds-ddl-operation" data-operation>
        <option value="create">CREATE：テーブル作成</option>
        <option value="insert">INSERT：行を追加</option>
        <option value="select">SELECT：行を取得</option>
        <option value="alter">ALTER：列を追加</option>
        <option value="update">UPDATE：行を書き換え</option>
        <option value="delete">DELETE：行を削除</option>
        <option value="drop">DROP：テーブル削除</option>
      </select>
    </label>
    <label for="ds-ddl-prediction">② DDLとDMLのどちら？（任意）
      <select id="ds-ddl-prediction" data-prediction>
        <option value="">予想せずに進む</option>
        <option value="DDL">DDL（表の構造）</option>
        <option value="DML">DML（表のデータ）</option>
      </select>
    </label>
  </div>
  <p><strong>選んだSQL</strong></p>
  <code class="ds-ddl-demo__sql" data-sql>CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(50));</code>
  <div class="ds-ddl-demo__controls">
    <button type="button" data-execute>③ 実行する（模擬操作）</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <p><strong data-kind>分類：実行後に表示</strong></p>
  <p>テーブルの列：<strong data-columns>テーブルなし</strong>　行数：<strong data-row-count>—</strong></p>
  <div class="ds-ddl-demo__table" data-table aria-label="employeesテーブルの現在の構造と行">
    <p>employees テーブルは存在しません。</p>
  </div>
  <div class="ds-ddl-demo__result">
    <p role="status" aria-live="polite" aria-atomic="true" data-feedback>最初はテーブルがありません。まずCREATEを実行してみましょう。</p>
    <p><strong>操作履歴</strong></p>
    <ol class="ds-ddl-demo__history" data-history><li>まだ実行していません。</li></ol>
  </div>
</div>
<noscript>
  <p>JavaScriptが無効な場合は、次の変化を確認してください。CREATEで「id」「name」の2列がある空の表を作成 → INSERTで1行追加 → SELECTでは表を変更せず取得 → ALTERで「department」列を追加 → UPDATEでnameを更新 → DELETEで行だけ削除 → DROPで表そのものを削除します。</p>
</noscript>
<script src="{{ '/assets/js/ds-ddl-dml-demo.js' | relative_url }}" defer></script>

**教材の前提：** `INSERT` はid=1の「佐藤」を追加し、`UPDATE` はid=1の名前を「鈴木」に変更し、`DELETE` はid=1の行を削除します。`id` は主キー（行を見分ける一意の値）なので、同じ `id` の行は追加できません。`UPDATE` や `DELETE` は、表があって条件に合う行がなければ0行を変更して完了します。教材は単純化した模擬操作であり、製品ごとのDDLトランザクションや制約、権限、SQL実行エラーのすべてを再現するものではありません。また、このページでは`SELECT`をDML側として扱いますが、DQLに分ける分類もあります。

0行更新と主キーの仕様は、PostgreSQLの公式文書で確認できます。 [UPDATE](https://www.postgresql.org/docs/current/sql-update.html) · [Primary Keys](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-PRIMARY-KEYS)

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
