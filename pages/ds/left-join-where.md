---
layout: page
title: LEFT JOINとWHEREの関係とは？（SQLのひっかけ問題）【DS検定】
description: "LEFT JOINのあとに右テーブルの条件をWHEREへ書くと、NULL行が除外され、結果としてINNER JOINに近い結果になることがあります。ONとWHEREの役割、NULLの扱い、DS検定での判断ポイントを整理します。"
permalink: /ds/left-join-where/
categories: [data-engineering]
tags: [ds, data-processing, sql]
prev: /ds/sql-where/
next: /ds/self-join/
last_modified_at: 2026-08-16
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

## 対応スキル項目（データエンジニアリング力シート）

- データ基盤
- データベース
- ★ SQLを用いてデータの抽出・結合・集計ができる
- ★ データベースの基本構造と操作（SELECT、JOINなど）を理解している

{% include ds_article_footer.html %}
