---
layout: page
title: GAN（敵対的生成ネットワーク）とは？GeneratorとDiscriminator【G検定】
description: "GAN（Generative Adversarial Network）を、GeneratorとDiscriminatorを敵対的に学習させる生成モデルとして整理します。潜在ノイズからデータを生成するGenerator、本物・生成データを見分けるDiscriminator、ミニマックス、モード崩壊を押さえ、VAEやDiffusionとの違いを確認します。"
permalink: /gk/gan/
tags: [gk, neural_network, generative_model, gan]
gk_section: ディープラーニングの応用例/データ生成/GAN・派生モデル
gk_order: 1
last_modified_at: 2026-09-23
---

## まず結論

**GAN（Generative Adversarial Network：敵対的生成ネットワーク）**は、

- **Generator（生成器）**：本物らしいデータを作る
- **Discriminator（識別器）**：本物データと生成データを見分ける

という2つのネットワークを**敵対的に学習**させる生成モデルです。

G検定では、**Generator＋Discriminator＋敵対的学習**を見たらGANを疑います。

## 直感的な説明

GANは、

> 偽物を作る側と、偽物を見破る側を競わせる

イメージです。

GeneratorはDiscriminatorをだませるように生成を改善し、Discriminatorはより正確に真偽を見分けるよう学習します。

## 定義・仕組み

基本GANでは、Generatorは潜在変数 z から生成データを作り、Discriminatorは入力が本物データか生成データかを判定します。

学習は**ミニマックスゲーム**として表現されます。

重要なのは、GANがVAEのようにEncoderで潜在分布を近似する方式ではないことです。

### モード崩壊

GANでは、Generatorが限られた種類の出力ばかり作る**モード崩壊（Mode Collapse）**が起こることがあります。

これは、見た目の品質とは別に、生成データの多様性が失われる問題です。

## いつ使う？（得意・不得意）

GAN系は、

- 画像生成
- 画像変換
- データ拡張
- 超解像

などに利用されてきました。

ただし、**GANなら常にVAEやDiffusionより高品質**と固定順位で覚えるのは避けます。モデル・データ・評価方法によって結果は変わります。

## G検定ひっかけポイント

### GAN＝VAE？

❌ Encoder / Decoderで潜在分布を学ぶ  
⭕ **Generator / Discriminatorを敵対的に学習**

### GAN＝Diffusion？

❌ ノイズを段階的に除去して生成する  
⭕ **Generatorが直接データを生成し、Discriminatorと競う**

### モード崩壊

❌ 勾配消失の別名  
⭕ **限られた種類の生成ばかりになる問題**

## まとめ（試験直前用）

- GAN＝**敵対的生成ネットワーク**
- Generator＝生成
- Discriminator＝真偽判定
- ミニマックスゲーム
- モード崩壊に注意
- VAE＝確率的潜在変数
- Diffusion＝反復的ノイズ除去

## 参考資料

- [Generative Adversarial Nets｜NeurIPS 2014](https://papers.nips.cc/paper/5423-generative-adversarial-nets)
- [VAEとGANの違い](/gk/vae-vs-gan/)

{% include gk_article_footer.html %}
