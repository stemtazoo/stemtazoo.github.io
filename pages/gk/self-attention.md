---
layout: page
title: Attention機構（Self-Attention）とは？【文脈理解の仕組み｜G検定対策】
permalink: /gk/self-attention/
tags: [gk, attention, transformer]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 3
---

## まず結論
- **Attention機構（Self-Attention）**とは、文中の各単語が「他のどの単語をどれくらい重視すべきか」を計算する仕組みである。
- G検定では「**文脈を考慮できる理由**」として Self-Attention を説明できるかが問われる。

## 直感的な説明
Self-Attentionは、  
**文章を読むときに、関係の深い単語同士を結びつける仕組み**です。

例：
> 「彼は**銀行**でお金を下ろした」

このとき  
- 「銀行」は  
  - 「彼」  
  - 「お金」  
と強く関係しています。

👉 Self-Attentionは  
**「銀行」という単語が、文中のどの単語を重視すべきか**  
を自動で計算します。

## 定義・仕組み
### Attentionの基本的な考え方
- 各単語について  
  - **どの単語を見るか**
  - **どれくらい重要か**
を重みとして計算する

### Self-Attentionの特徴
- 入力文の **単語同士でAttentionを計算**
- 自分自身（Self）を含めて全単語を見る
- 単語の距離に依存しない

👉 **長距離依存関係を捉えられる**

## いつ使う？（得意・不得意）
### 得意な点
- 文脈理解
- 長文処理
- 並列計算が可能
- 単語の関係性を直接捉えられる

### 注意点
- 計算量が大きい
- モデルが重くなりやすい

## G検定ひっかけポイント
ここが頻出 👇

### ❌ 単語を順番に処理する
- **誤り**
- それは RNN / LSTM

### ❌ 単語の出現回数を見る
- **誤り**
- それは BoW / TF-IDF

### ⭕ 正しい判断基準
- 「どの単語に注目するか」→ Attention
- 「文脈に応じて重みが変わる」→ Self-Attention
- 「Transformerの中核」→ Self-Attention

## Transformerとの関係
- Transformerは **Self-Attentionを中心に構成**
- BERTは Transformer Encoder を使用
- GPTは Transformer Decoder を使用

👉 **Self-AttentionがなければBERTは成り立たない**

## まとめ（試験直前用）
- Self-Attention＝単語間の重要度計算
- 文脈理解の中核技術
- 距離に依存しない
- 並列処理が可能
- RNNとは処理方式が違う
