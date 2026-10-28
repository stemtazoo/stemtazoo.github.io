---
layout: page
title: 整数型の除算は四捨五入？小数部分の切り捨てと科目Bの注意点【基本情報技術者試験】
description: FE科目Bの擬似言語で整数型の除算結果をどう読むかを、配列の添字と段階的な計算、触って確認できる例で整理します。
permalink: /fe/integer-division/
tags: [fe, fe-technology, algorithm]
fe_section: 科目B対策
fe_subsection: アルゴリズム
fe_order: 242
date: 2026-10-28
last_modified_at: 2026-10-28
---

## まず結論

**整数型の変数に除算結果を格納するときは、問題で指定された端数の扱いを確認します。** 小数が出たからといって、自動的に四捨五入するわけではありません。

今回の例は「正の値の小数部分を切り捨てる」ルールで考えます。

~~~text
9 ÷ 2 = 4.5 → idx1 = 4
4 ÷ 2 = 2   → idx2 = 2
~~~

> **試験中の判断：変数の型 → 端数処理の仕様 → 配列の添字の開始番号、の順に確認。**

## 直感的な説明

整数型は整数を保存する箱です。除算で小数が出たとき、その小数をどう整数にするかは仕様次第です。

| 元の計算 | 小数部分を切り捨て | 四捨五入 |
|---|---:|---:|
| 9 ÷ 2 = 4.5 | 4 | 5 |
| 7 ÷ 2 = 3.5 | 3 | 4 |
| 8 ÷ 2 = 4 | 4 | 4 |

結果が割り切れる例だけでは違いに気付けません。

### 数値を変えて確認する

<div id="fe-intdiv-demo" class="fe-intdiv-demo">
  <label for="fe-intdiv-count">配列の要素数：<strong id="fe-intdiv-count-value">9</strong></label>
  <input id="fe-intdiv-count" type="range" min="3" max="19" value="9" step="1" style="display:block;width:100%;margin:1rem 0">
  <div id="fe-intdiv-output" aria-live="polite"></div>
  <button type="button" id="fe-intdiv-reset">9要素に戻す</button>
</div>
<style>
.fe-intdiv-demo{border:1px solid #cbd5e1;border-radius:12px;padding:1.2rem;margin:1rem 0;background:#f8fafc;color:#243447}
.fe-intdiv-demo .fe-intdiv-step{background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:.8rem;margin:.6rem 0}
.fe-intdiv-demo strong{font-weight:700}
.fe-intdiv-demo button{padding:.5rem .8rem;border:1px solid #94a3b8;border-radius:7px;background:#fff;color:#243447;cursor:pointer}
</style>
<script>
(function () {
  function init() {
    const root = document.getElementById('fe-intdiv-demo');
    if (!root || root.dataset.ready) return;
    root.dataset.ready = '1';
    const input = document.getElementById('fe-intdiv-count');
    const countLabel = document.getElementById('fe-intdiv-count-value');
    const output = document.getElementById('fe-intdiv-output');
    function render() {
      const n = Number(input.value);
      const idx1 = Math.trunc(n / 2);
      const idx2 = Math.trunc(idx1 / 2);
      countLabel.textContent = String(n);
      output.innerHTML = '<div class="fe-intdiv-step">idx1 ← ' + n + ' ÷ 2 = ' + (n / 2) + ' → <strong>' + idx1 + '</strong></div>' +
        '<div class="fe-intdiv-step">idx2 ← ' + idx1 + ' ÷ 2 = ' + (idx1 / 2) + ' → <strong>' + idx2 + '</strong></div>' +
        '<p>ここでは各段階で小数部分を切り捨てます。最後にまとめて丸める計算とは異なります。</p>';
    }
    input.addEventListener('input', render);
    document.getElementById('fe-intdiv-reset').addEventListener('click', function () { input.value = '9'; render(); });
    render();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
</script>

## 定義・仕組み

### 整数型と除算

整数型の変数は、通常、小数部分を含む値をそのまま保存できません。ただし、**除算の結果がどう計算され、整数型への代入でどう変換されるかは言語・擬似言語の仕様によります**。

ここでは正の数の切り捨てを扱います。負の数では「0方向への切り捨て」と「床関数」は異なる場合があります。詳しくは[床関数とは？](/fe/floor-function/)を参照してください。

### 途中結果を順番に計算する

次のような処理を考えます。

~~~text
整数型：idx1 ← dataの要素数 ÷ 2
整数型：idx2 ← idx1 ÷ 2
return data[idx1] × data[idx2]
~~~

配列の添字は **1から始まる** とします。

| 添字 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 値 | 1 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |

要素数9なので、idx1 = 4、idx2 = 2です。よって data[4] × data[2] = 7 × 3 = **21** となります。

**注意：** この表の添字は1始まりです。Pythonのリストの0始まりと混同しないようにします。[配列の記事](/fe/array/)でも確認できます。

## 科目Bでどう使う？

擬似言語を追うときは、変数が更新されるたびに確定した値を書き出します。

~~~text
要素数 = 9
idx1 = 4  （4.5の小数部分を切り捨て）
idx2 = 2
data[4] = 7
data[2] = 3
戻り値 = 21
~~~

一度 idx1 に4が格納された後、idx2の計算で4.5を使い直すことはありません。

### 確認問題

要素数が11で、同じ切り捨てルールを使うとき、idx1とidx2はいくつですか。

<details markdown="1">
<summary>▶ 答えと解説を見る</summary>

idx1 = 11 ÷ 2 = 5.5 → **5**、idx2 = 5 ÷ 2 = 2.5 → **2** です。

</details>

## どんな場面で使う？

配列の中間付近の要素を選ぶ処理や、要素数を段階的に半分にするアルゴリズムで使います。

Pythonでは、正の整数に対して次の違いを確認できます。

~~~python
n = 9
print(n / 2)   # 4.5（通常の除算）
print(n // 2)  # 4（床除算）
print(int(n / 2))  # 4（整数へ変換）
~~~

※ Pythonの `//` は床除算なので、負の数では `int(a / b)` と結果が異なる場合があります。FEの擬似言語とPythonの仕様を同一視しないことが大切です。

## よくある誤解・混同

### 誤解1：指定がなければ四捨五入する

**四捨五入を勝手に仮定しない**ことが重要です。問題文・試験の擬似言語仕様を確認します。

### 誤解2：整数型なら、どの言語でも同じ結果になる

整数型への変換や整数同士の除算は、言語によって異なります。今回の正の数の例で切り捨てになることを、すべての言語へ一般化しません。

### 誤解3：途中の小数を最後にまとめて処理する

idx1に格納された値を使ってidx2を計算します。**各行の処理が終わった時点の値**を追いましょう。

### 誤解4：添字は必ず0から始まる

問題に「1から始まる」とあれば、data[1]が最初の要素です。

## まとめ（試験直前用）

- **整数型の除算**：端数処理の仕様を確認する
- **代入を追跡**：途中の整数値を確定させてから次の行へ進む
- **配列の添字**：0始まりか1始まりかを必ず確認する

四捨五入を実現する別の方法は[四捨五入を切り捨てで実現するには？](/fe/rounding-with-floor/)で確認できます。

{% include fe_article_footer.html %}
