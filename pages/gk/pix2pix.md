---
layout: page
title: Pix2Pixとは？ペア画像を使う条件付き画像変換【G検定対策】
description: "Pix2Pixを、入力画像と対応する正解画像のペアを使って画像から画像への変換を学習するConditional GANとして整理します。入力画像を条件とするGenerator、PatchGAN Discriminator、L1損失を押さえ、ペア不要のCycleGANとの違いを確認します。"
permalink: /gk/pix2pix/
tags: [gk, cnn, neural_network, gan]
gk_section: ディープラーニングの応用例/データ生成/GAN・派生モデル
gk_order: 5
last_modified_at: 2026-09-23
---

## まず結論

**Pix2Pix**は、対応する**入力画像と出力画像のペア**を使って、画像→画像変換を学習するConditional GANです。

G検定では、

- ペアあり → Pix2Pix
- ペアなし → CycleGAN

で切り分けます。

## 直感的な説明

Pix2Pixは、

> この入力画像なら、この完成画像

という正解ペアを見ながら画像変換を学ぶモデルです。

## 定義・仕組み

Generatorは入力画像を条件として出力画像を生成します。

Discriminatorは、入力画像と出力画像の組合せが本物のペアか生成されたペアかを判定します。

原論文では、敵対的損失に加えて**L1損失**を使い、出力を正解画像へ近づけます。

また、局所領域ごとの真偽を判定する**PatchGAN** Discriminatorが使われます。

## いつ使う？（得意・不得意）

代表例は、

- ラベル画像 → 写真
- 輪郭 → 物体画像
- 画像の外観変換

などです。

最大の条件は、**対応する教師画像ペアが必要**なことです。

## G検定ひっかけポイント

### Pix2Pix＝通常GAN？

❌ ノイズだけから自由生成する基本GAN  
⭕ **入力画像を条件とするConditional GAN**

### CycleGANとの違い

- Pix2Pix → **対応ペアあり**
- CycleGAN → **対応ペアなし**

## まとめ（試験直前用）

- Pix2Pix＝**paired image-to-image translation**
- Conditional GAN
- 入力画像が条件
- 対応する正解画像ペアを使う
- L1損失
- PatchGAN
- ペアなしならCycleGAN

## 参考資料

- [Image-to-Image Translation with Conditional Adversarial Networks｜CVPR 2017](https://arxiv.org/abs/1611.07004)

{% include gk_article_footer.html %}
