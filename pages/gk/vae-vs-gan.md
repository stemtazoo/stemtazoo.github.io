---
layout: page
title: VAEとGANの違い｜確率的潜在変数と敵対的学習【G検定】
description: "VAEとGANを、VAEはEncoder・Decoderと確率的潜在変数、GANはGenerator・Discriminatorの敵対的学習という仕組みで比較します。画質・安定性の固定順位ではなく、変分推論・KLダイバージェンス・ミニマックス・モード崩壊という判断軸で整理します。"
permalink: /gk/vae-vs-gan/
tags: [gk, neural_network, generative_model, cheatsheet]
gk_section: ディープラーニングの応用例/データ生成/生成モデル比較
gk_order: 2
last_modified_at: 2026-09-23
---

## まず結論

VAEとGANはどちらも生成モデルですが、**学習の仕組みが違います。**

| 観点 | VAE | GAN |
|---|---|---|
| 中心構造 | Encoder / Decoder | Generator / Discriminator |
| 潜在変数 | 確率分布として扱う | 潜在ノイズから生成 |
| 学習の考え方 | 変分推論・再構成 | 敵対的学習 |
| 代表的注意点 | 再構成とのトレードオフ | モード崩壊など |

G検定では、**分布・変分推論 → VAE、敵対・識別器 → GAN**で切ります。

## 直感的な説明

### VAE

入力データを潜在空間の確率分布へ写し、そこからサンプリングして再構成・生成します。

### GAN

Generatorが本物らしいデータを作り、Discriminatorが真偽を判定します。

## 定義・仕組み

### VAE

- Encoderが潜在分布のパラメータを推定
- 再パラメータ化して潜在変数をサンプリング
- Decoderがデータを再構成・生成
- 再構成項とKLダイバージェンスを扱う

### GAN

- Generatorが生成データを作る
- Discriminatorが本物 / 生成を判定
- 両者を敵対的に学習
- モード崩壊などの学習上の課題がある

## いつ使う？（得意・不得意）

VAEは潜在表現を明示的に扱いたい場面、GANは敵対的学習を利用した生成・画像変換などで使われます。

ただし、

- GAN＝必ず高画質
- VAE＝必ず安定
- GAN＝必ずVAEより優れる

のような絶対的な性能順位は避けます。

## G検定ひっかけポイント

### Generator / Discriminator

→ **GAN**

### Encoder / Decoder＋潜在分布

→ **VAE**

### モード崩壊

→ GANで代表的な問題

### KLダイバージェンス＋再構成

→ VAE

## まとめ（試験直前用）

- VAE＝**確率的潜在変数モデル**
- GAN＝**敵対的生成モデル**
- VAE：Encoder / Decoder
- GAN：Generator / Discriminator
- モード崩壊 → GAN
- **性能順位ではなく学習機構で判断する**

{% include gk_article_footer.html %}
