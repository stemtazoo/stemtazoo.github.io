---
layout: page
title: 論理回路から論理式を求める方法とは？AND・OR・NOTと式の簡単化【基本情報技術者試験】
description: 論理積・論理和に慣れていない人向けに、AND・OR・NOTを日常語へ置き換えながら、共通項をくくる方法、補元律、真理値表を使った論理式の簡単化を解説します。
permalink: /fe/logic-circuit-boolean-expression/
tags: [fe, fe-technology, basic-theory]
fe_section: テクノロジ系
fe_subsection: 基礎理論
fe_order: 40
date: 2026-07-22
last_modified_at: 2026-11-03
---

## まず結論

論理式は、最初から難しい数式として考えなくても大丈夫です。

まず、記号を次の日本語へ置き換えます。

```text
A • B
→ AかつB
→ AとBの両方が成り立つ

A + B
→ AまたはB
→ AとBのどちらかが成り立つ

A̅
→ Aではない
```

式を簡単化するときは、次の順番で考えます。

```text
1. 同じ部分を探す
2. 同じ部分を外へ出す
3. A + A̅ = 1 を使う
4. A • 1 = A を使う
```

覚える一文はこれです。

> **論理積 `•` は「両方とも」、論理和 `+` は「どちらか」。同じ部分があれば、まずくくる。**

## 直感的な説明

論理式の記号が出ると、急に数学の問題に見えるかもしれません。

しかし、式が表しているのは「条件の組合せ」です。

例えば、

```text
X • Y • Z
```

は、掛け算をしているのではありません。

```text
Xであり、
Yであり、
さらにZでもある
```

という意味です。

一方、

```text
X • Y • Z + X̅ • Y • Z
```

は、次の二つの条件を表します。

```text
Xであり、Yであり、Zである
または
Xではなく、Yであり、Zである
```

ここで両方に共通しているのは、

```text
Yであり、Zである
```

という部分です。

Xであっても、Xでなくてもよいため、結局必要なのは `Y • Z` だけです。

```text
Xの場合でも Y • Z
Xでない場合でも Y • Z
→ Xは結果に関係しない
→ Y • Z
```

これが、式変形の意味です。

## 定義・仕組み

### 論理積・論理和・否定

代表的な論理演算は、次のように表します。

| 名前 | 記号 | 日本語での意味 | 1になる条件 |
|---|---|---|---|
| 論理積（AND） | `A • B` | AかつB | AとBの両方が1 |
| 論理和（OR） | `A+B` | AまたはB | AとBのどちらかが1 |
| 否定（NOT） | `A̅` または `¬A` | Aではない | Aが0 |

特に、論理積の `•` は算数の掛け算ではなく、**「両方の条件を満たす」**という意味です。

### 共通部分をくくる

次の式を考えます。

```text
X • Y • Z + X̅ • Y • Z
```

両方の項に `Y • Z` が含まれています。

そこで、共通する `Y • Z` を外へ出します。

```text
X • Y • Z + X̅ • Y • Z
= Y • Z • (X + X̅)
```

これは、通常の計算で次のようにくくる考え方と同じです。

```text
a • b + c • b
= b • (a+c)
```

### 補元律を使う

`X` と `X̅` は、「Xである」と「Xではない」です。

どちらか一方は必ず成り立つため、

```text
X + X̅ = 1
```

となります。

したがって、

```text
Y • Z • (X + X̅)
= Y • Z • 1
= Y • Z
```

となります。

### よく使う法則

| 法則 | 式 | 日本語での意味 |
|---|---|---|
| 補元律 | `A+A̅=1` | AかAでないかのどちらかは必ず成り立つ |
| 補元律 | `A • A̅=0` | Aであり、同時にAでないことはない |
| 恒等律 | `A • 1=A` | 必ず成り立つ条件とのANDはA |
| 恒等律 | `A+0=A` | 成り立たない条件とのORはA |
| 分配法則 | `A • B+A • C=A • (B+C)` | 同じ部分をくくる |
| 吸収法則 | `A+A • B=A` | Aだけで既に条件を満たしている |
| べき等律 | `A+A=A` | AまたはAはA |
| べき等律 | `A • A=A` | AかつAはA |

公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

## 科目Aでどう出る？

科目Aでは、次のような形で出題されます。

- 論理式と等価な式を選ぶ
- 論理回路が表す式を選ぶ
- ベン図と一致する式を選ぶ
- 式を簡単化した結果を選ぶ

### まず日本語へ置き換える

式変形が難しく感じる場合は、いきなり法則を使わず、日本語へ置き換えます。

```text
X • Y • Z
→ XかつYかつZ

X̅ • Y • Z
→ Xではなく、YかつZ
```

二つを合わせると、

```text
XであってもYかつZ
XでなくてもYかつZ
```

です。

そのため、Xは結果に関係せず、

```text
Y • Z
```

が残ります。

### 式変形で解く

```text
X • Y • Z + X̅ • Y • Z
= Y • Z • (X + X̅)
= Y • Z • 1
= Y • Z
```

使った法則は、次の三つです。

```text
共通部分をくくる
→ 分配法則

X + X̅ = 1
→ 補元律

Y • Z • 1 = Y • Z
→ 恒等律
```

### 触って覚える：論理式の簡単化を8通りで確かめる

**Xの値を変えると、式全体の答えも変わるでしょうか？**

ここでは、元の式 `X • Y • Z + X̅ • Y • Z` と、簡単化した式 `Y • Z` を比べます。

1. X・Y・Zの値を0か1に設定します。
2. **両方の式で共通する出力**が0か1か予想します。
3. 「判定する」を押して、**2つのAND、OR、簡単化後のAND**の途中結果を確認します。
4. 「次の組合せ」で8通りを調べ、**Xを変えてもY・Zが同じなら出力も同じ**ことを確かめます。

**この教材の前提：** `•` はAND（かつ）、`+` はOR（または）、`X̅` はNOT X（Xではない）です。足し算や掛け算の数値計算ではありません。

<link rel="stylesheet" href="{{ '/assets/css/fe-logic-circuit-demo.css' | relative_url }}">

<div class="fe-logic-demo" id="fe-logic-demo" aria-label="元の論理式と簡単化後の論理式の出力比較">
  <p class="fe-logic-demo__step">① X・Y・Zの値を選ぶ</p>
  <div class="fe-logic-demo__controls">
    <label for="fe-logic-x">X
      <select id="fe-logic-x"><option value="0">0</option><option value="1">1</option></select>
    </label>
    <label for="fe-logic-y">Y
      <select id="fe-logic-y"><option value="0">0</option><option value="1">1</option></select>
    </label>
    <label for="fe-logic-z">Z
      <select id="fe-logic-z"><option value="0">0</option><option value="1">1</option></select>
    </label>
  </div>
  <p class="fe-logic-demo__step">② 出力を予想する</p>
  <div class="fe-logic-demo__controls">
    <label for="fe-logic-guess">2つの式の出力は？
      <select id="fe-logic-guess">
        <option value="">予想しなくても進められます</option>
        <option value="0">0</option><option value="1">1</option>
      </select>
    </label>
  </div>
  <p class="fe-logic-demo__step">③ 判定して、途中の計算を確認する</p>
  <div class="fe-logic-demo__expressions">
    <div class="fe-logic-demo__card">
      <strong>元の論理式</strong>
      <p class="fe-logic-demo__formula">X • Y • Z + X̅ • Y • Z</p>
      <p>AND → AND → OR</p>
      <p class="fe-logic-demo__value" id="fe-logic-original">？</p>
    </div>
    <div class="fe-logic-demo__card">
      <strong>簡単化した論理式</strong>
      <p class="fe-logic-demo__formula">Y • Z</p>
      <p>AND</p>
      <p class="fe-logic-demo__value" id="fe-logic-simplified">？</p>
    </div>
  </div>
  <div class="fe-logic-demo__actions">
    <button type="button" class="fe-logic-demo__primary" id="fe-logic-check">判定する</button>
    <button type="button" id="fe-logic-next">次の組合せ</button>
    <button type="button" id="fe-logic-reset">最初から</button>
  </div>
  <div class="fe-logic-demo__result">
    <p id="fe-logic-feedback" class="fe-logic-demo__feedback" role="status" aria-live="polite">X・Y・Zを選び、出力を予想してから判定してください。</p>
    <p id="fe-logic-details">まず結果を予想してください。判定するまで出力を隠しています。</p>
    <p id="fe-logic-count">0 / 8 通りを確認済み</p>
  </div>
  <p class="fe-logic-demo__step">④ 8通りの真理値を比較する</p>
  <p class="fe-logic-demo__legend">確認した組合せだけ結果を表示します。青い行は現在判定中の入力です。</p>
  <div class="fe-logic-demo__tablebox">
    <table>
      <thead><tr><th scope="col">X</th><th scope="col">Y</th><th scope="col">Z</th><th scope="col">元の式</th><th scope="col">Y • Z</th></tr></thead>
      <tbody>
        <tr data-logic-combination="000"><td>0</td><td>0</td><td>0</td><td data-logic-original>—</td><td data-logic-simple>—</td></tr>
        <tr data-logic-combination="001"><td>0</td><td>0</td><td>1</td><td data-logic-original>—</td><td data-logic-simple>—</td></tr>
        <tr data-logic-combination="010"><td>0</td><td>1</td><td>0</td><td data-logic-original>—</td><td data-logic-simple>—</td></tr>
        <tr data-logic-combination="011"><td>0</td><td>1</td><td>1</td><td data-logic-original>—</td><td data-logic-simple>—</td></tr>
        <tr data-logic-combination="100"><td>1</td><td>0</td><td>0</td><td data-logic-original>—</td><td data-logic-simple>—</td></tr>
        <tr data-logic-combination="101"><td>1</td><td>0</td><td>1</td><td data-logic-original>—</td><td data-logic-simple>—</td></tr>
        <tr data-logic-combination="110"><td>1</td><td>1</td><td>0</td><td data-logic-original>—</td><td data-logic-simple>—</td></tr>
        <tr data-logic-combination="111"><td>1</td><td>1</td><td>1</td><td data-logic-original>—</td><td data-logic-simple>—</td></tr>
      </tbody>
    </table>
  </div>
</div>
<noscript>
  <p>JavaScriptが無効な場合は、直後の真理値表で8通りを確認できます。元の式 `X • Y • Z + X̅ • Y • Z` と簡単化した式 `Y • Z` はすべて一致します。</p>
</noscript>
<script src="{{ '/assets/js/fe-logic-circuit-demo.js' | relative_url }}" defer></script>

### 真理値表で確認する

式変形に自信がない場合は、真理値表で確認できます。

| X | Y | Z | `X • Y • Z` | `X̅ • Y • Z` | 全体 | `Y • Z` |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 | 1 |

「全体」と `Y • Z` の結果がすべて同じなので、二つの式は等価です。

## 科目Bでどう使う？

科目Bでは、論理式の考え方が条件分岐を読むときに役立ちます。

例えば、

```text
利用者が有効
かつ
パスワードが正しい
```

という条件は、

```text
有効 • パスワード正しい
```

と考えられます。

疑似言語では、次のような条件です。

```text
if 有効 = true and パスワード正しい = true
```

読み方は同じです。

```text
AND
→ 全条件を満たす必要がある

OR
→ どれか一つを満たせばよい

NOT
→ 条件を反対にする
```

複雑な条件式も、まず一つずつ日本語へ戻して考えると読みやすくなります。

## よくある誤解・混同

### `•` を普通の掛け算だと思う

論理積の `•` は、数値を掛けるというより、条件を「かつ」でつないでいます。

```text
A • B
→ AかつB
→ AとBの両方が必要
```

### `+` を数値の足し算だと思う

論理和の `+` は、「または」を表します。

```text
A+B
→ AまたはB
```

AとBが両方とも1でも、結果は2ではなく1です。

### `X + X̅ = 0` だと思う

逆です。

```text
X + X̅ = 1
```

Xであるか、Xでないかのどちらかは必ず成り立ちます。

一方、

```text
X • X̅ = 0
```

です。

Xであり、同時にXでないことはありません。

### ベン図を描かなければ解けない

ベン図は確認には便利ですが、毎回描く必要はありません。

次の形を見つけたら、式変形の方が早く解けます。

```text
A • B + A̅ • B
= B • (A+A̅)
= B
```

### 共通項を一部分だけ見落とす

```text
X • Y • Z + X̅ • Y • Z
```

では、共通するのは `Y` だけではなく `Y • Z` です。

共通部分をできるだけまとめてくくると、式が簡単になります。

## まとめ（試験直前用）

- 論理積 `•` は「かつ」「両方とも」
- 論理和 `+` は「または」「どちらか」
- 否定は「〜ではない」
- 同じ部分があれば、分配法則でくくる
- `A+A̅=1`、`A • A̅=0`
- `A • B+A̅ • B=B` の形を覚える
- 式が難しく見えたら、まず日本語へ置き換える

> **数式として見る前に、「かつ・または・ではない」と読んでみる。**

{% include fe_article_footer.html %}
