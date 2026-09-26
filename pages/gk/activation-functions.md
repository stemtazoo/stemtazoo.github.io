---
layout: page
title: 活性化関数とは？ReLU・Sigmoid・tanh・Softmaxを切り分け【G検定】
description: "活性化関数の役割をニューラルネットワークへ非線形性を与えることとして整理し、ReLU・Sigmoid・tanh・Softmaxを使う場所、出力範囲、勾配消失やDead ReLUとの関係で比較します。G検定で選択肢を切る判断基準を確認できます。"
permalink: /gk/activation-functions/
tags: [gk, neural_network, activation]
gk_section: ディープラーニングの概要/活性化関数
gk_order: 1
last_modified_at: 2026-09-26
---

## まず結論

活性化関数の中心的な役割は、ニューラルネットワークに**非線形性**を与えることです。

| 関数 | 主な使いどころ | 判断キーワード |
|---|---|---|
| ReLU | 中間層 | 負は0、正はそのまま |
| Sigmoid | 二値分類の出力層 | 0〜1 |
| tanh | 中間層など | -1〜1 |
| Softmax | 多クラス分類の出力層 | 出力の合計が1 |

G検定では、まず**「なぜ必要か」→ 非線形性**、次に**「どこで使うか」**で切ると整理しやすいです。

## 直感的な説明

活性化関数がない多層ネットワークでは、線形変換を何層重ねても全体としては線形変換のままです。

つまり、層を増やしただけでは複雑な境界を表現できません。

活性化関数を入れることで出力に「曲がり」を作り、XORのような**線形分離できない関係**も表現できるようになります。

<link rel="stylesheet" href="{{ '/assets/css/gk-visualizer.css' | relative_url }}">

<div class="gk-learning-demo" data-gk-activation-demo>
  <p class="gk-learning-demo__title">触って比較：入力を動かすと出力はどう変わる？</p>
  <p class="gk-learning-demo__lead">関数を切り替えて、同じ入力に対する出力の違いを確認できます。</p>

  <div class="gk-learning-demo__controls" aria-label="活性化関数を選択">
    <button type="button" class="gk-learning-demo__button" data-function="relu" aria-pressed="true">ReLU</button>
    <button type="button" class="gk-learning-demo__button" data-function="sigmoid" aria-pressed="false">Sigmoid</button>
    <button type="button" class="gk-learning-demo__button" data-function="tanh" aria-pressed="false">tanh</button>
  </div>

  <svg class="gk-activation-demo__chart" viewBox="0 0 600 260" role="img" aria-label="選択した活性化関数のグラフ">
    <line class="gk-activation-demo__axis" x1="30" y1="227.6" x2="570" y2="227.6"></line>
    <line class="gk-activation-demo__axis" x1="300" y1="30" x2="300" y2="230"></line>
    <path class="gk-activation-demo__curve" data-activation-curve></path>
    <circle class="gk-activation-demo__point" data-activation-point r="6"></circle>
  </svg>

  <label for="gk-activation-x">入力 x：<strong data-activation-input>0.0</strong></label>
  <input id="gk-activation-x" class="gk-activation-demo__slider" data-activation-x type="range" min="-6" max="6" step="0.1" value="0">

  <p class="gk-activation-demo__readout">出力：<strong data-activation-output>0</strong><br><span data-activation-note>ReLU：負の入力は0、正の入力はそのまま。中間層で使われやすい。</span></p>
  <p class="gk-learning-demo__hint">見るポイント：関数の「形」より、出力範囲と使う場所を結び付けます。</p>
</div>

<div class="gk-learning-demo" data-gk-softmax-demo>
  <p class="gk-learning-demo__title">Softmaxは「複数のスコアをまとめて確率にする」</p>
  <p class="gk-learning-demo__lead">3クラスのスコアを動かしても、変換後の確率の合計は1になります。</p>

  <label>クラスAのスコア：<strong data-softmax-score-label>2.0</strong><input class="gk-activation-demo__slider" data-softmax-score type="range" min="-2" max="4" step="0.1" value="2"></label>
  <label>クラスBのスコア：<strong data-softmax-score-label>1.0</strong><input class="gk-activation-demo__slider" data-softmax-score type="range" min="-2" max="4" step="0.1" value="1"></label>
  <label>クラスCのスコア：<strong data-softmax-score-label>0.0</strong><input class="gk-activation-demo__slider" data-softmax-score type="range" min="-2" max="4" step="0.1" value="0"></label>

  <div class="gk-activation-demo__softmax">
    <div class="gk-activation-demo__bar-row"><span>A</span><div class="gk-activation-demo__bar-track"><div class="gk-activation-demo__bar" data-softmax-bar></div></div><strong data-softmax-prob></strong></div>
    <div class="gk-activation-demo__bar-row"><span>B</span><div class="gk-activation-demo__bar-track"><div class="gk-activation-demo__bar" data-softmax-bar></div></div><strong data-softmax-prob></strong></div>
    <div class="gk-activation-demo__bar-row"><span>C</span><div class="gk-activation-demo__bar-track"><div class="gk-activation-demo__bar" data-softmax-bar></div></div><strong data-softmax-prob></strong></div>
  </div>

  <p class="gk-activation-demo__readout">確率の合計 = <strong data-softmax-total>1.00</strong></p>
  <p class="gk-learning-demo__hint">Softmaxは1個の値を変換する曲線としてではなく、複数クラスをまとめて見るのがポイントです。</p>
</div>

<script src="{{ '/assets/js/gk-visualizer.js' | relative_url }}" defer></script>

## 定義・仕組み

ニューロンでは、入力の重み付き和とバイアスを計算した後、活性化関数を適用します。

> 出力 = 活性化関数（重み付き和 + バイアス）

### ReLU

- 入力が0以下 → 0
- 入力が正 → そのまま
- 計算が軽く、中間層で広く使われる
- 正の領域では勾配を保ちやすい
- 負の領域で勾配が0になり続けるとDead ReLUが起こりうる

ReLU系の違いは、[ReLU / Leaky ReLU / PReLU比較](/gk/relu-family-cheatsheet/)で確認できます。

### Sigmoid

- 出力範囲は0〜1
- 二値分類の出力を確率として扱いたい場面で使われる
- 飽和領域では微分が小さくなり、深い中間層では勾配消失の原因になりやすい

### tanh

- 出力範囲は-1〜1
- 0を中心とした出力を持つ
- Sigmoidと同様、飽和領域では勾配消失が起こりうる

### Softmax

- 複数クラスのスコアを確率分布として扱える形へ変換する
- 出力の合計が1になる
- 多クラス分類の出力層で使われることが多い

## いつ使う？（得意・不得意）

| 問題文の表現 | 疑う関数 |
|---|---|
| 中間層・負の入力は0 | ReLU |
| 二値分類・0〜1 | Sigmoid |
| -1〜1・0中心 | tanh |
| 多クラス・合計1 | Softmax |

活性化関数は「名前だけ」で選ぶのではなく、**中間層か出力層か、出力をどう解釈したいか**で判断します。

## G検定ひっかけポイント

- ❌「活性化関数の目的は出力範囲を制限することだけ」→ **中心は非線形性の導入**
- ❌「活性化関数がなくても、層を増やせば非線形になる」→ **線形変換だけなら全体も線形**
- ❌「Sigmoidは勾配消失を起こさない」→ **飽和領域で起こりやすい**
- ❌「ReLUなら勾配消失を完全に防げる」→ **起こりにくくするが万能ではない**
- ❌「Softmaxは中間層の標準的な活性化関数」→ **多クラス分類の出力層で使われることが多い**
- ⭕「XORのような非線形問題を扱う」→ **多層化＋非線形活性化が重要**

## まとめ（試験直前用）

- 活性化関数の役割 → **非線形性を入れる**
- ReLU → **中間層**
- Sigmoid → **二値分類の出力**
- Softmax → **多クラス分類の出力**
- Sigmoid / tanh → **飽和による勾配消失に注意**

**「なぜ必要？」と聞かれたら、まず非線形性を思い出します。**

## 参考資料（原論文）

- [Understanding the difficulty of training deep feedforward neural networks｜PMLR](https://proceedings.mlr.press/v9/glorot10a.html)
  - Glorot・Bengio（2010）。Sigmoidの飽和と深いネットワークの学習難易度を分析しており、活性化関数と勾配の関係を理解する一次資料として有用です。
- [Rectified Linear Units Improve Restricted Boltzmann Machines｜ICML](https://icml.cc/2010/papers/432.pdf)
  - Nair・Hinton（2010）。Rectified Linear Unit（ReLU）を扱った初期の代表的な原論文です。

{% include gk_article_footer.html %}
