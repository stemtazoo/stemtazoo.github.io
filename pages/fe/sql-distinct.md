---
layout: page
title: SQLのDISTINCTとは？重複行の除去と複数列の判定【基本情報技術者試験】
description: SELECT DISTINCTの重複排除を、列の組合せ・結合後の結果・COUNT(DISTINCT)・GROUP BY・NULLとの違いから理解。列を切り替える操作教材でFE科目Aに備えます。
permalink: /fe/sql-distinct/
tags: [fe, fe-technology, database, sql]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 95
date: 2026-11-04
last_modified_at: 2026-11-04
related_articles:
  - /fe/relational-operations/
  - /fe/sql-aggregate-functions/
  - /fe/sql-group-by-aggregate-functions/
---

## まず結論

**DISTINCT**は、SQLの`SELECT`で得られた結果から、**指定した列の値の組合せが重複する行を1行にまとめる**指定です。

```sql
SELECT DISTINCT 顧客名, 商品名
FROM 注文表;
```

ここでは「顧客名だけ」でも「商品名だけ」でもなく、**顧客名と商品名の組合せ**が同じ行を重複として扱います。

> DISTINCTは元の表の行を削除しません。取得結果の重複を取り除きます。

## 直感的な説明

次の5件の注文データを見てください。

| 顧客名 | 商品名 | 単価 |
|---|---|---:|
| 大山商店 | テレビ | 25,000 |
| 大山商店 | テレビ | 25,000 |
| 大山商店 | テレビ | 30,000 |
| 小川商店 | テレビ | 30,000 |
| 小川商店 | テレビ | 30,000 |

`SELECT DISTINCT 顧客名`なら、**大山商店・小川商店の2行**が残ります。

`SELECT DISTINCT 顧客名, 商品名, 単価`なら、同じ顧客・商品でも単価が違う行は別物なので、**3行**残ります。

**どの列で比較するか**が行数を決めるポイントです。

## 定義・仕組み

### SELECTとSELECT DISTINCT

```sql
SELECT 顧客名, 商品名, 単価
FROM 注文表;
```

これは指定した列をそのまま取得し、重複する結果行も残します。一方、

```sql
SELECT DISTINCT 顧客名, 商品名, 単価
FROM 注文表;
```

では、同じ3列の値の組合せが複数回出てきても1行だけ残します。**DISTINCTを列ごとに個別適用するわけではありません。**

### 触って覚える：指定する列を変えて結果を見る

まず予想してください。**「顧客名＋商品名」の2列を指定すると何行残るでしょうか？**

選択する列とDISTINCTの有無を変更し、予想してから「結果を表示」を押してください。元データ5行と、SELECT結果の行数を見比べましょう。

<link rel="stylesheet" href="{{ '/assets/css/fe-sql-distinct-visualizer.css' | relative_url }}">

<div id="fe-sql-distinct-demo" class="fe-sql-distinct-demo">
  <fieldset class="fe-sql-distinct-demo__choice">
    <legend>① SELECTで取り出す列</legend>
    <label><input type="radio" name="fe-distinct-columns" value="customer"> 顧客名だけ</label>
    <label><input type="radio" name="fe-distinct-columns" value="pair" checked> 顧客名＋商品名</label>
    <label><input type="radio" name="fe-distinct-columns" value="all"> 顧客名＋商品名＋単価</label>
  </fieldset>
  <label class="fe-sql-distinct-demo__toggle"><input type="checkbox" id="fe-distinct-enable" checked> DISTINCTを指定する</label>
  <p class="fe-sql-distinct-demo__query" data-query>SELECT DISTINCT 顧客名, 商品名 FROM 注文表;</p>
  <p><strong>② 残る行数を予想：</strong> <label for="fe-distinct-guess">予想した行数</label>
  <select id="fe-distinct-guess">
    <option value="">予想しないで表示</option>
    <option value="1">1行</option><option value="2">2行</option><option value="3">3行</option>
    <option value="4">4行</option><option value="5">5行</option>
  </select></p>
  <div class="fe-sql-distinct-demo__actions">
    <button type="button" data-show>結果を表示</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <div data-result hidden>
    <p data-feedback role="status" aria-live="polite"></p>
    <div class="fe-sql-distinct-demo__table-wrap">
      <table><thead data-head></thead><tbody data-body></tbody></table>
    </div>
    <p data-reason></p>
  </div>
  <p class="fe-sql-distinct-demo__note">固定の架空データでSELECT結果を再現する教材です。表へのSQL実行は行いません。結果の並び順は学習用に固定していますが、SQLで順序を保証したい場合はORDER BYが必要です。</p>
</div>
<noscript><p>JavaScriptなしでも本文の例で学べます。顧客名だけのDISTINCTは2行、顧客名＋商品名でも2行、3列すべてなら3行、DISTINCTなしなら5行です。</p></noscript>
<script src="{{ '/assets/js/fe-sql-distinct-visualizer.js' | relative_url }}" defer></script>

### JOIN後にDISTINCTを使う

たとえば注文表と商品表を商品番号で結合し、顧客名・商品名・単価を取得します。

```sql
SELECT DISTINCT o.顧客名, p.商品名, p.単価
FROM 注文表 AS o
JOIN 商品表 AS p
  ON o.商品番号 = p.商品番号;
```

**JOINで対応する行を結び付けた後、SELECTで選んだ列の組合せについて重複を除きます。** 同じ顧客が同一商品を2回注文していても、選んだ3列が同じなら結果は1行です。注文番号などをSELECTに追加すると、重複ではなくなる場合があります。

ここで重要なのは、**結合条件の誤りによる不要な行の増殖をDISTINCTでごまかさない**ことです。最初に結合条件を確認しましょう。

### GROUP BYとの違い

```sql
SELECT DISTINCT 顧客名
FROM 注文表;
```

は重複を取り除いて顧客名を並べます。

```sql
SELECT 顧客名, COUNT(*)
FROM 注文表
GROUP BY 顧客名;
```

は顧客ごとにグループを作り、**件数などを集計**します。単純な列の一覧では同じ顧客名が並ぶ場合もありますが、学習目的は異なります。詳細は[GROUP BYの記事](/fe/sql-group-by-aggregate-functions/)で確認してください。

### COUNT(DISTINCT)とNULL

```sql
SELECT COUNT(DISTINCT 顧客名)
FROM 注文表;
```

は、**NULLを除いた異なる顧客名の数**を返します。この例では2です。

`SELECT DISTINCT 顧客名` は、複数のNULLが存在する場合、そのNULLを重複としてまとめて**1行にできる**点に注意してください。一方、`COUNT(DISTINCT 顧客名)` はNULLを数えません。

## 科目Aでどう出る？

| 問題文の手掛かり | 判断 |
|---|---|
| 取得結果の重複する行を除きたい | DISTINCT |
| 顧客名と商品名の組合せで重複を判定 | SELECT DISTINCT 顧客名, 商品名 |
| 重複を除いた件数を数える | COUNT(DISTINCT 列名) |
| グループ別に件数・合計を求める | GROUP BY |
| 行を削除して元の表から消す | DELETE（DISTINCTではない） |

### 確認問題

ある表に、次の5行があるとします。

| 部署 | 担当 |
|---|---|
| 設計 | 佐藤 |
| 設計 | 佐藤 |
| 設計 | 鈴木 |
| 保全 | 佐藤 |
| 保全 | 佐藤 |

`SELECT DISTINCT 部署, 担当 FROM 担当表` の結果は何行でしょうか。

- ア：2行
- イ：3行
- ウ：4行
- エ：5行

<details markdown="1">
<summary>正解と解説を見る（タップして開く）</summary>

**正解：イ（3行）。** 残る組合せは「設計・佐藤」「設計・鈴木」「保全・佐藤」の3種類です。担当だけが同じでも、部署が違えば別の行です。

</details>

## どんな場面で使う？

重複した注文データから顧客の一覧を作りたい場合や、複数表を結合した結果から重複を除いて表示したい場合に利用します。ただし、DISTINCTを付けるとソートやハッシュ処理などのコストが生じる場合があります。必要な列と結合条件を正しく指定することが先決です。

## よくある誤解・混同

### 「DISTINCTは最初の列だけに適用される」？

違います。`SELECT DISTINCT A, B` は**AとBの組合せ**で重複を調べます。

### 「DISTINCTを使うと表の行が削除される」？

違います。SELECTの結果から重複を除くだけで、保存済みのデータは変化しません。

### 「DISTINCTなら結果の並び順も決まる」？

違います。順序が必要なら`ORDER BY`を指定します。

### 「COUNT(DISTINCT 列名)はNULLも1種類として数える」？

違います。COUNT(DISTINCT 列名)ではNULLは数えません。

## まとめ（試験直前用）

- DISTINCTは**取得結果の重複する行**を1行にまとめる。
- 複数列なら**その列の組合せ**で判定する。
- JOIN後でも、選択した列の組合せが同じなら重複を除く。
- COUNT(DISTINCT 列名)はNULLを除いた異なる値の数。
- GROUP BYはグループごとの集計をする。DISTINCTと使いどころを区別する。

{% include fe_article_footer.html %}
