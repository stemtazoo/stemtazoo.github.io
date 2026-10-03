---
layout: page
title: 主キーとは？重複・NULL・複合主キーを整理【基本情報技術者試験】
description: 主キーを、表の行を一意に識別するキーとして整理します。重複不可・NULL不可と複合主キーに加え、UPDATEの対象行、変更後の候補、制約確認を操作図で追います。既存行との重複と更新対象どうしの重複、主キー自体を更新できる条件を、科目Aの判断につなげます。
permalink: /fe/primary-key/
tags: [fe, fe-technology, database]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 25
date: 2026-09-23
last_modified_at: 2026-10-03
---

## まず結論

**主キー（PRIMARY KEY）**は、表の中の**1行を一意に識別するためのキー**です。

基本情報技術者試験では、まず次の2つを押さえます。

~~~text
主キー
├─ 同じ値を重複させない
└─ NULLにできない
~~~

つまり、**主キーを見れば、どの行なのか一つに決まる**ことが重要です。

また、主キーは必ず1列とは限りません。複数の列を組み合わせた**複合主キー**も作れます。

## 直感的な説明

社員表を考えてみます。

| 社員番号 | 氏名 | 部署 |
|---|---|---|
| 1001 | 山田 | 設計 |
| 1002 | 鈴木 | 営業 |
| 1003 | 佐藤 | 設計 |

社員番号を主キーにすると、1002を見れば鈴木さんの行だと一つに決まります。

同じ社員番号が複数あると、社員番号だけでは行を一意に特定できません。また、主キーがNULLでも、その行を識別する値がありません。

そのため、主キーには**重複もNULLも認められません**。

## 定義・仕組み

### 主キーの役割

主キーは、その表にある各行を一意に識別します。

~~~text
主キーの値
↓
表の中の1行が決まる
~~~

関係データベースの基本については、先に[関係データベースとは？](/fe/relational-model/)を確認すると理解しやすくなります。

### 一意性とNULL

主キーの値は重複できず、NULLにもできません。

~~~text
重複しない
＋
NULLではない
↓
主キーで行を一意に識別
~~~

### 複合主キー

1列だけでは一意に識別できない場合、複数列を組み合わせて主キーにできます。

| 注文番号 | 商品番号 | 数量 |
|---|---|---:|
| 1001 | A01 | 2 |
| 1001 | A02 | 1 |
| 1002 | A01 | 3 |

注文番号だけでは重複し、商品番号だけでも重複します。しかし、**注文番号＋商品番号**の組合せなら各行を識別できます。これが複合主キーです。

### 資料で確認する

SQLの主キー制約とUPDATEの動作は、[PostgreSQL公式：制約](https://www.postgresql.org/docs/current/ddl-constraints.html)と[PostgreSQL公式：UPDATE](https://www.postgresql.org/docs/current/sql-update.html)で確認できます。主キーは重複不可・NULL不可、UPDATEは条件に一致するすべての行が対象になる、という判断を裏付ける資料です。


関係モデルの原典は、E. F. Coddが1970年に発表した論文 **“A Relational Model of Data for Large Shared Data Banks”** です。

- [IBM Research：A Relational Model of Data for Large Shared Data Banks](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks)
- [DOI：10.1145/362384.362685](https://doi.org/10.1145/362384.362685)

基本情報技術者試験の出題範囲は、IPAのシラバスから確認できます。

- [IPA：試験要綱・シラバスについて](https://www.ipa.go.jp/shiken/syllabus/gaiyou.html)

試験では、**主キーは行を一意に識別する**という役割から各性質を判断できるようにします。

## 科目Aでどう出る？

主キーの説明を選ぶ問題では、**同じ主キー値を持つ行が複数存在しない**という表現が重要な手掛かりです。

~~~text
主キー
→ 行を一意に識別
→ 同じ主キー値が複数あるのはNG
~~~

一方、次の説明は主キーの性質ではありません。

| 選択肢の考え方 | 判断 |
|---|---|
| 主キーを条件にしないと検索できない | 誤り。主キー以外でも検索できる |
| 数値型を主キーにすると算術演算できない | 誤り。キーの役割とデータ型は別 |
| 同じ主キー値の行が複数存在しない | **正しい** |
| 複数列から主キーを構成できない | 誤り。複合主キーがある |

試験では、**検索方法やデータ型ではなく「行を一意に識別できるか」**に戻って判断します。


### UPDATEは「対象行 → 変更内容 → 制約」で読む

UPDATE文は、既存の行の値を変更するSQLです。まずWHEREで対象行を調べ、次にSETによる変更後の値を考え、最後に表の制約を満たすか確認します。これは**問題を読む順序**であり、DB内部の実行順序を指定するものではありません。

~~~sql
UPDATE 表名
SET 列名 = 変更後の値
WHERE 条件;
~~~

- **WHERE**：どの行を対象にするか。条件に一致するすべての行が対象。
- **SET**：どの列を何に変えるか。
- **制約確認**：変更後の表で主キーが重複せず、NULLにもならないか。

WHEREを省略すると、通常は表の全行が更新対象になります。また、WHEREがあっても対象が1行とは限りません。

例として、社員番号を主キーにした次の社員表を考えます。この例では外部キーなどの追加制約やトリガーはなく、通常のUPDATEで主キー制約を確認します。

~~~sql
CREATE TABLE 社員 (
    社員番号 INT PRIMARY KEY,
    氏名 VARCHAR(20),
    部署 VARCHAR(20)
);
~~~

| 社員番号（主キー） | 氏名 | 部署 |
|---|---|---|
| 1001 | 山田 | 設計 |
| 1002 | 鈴木 | 営業 |
| 1003 | 佐藤 | 設計 |
| 1004 | 高橋 | 品質 |

それぞれのケースは、同じ更新前の表から独立して考えます。

| 更新の内容 | 対象行 | 主キー制約の判断 |
|---|---|---|
| 1002の社員番号を1001に変更 | 1002の1行 | 既存の1001と重複するので不可 |
| 設計部署の社員番号をすべて1010に変更 | 1001と1003の2行 | 更新対象どうしで1010が重複するので不可 |
| 1002の社員番号をNULLに変更 | 1002の1行 | 主キーのNULL不可に違反 |
| 1002の部署を企画に変更 | 1002の1行 | 主キーを変えず、示した制約に違反しない |
| 1002の社員番号を1010に変更 | 1002の1行 | 未使用の番号で重複もNULLもないため可能 |

**変更先の1010が元の表になくても、複数の行を同じ1010にすれば重複します。** 更新しない行との比較だけでなく、更新対象どうしの重複も調べます。

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}">

<div class="fe-learning-demo fe-pk-demo" data-fe-pk-demo>
  <p class="fe-learning-demo__title">触って確認：更新対象・変更後の候補・保存結果を分ける</p>
  <p>ケースを選び、WHEREの対象行、SETの候補、制約確認の順に進めます。各ケースは同じ更新前の表から始まります。</p>
  <div class="fe-learning-demo__controls">
    <button type="button" class="fe-learning-demo__button" data-pk-case="0" disabled>既存行と重複</button>
    <button type="button" class="fe-learning-demo__button" data-pk-case="1" disabled>対象2行が重複</button>
    <button type="button" class="fe-learning-demo__button" data-pk-case="2" disabled>主キーをNULLに</button>
    <button type="button" class="fe-learning-demo__button" data-pk-case="3" disabled>部署を変更</button>
    <button type="button" class="fe-learning-demo__button" data-pk-case="4" disabled>未使用の主キーへ</button>
  </div>
  <pre><code data-pk-sql>ケースごとのSQLは、操作が有効になると表示されます。</code></pre>
  <div class="fe-pk-demo__tables">
    <section class="fe-pk-demo__panel"><h3>更新前の表</h3><div class="fe-pk-demo__scroll"><table><thead><tr><th>社員番号</th><th>氏名</th><th>部署</th><th>判定</th></tr></thead><tbody><tr data-pk-original><td>1001</td><td>山田</td><td>設計</td><td data-pk-marker>未選択</td></tr>
<tr data-pk-original><td>1002</td><td>鈴木</td><td>営業</td><td data-pk-marker>未選択</td></tr>
<tr data-pk-original><td>1003</td><td>佐藤</td><td>設計</td><td data-pk-marker>未選択</td></tr>
<tr data-pk-original><td>1004</td><td>高橋</td><td>品質</td><td data-pk-marker>未選択</td></tr></tbody></table></div></section>
    <section class="fe-pk-demo__panel"><h3>変更後の候補（未保存）</h3><div class="fe-pk-demo__scroll"><table><thead><tr><th>社員番号</th><th>氏名</th><th>部署</th><th>判定</th></tr></thead><tbody data-pk-preview><tr><td colspan="4">まだ候補を作っていません。</td></tr></tbody></table></div></section>
    <section class="fe-pk-demo__panel"><h3>保存結果</h3><div class="fe-pk-demo__scroll"><table><thead><tr><th>社員番号</th><th>氏名</th><th>部署</th><th>判定</th></tr></thead><tbody data-pk-result><tr><td>1001</td><td>山田</td><td>設計</td><td>未選択</td></tr>
<tr><td>1002</td><td>鈴木</td><td>営業</td><td>未選択</td></tr>
<tr><td>1003</td><td>佐藤</td><td>設計</td><td>未選択</td></tr>
<tr><td>1004</td><td>高橋</td><td>品質</td><td>未選択</td></tr></tbody></table></div></section>
  </div>
  <p class="fe-pk-demo__status" data-pk-status role="status" aria-live="polite">操作が使えない場合も、本文の表で各ケースの結果を確認できます。</p>
  <div class="fe-learning-demo__controls"><button type="button" class="fe-learning-demo__button" data-pk-next disabled>SETの候補を見る</button></div>
  <p class="fe-learning-demo__hint">見るポイント：「対象」の行と、破線で示す「制約違反」を確認します。制約に違反する候補は保存結果に反映されません。同じケースのボタンを押すと最初から確認できます。</p>
</div>

<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}" defer></script>

## どんな場面で使う？

社員、商品、注文などのデータでは、どの行を操作するのかを確実に識別する必要があります。

~~~text
社員番号 → 社員を識別
商品番号 → 商品を識別
注文番号 → 注文を識別
~~~

また、別の表から主キーを参照する列が**外部キー**です。

~~~text
部署表
部署番号 ← 主キー

社員表
部署番号 ← 外部キー
~~~

主キーは1行を識別し、外部キーは表どうしを関連付ける、と分けて考えます。

## よくある誤解・混同

### 主キーは検索専用の列

違います。主キーの本質は、**表の中の行を一意に識別すること**です。主キー以外の列でも検索できます。

### 主キーは必ず数値

違います。データ型が数値であること自体は主キーの条件ではありません。

### 主キーは必ず1列

違います。複数列の組合せで一意に識別する**複合主キー**もあります。

### 重複しなければNULLでもよい

主キーではNULLも認められません。

~~~text
主キー
→ 重複不可
＋
NULL不可
~~~

### 主キーの値は更新できない？

主キーだからという理由だけで、値の変更が禁止されるわけではありません。更新後も重複せずNULLでもなく、ほかの制約にも違反しなければ更新できます。

実際の表では、外部キーで参照されている場合などに別の制約も確認します。**主キーを変更するかどうかより、変更後も制約を満たせるか**で判断します。

### NULLは空文字や0と同じ？

NULLは値が不明・存在しないことを表すもので、空文字や数値の0とは区別します。主キーのNULL不可から、0も禁止されるとは判断できません。空文字の扱いにはDBMSによる違いがあります。

### 主キー以外の列なら、どんな更新でもできる？

主キー以外でも、NOT NULL、UNIQUE、CHECK、外部キーなどの制約があれば、その条件を満たす必要があります。例の部署変更が可能なのは、示した表定義にその変更を禁止する制約がないためです。

### 主キーと外部キーは同じ

役割が違います。

~~~text
主キー
→ 自分の表の行を一意に識別

外部キー
→ 表どうしを関連付ける
~~~

## まとめ（試験直前用）

- **主キー** → 表の中の1行を一意に識別する
- **同じ主キー値は重複できず、NULLにもできない**
- **複数列を組み合わせた複合主キーも作れる**
- UPDATEは**WHEREの対象行 → SETの変更内容 → 制約確認**で読む
- **既存行との重複だけでなく、更新対象どうしの重複も確認する**

迷ったら、

~~~text
この値（または値の組合せ）で
1行だけに決まる？
↓
主キーの中心的な役割
~~~

と考えます。

{% include fe_article_footer.html %}
