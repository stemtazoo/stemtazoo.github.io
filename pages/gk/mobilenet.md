---
layout: page
title: MobileNet（軽量CNN）とは？G検定対策
permalink: /gk/mobilenet/
tags: [gk, cnn]
---

## まず結論

* **MobileNet**とは、モバイル端末や組み込み機器での利用を目的に、**計算量とパラメータ数を大幅に削減**した軽量なCNNアーキテクチャ。
* G検定では**「ResNetより軽量」「Depthwise Convolutionを使う」**ことを正しく理解しているかが問われる。

## 直感的な説明

* 通常のCNNは、

  * 精度は高いが
  * 計算が重く、メモリも多く使います。
* MobileNetは、
  👉 **精度を少しだけ犠牲にして、圧倒的に軽く・速く動く**ように設計されています。

## 定義・仕組み

* MobileNetの最大の特徴は、

  * **Depthwise Separable Convolution** の採用です。

* これは、

  1. **Depthwise Convolution**：各チャネルごとに空間方向の畳み込みを行う
  2. **Pointwise Convolution（1×1）**：チャネル方向を統合する
     という2段階処理です。

* これにより、

  * 計算量
  * パラメータ数
    を大幅に削減できます。

## いつ使う？（得意・不得意）

### 使われる場面（得意）

* モバイル端末
* エッジAI
* リアルタイム画像認識

### 注意点・不得意

* 大規模モデル（ResNetなど）と比べると精度は劣る
* 計算資源が十分な環境では必須ではない

## G検定ひっかけポイント

* よくある誤り表現：

  * ❌ 「ResNetよりもパラメータ数が多い」
  * ❌ 「高精度化のためにモデルを巨大化している」

* 正しい理解：

  * **軽量化が目的**
  * **Depthwise Convolutionで効率化**

* 判断基準：

  * **軽量・モバイル → MobileNet**
  * **高精度・深い → ResNet**

## まとめ（試験直前用）

* MobileNet＝軽量CNN
* モバイル・エッジ向け
* Depthwise Separable Convolutionが鍵
* ResNetよりパラメータは少ない
* 「大きくなる」は誤り
