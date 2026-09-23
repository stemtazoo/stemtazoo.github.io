---
layout: page
title: Transformerとは？Self-AttentionとBERT・GPTの関係【G検定対策】
description: "Transformerを、RNNの再帰処理を使わずAttentionを中心に系列を扱うニューラルネットワークとして整理します。Self-Attention、位置情報、Encoder / Decoder、マスク、学習時の並列化を押さえ、BERT・GPTとの関係をG検定向けに切り分けます。"
permalink: /gk/transformer/
tags: [gk, neural_network, transformer, attention]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 1
last_modified_at: 2026-09-23
---

## まず結論

**Transformer**は、RNNのような再帰処理を使わず、**Attentionを中心に系列中の要素同士の関係を扱うニューラルネットワーク構造**です。

G検定では次を押さえます。

- 中核は **Self-Attention**
- RNNのように1時刻ずつ隠れ状態を渡さない
- 系列の順番は **位置情報**で補う
- Encoder / Decoder の組合せがある
- BERTやGPTの土台になっている

特に、**Transformer＝必ず文章生成モデル**ではありません。

## 直感的な説明

RNNは、文章を前から順に読みながら情報を受け渡すイメージです。

Transformerは、各トークンが他のトークンとの関係をAttentionで計算し、

> **どの情報をどれくらい参照するか**

を直接決めます。

ただし、「いつでも未来の単語まで全部見られる」わけではありません。

GPTのような自己回帰モデルでは、**未来側を見ないようにマスク**します。

## 定義・仕組み

### Self-Attention

Self-Attentionでは、同じ系列から Query・Key・Value を作り、要素同士の関連度を計算します。

詳しくは[Attention](/gk/attention/)で整理しています。

### 位置情報

Attentionだけでは、入力の並び順そのものは自動では分かりません。

そのためTransformerでは、**Positional Encoding / Positional Embedding**などを使って位置情報を与えます。

### Encoder / Decoder

原論文のTransformerは、EncoderとDecoderを組み合わせた構造です。

- **Encoder**：入力系列から文脈表現を作る
- **Decoder**：これまでの出力やEncoder側の情報を使って出力系列を生成する

その後、

- BERT → Encoder中心
- GPT → Decoder型
- 翻訳モデル → Encoder + Decoder

のような派生が広く使われています。

詳しくは[Transformerの全体構造](/gk/transformer-architecture/)で確認できます。

### 並列計算

RNNでは、前の時刻の隠れ状態が次の計算に必要なため、系列方向の処理が直列になりやすくなります。

Transformerでは、**学習時に系列中の複数位置をまとめて計算しやすい**ことが大きな利点です。

ただし、GPTのように次トークンを1つずつ生成する**自己回帰推論では、出力生成そのものは逐次的**です。

## いつ使う？（得意・不得意）

Transformer系は、

- 自然言語処理
- 画像
- 音声
- マルチモーダル

など幅広い分野で使われています。

注意点は、標準的なSelf-Attentionでは系列長が伸びると計算量・メモリ使用量が大きくなりやすいことです。

そのため、長い系列を効率よく扱うためのさまざまな改良もあります。

## G検定ひっかけポイント

### Transformer＝RNN？

❌ RNNの一種  
⭕ **再帰処理を使わずAttentionを中心に構成する**

### Attentionなら未来も見える？

❌ 常に系列全体を無制限に参照する  
⭕ **参照範囲はマスクや構造に依存する**

GPT系では未来側をマスクします。

### Transformer＝常に並列？

❌ 生成時も全トークンを一度に出せる  
⭕ **学習時は並列化しやすいが、自己回帰生成は逐次的**

### Transformer＝GPT？

❌ Transformerという1つの言語モデルがGPT  
⭕ **Transformerは構造、GPTはその構造を使う代表的モデル系列**

## まとめ（試験直前用）

- Transformer＝**Attention中心のニューラルネットワーク構造**
- RNNの再帰処理を使わない
- Self-Attentionで要素間の関係を扱う
- 位置情報を別途与える
- BERT＝Encoder系、GPT＝Decoder系
- **学習時の並列化と自己回帰生成時の逐次処理を混同しない**

## 参考資料

- [Attention Is All You Need｜arXiv](https://arxiv.org/abs/1706.03762)

{% include gk_article_footer.html %}
