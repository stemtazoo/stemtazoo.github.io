---
layout: page
title: Stable Diffusionとは？Latent Diffusionの仕組み【G検定対策】
description: "Stable Diffusionを、画像そのものではなく圧縮した潜在空間で拡散・ノイズ除去を行うLatent Diffusion系の画像生成モデルとして整理します。VAE系のオートエンコーダ、デノイザ、テキスト条件付けの役割を分け、通常の拡散モデルやGANとの違いをG検定向けに確認します。"
permalink: /gk/stable-diffusion/
tags: [gk, neural_network, generative_model, diffusion]
gk_section: ディープラーニングの応用例/データ生成/拡散モデル
gk_order: 2
last_modified_at: 2026-09-23
---

## まず結論

**Stable Diffusion**は、Latent Diffusionの考え方を使い、**画像を圧縮した潜在空間でノイズ除去を繰り返す画像生成モデル**です。

G検定では、

- Diffusion → ノイズを加える / 除去する
- Stable Diffusion → **潜在空間でDiffusionを行う**
- GAN → 生成器と識別器の敵対的学習

と切り分けます。

## 直感的な説明

通常の画像空間で高解像度画像を直接扱うと、計算量が大きくなります。

Stable Diffusionでは、

1. 画像を圧縮して潜在表現にする
2. 潜在空間でノイズを加える・除去する
3. 最後に画像へ戻す

という流れを使います。

> **大きな画像のままではなく、圧縮した表現の上で拡散する**

のがポイントです。

## 定義・仕組み

### Latent Diffusion

Latent Diffusion Model（LDM）は、事前学習したオートエンコーダで画像を潜在表現へ変換し、その**潜在空間上でDiffusion Modelを学習**します。

これにより、ピクセル空間で拡散する方式と比べて、計算量を抑えながら高解像度画像を扱いやすくします。

### 代表的な構成要素

Stable Diffusion系の基本的な構成では、次の役割を分けて考えます。

- **オートエンコーダ**：画像 ↔ 潜在表現
- **デノイザ**：潜在空間のノイズを予測・除去
- **テキストエンコーダ**：プロンプトを条件情報へ変換
- **Attention / Cross-Attention**：テキスト条件を画像生成へ反映

初期の代表的なStable DiffusionではU-Net系デノイザとCLIP系テキストエンコーダが使われました。

ただし、Stable Diffusion系の新しいモデルでは内部構造が変わる場合もあるため、**U-NetやCLIPをStable Diffusionの絶対条件として覚えない**ようにします。

## いつ使う？（得意・不得意）

代表的な用途は、

- Text-to-Image
- Image-to-Image
- Inpainting
- 画像編集

などです。

注意点として、Diffusion系は生成時に反復的なデノイジングを行うため、1回の順伝播だけで生成するモデルより計算が多くなる場合があります。

一方、潜在空間で処理することで、ピクセル空間のDiffusionより計算負荷を下げることが狙いです。

## G検定ひっかけポイント

### Stable Diffusion＝GAN？

❌ 生成器と識別器を競わせる  
⭕ **Diffusionを潜在空間で行う**

### Diffusionは必ず画像空間？

❌ Diffusion Modelは必ずピクセル空間で動く  
⭕ **潜在空間で拡散するLatent Diffusionもある**

### Stable Diffusion＝VAE？

❌ VAEだけで画像生成する  
⭕ **オートエンコーダは画像と潜在表現の変換を担当し、生成の中心にはDiffusionがある**

### Text-to-Image＝Stable Diffusionだけ？

❌ テキストから画像なら必ずStable Diffusion  
⭕ **Text-to-Imageはタスク名であり、他のモデルでも実現できる**

## まとめ（試験直前用）

- Stable Diffusion＝**Latent Diffusion系**
- 画像を潜在空間へ圧縮してから拡散
- 潜在空間でノイズ除去を繰り返す
- テキスト条件をAttentionなどで反映
- GANではない
- U-NetやCLIPは代表的構成だが、名称そのものの絶対条件ではない

## 参考資料

- [High-Resolution Image Synthesis with Latent Diffusion Models｜arXiv](https://arxiv.org/abs/2112.10752)
- [Diffusion Model](/gk/diffusion-model/)

{% include gk_article_footer.html %}
