---
layout: page
title: GAN派生モデルまとめ｜DCGAN・Conditional GAN・Pix2Pix・CycleGAN【G検定】
description: "GANの代表的派生を、DCGANは畳み込み構造、Conditional GANは条件付き生成、Pix2Pixはペアあり画像変換、CycleGANはペアなし画像変換という判断軸で比較します。画質順位ではなく、条件・データの対応関係・学習構造でG検定の選択肢を切ります。"
permalink: /gk/gan-variants/
tags: [gk, neural_network, gan, cheatsheet]
gk_section: ディープラーニングの応用例/データ生成/GAN・派生モデル
gk_order: 2
last_modified_at: 2026-09-26
---

## まず結論

GAN派生モデルは、**性能順位ではなく「何を追加したか」**で切り分けます。

| モデル | 判断軸 |
|---|---|
| GAN | GeneratorとDiscriminatorの敵対的学習 |
| DCGAN | GANにCNN系構造 |
| Conditional GAN | 条件を与えて生成 |
| Pix2Pix | ペアあり画像→画像変換 |
| CycleGAN | ペアなし画像→画像変換 |

## 直感的な説明

- DCGAN → **画像向けの畳み込み構造**
- Conditional GAN → **条件を指定する**
- Pix2Pix → **正解ペアを見て変換**
- CycleGAN → **正解ペアなしで変換**

と整理します。

## 定義・仕組み

### DCGAN

[DCGAN](/gk/dcgan/)はGANへCNN系アーキテクチャを導入した代表モデルです。

### Conditional GAN

[Conditional GAN](/gk/conditional-gan/)はラベル・属性・画像などの条件を与えて生成を制御します。

### Pix2Pix

[Pix2Pix](/gk/pix2pix/)は入力画像を条件とし、対応する出力画像ペアから画像変換を学びます。

### CycleGAN

[CycleGAN](/gk/cyclegan/)は対応ペアなしで画像変換を学び、Cycle Consistencyを利用します。

## いつ使う？（得意・不得意）

問題文で、

- CNNをGANへ導入 → DCGAN
- ラベルで生成制御 → Conditional GAN
- ペア画像あり → Pix2Pix
- ペア画像なし → CycleGAN

を探します。

## G検定ひっかけポイント

### 「高品質」だけで判定しない

❌ 高品質画像ならDCGAN / StyleGANと即断  
⭕ **モデル構造・条件・データ要件を見る**

### Pix2PixとConditional GAN

Pix2PixはConditional GANの考え方を画像変換へ使った具体例です。

### CycleGAN

重要なのは単なる「スタイル変換」ではなく、**対応ペア不要＋循環一貫性**です。

## まとめ（試験直前用）

- GAN＝敵対的学習
- DCGAN＝CNN
- Conditional GAN＝条件付き
- Pix2Pix＝ペアあり
- CycleGAN＝ペアなし＋Cycle Consistency
- **画質ランキングで覚えない**

## 参考資料（原論文）

- [Generative Adversarial Nets｜NeurIPS](https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html)
  - GANの原論文です。
- [Conditional Generative Adversarial Nets｜arXiv](https://arxiv.org/abs/1411.1784)
  - Conditional GANの原論文です。
- [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks｜arXiv](https://arxiv.org/abs/1511.06434)
  - DCGANの原論文です。
- [Image-to-Image Translation with Conditional Adversarial Networks｜CVF](https://openaccess.thecvf.com/content_cvpr_2017/html/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.html)
  - Pix2Pixの原論文です。
- [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks｜CVF](https://openaccess.thecvf.com/content_iccv_2017/html/Zhu_Unpaired_Image-To-Image_Translation_ICCV_2017_paper.html)
  - CycleGANの原論文です。

{% include gk_article_footer.html %}
