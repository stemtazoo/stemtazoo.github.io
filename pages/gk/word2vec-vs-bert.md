---
layout: page
title: Word2VecとBERTの違いとは？静的表現と文脈表現【G検定対策】
description: "Word2VecとBERTを、同じ単語に基本的に同じベクトルを使う静的表現か、文脈に応じて表現が変わる文脈依存表現かで比較します。学習時に文脈を使うWord2Vecと、Transformerで前後関係を扱うBERTの違いをG検定向けに整理します。"
permalink: /gk/word2vec-vs-bert/
tags: [gk, nlp, transformer]
gk_section: ディープラーニングの応用例/自然言語処理/分散表現
gk_order: 8
last_modified_at: 2026-10-19
---

## まず結論

Word2VecとBERTの大きな違いは、**同じ単語のベクトルが文脈によって変わるか**です。

- **Word2Vec**：同じ単語には基本的に同じベクトル → 静的表現
- **BERT**：周囲の文脈に応じて表現が変わる → 文脈依存表現

G検定では、

> **固定ベクトル → Word2Vec**
>
> **文脈で変わる → BERT**

で切り分けます。

## 直感的な説明

英単語「bank」は、「銀行」と「川岸」の両方を意味します。

- I went to the bank to deposit money.（預金するために銀行へ行った）
- We sat on the river bank.（川岸に座った）

同じ語形でも、周囲の語によって意味が変わります。

Word2Vecでは、ある単語に対して学習後は基本的に1つの静的ベクトルを使います。

BERTでは、文全体の文脈を利用して、その位置の表現を変化させます。

## 定義・仕組み

### Word2Vec

[Word2Vec](/gk/word2vec/)は、CBOWやSkip-gramを使って、周囲の単語との関係から単語ベクトルを学びます。

重要なのは、

- **学習時には文脈を使う**
- しかし学習後の単語表現は**基本的に静的**

という点です。

したがって、

> 「Word2Vecは文脈を一切使わない」

という説明は不正確です。

### BERT

[BERT](/gk/bert/)はTransformer Encoderを使い、前後の情報を考慮して各位置の表現を作ります。

同じ単語でも、置かれた文によって内部表現が変わります。

そのため、文脈による語義の違いを扱いやすいのが特徴です。

### 静的Embeddingと文脈依存Embeddingの位置付け

| 表現 | 代表例 | 同じ単語の扱い |
| --- | --- | --- |
| 静的Embedding | Word2Vec、GloVe | 学習後は基本的に固定ベクトルを使う |
| 文脈依存Embedding | ELMo、BERT | 入力文脈に応じた表現を作る |

ELMoは双方向LSTMを使う文脈依存表現、BERTはTransformer Encoderを使う文脈依存表現です。**文脈依存なら必ずTransformer、とは限りません。** Word2Vec以外の静的表現は[Word2Vec・fastText・GloVeの比較](/gk/word2vec-fasttext-glove/)で確認できます。

## いつ使う？（得意・不得意）

### Word2Vecが向く場面

- 軽量な単語ベクトルがほしい
- 単語類似度を計算したい
- 静的な特徴量として利用したい

### BERTが向く場面

- 文書分類
- 質問応答
- 感情分析
- 文脈によって意味が変わる語を扱う

ただし、BERTの方が常に適しているわけではありません。計算量や用途によってWord2Vecの方が扱いやすい場合もあります。

## G検定ひっかけポイント

### Word2Vecは文脈を使わない

「学習時にも周辺語を使わない」という意味なら誤りです。

学習時には周辺語を使います。試験では、**最終的な表現が静的か文脈依存か**で判断する方が安全です。

### BERTは単語ごとに固定ベクトルを持つだけ

誤りです。

BERTでは、周囲の文脈を反映した表現を生成します。

### BERTなら必ず生成モデル

誤りです。

BERTは代表的には文脈理解・分類・抽出などで使われ、自己回帰生成を中心とするGPTとは役割が異なります。

**判断基準**

- 静的な単語ベクトル → Word2Vec
- 文脈によって表現が変わる → BERT
- 周囲→中心 / 中心→周囲 → Word2VecのCBOW / Skip-gram
- 双方向・MLM・Encoder → BERT

## まとめ（試験直前用）

- Word2Vec＝静的な単語表現
- BERT＝文脈依存の表現
- Word2Vecも学習時には周辺語を使う
- 同じ単語を文脈ごとに表現し分けるのはBERT側
- **固定か、文脈で変わるか**で切る

## 参考資料（原論文）

- [Efficient Estimation of Word Representations in Vector Space｜arXiv](https://arxiv.org/abs/1301.3781)
  - 周囲と中心語の予測から単語表現を学ぶWord2Vecの基本構造を確認できます。
- [Deep contextualized word representations｜arXiv](https://arxiv.org/abs/1802.05365)
  - 双方向言語モデルを使い、文脈に応じた表現を作るELMoの原論文です。
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding｜arXiv](https://arxiv.org/abs/1810.04805)
  - 前後の文脈を使うTransformerによる表現学習を確認できます。

{% include gk_article_footer.html %}
