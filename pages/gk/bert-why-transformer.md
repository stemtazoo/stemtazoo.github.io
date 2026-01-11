---
layout: page
title: BERTはなぜRNNではなくTransformerなのか？G検定対策
permalink: /gk/bert-why-transformer/
tags: [gk, attention, transformer]
gk_section: ディープラーニングの応用例/自然言語処理
gk_order: 18
---

## まず結論

* **BERTは、長距離の文脈依存を効率よく学習するために、RNNではなくTransformerを採用しています。**
* G検定では「**なぜRNNでは不十分なのか**」「**Transformerの利点は何か**」が問われます。

## 直感的な説明

* **RNN**は、単語を**左から順番に読む**モデルです。
* **Transformer**は、文全体を**一度に見渡す**モデルです。
* 長い文章になるほど、

  * RNN：前の情報が後ろに届きにくい
  * Transformer：どの単語同士の関係も一気に見られる
    という違いが出ます。

## 定義・仕組み

* **RNN系モデル**

  * 時系列に沿って順番に処理
  * BPTTによる学習が必要
  * 長文では勾配消失が起きやすい

* **Transformer**

  * Attention（自己注意機構）を使用
  * 単語間の関係を直接計算
  * 並列計算が可能

* **BERT**

  * Transformerエンコーダのみを使用
  * 双方向に文脈を考慮

## いつ使う？（得意・不得意）

### RNN

* 得意：

  * 短い時系列データ
* 不得意：

  * 長距離依存
  * 並列処理ができない

### Transformer（BERT）

* 得意：

  * 長文の理解
  * 文脈依存表現
* 不得意：

  * 計算量が大きい

## G検定ひっかけポイント

* **最大のひっかけ**

  * 「BERTはRNNを改良したモデルである」→ ❌
* 正しい理解

  * BERTはTransformerベース
* 選択肢で

  * 「順番に処理」→ RNN
  * 「Attentionで単語間関係を直接扱う」→ Transformer
* **文全体を一度に見る**がキーワード

## まとめ（試験直前用）

* RNNは順次処理、長距離が苦手
* TransformerはAttentionで一括処理
* BERTはTransformerエンコーダ
* 長文・文脈重視ならTransformer
