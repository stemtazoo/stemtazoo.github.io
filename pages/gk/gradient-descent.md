---
layout: page
title: 勾配降下法（Gradient Descent）とは？学習率と更新方向【G検定】
description: "勾配降下法を、損失関数の勾配とは逆方向へパラメータを更新する最適化の基本として整理します。誤差逆伝播法が勾配を計算し、勾配降下法がその勾配を更新に使う役割分担、学習率が大きすぎる場合と小さすぎる場合の違いを確認します。"
permalink: /gk/gradient-descent/
tags: [gk, neural_network, optimization]
gk_section: ディープラーニングの概要/最適化手法
gk_order: 1
last_modified_at: 2026-09-20
---

## まず結論

**勾配降下法（Gradient Descent）は、損失が小さくなるように、勾配とは逆方向へパラメータを少しずつ更新する最適化の基本的な考え方**です。

G検定では、

```text
Backprop → 勾配を計算
勾配降下法 → 勾配を使って更新
```

と役割を分けると迷いにくくなります。

## 直感的な説明

山の高さを損失だと考えます。

現在地で傾きを調べ、**高くなる方向とは逆へ少し移動する**ことを繰り返して、より低い場所を目指すイメージです。

この「一度にどれだけ進むか」を決めるのが**学習率**です。

## 定義・仕組み

ニューラルネットワークでは、損失関数に対する各パラメータの勾配を求めます。

その勾配を使って、損失が減る方向へ重みやバイアスを更新します。

### 学習率

- 大きすぎる → 最小値を飛び越え、振動・発散することがある
- 小さすぎる → 更新が小さく、収束が遅くなる

### 操作して確認：学習率で進み方はどう変わる？

**見るポイント：同じ場所から始めても、学習率によって最小点への近づき方が変わります。** 学習率を選び、「1回更新」を数回押してください。学習率を切り替えると、同じ開始位置に戻ります。

この教材では、パラメータを1個の値 **w**、損失を **L = w² / 2** とした単純な例を使います。勾配はwなので、更新は **次のw = 現在のw − 学習率 × 現在のw** です。開始位置はw = 3、最小点はw = 0です。

<link rel="stylesheet" href="{{ '/assets/css/gk-visualizer.css' | relative_url }}">

<div class="gk-learning-demo gk-gradient-demo" data-gk-gradient-demo>
  <p class="gk-learning-demo__title">学習率を変えて、1回ずつ更新</p>
  <div class="gk-learning-demo__controls" role="group" aria-label="学習率を選ぶ">
    <button type="button" class="gk-learning-demo__button" data-gd-rate="0.1" aria-pressed="false" disabled>0.1：小さい</button>
    <button type="button" class="gk-learning-demo__button" data-gd-rate="0.5" aria-pressed="true" disabled>0.5：中くらい</button>
    <button type="button" class="gk-learning-demo__button" data-gd-rate="2.2" aria-pressed="false" disabled>2.2：大きい</button>
  </div>
  <svg class="gk-gradient-demo__chart" viewBox="0 0 600 300" role="img" aria-label="横軸はパラメータw、縦軸は損失L。曲線の最小点はwが0の位置。点と破線で更新の経路を表示">
    <defs><clipPath id="gk-gradient-clip"><rect x="50" y="35" width="500" height="225"></rect></clipPath></defs>
    <path class="gk-gradient-demo__axis" d="M50 255 H550 M300 35 V255"></path>
    <path class="gk-gradient-demo__curve" d="M50 45 Q300 465 550 45"></path>
    <g clip-path="url(#gk-gradient-clip)">
      <polyline class="gk-gradient-demo__trail" data-gd-trail points="425,202.5"></polyline>
      <circle class="gk-gradient-demo__point" data-gd-point cx="425" cy="202.5" r="7"></circle>
    </g>
    <g class="gk-gradient-demo__labels"><text x="50" y="280">−6</text><text x="290" y="280">0</text><text x="540" y="280">6</text><text x="310" y="30">損失 L</text><text x="535" y="298">w</text><text x="310" y="55">18</text></g>
  </svg>
  <p class="gk-learning-demo__hint">実線：損失の曲線 ／ ●：現在地 ／ 破線：更新の経路。図の目盛りは固定です。</p>
  <div class="gk-learning-demo__controls">
    <button type="button" class="gk-learning-demo__button" data-gd-step disabled>1回更新</button>
    <button type="button" class="gk-learning-demo__button" data-gd-reset disabled>最初に戻す</button>
  </div>
  <p class="gk-activation-demo__readout" data-gd-values>更新0回 ／ w = 3.000 ／ 損失 L = 4.500</p>
  <p class="gk-activation-demo__readout" data-gd-status role="status" aria-live="polite" aria-atomic="true">学習率0.5、w = 3から開始します。</p>
  <noscript><p>操作にはJavaScriptが必要です。下の表でも学習率による違いを確認できます。</p></noscript>
</div>

<script src="{{ '/assets/js/gk-visualizer.js' | relative_url }}" defer></script>

| 学習率 | 開始時 → 1回目 → 2回目のw | この例での動き |
|---|---|---|
| 0.1 | 3 → 2.7 → 2.43 | 最小点に近づくが、進み方が遅い |
| 0.5 | 3 → 1.5 → 0.75 | 0.1より速く最小点に近づく |
| 2.2 | 3 → −3.6 → 4.32 | 最小点を飛び越え、左右に振れながら遠ざかる |

**勾配と逆向きに進んでも、歩幅が大きすぎると更新後の損失は増えます。** 「学習率は大きいほどよい」という選択肢を切る判断軸です。図の範囲外に出た場合、最小点に十分近づいた場合、または20回更新した場合に教材を停止します。

0.5が常に適切という意味ではありません。適切な学習率は損失曲面などによって変わり、実際の学習ではこの単純な曲線のように進むとは限りません。
### データをどれだけ使って勾配を求めるか

- 全データ → バッチ勾配降下法
- 1サンプルずつ → 確率的勾配降下法（SGD）
- 一部のまとまり → ミニバッチ学習

## いつ使う？（得意・不得意）

勾配を利用できるモデルの学習で広く使われます。

ただし、勾配降下法は**未知データでの性能を直接保証する仕組みではありません**。訓練損失を下げても過学習が起こることはあります。

また、実際の深層学習ではSGD、Momentum、Adamなど、勾配降下の考え方を発展させた更新方法が使われます。

## G検定ひっかけポイント

### 勾配降下法と誤差逆伝播法は同じ

誤りです。

- [誤差逆伝播法](/gk/backpropagation/) → 勾配を効率よく**計算**
- 勾配降下法 → 求めた勾配を使って**更新**

### 学習率は大きいほど速くてよい

誤りです。大きすぎると最適な領域を飛び越え、学習が不安定になることがあります。

### 勾配降下法は過学習を防ぐ

誤りです。過学習対策には正則化、Dropout、Early Stoppingなどを使います。

## まとめ（試験直前用）

- 勾配降下法＝**損失が下がる方向へパラメータを更新**
- 更新方向は勾配と逆向き
- 学習率が大きすぎると不安定、小さすぎると遅い
- Backpropは勾配計算、勾配降下法は更新
- バッチ・SGD・ミニバッチは、勾配計算に使うデータ量が違う

関連： [バッチ勾配降下法](/gk/batch-gradient-descent/) / [SGD](/gk/sgd/) / [最適化手法まとめ](/gk/optimization-cheatsheet/)

{% include gk_article_footer.html %}
