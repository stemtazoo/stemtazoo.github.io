---
layout: page
title: RNN Encoder-Decoder（Seq2Seq）とは？固定長ベクトルとAttention【G検定】
description: "RNN Encoder-Decoder（Seq2Seq）を、Encoderが入力系列を表現へ変換し、Decoderが出力系列を生成する系列変換モデルとして整理します。初期モデルの固定長ベクトルがボトルネックになり、Attentionで入力各位置を参照するようになった流れを確認します。"
permalink: /gk/rnn-encoder-decoder/
tags: [gk, rnn, nlp]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 7
last_modified_at: 2026-09-23
---

## まず結論

**RNN Encoder-Decoder（Seq2Seq）**は、

- Encoder：入力系列を読み取る
- Decoder：条件付けられた出力系列を生成する

という2つの系列モデルを組み合わせる構造です。

初期のSeq2Seqでは、入力系列を**固定次元のベクトル**へまとめてDecoderへ渡しました。

## 直感的な説明

機械翻訳なら、

> 日本語を最後まで読んで表現へまとめる → その表現から英語を1語ずつ生成する

イメージです。

入力と出力の長さが同じである必要はありません。

## 定義・仕組み

### Encoder

入力系列を順番に処理し、文脈を表す内部表現へ変換します。

### Decoder

Encoderの表現を条件として、出力系列を1ステップずつ生成します。

初期のRNN Encoder-Decoderでは、入力を**1つの固定長ベクトルへ圧縮**することがボトルネックになりました。

### Attentionへの発展

Attention付きEncoder-Decoderでは、Decoderが出力の各時刻で**Encoder側の複数の状態を重み付きで参照**できます。

そのため、すべてを1つの固定長ベクトルへ押し込む必要がなくなります。

## いつ使う？（得意・不得意）

代表例は、

- 機械翻訳
- 要約
- 音声認識
- 系列→系列変換

です。

初期RNN Seq2Seqでは長い系列や逐次計算が課題になり、AttentionやTransformerへ発展しました。

## G検定ひっかけポイント

### Seq2Seq＝Attention？

❌ Seq2Seqは必ずAttentionを使う  
⭕ **初期Seq2Seqは固定長表現で、Attentionは後から導入された拡張**

### Seq2Seq＝Transformer？

❌ RNN Encoder-Decoderの別名  
⭕ **Transformerも系列変換に使えるが、再帰を使わない別アーキテクチャ**

### Teacher Forcing

学習時に正解トークンを次のDecoder入力へ使う方法で、Seq2Seqの構造そのものとは別概念です。

## まとめ（試験直前用）

- Seq2Seq＝**系列→系列**
- EncoderとDecoder
- 初期型は固定長ベクトル
- Attentionで入力各位置を参照可能
- TransformerはRNNなしの別構造
- Teacher Forcingは学習時の工夫

## 参考資料

- [Learning Phrase Representations using RNN Encoder-Decoder｜arXiv](https://arxiv.org/abs/1406.1078)
- [Sequence to Sequence Learning with Neural Networks｜arXiv](https://arxiv.org/abs/1409.3215)

{% include gk_article_footer.html %}
