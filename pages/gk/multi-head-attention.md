---
layout: page
title: Multi-Head Attentionとは？複数の射影でAttentionを並列計算【G検定】
description: "Multi-Head Attentionを、Query・Key・Valueを複数の表現部分空間へ線形射影し、それぞれでAttentionを並列計算して結合する仕組みとして整理します。各ヘッドが必ず特定の文法役割を学ぶとは限らない点も含め、Single-Headとの違いを確認します。"
permalink: /gk/multi-head-attention/
tags: [gk, attention, transformer]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 4
last_modified_at: 2026-09-24
---

## まず結論

**Multi-Head Attention**は、Query・Key・Valueを複数の表現部分空間へ射影し、**複数のAttentionを並列に計算して、その結果を結合する仕組み**です。

G検定では、

- 複数head
- Q / K / V
- 異なる線形射影
- concat

を押さえます。

## 直感的な説明

1つのAttentionだけで表現するのではなく、複数の小さなAttentionを同時に計算し、その結果をまとめます。

「複数の視点」と説明されることがありますが、

> あるheadは必ず主語、別のheadは必ず目的語

のように、**各headの意味的役割が事前に決まっているわけではありません。**

## 定義・仕組み

代表的な流れは次の通りです。

1. Q・K・Vをheadごとに異なる線形変換へ射影
2. 各headでScaled Dot-Product Attentionを計算
3. headの出力をconcat
4. 最終線形変換を適用

原典Transformerでは、モデル全体の次元を複数headへ分割してAttentionを計算します。

そのため、

> head数を増やせば計算量やパラメータが単純にhead数倍になる

とは限りません。

## いつ使う？（得意・不得意）

Multi-Head AttentionはTransformerの主要構成要素です。

- Self-Attention
- Encoder-Decoder Attention
- Vision Transformerなど

で利用されます。

目的は単純な高速化ではなく、**複数の表現部分空間でAttentionを計算できるようにすること**です。

## G検定ひっかけポイント

### 各headの役割

❌ headごとに文法役割が固定されている  
⭕ **異なる射影空間でAttentionを学習する**

### head数

❌ 多いほど必ず高性能  
⭕ **適切なhead数はモデル設計・タスク依存**

### パラメータ削減

❌ Multi-Head Attentionの主目的  
⭕ **複数の表現部分空間で関係を捉えること**

## まとめ（試験直前用）

- Multi-Head＝**複数headでAttention**
- Q / K / Vをheadごとに射影
- 各headを並列計算
- 出力をconcat
- headの役割は固定されていない
- 多いほど必ず良いわけではない

## 参考資料

- [Attention Is All You Need｜arXiv](https://arxiv.org/abs/1706.03762)

{% include gk_article_footer.html %}
