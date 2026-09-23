---
layout: page
title: DCGANとは？GANにCNNを導入した画像生成モデル【G検定】
description: "DCGAN（Deep Convolutional GAN）を、Generator・Discriminatorへ畳み込み系ネットワークを導入し、画像生成向けの設計指針を示したGANとして整理します。転置畳み込み、Batch Normalization、ReLU・Leaky ReLUを押さえ、物体検出CNNとの違いを確認します。"
permalink: /gk/dcgan/
tags: [gk, neural_network, cnn, gan]
gk_section: ディープラーニングの応用例/データ生成/GAN・派生モデル
gk_order: 3
last_modified_at: 2026-09-23
---

## まず結論

**DCGAN（Deep Convolutional GAN）**は、GANへ畳み込み系ネットワークを導入し、画像生成に適したアーキテクチャ設計を示したモデルです。

G検定では、**GAN＋CNN**が最重要キーワードです。

## 直感的な説明

基本GANの考え方はそのままに、画像の空間構造を扱いやすいCNNをGenerator・Discriminatorへ取り入れたものと考えます。

## 定義・仕組み

DCGAN原論文では、代表的な設計指針として、

- Generatorで空間サイズを広げる畳み込み系処理
- Discriminatorで畳み込みによる特徴抽出
- Batch Normalization
- GeneratorでReLU（出力はtanh）
- DiscriminatorでLeaky ReLU

などが示されました。

重要なのは、DCGANが**物体検出モデルではなく生成モデル**であることです。

## いつ使う？（得意・不得意）

DCGANはGAN研究の発展で重要な画像生成モデルです。

ただし、

> DCGAN＝高解像度画像を作るためのモデル

とだけ覚えるのは不十分です。中心は**畳み込みアーキテクチャをGANへ導入したこと**です。

## G検定ひっかけポイント

- GAN＋CNN → **DCGAN**
- Generator / Discriminator → GAN系
- YOLO / SSD → 物体検出でありDCGANではない
- **高画質という性能評価だけでモデルを判定しない**

## まとめ（試験直前用）

- DCGAN＝**Deep Convolutional GAN**
- GANにCNN系構造を導入
- Generator / Discriminatorを使用
- 画像生成向けの代表的設計
- 物体検出CNNとは別物

## 参考資料

- [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks｜arXiv](https://arxiv.org/abs/1511.06434)

{% include gk_article_footer.html %}
