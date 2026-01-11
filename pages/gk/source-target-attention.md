---
layout: page
title: Source-Target Attention（Encoder-Decoder Attention）とは？G検定対策
permalink: /gk/source-target-attention/
tags: [gk, attention, transformer]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 2
---

## まず結論

* **Source-Target Attention**とは、**入力文（Source）と出力文（Target）が異なる系列であることを前提に、両者の対応関係を学習するAttention機構**。
* G検定では**「Self-Attentionとの違い」「Encoder-Decoder Attentionとの関係」**を正しく区別できるかが問われる。

## 直感的な説明

* 機械翻訳を考えると、

  * 入力：英語文（Source）
  * 出力：日本語文（Target）
    となります。
* Source-Target Attentionは、
  👉 **出力側の各単語が、入力文のどの単語を見るべきかを学習する仕組み**です。
* 人で言えば、
  👉 **翻訳するときに、元の文章を見返しながら単語を選ぶ**イメージです。

## 定義・仕組み

* Source-Target Attentionでは、

  * Query：Target 側のトークン
  * Key / Value：Source 側のトークン
    を用いてAttentionを計算します。

* 特徴：

  * 入力系列と出力系列は**異なってよい**
  * 翻訳・要約などで使用

* Transformerでは、
  👉 **Encoder-Decoder Attention** がこれに該当します。

## いつ使う？（得意・不得意）

### 得意な場面

* 機械翻訳
* 文書要約
* 質問応答（入力と出力が異なる系列）

### 注意点・不得意

* 入力と出力が同一系列の場合は不適切
* Self-Attentionとは用途が異なる

## G検定ひっかけポイント

* よくある誤解：

  * ❌ 「Self-Attentionと同じ」
  * ❌ 「入力と出力のトークン数が同じである必要がある」

* 正しい理解：

  * **Source と Target は別系列**
  * **対応関係を学習する**

* 判断基準：

  * 「入力と出力が別」→ Source-Target Attention
  * 「同一系列内の注意」→ Self-Attention

## まとめ（試験直前用）

* Source-Target Attention＝系列間Attention
* 入力（Source）と出力（Target）は別
* 翻訳・要約で使用
* TransformerではEncoder-Decoder Attention
* Self-Attentionとは別概念
