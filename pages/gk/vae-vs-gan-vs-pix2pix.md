---
layout: page
title: VAE・GAN・Pix2Pixの使い分け｜入力条件と学習データ【G検定】
description: "VAE・通常GAN・Pix2Pixを、学習時に使う実データや画像ペアと、生成時に指定する潜在変数や入力画像から整理します。Pix2PixがConditional GANの具体例であることを押さえ、画像生成の性能順位ではなく、必要な条件と用意できるデータで判断します。"
permalink: /gk/vae-vs-gan-vs-pix2pix/
tags: [gk, neural_network, cheatsheet]
gk_section: ディープラーニングの応用例/データ生成/生成モデル比較
gk_order: 3
last_modified_at: 2026-10-19
---

## まず結論

生成モデルを選ぶときは、**何を手掛かりに学習し、生成時に何を指定するか**を確認します。

このページは、基本形のVAE・GANと、入力画像を条件にするPix2Pixの位置付けを整理します。VAEとGANの学習信号そのものを詳しく比べたい場合は、[再構成・KL項と敵対的学習の比較](/gk/vae-vs-gan/)を参照してください。

## 直感的な説明

「画像を作る」だけではモデルを決められません。

- データから潜在分布を学び、そこから生成するのか
- 本物と生成物を識別する相手と競わせるのか
- 線画などの入力画像に対応する出力画像を作りたいのか

という、目的と条件の違いを見ます。**Pix2PixはGANと無関係な第三の学習原理ではなく、Conditional GANによる画像変換**です。

## 定義・仕組み

| 基本モデル | 学習時に使う情報 | 生成・変換時の主な手掛かり | 確認する先 |
| --- | --- | --- | --- |
| VAE | 実データから潜在分布を推定し、再構成する | 潜在変数をサンプリングする | [VAE](/gk/vae/) |
| 通常のGAN | 実データと生成データを識別する学習 | 潜在ノイズ | [GAN](/gk/gan/) |
| Pix2Pix | 対応する入力画像・正解画像のペア | 変換元の入力画像 | [Pix2Pix](/gk/pix2pix/) |

表は基本形の比較です。条件付きVAEや他のConditional GANもあるため、**VAEは画像条件を使えない、画像を入力すれば必ずPix2Pix**とは判断しません。

## いつ使う？（得意・不得意）

| 確認したい要件 | 着眼点 |
| --- | --- |
| 潜在分布と再構成を扱いたい | VAEの仕組みを確認する |
| 識別器との敵対的学習を使いたい | GANの仕組みを確認する |
| 入力線画に対応する画像へ変換したい | Pix2Pixの画像条件と学習ペアを確認する |
| 対応する画像ペアを用意できない | Pix2Pixの前提と合うか再確認する。ペアなし変換は[CycleGAN](/gk/cyclegan/)へ |

同じ画像生成でも、与える条件と学習データの用意の仕方が異なります。

## G検定ひっかけポイント

- 「VAEは学習時もノイズだけを入力」→ 誤り。実データをEncoderへ入力する。
- 「Pix2Pixは条件なしGAN」→ 誤り。入力画像が条件になる。
- 「Pix2Pixはペア画像を使わない」→ 誤り。対応する画像ペアを使う。
- 「最もリアルなら必ずGAN」→ 画質の固定順位ではなく、条件と学習構造を見る。

## まとめ（試験直前用）

- 基本形のVAE：**実データから潜在分布を学ぶ**
- 通常GAN：**識別器との敵対的学習**
- Pix2Pix：**入力画像を条件にするGANで、学習には画像ペアが必要**
- 同列の性能ランキングではなく、条件とデータの対応を見る

## 参考資料（原論文）

- [Auto-Encoding Variational Bayes｜arXiv](https://arxiv.org/abs/1312.6114)
  - VAEの原論文です。
- [Generative Adversarial Nets｜NeurIPS](https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html)
  - GANの原論文です。
- [Image-to-Image Translation with Conditional Adversarial Networks｜CVF](https://openaccess.thecvf.com/content_cvpr_2017/html/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.html)
  - Pix2Pixの原論文です。ペア画像を用いる条件付き画像変換を提案しています。

{% include gk_article_footer.html %}
