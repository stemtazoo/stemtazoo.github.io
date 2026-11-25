---
layout: page
title: LEFT JOINとWHEREの関係とは？（SQLのひっかけ問題）【DS検定】
description: "LEFT JOINのあとに右テーブルの条件をWHEREへ書くと、NULL行が除外され、結果としてINNER JOINに近い結果になることがあります。ONとWHEREの役割、NULLの扱い、DS検定での判断ポイントを整理します。"
permalink: /ds/left-join-where/
categories: [data-engineering]
tags: [ds, data-processing, sql]
ds_area: dataengineering
ds_section: data-processing
prev: /ds/sql-where/
next: /ds/self-join/
last_modified_at: 2026-11-25
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

LEFT JOINのあとに**右テーブルの条件をWHEREへ書くと、NULL行が除外されて左側の行が消えることがあります。**

DS検定では、次の切り分けが重要です。

| 条件を書く場所 | 役割 |
|---|---|
| `ON` | どの行を結合するか決める |
| `WHERE` | 結合後の結果を絞り込む |

> LEFT JOINなのに左側の全行が残らない → **WHEREの右テーブル条件を確認する**

## 直感的な説明

LEFT JOINは、本来「左の表をすべて残す」結合です。

たとえば、全従業員に進行中プロジェクトを付けたいとします。

- 従業員は全員表示したい
- activeなプロジェクトだけ付けたい

ところが、結合後に `WHERE P.status = 'active'` と書くと、プロジェクトがない従業員では `P.status` がNULLになります。

NULLは `P.status = 'active'` を満たさないため、その行が消えます。

結果として、**LEFT JOINなのに「activeなプロジェクトを持つ人だけ」が残る**ことがあります。

## 定義・仕組み

### WHEREへ条件を書く場合

```sql
SELECT E.name, P.project_name
FROM Employees E
LEFT JOIN Projects P
  ON E.id = P.employee_id
WHERE P.status = 'active';
```

初学者向けには、次の順で考えると分かりやすいです。

1. `LEFT JOIN` で左側の従業員を残す
2. 結合できない右側はNULLになる
3. `WHERE P.status = 'active'` で結合後の行を絞る
4. `P.status` がNULLの行は残らない

| `P.status` | WHERE条件の結果 |
|---|---|
| `active` | 残る |
| `inactive` | 消える |
| `NULL` | 消える |

### ONへ条件を書く場合

全従業員を残したまま、activeなプロジェクトだけ結合したい場合は、条件を `ON` に書きます。

```sql
SELECT E.name, P.project_name
FROM Employees E
LEFT JOIN Projects P
  ON E.id = P.employee_id
 AND P.status = 'active';
```

この場合は、

- 左側の従業員は全員残る
- activeなプロジェクトだけ結合する
- 該当しなければ右側がNULLになる

という結果になります。

### 触って覚える：条件の場所で結果の行が変わる

「WHEREに置く」を押し、案件がない鈴木さんの行が残るか見てください。最初は「ONに置く」が選ばれています。社員は3人で、佐藤さんには進行中の案件、田中さんには終了済みの案件があります。

<link rel="stylesheet" href="{{ '/assets/css/first-step-demos.css' | relative_url }}">
<div class="first-step-demo" data-first-step="join" hidden>
  <fieldset>
    <legend><code>P.status = 'active'</code> を書く場所</legend>
    <label><input type="radio" name="demo-join-mode" value="on" checked> ONに置く</label>
    <label><input type="radio" name="demo-join-mode" value="where"> WHEREに置く</label>
  </fieldset>
  <ul data-board aria-label="結合結果"></ul>
  <p role="status" data-result></p>
</div>
<noscript><p>ONに条件を書くと、佐藤・鈴木・田中の3行が残り、鈴木と田中の案件はNULLになります。WHEREに書くと、進行中の案件を持つ佐藤だけが残ります。</p></noscript>

<script defer src="{{ '/assets/js/first-step-demos.js' | relative_url }}"></script>

## どんな場面で使う？

### 左側を必ず残したい集計

たとえば、

- 社員一覧に担当案件を付ける
- 全顧客に最新注文情報を付ける
- 全商品に在庫情報を付ける

といった場合です。

右テーブル側の条件をWHEREへ書くと、**対応データがない左側の行まで消える**ことがあるため注意します。

### SQLの結果を読み取る問題

DS検定では、

- LEFT JOINとINNER JOINの違い
- `ON` と `WHERE` の違い
- NULLの扱い

を組み合わせた判断問題として考えると整理しやすいです。

## よくある誤解・混同

### ❌ LEFT JOINなら必ず左側は全部残る

LEFT JOIN直後は残りますが、その後のWHEREで消えることがあります。

### ❌ ONとWHEREはどちらに条件を書いても同じ

違います。

| 構文 | 判断ポイント |
|---|---|
| `ON` | 結合する相手を制限する |
| `WHERE` | 結合後の行そのものを除外する |

### ❌ `NULL = 'active'` はfalseとして扱えばよい

SQLのNULL比較は通常の真偽値だけではなくUNKNOWNになります。WHEREではTRUEの行だけが残るため、結果としてNULL行は除外されます。

## まとめ（試験直前用）

- LEFT JOINは左側を残す結合
- `ON` は**結合条件**
- `WHERE` は**結合後の絞り込み**
- 右テーブル条件をWHEREへ書くとNULL行が消える
- **LEFTなのに全件出ない → WHEREを確認する**

## 公式情報・参考リンク

- [PostgreSQL Documentation｜Table Expressions](https://www.postgresql.org/docs/current/queries-table-expressions.html)
  - JOIN条件とWHERE条件の適用位置を確認できる公式ドキュメントです。外部結合では、ONでの条件付けと結合後のWHERE絞り込みで結果が変わる点が重要です。

## 対応スキル項目（ver.6 データエンジニアリング）

- **分類**：ITエンジニアリング
- **スキルカテゴリ**：プログラミング
- **サブカテゴリ**：SQL
- **必須スキル**：◯
- ★ SQLの構文を一通り知っていて、記述・実行できる（DML・DDLの理解、各種JOINの使い分け、集計関数とGROUP BY、CASE文を使用した縦横変換、副問合せやEXISTSの活用など）
- [ver.6 ★1スキルチェックで確認する](/ds/engineering-skillcheck/)
