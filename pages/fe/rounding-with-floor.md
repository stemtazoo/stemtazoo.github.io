---
layout: page
title: 四捨五入を切り捨てで実現するには？0.5を足す理由と境界値【基本情報技術者試験】
description: 正の値の四捨五入を「0.5を足して床関数で切り捨てる」式に置き換える理由と、境界値を使ったFE科目Aの判断方法、Pythonのroundとの違いを解説します。
permalink: /fe/rounding-with-floor/
tags: [fe, fe-technology, basic-theory, algorithm]
fe_section: テクノロジ系
fe_subsection: 基礎理論
fe_order: 241
date: 2026-10-25
last_modified_at: 2026-10-25
---

## まず結論

**0以上の数を、小数第1位で四捨五入して整数にする**には、数に`0.5`を足してから、**その値以下の最大の整数**を取り出す方法があります。

~~~text
四捨五入する値 = x
結果 = floor(x + 0.5)   （x ≧ 0）
~~~

`floor`（床関数）は、引数以下の最大の整数を返す関数です。

> **0.5を足す → 整数に切り捨てる。境界は「小数部分が0.5かどうか」。**

このページは**四捨五入を別の計算手順で実現する方法**を扱います。床関数そのものの定義や負数の扱いは[床関数とは？](/fe/floor-function/)で確認できます。

## 直感的な説明

「2.5以上なら3、2.5未満なら2」とする四捨五入を考えます。

~~~text
2.49 + 0.5 = 2.99 → 整数部分は2
2.50 + 0.5 = 3.00 → 整数部分は3
2.51 + 0.5 = 3.01 → 整数部分は3
~~~

**0.5を足すことで、もともとの「小数部分が0.5」という境界が、整数の境界へ移る**わけです。

### 数値を変えて確認する

<link rel="stylesheet" href="{{ '/assets/css/fe-rounding-floor-visualizer.css' | relative_url }}">

<div class="fe-round-floor" data-fe-round-floor-demo>
  <p class="fe-round-floor__title">四捨五入が切り替わるところ</p>
  <label for="fe-round-floor-input">数値 x：<strong data-round-x>2.49</strong></label>
  <input id="fe-round-floor-input" type="range" min="2.40" max="2.60" step="0.01" value="2.49" data-round-slider>
  <div class="fe-round-floor__presets" aria-label="境界値の例">
    <button type="button" data-round-preset="2.49">2.49</button>
    <button type="button" data-round-preset="2.50">2.50</button>
    <button type="button" data-round-preset="2.51">2.51</button>
  </div>
  <div class="fe-round-floor__steps">
    <div><span>① 0.5を足す</span><strong data-round-plus>2.99</strong></div>
    <div><span>② 床関数で切り捨てる</span><strong data-round-result>2</strong></div>
  </div>
  <p class="fe-round-floor__hint" data-round-message aria-live="polite">2.49は2.50未満なので、結果は2です。</p>
  <p class="fe-round-floor__hint">見るポイント：2.49から2.50へ変える瞬間に、結果が2から3へ変わります。</p>
</div>

<script src="{{ '/assets/js/fe-rounding-floor-visualizer.js' | relative_url }}" defer></script>

## 定義・仕組み

### 床関数を使う理由

`floor(a)`は、`a`以下で最大の整数を返します。0以上の値なら、小数部分を切り捨てる操作と同じです。

例えば、`floor(2.99) = 2`、`floor(3.00) = 3`です。

そこで、四捨五入したい値`x`に先に0.5を加えます。

| x | x + 0.5 | floor(x + 0.5) |
|---:|---:|---:|
| 1.4 | 1.9 | 1 |
| 1.5 | 2.0 | 2 |
| 2.4 | 2.9 | 2 |
| 2.5 | 3.0 | 3 |
| 2.6 | 3.1 | 3 |

### 平均値を整数に丸める場合

`N`個の観測値の合計を`S`とすると、平均値は`S / N`です（`N`は1以上、`S`は0以上とします）。

平均値を四捨五入して整数にするときは、

~~~text
floor(S / N + 0.5)
~~~

と書けます。まず平均値を計算し、0.5を加え、最後に床関数で整数へ変えます。

**0.5を掛けたり、平均値から0.5を引いたりするのではありません。**

## 科目Aでどう出る？

FE科目Aでは、四捨五入の結果が得られる式を選ぶときに、**境界値を代入して確認する**と判断が速くなります。

たとえば、`floor(x + 0.4)`と`floor(x + 0.5)`を比べます。

| x | floor(x + 0.4) | floor(x + 0.5) |
|---:|---:|---:|
| 2.49 | 2 | 2 |
| **2.50** | **2（誤り）** | **3（正しい）** |
| 2.60 | 3 | 3 |

2.6だけでは両方とも3になって区別できません。**2.5を入れると、0.4では足りない**と分かります。

選択肢に`-0.5`や`-0.4`がある場合も、2.5を代入すれば正しい結果3にならないので除外できます。

### 確認問題

0以上の実数`x`を四捨五入して整数にする処理として、適切な式はどれでしょうか。`floor`は引数以下の最大の整数を返すものとします。

- ア. `floor(x - 0.5)`
- イ. `floor(x - 0.4)`
- ウ. `floor(x + 0.4)`
- エ. `floor(x + 0.5)`

<details markdown="1">
<summary>▶ 答えと解説を見る</summary>

**正解：エ**

`x = 2.5`で確認します。四捨五入の正しい結果は3です。

- ア：`floor(2.0) = 2`
- イ：`floor(2.1) = 2`
- ウ：`floor(2.9) = 2`
- エ：`floor(3.0) = 3`

ただし、**1つの値で当てはまることだけでは、すべての値で正しい証明にはなりません**。境界値は選択肢を素早く切る手掛かりであり、仕組みは「0.5の境界を整数の境界へ移す」ことで説明できます。

</details>

## どんな場面で使う？

点数や測定値の平均を整数表示したい場合など、丸め方が「0.5以上で切上げ」と決まっているときに使えます。

Pythonなら、床関数は`math.floor()`で確認できます。

~~~python
import math

for x in [2.49, 2.50, 2.51]:
    print(x, math.floor(x + 0.5))

# 2.49 2
# 2.5 3
# 2.51 3
~~~

一方、Python標準の`round()`は、ちょうど中間にある値を偶数側へ丸める方式を使います。結果が常に一致するとは限りません。

~~~python
print(round(2.5))             # 2
print(math.floor(2.5 + 0.5))  # 3
~~~

実務で金額などの端数処理をする際は、**指定された丸めルール**や小数の計算精度も確認します。単純に`round()`へ置き換えないことが大切です。

## よくある誤解・混同

### 誤解1：0.4を足しても四捨五入になる

`x = 2.5`なら、`2.5 + 0.4 = 2.9`なので床関数の結果は2です。

境界値の0.5で切り上がるようにするには、**0.5を足す必要があります**。

### 誤解2：負の数にも同じ式がそのまま使える

`floor(x + 0.5)`が、一般的な「0.5以上なら絶対値の大きい方向へ丸める」方法と一致するのは、今回のような**0以上の値**の場合です。

例えば`x = -2.5`なら、

~~~text
floor(-2.5 + 0.5) = floor(-2.0) = -2
~~~

です。一方、負数の端数がちょうど0.5なら0から遠い方向へ丸める規則では`-3`になります。

**正数の式を無条件に負数へ適用しない**ようにしましょう。床関数と小数点以下の切捨ての違いは[床関数の記事](/fe/floor-function/)でも説明しています。

### 誤解3：Pythonのround()は必ず0.5を切り上げる

Pythonの`round(2.5)`は2です。`round(3.5)`は4になります。

試験の「四捨五入」とプログラミング言語の丸め規則を混同しないようにします。

## まとめ（試験直前用）

- **0以上の値の四捨五入**は`floor(x + 0.5)`で実現できる
- `floor`は引数以下の最大の整数を返す
- **2.49と2.50**を代入すると、境界が分かる
- 負の数では丸め方の定義を確認する
- Pythonの`round()`と「0.5を足して切り捨てる処理」は常に同じではない

{% include fe_article_footer.html %}
