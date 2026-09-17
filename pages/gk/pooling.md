---
layout: page
title: プーリング（Pooling）
description: "プーリング（Pooling）について、G検定で問われる画像認識・CNN分野の観点から、画像タスクでの役割、特徴抽出の流れ、代表モデルとの関係を整理します。暗記だけでなく、似た概念との混同を避ける見分け方や、選択肢を切るためのポイントも確認します。"
permalink: /gk/pooling/
tags: [gk, neural_network, cnn, pooling]
gk_section: ディープラーニングの要素技術/ネットワークの構成要素
gk_order: 3
last_modified_at: 2026-09-17
---

## まず結論

* **プーリングは特徴マップを縮小する処理**
* 重要な特徴を残しつつ **計算量と過学習を抑える**
* **位置ズレに強くなる** のが大きな利点

---

## 直感的な説明

プーリングは、

> 「細かい情報を少し捨てて、大事なところだけ残す」

処理です。

* 多少位置がズレても同じ特徴とみなす
* 情報をまとめて扱う

ことで、
**安定した認識** ができるようになります。

<link rel="stylesheet" href="{{ '/assets/css/gk-visualizer.css' | relative_url }}">

<div class="gk-learning-demo" data-gk-pooling-demo>
  <p class="gk-learning-demo__title">触って確認：4×4の特徴マップを2×2に縮小する</p>
  <p class="gk-learning-demo__lead">Max PoolingとAverage Poolingを切り替えて、残る値の違いを比べてみてください。</p>

  <div class="gk-learning-demo__controls">
    <button type="button" class="gk-learning-demo__button" data-pooling-mode="max" aria-pressed="true">Max Pooling</button>
    <button type="button" class="gk-learning-demo__button" data-pooling-mode="average" aria-pressed="false">Average Pooling</button>
  </div>

  <div class="gk-pooling-demo__stage">
    <div>
      <strong>入力：4×4</strong>
      <div class="gk-pooling-demo__grid" aria-label="入力特徴マップ">
        <div class="gk-pooling-demo__cell" data-block="a">1</div>
        <div class="gk-pooling-demo__cell" data-block="a">3</div>
        <div class="gk-pooling-demo__cell" data-block="b">2</div>
        <div class="gk-pooling-demo__cell" data-block="b">4</div>
        <div class="gk-pooling-demo__cell" data-block="a">5</div>
        <div class="gk-pooling-demo__cell" data-block="a">6</div>
        <div class="gk-pooling-demo__cell" data-block="b">1</div>
        <div class="gk-pooling-demo__cell" data-block="b">2</div>
        <div class="gk-pooling-demo__cell" data-block="c">0</div>
        <div class="gk-pooling-demo__cell" data-block="c">2</div>
        <div class="gk-pooling-demo__cell" data-block="d">7</div>
        <div class="gk-pooling-demo__cell" data-block="d">3</div>
        <div class="gk-pooling-demo__cell" data-block="c">4</div>
        <div class="gk-pooling-demo__cell" data-block="c">1</div>
        <div class="gk-pooling-demo__cell" data-block="d">5</div>
        <div class="gk-pooling-demo__cell" data-block="d">8</div>
      </div>
    </div>

    <div class="gk-pooling-demo__arrow" aria-hidden="true">→</div>

    <div>
      <strong>出力：2×2</strong>
      <div class="gk-pooling-demo__grid is-output" aria-label="プーリング後の特徴マップ">
        <div class="gk-pooling-demo__cell is-result" data-pooling-output>6</div>
        <div class="gk-pooling-demo__cell is-result" data-pooling-output>4</div>
        <div class="gk-pooling-demo__cell is-result" data-pooling-output>4</div>
        <div class="gk-pooling-demo__cell is-result" data-pooling-output>8</div>
      </div>
    </div>
  </div>

  <p class="gk-pooling-demo__summary" data-pooling-summary>Max Pooling：各2×2領域の最大値だけを残し、強い特徴を拾います。</p>
  <p class="gk-learning-demo__hint">見るポイント：4個の値が1個にまとまり、位置の細かさと引き換えに特徴マップが小さくなります。</p>
</div>

<script src="{{ '/assets/js/gk-visualizer.js' | relative_url }}" defer></script>

---

## 定義・仕組み

### プーリング層とは

* 畳み込み後の **特徴マップ** に対して適用
* 一定範囲ごとに代表値を取り出す

---

### Max Pooling

* 範囲内の **最大値** を採用

**特徴**

* 強い特徴を残しやすい
* 画像認識で最も一般的

---

### Average Pooling

* 範囲内の **平均値** を採用

**特徴**

* 全体的な傾向を反映
* Max Poolingより使われる頻度は低い

---

### 出力サイズへの影響

* プーリングサイズが大きいほど

  * 出力サイズは小さくなる
  * 情報は粗くなる

---

## いつ使う？（得意・不得意）

### 得意なこと

* 位置ズレへの耐性（平行移動不変性）
* 計算量削減
* 過学習の抑制

### 注意点

* 情報を捨てるため

  * 細かい位置情報は失われる

---

## G検定ひっかけポイント

* ❌「プーリングは学習される」→ **誤り**
* ❌「プーリングは特徴を増やす」→ **誤り**
* ✅ プーリングは **固定処理**
* ✅ 位置ズレに強くなる
* ✅ Max Poolingが主流

---

## まとめ（試験直前用）

* プーリングは **特徴マップ縮小**
* Max Poolingが定番
* 位置ズレに強くなる
* 情報を捨てる点に注意

👉 次は **CNN代表モデルまとめ（LeNet / AlexNet / VGG / ResNet）** です。

{% include gk_article_footer.html %}
