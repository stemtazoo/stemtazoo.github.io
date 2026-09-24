---
layout: page
title: BERTはなぜTransformer Encoderを使う？RNNとの違い【G検定】
description: "BERTがTransformer Encoderを用いる理由を、Self-Attentionで各位置間の関係を直接扱えること、系列方向の再帰を使わず学習時に並列化しやすいこと、左右の文脈を利用するMLMとの相性から整理します。RNNが長文を扱えないという絶対表現は避けます。"
permalink: /gk/bert-why-transformer/
tags: [gk, attention, transformer]
gk_section: ディープラーニングの応用例/自然言語処理/Transformer・言語モデル
gk_order: 3
last_modified_at: 2026-09-24
---

## まず結論

BERTは**Transformer Encoder**を使い、Self-Attentionによって各トークン位置の関係を直接扱います。

G検定では、

- 再帰なし
- Self-Attention
- 学習時に並列化しやすい
- 左右の文脈を利用

を押さえます。

## 直感的な説明

RNNは隠れ状態を時刻順に渡します。

Transformer Encoderは、系列内の各位置から他の位置へAttentionを計算します。

そのため、あるトークンが離れたトークンを参照するとき、RNNのように多数の再帰ステップを経由する必要がありません。

## 定義・仕組み

### RNN

前時刻の隠れ状態から次時刻を計算するため、系列方向に依存関係があります。

LSTMやGRUは長期依存を扱いやすくする工夫を持ちます。

したがって、

> RNNは長文を扱えない

とは言いません。

### Transformer Encoder

Self-Attentionにより、各位置間の関係を直接計算します。

学習時には系列内の多くの位置をまとめて計算しやすい一方、Attentionの計算量は系列長に応じて大きくなるという別の課題があります。

### BERT

原版BERTはTransformer Encoderを重ね、MLMなどで事前学習します。

MLMでは左右の文脈を利用してマスク位置を予測します。

## いつ使う？（得意・不得意）

BERT系は文脈表現、分類、抽出、質問応答などで利用されます。

RNNとTransformerは単純な優劣ではなく、計算資源・系列長・タスクによって使い分けます。

## G検定ひっかけポイント

### BERT＝RNN改良版？

❌ 再帰型ネットワーク  
⭕ **Transformer Encoderベース**

### Transformer＝完全に計算量が少ない？

❌ 系列が長くても常に軽量  
⭕ **並列化しやすいがAttention計算量は別論点**

### RNN＝長距離依存を一切扱えない？

❌ 不可能  
⭕ **難しさがあり、LSTM/GRUなどで改善されてきた**

## まとめ（試験直前用）

- BERT＝**Transformer Encoder**
- Self-Attention
- 再帰なし
- 学習時に並列化しやすい
- MLMで左右文脈を利用
- RNNとの比較は固定順位で覚えない

## 参考資料

- [BERT｜arXiv](https://arxiv.org/abs/1810.04805)
- [Attention Is All You Need｜arXiv](https://arxiv.org/abs/1706.03762)

{% include gk_article_footer.html %}
