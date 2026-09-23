---
layout: page
title: Attention（注意機構）とは？Query・Key・Valueを整理【G検定】
description: "Attention（注意機構）を、QueryとKeyの対応から重みを計算し、Valueを重み付きで集約する仕組みとして整理します。Self-Attention、マスク、RNNとの関係、Transformerの中核技術という位置付けを確認し、「常に系列全体を見る」という誤解を防ぎます。"
permalink: /gk/attention/
tags: [gk, neural_network, attention]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 9
last_modified_at: 2026-09-23
---

## まず結論

**Attention（注意機構）**は、入力の中から**どの情報をどれくらい参照するかを重み付けする仕組み**です。

G検定では、

- Query（Q）
- Key（K）
- Value（V）
- Self-Attention

を押さえます。

AttentionはRNNそのものではなく、RNNと組み合わせることも、TransformerのようにAttentionを中心に構成することもできます。

## 直感的な説明

文章を読んで質問に答えるとき、すべての単語を同じ重要度では見ません。

たとえば、

> 「昨日買った赤い車はどこにある？」

という文で「何の色？」と聞かれれば、「赤い」に強く注目します。

Attentionは、この**注目度を数値の重みとして計算する**イメージです。

## 定義・仕組み

### Query / Key / Value

Attentionでは、代表的に次の3つを使います。

- **Query**：何を探しているか
- **Key**：各情報が何を表しているか
- **Value**：実際に取り出す情報

QueryとKeyの対応から重みを計算し、その重みに応じてValueを集約します。

> **QとKで「どこを見るか」を決め、Vから情報を集める**

と覚えると分かりやすいです。

### Self-Attention

Self-Attentionでは、Q・K・Vを**同じ入力系列**から作ります。

これにより、系列中の要素同士の関係を扱えます。

Self-Attentionは[Transformer](/gk/transformer/)の中核技術です。

### 参照範囲はマスクに依存する

Attentionだからといって、必ず系列全体を自由に参照するわけではありません。

たとえばGPT系では、未来のトークンを参照しないように**Causal Mask**を使います。

一方、BERT系のEncoderでは、基本的に左右の文脈を利用します。

## いつ使う？（得意・不得意）

Attentionは、

- 機械翻訳
- 文章理解
- 文章生成
- 画像認識
- マルチモーダル

など幅広く使われます。

長距離の関係を直接参照しやすい一方、標準的なSelf-Attentionでは系列長が大きくなると計算量・メモリ使用量が増えやすくなります。

## G検定ひっかけポイント

### Attention＝RNN？

❌ AttentionはRNNの一種  
⭕ **RNNと組み合わせることもできる独立した仕組み**

### Attention＝必ず全情報を見る？

❌ 常に未来を含む系列全体を参照する  
⭕ **マスクによって参照できる範囲を制限できる**

### Q / K / V

- Q → 何を探すか
- K → 何を持っているか
- V → 実際に取り出す情報

### Self-Attention

❌ 別の系列だけを参照する仕組み  
⭕ **同じ系列内の要素同士の関係を扱う**

## まとめ（試験直前用）

- Attention＝**情報への注目度を重み付け**
- QとKから重みを計算
- Vを重み付きで集約
- Self-Attention＝同じ系列内の関係
- Transformerの中核技術
- **参照範囲はマスク・構造に依存する**

{% include gk_article_footer.html %}
