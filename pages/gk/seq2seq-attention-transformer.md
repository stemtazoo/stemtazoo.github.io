---
layout: page
title: Seq2Seq・Attention・Transformerの違い｜何を解決した？【G検定】
description: "RNN型Seq2Seq、Attention、Transformerを、固定長ベクトルのボトルネック、入力系列への動的参照、再帰を使わないAttention中心の構造という流れで比較します。「Transformer＝Self-Attentionだけ」「生成時も完全並列」という誤解を避けて整理します。"
permalink: /gk/seq2seq-attention-transformer/
tags: [gk, rnn, attention, transformer, nlp]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 10
last_modified_at: 2026-09-23
---

## まず結論

Seq2Seq・Attention・Transformerは、次のように整理します。

- **初期RNN Seq2Seq**：入力を固定長表現へまとめる
- **Attention付きSeq2Seq**：必要な入力位置を動的に参照
- **Transformer**：再帰を使わずAttentionを中心に系列を処理

G検定では、**何を改善したか**を見るのが重要です。

## 直感的な説明

### 初期Seq2Seq

全文を1つのメモへまとめてから出力するイメージです。

### Attention

出力するときに、元の入力の必要な箇所を見返します。

### Transformer

RNNで前から順に隠れ状態を渡す代わりに、Attentionで要素間の関係を直接計算します。

## 定義・仕組み

### 初期RNN Seq2Seq

Encoderが入力系列を固定次元ベクトルへ変換し、Decoderがそのベクトルから出力を生成します。

長い入力ほど1つの固定長表現がボトルネックになりやすい点が問題でした。

### Attention

Decoderが出力時刻ごとに、Encoderの複数の状態へ異なる重みを付けて参照します。

これにより、入力全体を単一ベクトルだけで表す必要がなくなります。

### Transformer

Transformerは、RNNの再帰を使わず、

- Self-Attention
- Encoder-Decoder Attention（構成による）
- Feed Forward Network
- 位置情報

などで構成されます。

学習時には系列内の多くの位置をまとめて計算しやすい一方、GPTのような自己回帰生成では出力は通常1トークンずつ生成します。

## いつ使う？（得意・不得意）

このページでは性能順位ではなく、技術の役割を整理します。

- 固定長表現 → 初期Seq2Seqの制約
- 入力の各位置を参照 → Attention
- 再帰なし・Attention中心 → Transformer

## G検定ひっかけポイント

### Transformer＝Self-Attentionだけ？

❌ Self-Attentionしか使わない  
⭕ **FFNや位置情報、構成によってCross-Attentionなども使う**

### Transformer＝完全並列？

❌ 自己回帰生成時も全出力トークンを同時生成  
⭕ **学習時は並列化しやすいが、自己回帰生成は逐次的**

### Attention＝Transformer？

❌ 同義  
⭕ **Attentionは仕組み、Transformerはアーキテクチャ**

## まとめ（試験直前用）

- 初期Seq2Seq＝固定長ベクトル
- Attention＝必要な入力位置を重み付き参照
- Transformer＝再帰なし・Attention中心
- AttentionとTransformerは同義ではない
- TransformerにはFFN・位置情報などもある
- **学習時の並列化と生成時の逐次性を分ける**

## 参考資料

- [Neural Machine Translation by Jointly Learning to Align and Translate｜arXiv](https://arxiv.org/abs/1409.0473)
- [Attention Is All You Need｜arXiv](https://arxiv.org/abs/1706.03762)

{% include gk_article_footer.html %}
