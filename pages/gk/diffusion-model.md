---
layout: page
title: Diffusion Model（拡散モデル）
description: "Diffusion Model（拡散モデル）を、データへ徐々にノイズを加える拡散過程と、ノイズからデータを復元する逆過程を学ぶ生成モデルとして整理します。GANの敵対的学習、VAEの潜在変数モデルとの違いを仕組みで比較し、性能ランキングに頼らずG検定の選択肢を切る判断軸を確認します。"
permalink: /gk/diffusion-model/
tags: [gk, neural_network, generative_model]
gk_section: ディープラーニングの応用例/データ生成/拡散モデル
gk_order: 1
last_modified_at: 2026-09-23
---

## まず結論

**Diffusion Model（拡散モデル）**は、データに徐々にノイズを加える過程と、その逆向きに**ノイズからデータを復元する過程**を利用する生成モデルです。

G検定では、モデル同士を性能順位で覚えるより、次の仕組みで切り分けます。

- **GAN**：生成器と識別器の**敵対的学習**
- **VAE**：**潜在変数**を確率分布として扱い、再構成する
- **Diffusion**：**ノイズを加える → 段階的にノイズを除去する**

特に **「ノイズ」「逆拡散」「denoising」** がDiffusionの重要キーワードです。

## 直感的な説明

Diffusion Modelは、

> **画像を少しずつノイズで壊し、その逆の戻し方を学ぶ**

イメージです。

学習時には、元データへ少しずつノイズを加えます。

生成時には、ランダムなノイズからスタートして、学習したノイズ除去を繰り返しながらデータらしい形へ近づけます。

## 定義・仕組み

### Forward Process（拡散過程）

元データに少しずつノイズを加えていきます。

イメージは、

**元画像 → 少しノイズ → さらにノイズ → ほぼランダムなノイズ**

です。

### Reverse Process（逆過程）

モデルは、ノイズを含むデータから、元のデータ方向へ戻す処理を学びます。

DDPM（Denoising Diffusion Probabilistic Models）では、各段階で加えられたノイズを予測しながら逆向きの生成過程を学ぶ方法が代表的です。

生成時には、

**ランダムノイズ → ノイズ除去を反復 → 生成データ**

という流れになります。

### GAN・VAEとの違い

| 観点 | GAN | VAE | Diffusion |
|---|---|---|---|
| 中心となる考え方 | 生成器と識別器の競争 | 潜在変数と再構成 | ノイズ付加とノイズ除去 |
| 学習のキーワード | 敵対的学習 | Encoder / Decoder、潜在分布 | Forward / Reverse Process |
| 生成の流れ | 生成器がデータを生成 | 潜在変数からDecoderで生成 | ノイズから段階的に生成 |
| G検定での見分け方 | 識別器と競わせる | 潜在空間・再構成 | ノイズ・逆拡散・denoising |

重要なのは、**「どれが常に最も高性能か」ではなく、仕組みが違う**ことです。

## いつ使う？（得意・不得意）

Diffusion Modelは、画像生成をはじめ、画像編集、超解像などさまざまな生成タスクで利用されています。

[Stable Diffusion](/gk/stable-diffusion/)は、拡散モデルを利用した代表例です。

### 注意点

典型的なDiffusion Modelでは、生成時にノイズ除去を複数回繰り返すため、**反復計算が必要**です。

一方で、サンプリングを高速化する研究・手法もあるため、

> Diffusionは必ず遅い

と絶対的に覚えるのは避けます。

## G検定ひっかけポイント

### DiffusionはGANの一種？

❌ 生成器と識別器を競わせる  
⭕ **ノイズを加える過程と、ノイズを除去する逆過程を利用する**

生成器と識別器の敵対的学習はGANの特徴です。

### VAEと同じ仕組み？

❌ 潜在分布から復元することがDiffusionの中心  
⭕ **Diffusionの代表的な判断軸はノイズ付加と反復的なノイズ除去**

VAEについては[VAEとは？](/gk/vae/)で確認できます。

### 「高画質ならDiffusion」と決めつけない

生成品質だけではモデルの種類を判定できません。

問題文では、

- 識別器との競争 → **GAN**
- 潜在変数・再構成 → **VAE**
- ノイズ・逆拡散・denoising → **Diffusion**

と、**仕組みのキーワード**で判断します。

### 画像専用？

❌ Diffusionは画像にしか使えない  
⭕ **拡散という生成の考え方は画像以外にも応用できる**

G検定では画像生成の代表例として見ることが多いですが、概念そのものを画像専用と決めつけないようにします。

## まとめ（試験直前用）

- Diffusion＝**ノイズを加え、その逆向きのノイズ除去を学ぶ生成モデル**
- Forward Process＝ノイズを加える
- Reverse Process＝ノイズからデータ方向へ戻す
- GAN＝敵対的学習
- VAE＝潜在変数と再構成
- **性能順位ではなく、生成の仕組みで切り分ける**

## 参考資料

- [Denoising Diffusion Probabilistic Models｜NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)
- [VAEとGANの違い](/gk/vae-vs-gan/)
- [Stable Diffusion](/gk/stable-diffusion/)

{% include gk_article_footer.html %}
