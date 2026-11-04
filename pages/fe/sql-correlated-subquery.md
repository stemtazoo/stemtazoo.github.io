---
layout: page
title: SQLの相関サブクエリとは？COUNT・EXISTS・INと0件の扱い【基本情報技術者試験】
description: 相関サブクエリとIN・NOT IN・EXISTS・NOT EXISTSを比較。NULLを含むNOT INの落とし穴、COUNTが0を返す場合、外側の各行の判定を操作教材で学びます。
permalink: /fe/sql-correlated-subquery/
tags: [fe, fe-technology, database, sql]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 130
date: 2026-09-27
last_modified_at: 2026-11-04
---

## まず結論

**相関サブクエリ**とは、サブクエリの中から**外側の問合せの行を参照して判定するSQL**です。

基本情報技術者試験では、次の3点を押さえると選択肢を切りやすくなります。

```text
内側で外側の別名を参照している
→ 相関サブクエリ

COUNTで件数を求める
→ 該当行が0件でも0として比較できる

EXISTS / IN
→ 該当する行・値が存在しなければ候補にならない
```

特に重要なのは、

> **「5件未満」には0件も含まれる**

という点です。

0件を条件に含めたい問題では、**「0を返せるSQLなのか」「そもそも候補行が消えてしまわないか」**まで確認します。

## 直感的な説明

例えば、部署ごとの「プログラマ人数が3人未満」の部署を探すとします。

相関サブクエリでは、外側の部署を1つずつ見ながら、その部署に属するプログラマの人数を内側で数えるイメージです。

```text
外側：部署Aを見る
  ↓
内側：部署Aのプログラマを数える
  ↓
2人 → 3人未満なので残す

外側：部署Bを見る
  ↓
内側：部署Bのプログラマを数える
  ↓
0人 → 3人未満なので残す

外側：部署Cを見る
  ↓
内側：部署Cのプログラマを数える
  ↓
4人 → 3人未満ではないので除外
```

ポイントは、**内側の問合せを独立して読むのではなく、外側の現在行を渡して実行する**ことです。

## 定義・仕組み

### 相関サブクエリ

次のSQLを考えます。

```sql
SELECT DISTINCT A.部署コード
FROM 社員 A
WHERE 3 > (
    SELECT COUNT(*)
    FROM 社員 B
    WHERE B.部署コード = A.部署コード
      AND B.職務 = 'プログラマ'
);
```

内側のSQLには、外側の表別名 `A` が登場しています。

```sql
B.部署コード = A.部署コード
```

この条件によって、

> **「今、外側で見ている社員と同じ部署」**

という意味になります。

したがって、外側の各行について内側の件数を求め、条件を満たすか判定します。

### COUNTは0件でも0を返す

`COUNT(*)` は、条件に合う行の件数を返します。

```text
3件見つかる
→ COUNT(*) = 3

1件見つかる
→ COUNT(*) = 1

1件も見つからない
→ COUNT(*) = 0
```

そのため、

```sql
3 > (SELECT COUNT(*) ...)
```

なら、0件も条件を満たします。

```text
0 < 3 → TRUE
1 < 3 → TRUE
2 < 3 → TRUE
3 < 3 → FALSE
```

`COUNT(列名)` はNULLを除いて数えるため、単純な行数を数えたいときは `COUNT(*)` が分かりやすいです。列にNULLがないことが分かっている場合は、`COUNT(列名)` でも同じ件数になります。

集計関数そのものの基本は、[SQLの集計関数とは？COUNT・SUM・AVG・MAXとWHEREの違い](/fe/sql-aggregate-functions/)で整理しています。

### GROUP BYでは「0件のグループ」は作られない

次のように、先にプログラマだけへ絞ってから部署ごとにまとめる場合を考えます。

```sql
SELECT 部署コード
FROM 社員
WHERE 職務 = 'プログラマ'
GROUP BY 部署コード
HAVING COUNT(*) < 3;
```

プログラマが1人または2人いる部署は抽出できます。

しかし、プログラマが0人の部署は、

```text
WHERE 職務='プログラマ'
↓
残る行が0件
↓
GROUP BYする行がない
↓
部署のグループ自体が作られない
```

ため、結果に現れません。

ここが試験で非常に重要な違いです。

> **COUNTが0を返すことと、GROUP BYの結果に0件のグループが現れることは別です。**

`GROUP BY` と `HAVING` の基本は、[SQLのGROUP BYとは？集計関数・WHERE・HAVINGの見分け方](/fe/sql-group-by-aggregate-functions/)で確認できます。

### EXISTSは「1件でもあるか」を見る

`EXISTS` は、サブクエリが1行でも返せばTRUEになります。

```sql
WHERE EXISTS (
    SELECT 1
    FROM 社員 B
    WHERE B.部署コード = A.部署コード
      AND B.職務 = 'プログラマ'
)
```

これは、

```text
同じ部署にプログラマが1人でもいる
→ TRUE

1人もいない
→ FALSE
```

という判定です。

そのため、**0人の部署を残したい条件**では、単純な `EXISTS` では落ちてしまいます。

### INは「値が候補集合にあるか」を見る

`IN` は、サブクエリなどで作った値の集合に、対象の値が含まれるかを判定します。**INを使う副問合せが、必ずしも相関副問合せとは限りません**。内側から外側の列を参照するときだけ相関副問合せです。

```text
候補集合に部署Aがある
→ TRUE

候補集合に部署Bがない
→ FALSE
```

つまり、0件の部署がサブクエリの候補集合に現れなければ、その部署は `IN` では選ばれません。

### IN・NOT IN・EXISTS・NOT EXISTSの違い

| 条件 | 判定すること | 典型的な用途 |
|---|---|---|
| `IN (副問合せ)` | 値が内側の結果に含まれるか | 条件を満たす社員番号を抽出 |
| `NOT IN (副問合せ)` | 値が候補に含まれないか | 対象外の社員番号を抽出（NULLに注意） |
| `EXISTS (副問合せ)` | 内側の結果が1行でも存在するか | 関連行がある社員を抽出 |
| `NOT EXISTS (副問合せ)` | 内側の結果が0行か | 関連行がない社員を抽出 |

たとえば「IPスキルを持つ社員」を調べる場合、次のSQLはいずれも**社員番号がNULLでない前提で**同じ社員を選びます。

```sql
-- IN：まずIPスキルを持つ社員番号の集合を得る
SELECT *
FROM 社員 AS e
WHERE e.社員番号 IN (
    SELECT s.社員番号
    FROM 社員スキル AS s
    WHERE s.スキルコード = 'IP'
);
```

```sql
-- EXISTS：外側の社員1行を内側の条件に渡す（相関副問合せ）
SELECT *
FROM 社員 AS e
WHERE EXISTS (
    SELECT 1
    FROM 社員スキル AS s
    WHERE s.社員番号 = e.社員番号
      AND s.スキルコード = 'IP'
);
```

`NOT EXISTS`なら、`EXISTS`を`NOT EXISTS`に変えれば**IPスキルが存在しない社員**を選べます。`NOT IN`でも似た結果になる場合がありますが、次のNULLの違いを必ず確認しましょう。

### NOT INとNULL：単純な「含まれない」とは限らない

SQLでは、NULLは通常の値とは異なり、比較の結果が**UNKNOWN（不明）**になる場合があります。たとえば内側の結果が `('002', NULL)` のとき、

```sql
WHERE 社員番号 NOT IN ('002', NULL)
```

では、`'001'`も`'003'`も **TRUEではなくUNKNOWN** になるため、WHEREで抽出されません。`'002'`なら一致があるのでFALSEです。

`NOT EXISTS`では、外側の社員番号と一致する**行があるか**を調べます。内側の社員番号がNULLの行は、通常の等号比較では外側の社員番号と一致しないため、上記と同じNULLによる落とし穴を避けられます。

**「NOT INとNOT EXISTSは常に同じ」ではありません。** 試験問題にNULLの有無が書かれていたら、最優先で確認してください。

### 触って覚える：外側の社員を変えて判定しよう

まず予想しましょう。**IPスキルを持たない社員を探すとき、社員スキル表に社員番号NULLのIPスキル行を追加すると、NOT INの結果はどうなるでしょうか？**

次の教材で社員、条件、NULLを含むかを変更し、判定理由を確認してください。画面上の結果は固定データを使うシミュレーションで、SQLを実際に実行するものではありません。

<link rel="stylesheet" href="{{ '/assets/css/fe-subquery-comparison.css' | relative_url }}">

<div id="fe-subquery-demo" class="fe-subquery-demo">
  <div class="fe-subquery-demo__tables">
    <div>
      <strong>社員表（外側）</strong>
      <table>
        <thead><tr><th scope="col">番号</th><th scope="col">氏名</th></tr></thead>
        <tbody><tr><td>001</td><td>田中</td></tr><tr><td>002</td><td>鈴木</td></tr><tr><td>003</td><td>佐藤</td></tr><tr><td>004</td><td>高橋</td></tr></tbody>
      </table>
    </div>
    <div>
      <strong>社員スキル表（内側）</strong>
      <table>
        <thead><tr><th scope="col">番号</th><th scope="col">スキル</th></tr></thead>
        <tbody data-skills><tr><td>001</td><td>FE</td></tr><tr><td>002</td><td>IP</td></tr><tr><td>002</td><td>FE</td></tr><tr><td>004</td><td>DB</td></tr></tbody>
      </table>
    </div>
  </div>
  <div class="fe-subquery-demo__controls">
    <label for="fe-subquery-person">① 外側で判定する社員</label>
    <select id="fe-subquery-person"><option value="001">001 田中</option><option value="002" selected>002 鈴木</option><option value="003">003 佐藤</option><option value="004">004 高橋</option></select>
    <label for="fe-subquery-mode">② SQLの条件</label>
    <select id="fe-subquery-mode"><option value="in">IN</option><option value="notin">NOT IN</option><option value="exists" selected>EXISTS</option><option value="notexists">NOT EXISTS</option></select>
    <label class="fe-subquery-demo__checkbox"><input id="fe-subquery-null" type="checkbox"> 社員番号NULL、スキルIPの行を内側に追加する</label>
  </div>
  <p data-query class="fe-subquery-demo__query">WHERE EXISTS (SELECT 1 FROM 社員スキル s WHERE s.社員番号 = e.社員番号 AND s.スキルコード = 'IP')</p>
  <fieldset class="fe-subquery-demo__prediction">
    <legend>③ この社員は抽出される？</legend>
    <label><input type="radio" name="fe-subquery-guess" value="yes"> 抽出される</label>
    <label><input type="radio" name="fe-subquery-guess" value="no"> 抽出されない</label>
  </fieldset>
  <div class="fe-subquery-demo__actions">
    <button type="button" data-check>結果と理由を見る</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <div data-result hidden class="fe-subquery-demo__result">
    <p data-feedback role="status" aria-live="polite"></p>
    <p data-detail></p>
  </div>
  <p class="fe-subquery-demo__note">社員番号は外側ではNULLなし。内側のIPスキル社員番号は通常「002」、チェック時は「002とNULL」です。IN／NOT INはその集合との比較、EXISTS／NOT EXISTSは社員番号一致行の存在で判断します。WHEREはTRUEの行だけを抽出します。</p>
</div>
<noscript><p>JavaScriptなしでも判定できます。通常のIPスキル社員番号は002なので、INとEXISTSは002だけ、NOT INとNOT EXISTSは001・003・004を抽出します。内側にNULLがある場合、NOT INは002もそれ以外も抽出しませんが、NOT EXISTSは001・003・004を抽出します。</p></noscript>
<script src="{{ '/assets/js/fe-subquery-comparison.js' | relative_url }}" defer></script>

## 科目Aでどう出る？

科目Aでは、複数のSQL文から、条件どおりのデータを抽出するものを選ぶ問題として出ます。

このタイプは、SQL全体を一度に読もうとせず、次の順番で見ると整理しやすくなります。

```text
1. 外側は何を候補にしているか
2. 内側は外側の行を参照しているか
3. 内側で何を数えているか
4. 0件のとき何が返るか
5. 最後の比較条件を満たすか
```

### まず「何を数えているか」を確認する

例えば、

```sql
SELECT COUNT(*)
FROM 社員 B
WHERE B.部署コード = A.部署コード
  AND B.職務 = 'プログラマ'
```

なら、

```text
同じ部署
＋
職務がプログラマ
↓
その人数を数える
```

です。

一方、

```sql
AND B.職務 <> 'プログラマ'
```

なら、数えているのは**プログラマ以外**です。

`COUNT` が書かれているだけで正しいと判断せず、**COUNTの前にWHEREで何を残したか**を確認します。

### 「未満」に0が含まれることを確認する

```text
5人未満
→ 0, 1, 2, 3, 4人

5人以下
→ 0, 1, 2, 3, 4, 5人
```

この違いはSQL以前の条件整理ですが、試験では非常に重要です。

「0人」まで含むなら、

> **0件のとき、そのSQLはどうなる？**

と必ず確認します。

### 外側の候補集合にも注意する

相関サブクエリが0を返せても、外側の表に候補自体が存在しなければ結果には出ません。

例えば、

```sql
FROM 社員 A
```

から部署コードを出している場合、社員が1人もいない部署は外側に登場しません。

試験では、**どの表から候補を取り出しているか**も確認します。

## どんな場面で使う？

相関サブクエリは、外側の各行について、関連するデータを個別に調べたいときに使えます。

例えば、

- 各部署について、その部署の社員数を調べる
- 各顧客について、その顧客の注文件数を調べる
- 各商品について、その商品の在庫が存在するか調べる
- 各社員について、その社員より給与が高い人がいるか調べる

といった場面です。

イメージは常に、

```text
外側の1行を決める
↓
その値を内側へ渡す
↓
内側で関連データを調べる
↓
条件を満たせば外側の行を残す
```

です。

実務ではJOINや集計を使って同じ結果を表現できる場合もありますが、FE試験ではまず、**相関条件が何を結び付けているかを読めること**が重要です。

## よくある誤解・混同

### COUNTが0なら、その部署は必ず結果に出る

必ずではありません。

`COUNT` のサブクエリまで到達するには、まず外側の問合せにその候補が必要です。

```text
外側に候補がある
＋
内側COUNTが0
→ 0として比較できる

外側に候補自体がない
→ そもそも判定されない
```

### GROUP BY + HAVING COUNT(*) < 5なら0人も含む

そのままでは含まれない場合があります。

先に `WHERE 職務='プログラマ'` で絞っていると、プログラマ0人の部署には行が残らず、グループ自体が作られません。

```text
COUNTの結果が0
≠
0件のグループが存在する
```

と切り分けます。

### EXISTSの中にCOUNTを書けば0件も判定できる

`EXISTS` が見るのは、サブクエリが**行を返すかどうか**です。

集計関数を使うと、書き方によっては0件でも集計結果の1行が返るため、意図と違う判定になることがあります。

試験では、`EXISTS` を見たらまず、

> **「何か1行でも存在するか」を判定している**

と捉えます。

### NOT INとNOT EXISTSはどちらも「ない」だから同じ？

違います。**内側の候補にNULLが含まれるとNOT INはUNKNOWNになる場合がある**一方、NOT EXISTSは一致する行が存在するかを評価します。NULLを含むデータの否定条件では、違いを確認する必要があります。

### INと相関サブクエリは同じ

同じ結果を作れる場合はありますが、考え方は違います。

```text
IN
→ 値が候補集合に含まれるか

相関サブクエリ
→ 外側の現在行を使って内側を評価する
```

SQLの見た目よりも、**何を比較・判定しているか**を読みます。

## まとめ（試験直前用）

- 相関サブクエリは、**内側から外側の現在行を参照する**
- `COUNT(*)` は、該当行が0件でも **0** を返せる
- `GROUP BY` は、元になる行が0件なら**グループ自体が作られない**
- `EXISTS` は「1件でもあるか」、`IN` は「値が候補集合にあるか」を見る
- `NOT EXISTS` は一致行が0件かを判定する。`NOT IN` は候補集合にNULLが含まれるとUNKNOWNに注意
- 「5件未満」には **0件も含まれる**
- 試験では、**何を数えているか・0件のときどうなるか・外側の候補は何か**を確認する

> **0件を含む条件では、「0を返せるか」だけでなく「候補そのものが消えないか」を見る。**

## 公式情報・参考リンク

- [PostgreSQL Documentation｜Subquery Expressions](https://www.postgresql.org/docs/current/functions-subquery.html)
  - EXISTSやINなど、サブクエリ式の意味を確認できる公式リファレンスです。
- [PostgreSQL Documentation｜Aggregate Functions](https://www.postgresql.org/docs/current/functions-aggregate.html)
  - COUNTなどの集計関数の仕様を確認できます。
- [IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)
  - 基本情報技術者試験の公式情報と最新の試験範囲を確認できます。

{% include fe_article_footer.html %}
