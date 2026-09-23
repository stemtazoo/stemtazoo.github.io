---
layout: page
title: TransformerのEncoder・Decoderとは？BERT・GPTとの関係【G検定】
description: "TransformerのEncoder・Decoderを、入力から文脈表現を作るEncoder、過去の出力などを条件に系列を生成するDecoderとして整理します。BERTはEncoder系、GPTはDecoder型という代表的関係と、Encoder＝理解専用・Decoder＝生成専用と決めつけない判断軸を確認します。"
permalink: /gk/transformer-architecture/
tags: [gk, transformer, attention]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 2
last_modified_at: 2026-09-23
---

## まず結論

Transformerの基本構造では、**Encoder**と**Decoder**が異なる役割を持ちます。

- **Encoder**：入力系列から文脈を含む表現を作る
- **Decoder**：これまでの出力などを条件に次の出力を作る

G検定では、代表例として、

- BERT → Encoder系
- GPT → Decoder型
- 原典の機械翻訳Transformer → Encoder + Decoder

を切り分けます。

## 直感的な説明

機械翻訳を例にすると、

- Encoder → 翻訳元の文章を表現に変換する
- Decoder → その表現と、これまでに生成した語を使って翻訳文を作る

という役割です。

「読む＝Encoder、書く＝Decoder」という覚え方は入口として便利ですが、**Encoderは理解専用、Decoderは生成以外に使えない**と絶対視しないようにします。

## 定義・仕組み

### Encoder

Encoderでは、主に、

- Self-Attention
- Feed Forward Network
- 残差接続
- Layer Normalization

などを使って入力系列を文脈化します。

BERTは代表的なEncoder系モデルです。

### Decoder

原典TransformerのDecoderでは、

- 未来を見ないMasked Self-Attention
- Encoder出力を参照するAttention
- Feed Forward Network

などを使って出力系列を生成します。

GPT系は、EncoderとのCross-Attentionを持たない**Decoder-only Transformer**として考えるのが基本です。

### マスクの役割

文章生成では、まだ生成していない未来のトークンを答えとして見てしまわないようにします。

そのためDecoder型の自己回帰モデルでは、未来側を隠す**Causal Mask**が重要です。

## いつ使う？（得意・不得意）

代表的な整理は次のとおりです。

| 構成 | 代表例 | 典型的な用途 |
|---|---|---|
| Encoder-only | BERT | 分類、抽出、文脈表現 |
| Decoder-only | GPT | 自己回帰生成 |
| Encoder-Decoder | 原典Transformer、T5系など | 翻訳、入力から出力系列を作るタスク |

これは代表的な傾向であり、**用途を完全に固定する分類ではありません。**

## G検定ひっかけポイント

### Encoder＝生成できない？

❌ Encoderは生成に一切使えない  
⭕ **Encoderは主に表現を作り、生成システムの一部として使われることもある**

### Decoder＝必ずEncoderを見る？

❌ Decoderは常にEncoder出力を参照する  
⭕ **GPTのようなDecoder-onlyモデルもある**

### Decoder＝双方向？

❌ 自己回帰生成で未来のトークンも参照する  
⭕ **Causal Maskで未来側を見ないようにする**

### BERT / GPT

- BERT → Encoder系
- GPT → Decoder型

ただし、これは**代表的な構造の違い**として覚えます。

## まとめ（試験直前用）

- Encoder＝**入力から文脈表現を作る**
- Decoder＝**条件に基づいて出力系列を作る**
- BERT＝Encoder系
- GPT＝Decoder-only系
- 原典Transformer＝Encoder + Decoder
- Decoder-onlyではEncoderは不要
- 自己回帰生成ではCausal Maskに注意

{% include gk_article_footer.html %}
