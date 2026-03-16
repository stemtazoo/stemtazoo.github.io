---
layout: page
title: GANとConditional GANの違いとは？【1ページ比較・G検定対策】
permalink: /gk/gan-vs-conditional-gan/
tags: [gk, neural_network, cheatsheet]
gk_section: ディープラーニングの応用例/データ生成
gk_order: 9
---

## まず結論

通常のGANは**条件なしでランダム生成**を行うのに対し、Conditional GANは**条件を与えて生成結果を制御できるGAN**で、G検定ではこの違いを使って選択肢を切ることが最重要。

## 直感的な説明

通常のGANは、

> 開けるまで中身が分からないガチャ

のようなものです。

一方、Conditional GANは、

> 「犬を出して」「数字の3を出して」

と**注文できるガチャ**です。

つまり、

* GAN：何が出るか分からない
* Conditional GAN：何を出すか指定できる

という違いがあります。

## 定義・仕組み

### 通常のGAN（Generative Adversarial Network）

* 入力：ランダムノイズのみ
* 出力：ランダムな生成データ
* 条件情報：なし

### Conditional GAN（条件付きGAN）

* 入力：ランダムノイズ + 条件
* 出力：条件に沿った生成データ
* 条件情報：クラスラベル・属性・画像など

Discriminatorも同様に、

* データ + 条件

を使って真偽判定を行います。

## いつ使う？（得意・不得意）

### 通常のGANが向く場面

* 完全に自由なデータ生成
* 条件を指定する必要がない場合

### Conditional GANが向く場面

* 生成結果を制御したい場合
* クラス別・属性別に生成したい場合
* 入力に応じた出力が必要な場合（Pix2Pixなど）

## G検定ひっかけポイント

G検定では、**「GAN＝全部同じ」だと思わせる選択肢**が出ます。

### よくあるひっかけ

* Conditional GANを独立したモデル名だと誤解
* Pix2Pixと通常GANを同列に並べる

### 判断基準（ここで切る）

* **条件がある？** → Conditional GAN
* **条件がない？** → 通常のGAN
* **入力画像が条件？** → Pix2Pix（Conditional GAN）
* **ペアなし画像変換？** → CycleGAN

選択肢で

> 「条件情報を用いて生成を制御する」

とあれば、Conditional GAN側です。

## まとめ（試験直前用）

* 通常のGANは条件なし生成
* Conditional GANは条件付き生成
* 条件はラベル・属性・画像など
* Pix2PixはConditional GANの一種
* G検定では「条件の有無」で即判断
