---
layout: page
title: CycleGANとは？ペアなし画像変換とCycle Consistency【G検定】
description: "CycleGANを、対応する画像ペアがなくても2つのドメイン間の画像変換を学習できるGANとして整理します。A→BとB→Aの2方向変換、Cycle Consistency Lossを押さえ、ペア画像を使うPix2Pixとの違いをG検定向けに確認します。"
permalink: /gk/cyclegan/
tags: [gk, cnn, neural_network, gan]
gk_section: ディープラーニングの応用例/データ生成/GAN・派生モデル
gk_order: 6
last_modified_at: 2026-09-23
---

## まず結論

**CycleGAN**は、入力と出力が1対1で対応した画像ペアを用意しなくても、2つの画像ドメイン間の変換を学習できるモデルです。

最大のキーワードは、**Cycle Consistency（循環一貫性）**です。

## 直感的な説明

写真の集合Aと絵画の集合Bはあるけれど、

> この写真に対応する正解の絵画

というペアはない状況を考えます。

CycleGANは、

- A → B
- B → A

の両方向を学び、変換して戻したときに元の画像へ近づくよう制約します。

## 定義・仕組み

CycleGANでは主に、

- A→BのGenerator
- B→AのGenerator
- 各ドメインのDiscriminator
- Cycle Consistency Loss

を使います。

たとえば A→B→A と戻したとき、元のAへ近づくように学習します。

## いつ使う？（得意・不得意）

代表例は、

- 馬 ↔ シマウマ
- 夏 ↔ 冬
- 写真 ↔ 絵画風

などの**unpaired image-to-image translation**です。

「教師なし」とだけ覚えるより、**対応ペアが不要**と覚える方が誤解が少なくなります。

## G検定ひっかけポイント

### Pix2Pix

→ 対応する入力・正解画像の**ペアあり**

### CycleGAN

→ **ペアなし＋Cycle Consistency**

### Cycle Consistency

❌ 同じ画像を2回生成する  
⭕ **A→B→Aのように戻したとき元へ近づける**

## まとめ（試験直前用）

- CycleGAN＝**ペアなし画像変換**
- A→BとB→A
- Cycle Consistency Loss
- Pix2Pix＝ペアあり
- 「教師なし」より**unpaired**で覚える

## 参考資料

- [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks｜ICCV 2017](https://arxiv.org/abs/1703.10593)

{% include gk_article_footer.html %}
