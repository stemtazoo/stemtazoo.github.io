---
layout: page
title: Conditional GAN（条件付きGAN）とは？Pix2Pixとの関係【G検定対策】
permalink: /gk/conditional-gan/
tags: [gk, neural_network, cnn]
gk_section: ディープラーニングの応用例/データ生成
gk_order: 13
---

## まず結論

Conditional GAN（条件付きGAN）は**「条件情報を与えて生成を制御するGAN」**で、G検定では「Pix2PixはConditional GANの一種」という位置づけを正しく理解できているかが問われる。

## 直感的な説明

通常のGANは、

> 何が出てくるか分からない福袋

のようなものです。

一方、Conditional GANは、

> 「赤い服がほしい」「犬の画像を出して」

のように、**条件を指定して生成するGAN**です。

Pix2Pixの場合、その条件が

* **入力画像そのもの**

になります。

つまり、

* Conditional GAN：条件つき生成の枠組み
* Pix2Pix：条件として「画像」を与える具体例

という関係です。

## 定義・仕組み

Conditional GANは、GANに**条件情報（condition）**を追加したモデルです。

### 仕組みのポイント

* Generator：

  * ノイズ + 条件 → 生成データ
* Discriminator：

  * データ + 条件 → 本物／偽物判定

条件には、

* クラスラベル
* 属性情報
* **入力画像（Pix2Pix）**

などが使われます。

重要なのは、

> **条件を与えることで、生成結果をコントロールできる**

という点です。

## いつ使う？（得意・不得意）

### 得意なケース

* 生成結果を指定したいとき
* クラスや属性ごとに生成したいとき
* 入力に応じた出力が必要なとき（→ Pix2Pix）

### 苦手・注意点

* 条件情報が用意できない場合
* 完全に自由な生成だけをしたい場合

## G検定ひっかけポイント

G検定では、**Conditional GANを単独モデルと誤解させる**問題が出やすいです。

### よくある誤解

* Conditional GAN ＝ Pix2Pix
* Conditional GAN ＝ 特定の1モデル名

これは間違いです。

### 正しい理解（ここで切る）

* Conditional GAN：**考え方・枠組み**
* Pix2Pix：**Conditional GANの具体的モデル**
* CycleGAN：Conditional GANではない（ペアなし）

選択肢で

> 「条件付きGANの一種として入力画像を条件に用いる」

とあれば、Pix2Pixを指している可能性が高いです。

## まとめ（試験直前用）

* Conditional GANは**条件を与えて生成するGAN**
* 条件にはラベル・属性・画像などが使える
* Pix2Pixは**入力画像を条件にしたConditional GAN**
* Conditional GANはモデル名ではなく枠組み
* G検定ではPix2Pixとの上下関係を整理して覚える
