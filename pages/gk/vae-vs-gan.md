---
layout: page
title: VAEとGANの違い｜確率的潜在変数と敵対的学習【G検定】
description: "VAEとGANを、VAEはEncoder・Decoderと確率的潜在変数、GANはGenerator・Discriminatorの敵対的学習という仕組みで比較します。画質・安定性の固定順位ではなく、変分推論・KLダイバージェンス・ミニマックス・モード崩壊という判断軸で整理します。"
permalink: /gk/vae-vs-gan/
tags: [gk, neural_network, generative_model, cheatsheet]
gk_section: ディープラーニングの応用例/データ生成/生成モデル比較
gk_order: 2
last_modified_at: 2026-11-25
---

## まず結論

VAEとGANはどちらも生成モデルですが、**どんな信号でパラメータを学習するか**が違います。このページは再構成・KL項と敵対的学習を区別するための比較です。入力画像を条件にするPix2Pixまで含む選び方は、[生成と条件付き画像変換の比較](/gk/vae-vs-gan-vs-pix2pix/)へ進めます。

<table class="study-comparison study-comparison--pair" id="vae-gan-pair" role="table" aria-label="VAEとGANの比較">
  <thead role="rowgroup">
    <tr role="row"><th scope="col" role="columnheader">観点</th><th scope="col" role="columnheader" id="vae-gan-pair-col-1">VAE</th><th scope="col" role="columnheader" id="vae-gan-pair-col-2">GAN</th></tr>
  </thead>
  <tbody role="rowgroup">
    <tr role="row">
      <th scope="row" role="rowheader" id="vae-gan-pair-row-1">中心構造</th>
      <td role="cell" headers="vae-gan-pair-row-1 vae-gan-pair-col-1"><span class="study-comparison__label" aria-hidden="true">VAE</span>Encoder / Decoder</td>
      <td role="cell" headers="vae-gan-pair-row-1 vae-gan-pair-col-2"><span class="study-comparison__label" aria-hidden="true">GAN</span>Generator / Discriminator</td>
    </tr>
    <tr role="row">
      <th scope="row" role="rowheader" id="vae-gan-pair-row-2">潜在変数</th>
      <td role="cell" headers="vae-gan-pair-row-2 vae-gan-pair-col-1"><span class="study-comparison__label" aria-hidden="true">VAE</span>確率分布として扱う</td>
      <td role="cell" headers="vae-gan-pair-row-2 vae-gan-pair-col-2"><span class="study-comparison__label" aria-hidden="true">GAN</span>潜在ノイズから生成</td>
    </tr>
    <tr role="row">
      <th scope="row" role="rowheader" id="vae-gan-pair-row-3">学習の考え方</th>
      <td role="cell" headers="vae-gan-pair-row-3 vae-gan-pair-col-1"><span class="study-comparison__label" aria-hidden="true">VAE</span>変分推論・再構成</td>
      <td role="cell" headers="vae-gan-pair-row-3 vae-gan-pair-col-2"><span class="study-comparison__label" aria-hidden="true">GAN</span>敵対的学習</td>
    </tr>
    <tr role="row">
      <th scope="row" role="rowheader" id="vae-gan-pair-row-4">代表的注意点</th>
      <td role="cell" headers="vae-gan-pair-row-4 vae-gan-pair-col-1"><span class="study-comparison__label" aria-hidden="true">VAE</span>再構成とのトレードオフ</td>
      <td role="cell" headers="vae-gan-pair-row-4 vae-gan-pair-col-2"><span class="study-comparison__label" aria-hidden="true">GAN</span>モード崩壊など</td>
    </tr>
  </tbody>
</table>

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

### 学習信号を説明から見分ける

| 説明 | 対応する基本モデル |
| --- | --- |
| 入力を再構成し、潜在分布を事前分布へ近付ける | VAE：再構成項とKL項 |
| 本物と生成物を見分ける識別器と、識別器を欺く生成器を学習する | GAN：敵対的学習 |

VAEにもGANにも潜在変数や乱数が登場するため、「乱数から画像を作る」だけでは区別できません。**再構成と分布の制約か、生成器と識別器の競争か**を見ます。

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

## 参考資料（原論文）

- [Auto-Encoding Variational Bayes｜arXiv](https://arxiv.org/abs/1312.6114)
  - Kingma・WellingによるVAEの原論文です。再パラメータ化と変分下限を使う学習法を提案しています。
- [Generative Adversarial Nets｜NeurIPS](https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html)
  - GoodfellowらによるGANの原論文です。GeneratorとDiscriminatorを競わせる敵対的学習を提案しています。

{% include gk_article_footer.html %}
