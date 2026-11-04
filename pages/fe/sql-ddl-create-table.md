---
layout: page
title: SQLのDDLとは？CREATE TABLEと制約の書き方【基本情報技術者試験】
description: DDLとDMLを区別し、CREATE TABLE・ALTER TABLE・DROP TABLE、データ型、主キー・外部キー・NOT NULL・UNIQUE・CHECKをSQL例と制約判定教材で学びます。
permalink: /fe/sql-ddl-create-table/
tags: [fe, fe-technology, database, sql]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 92
date: 2026-11-04
last_modified_at: 2026-11-04
related_articles:
  - /fe/database-schema/
  - /fe/primary-key/
  - /fe/database-view-select-privilege/
  - /fe/grant-revoke-sql-privileges/
---

## まず結論

**DDL（Data Definition Language：データ定義言語）**は、表や制約などの**データベースの構造を定義・変更・削除**するSQLです。

基本情報技術者試験（FE）では、**構造を作るDDLと、表に入ったデータを扱うDMLを区別する**ことが重要です。

| 種類 | 代表的なSQL | 目的 |
|---|---|---|
| DDL | `CREATE TABLE`、`ALTER TABLE`、`DROP TABLE` | 表の構造を作る・変更する・削除する |
| DML | `SELECT`、`INSERT`、`UPDATE`、`DELETE` | 表のデータを検索・追加・更新・削除する |
| 権限管理（DCLと分類される場合がある） | `GRANT`、`REVOKE` | 利用者に操作権限を与える・取り消す |

なお、SQLの命令分類には教科書や資料による違いがあります。試験では**その文が構造を扱うのか、データを扱うのか**から判断しましょう。

## 直感的な説明

設備台帳を作る場面で考えてみます。まず「設備番号・名称・所属部署」という**列の設計図**を作るのがDDLです。

その台帳に「設備番号M001、名称ポンプ」という**実際のデータ**を登録するのがDMLです。

```text
CREATE TABLE → 台帳の枠を作る（DDL）
INSERT       → 台帳に1行登録する（DML）
ALTER TABLE  → 台帳の列を追加する（DDL）
UPDATE       → 登録済みの値を直す（DML）
DROP TABLE   → 台帳の表自体を削除する（DDL）
DELETE       → 表の行を削除する（DML）
```

**DROP TABLEとDELETEは、消す対象が「表自体」か「表の中の行」かで区別**します。

## 定義・仕組み

### CREATE TABLE：表と制約を定義する

次の例では部署表を先に作り、社員表から部署表を参照します。

```sql
CREATE TABLE 部署 (
    部署コード CHAR(3) PRIMARY KEY,
    部署名 VARCHAR(30) NOT NULL
);

CREATE TABLE 社員 (
    社員コード CHAR(5) PRIMARY KEY,
    氏名 VARCHAR(20) NOT NULL,
    部署コード CHAR(3),
    年齢 NUMERIC(3, 0) CHECK (年齢 >= 0),
    FOREIGN KEY (部署コード)
        REFERENCES 部署(部署コード)
);
```

- `社員コード` は重複せず、NULLにもできない主キー。
- `氏名` はNULLを登録できない。
- `部署コード` は参照先の部署コードと対応する外部キー。
- `年齢` は0以上を許可する制約付きの数値列。

ここでは外部キー列のNULLを許可しています。**外部キーを指定しただけでNOT NULLになるわけではありません**。NULL以外の値を設定するときは、参照先の部署表に対応する値が必要です。

### データ型：CHAR・VARCHAR・NUMERIC

| データ型 | 意味 | 例 |
|---|---|---|
| `CHAR(3)` | 固定長の文字列 | 3文字の部署コード |
| `VARCHAR(30)` | 最大長を指定する可変長文字列 | 最大30文字の部署名 |
| `NUMERIC(6,2)` | 桁数と小数部の桁数を指定する正確な数値型 | 全6桁、うち小数部2桁 |

`NUMERIC(6,2)` は整数部に最大4桁、小数部に2桁の精度を持つ例です。文字列の長さの単位や空白の扱いはDBMSにより異なる場合があります。

### 制約：どの値が登録できる？

| 制約 | 役割 | 覚えるポイント |
|---|---|---|
| `PRIMARY KEY` | 行を一意に識別 | 重複不可・NULL不可 |
| `FOREIGN KEY` | 別の表との参照関係を守る | 参照先のキーに存在する値など |
| `NOT NULL` | NULLを禁止 | 空文字列との違いに注意 |
| `UNIQUE` | 指定した列・列の組の一意性を保証 | NULLの扱いはDBMSによる |
| `CHECK` | 条件を満たす値を制限 | 例：`CHECK (年齢 >= 0)` |

**外部キーの指定は `FOREIGN KEY (列名) REFERENCES 参照先表(列名)`** と読みます。参照先には通常、主キーや一意性が保証された列を指定します。詳細は[主キーの記事](/fe/primary-key/)へ進んでください。

### 触って覚える：このデータは登録できる？

最初に予想してください。**社員コードが重複したら登録できるでしょうか？** 制約を切り替えると、対象の表と「登録しようとする1行」が変わります。予想してから結果を表示してください。

<link rel="stylesheet" href="{{ '/assets/css/fe-sql-ddl-visualizer.css' | relative_url }}">

<div id="fe-ddl-demo" class="fe-ddl-demo">
  <div class="fe-ddl-demo__choices" role="group" aria-label="確認する制約">
    <button type="button" data-case="primary" aria-pressed="true">主キーの重複</button>
    <button type="button" data-case="foreign" aria-pressed="false">外部キー</button>
    <button type="button" data-case="notnull" aria-pressed="false">NOT NULL</button>
    <button type="button" data-case="check" aria-pressed="false">CHECK</button>
    <button type="button" data-case="valid" aria-pressed="false">登録できる例</button>
  </div>
  <p data-rule class="fe-ddl-demo__rule">社員コード：PRIMARY KEY（重複不可・NULL不可）</p>
  <p data-reference class="fe-ddl-demo__reference"></p>
  <div class="fe-ddl-demo__table-wrap">
    <table>
      <thead><tr><th data-heading="0" scope="col">社員コード</th><th data-heading="1" scope="col">氏名</th></tr></thead>
      <tbody data-existing><tr><td>A001</td><td>田中</td></tr><tr><td>A002</td><td>鈴木</td></tr></tbody>
    </table>
  </div>
  <p><strong>これから登録する行：</strong><span data-new-row>A001 / 佐藤</span></p>
  <fieldset class="fe-ddl-demo__guess">
    <legend>登録できると予想しますか？</legend>
    <label><input type="radio" name="fe-ddl-guess" value="yes"> 登録できる</label>
    <label><input type="radio" name="fe-ddl-guess" value="no"> 登録できない</label>
  </fieldset>
  <div class="fe-ddl-demo__actions">
    <button type="button" data-check>判定する</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <div data-result hidden class="fe-ddl-demo__result">
    <p data-feedback role="status" aria-live="polite"></p>
    <p data-explanation></p>
  </div>
  <p class="fe-ddl-demo__note">固定された教材データの制約判定です。実際のDBMSでSQLを実行するわけではありません。外部キーの例では参照先「部署表」にD01・D02が登録済みと仮定します。</p>
</div>
<noscript><p>JavaScriptが無効でも学習できます。主キーの重複、存在しない外部キー、NOT NULL列へのNULL、CHECKに反する負の値は登録できません。既存と重複しない社員コード・参照先に存在する部署コードなら登録できます。</p></noscript>
<script src="{{ '/assets/js/fe-sql-ddl-visualizer.js' | relative_url }}" defer></script>

### ALTER TABLE・DROP TABLE

```sql
ALTER TABLE 社員 ADD COLUMN 入社年 NUMERIC(4,0);

DROP TABLE 社員;
```

`ALTER TABLE` は既存の表の構造を変更し、`DROP TABLE` は表自体を削除します。**データだけを消したい場合の `DELETE` とは異なります。**

### CREATE VIEW・権限管理との役割分担

`CREATE VIEW` は実表やビューを基にビューを定義します。詳細は[ビューの記事](/fe/database-view-select-privilege/)で確認できます。

`GRANT` と `REVOKE` は利用者の権限を管理する命令です。[権限管理の記事](/fe/grant-revoke-sql-privileges/)を参照してください。

## 科目Aでどう出る？

| 問題文の表現 | SQLの分類・用語 |
|---|---|
| 新しい表を作る | `CREATE TABLE`（DDL） |
| 既存の表に列を追加 | `ALTER TABLE`（DDL） |
| 表自体を削除 | `DROP TABLE`（DDL） |
| 表に行を追加 | `INSERT`（DML） |
| 表のデータを更新 | `UPDATE`（DML） |
| 重複もNULLも許さず行を識別 | `PRIMARY KEY` |
| 他表のキーへの参照を指定 | `FOREIGN KEY ... REFERENCES` |

### 確認問題

次のSQLの `FOREIGN KEY` の役割として最も適切なのはどれか。

```sql
CREATE TABLE 注文 (
    注文番号 INTEGER PRIMARY KEY,
    商品番号 CHAR(4),
    FOREIGN KEY (商品番号) REFERENCES 商品(商品番号)
);
```

※商品表の`商品番号`は主キーとします。

- ア：注文表の商品番号が必ずNULLにならないようにする。
- イ：注文表の商品番号に、商品表に存在する商品番号などの参照規則を適用する。
- ウ：注文表の商品番号が表内で重複しないようにする。

<details markdown="1">
<summary>正解と理由を見る（タップして開く）</summary>

**正解：イ。** 外部キーは参照先の表との整合性を守る制約です。外部キーの列は、指定がなければNULLを許す場合があり、表内で同じ商品番号を複数の注文が参照することもできます。アはNOT NULL、ウはUNIQUEやPRIMARY KEYに近い説明です。

</details>

## どんな場面で使う？

業務システムで設備台帳や在庫表を新しく作るとき、データ型・主キー・外部キーを設定するために利用します。業務ルールを表の制約として表現すると、アプリケーションから誤ったデータが登録されることを防ぎやすくなります。

## よくある誤解・混同

### 「FOREIGN KEYは必ずNULL禁止」？

違います。NULLを禁止するには、必要に応じて`NOT NULL`も指定します。

### 「UNIQUEとPRIMARY KEYは同じ」？

どちらも一意性を扱いますが、主キーにはNULL不可の性質があります。UNIQUE列のNULLの扱いはDBMSの仕様に注意が必要です。

### 「CREATE TABLEとINSERTは両方とも表を作る」？

違います。前者は**表の枠を定義**し、後者は**すでにある表に行を追加**します。

## まとめ（試験直前用）

- DDLは**表などの構造**を定義・変更・削除する。
- `CREATE TABLE` は新規作成、`ALTER TABLE` は構造変更、`DROP TABLE` は削除。
- `PRIMARY KEY` は重複・NULL不可。外部キーは参照先との整合性。
- `NOT NULL` はNULL禁止、`UNIQUE` は一意性、`CHECK` は条件による値の制限。
- **表自体を消すDROPと、行を消すDELETEを混同しない。**

{% include fe_article_footer.html %}
