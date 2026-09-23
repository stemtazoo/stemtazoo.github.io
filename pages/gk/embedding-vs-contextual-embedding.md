---
layout: page
title: 静的Embeddingと文脈依存Embeddingの違い｜Word2Vec・ELMo・BERT【G検定】
description: "静的Embeddingと文脈依存Embeddingを、学習後に単語ごとに固定ベクトルを使うWord2Vecなどと、文脈に応じて各位置の表現が変わるELMo・BERTで比較します。Word2Vecも学習時には周辺語を使うため、「文脈を使わない」と単純化しない判断軸を確認します。"
permalink: /gk/embedding-vs-contextual-embedding/
tags: [gk, nlp, attention]
gk_section: ディープラーニングの応用例/自然言語処理
gk_order: 17
last_modified_at: 2026-09-23
---

## まず結論

Embeddingの大きな違いは、**同じ単語の表現が文脈によって変わるか**です。

- **静的Embedding**：単語ごとに基本的に1つの固定ベクトル
- **文脈依存Embedding**：文章中の位置・前後関係によって表現が変わる

代表例は、

- Word2Vec / GloVe → 静的
- ELMo / BERT → 文脈依存

です。

## 直感的な説明

「bank」という単語は、

- 銀行
- 川岸

のように文脈で意味が変わります。

静的Embeddingでは、学習後は基本的に同じ単語へ同じベクトルを使います。

文脈依存Embeddingでは、**周囲の文章を見て、その位置の表現を変えます。**

## 定義・仕組み

### 静的Embedding

Word2Vecなどでは、周囲の単語との関係を使って単語ベクトルを学習します。

したがって、

> **Word2Vecは文脈を使わない**

という説明は不正確です。

正しくは、

- 学習時 → 周辺文脈を利用する
- 学習後 → 単語ごとの表現は基本的に固定

です。

### ELMo

ELMoは双方向LSTMを使い、文章中の文脈に応じた表現を作ります。

### BERT

BERTはTransformer Encoderを使い、各位置の表現を前後の文脈から作ります。

同じトークンでも文脈が違えば内部表現が変わります。

## いつ使う？（得意・不得意）

### 静的Embedding

- 軽量な単語ベクトルがほしい
- 単語類似度を扱いたい
- 文脈ごとの意味分けが不要

### 文脈依存Embedding

- 多義語を文脈で区別したい
- 文書分類・質問応答・抽出
- 文全体の意味関係を使いたい

ただし、文脈依存モデルの方が常に最適とは限りません。計算量・データ量・用途によって静的Embeddingが適する場合もあります。

## G検定ひっかけポイント

### Word2Vec＝文脈を使わない？

❌ 周辺語を一切利用しない  
⭕ **学習時には周辺語を使うが、学習後の表現は静的**

### BERT＝単語ごとに固定ベクトル？

❌ どの文章でも同じ表現  
⭕ **文脈に応じて各位置の表現が変わる**

### ELMo＝Transformer？

❌ Self-Attention中心  
⭕ **双方向LSTMを使う文脈依存表現**

## まとめ（試験直前用）

- Word2Vec / GloVe＝**静的Embedding**
- ELMo / BERT＝**文脈依存Embedding**
- Word2Vecも学習時には文脈を使う
- 判断軸は**最終表現が固定か、文脈で変わるか**
- 新しい手法ほど常に優れるわけではない

## 参考資料

- [Efficient Estimation of Word Representations in Vector Space｜arXiv](https://arxiv.org/abs/1301.3781)
- [Deep contextualized word representations｜arXiv](https://arxiv.org/abs/1802.05365)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding｜arXiv](https://arxiv.org/abs/1810.04805)

{% include gk_article_footer.html %}
