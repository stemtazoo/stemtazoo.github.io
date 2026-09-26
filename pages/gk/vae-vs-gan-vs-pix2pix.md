---
layout: page
title: VAE・GAN・Pix2Pixの違い｜生成と画像変換を整理【G検定】
description: "VAE・GAN・Pix2Pixを、VAEは確率的潜在変数、GANは敵対的学習、Pix2Pixは入力画像を条件にしたペアあり画像変換という仕組みで比較します。「ノイズ→画像」という単純化を避け、学習時の入力・条件・目的からG検定の選択肢を切ります。"
permalink: /gk/vae-vs-gan-vs-pix2pix/
tags: [gk, neural_network, cheatsheet]
gk_section: ディープラーニングの応用例/データ生成/生成モデル比較
gk_order: 3
last_modified_at: 2026-09-26
---

## まず結論

| モデル | 中心となる仕組み |
|---|---|
| VAE | 確率的潜在変数＋Encoder / Decoder |
| GAN | Generator / Discriminatorの敵対的学習 |
| Pix2Pix | 入力画像を条件にしたConditional GAN |

G検定では、単に「入力がノイズか画像か」だけでなく、**学習構造と条件**を見ます。

## 直感的な説明

### VAE

学習データをEncoderで潜在分布へ写し、そこからサンプリングしてDecoderで再構成・生成します。

### GAN

GeneratorとDiscriminatorを競わせて生成を学びます。

### Pix2Pix

入力画像と正解画像のペアを使い、入力画像に対応する別画像を生成します。

## 定義・仕組み

### VAE

学習時の入力は実データです。Encoderが潜在分布を推定し、Decoderが再構成します。生成時には潜在分布からサンプリングできます。

### GAN

Generatorは潜在ノイズから生成し、Discriminatorは本物・生成データを見分けます。

### Pix2Pix

Generatorは入力画像を条件として画像を変換します。学習には対応する画像ペアを使います。

## いつ使う？（得意・不得意）

- 潜在分布・変分推論 → VAE
- 敵対的学習 → GAN
- paired image-to-image → Pix2Pix

と切り分けます。

## G検定ひっかけポイント

### VAEの入力

❌ 学習時はランダムノイズだけを入力する  
⭕ **学習データをEncoderへ入力し、潜在分布を推定する**

### Pix2Pix

❌ 条件なしで自由生成するGAN  
⭕ **入力画像を条件とするConditional GAN**

### 画質で判断

❌ 最もリアルなら必ずGAN  
⭕ **学習構造・条件から判断する**

## まとめ（試験直前用）

- VAE＝確率的潜在変数
- GAN＝敵対的学習
- Pix2Pix＝条件付き画像変換
- Pix2Pixはペアデータを使う
- VAE学習時は実データをEncoderへ入力
- **性能順位より仕組みで切る**

## 参考資料（原論文）

- [Auto-Encoding Variational Bayes｜arXiv](https://arxiv.org/abs/1312.6114)
  - VAEの原論文です。
- [Generative Adversarial Nets｜NeurIPS](https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html)
  - GANの原論文です。
- [Image-to-Image Translation with Conditional Adversarial Networks｜CVF](https://openaccess.thecvf.com/content_cvpr_2017/html/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.html)
  - Pix2Pixの原論文です。ペア画像を用いる条件付き画像変換を提案しています。

{% include gk_article_footer.html %}
