---
layout: page
title: Embedding と ELMo・BERT の違いとは？G検定対策
permalink: /gk/embedding-vs-contextual-embedding/
tags: [gk, nlp, attention]
---

## まず結論

* **Embedding（Word2Vec など）**は単語ごとに1つの固定ベクトルを割り当てるのに対し、**ELMo や BERT**は文脈に応じてベクトルが変わる**文脈依存型Embedding**です。
* G検定では「**静的か文脈依存か**」「**同じ単語でも意味が変わるか**」が問われます。

## 直感的な説明

* 通常の Embedding は「**辞書の意味**」です。単語に1つの意味しかありません。
* ELMo や BERT は「**会話の中の意味**」です。同じ単語でも、前後の文で意味が変わります。
* 例：「**bank**」

  * Embedding：金融機関 or 川岸を区別できない
  * ELMo / BERT：文脈から意味を判断できる

## 定義・仕組み

* **Embedding（静的Embedding）**

  * Word2Vec / GloVe など
  * 単語ごとに1つのベクトル
  * 文脈を考慮しない

* **ELMo**

  * 双方向RNN（LSTM）を使用
  * 文全体の文脈を考慮して単語表現を生成

* **BERT**

  * Transformer（Attention）を使用
  * 双方向に文脈を考慮
  * より強力な文脈表現が可能

## いつ使う？（得意・不得意）

### 静的Embedding

* 得意：

  * 計算が軽い
  * 実装が簡単
* 不得意：

  * 多義語を区別できない

### 文脈依存Embedding（ELMo / BERT）

* 得意：

  * 多義語を区別できる
  * 高精度なNLPタスクに有効
* 不得意：

  * 計算コストが高い

## G検定ひっかけポイント

* **最大のひっかけ**

  * 「ELMo や BERT は単語ごとに1つのベクトルを持つ」→ ❌
* 正しい理解

  * 同じ単語でも文脈によってEmbeddingが変わる
* よくある混同

  * ELMo = Word2Vec の改良版 → ❌
  * BERT = 単なるEmbedding → ❌
* 選択肢で

  * 「文脈を考慮しない」→ 静的Embedding
  * 「文脈を考慮する」→ ELMo / BERT

## まとめ（試験直前用）

* Embedding：固定ベクトル（静的）
* ELMo / BERT：文脈依存ベクトル
* 多義語を扱えるのは文脈依存型
* 文脈という言葉が出たら要注意
