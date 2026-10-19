---
layout: page
title: TF-IDF・Word2Vec・BERTの使い分け｜特徴量の単位で比較【G検定】
description: "TF-IDFは文書ごとの語の重み、Word2Vecは語ごとの静的ベクトル、BERTは文中の位置ごとの文脈表現を得る手法として比較します。文書検索・単語類似度・文脈理解で必要な特徴量を選び、TF-IDFの重みの変化と文脈依存表現を区別します。"
permalink: /gk/tfidf-word2vec-bert/
tags: [gk, nlp, neural_network]
gk_section: ディープラーニングの応用例/自然言語処理/分散表現
gk_order: 9
last_modified_at: 2026-10-19
---

## まず結論

TF-IDF・Word2Vec・BERTは、**何を特徴量として取り出すか**で使い分けます。このページは、文書の頻度特徴・単語の静的ベクトル・文脈依存表現の選択マップです。

| 手法 | 主に得るもの | 選択肢の手掛かり |
| --- | --- | --- |
| TF-IDF | 文書ごとの語の重み | 頻度・珍しさ・文書検索 |
| Word2Vec | 語ごとに保存した密なベクトル | 類似語・静的な単語分散表現 |
| BERT | 入力文脈を反映した各位置の表現 | 前後関係・文脈理解 |

CBOW／Skip-gramの学習は[Word2Vec](/gk/word2vec/)、同じ語の文脈による変化は[Word2VecとBERTの比較](/gk/word2vec-vs-bert/)で確認できます。

## 直感的な説明

同じ文章でも、見たいものが異なります。

- 文書中で特徴的な語を探す → TF-IDF
- 単語どうしの類似性を扱う → Word2Vec
- 文中でその語がどの意味・役割かを扱う → BERT

どれが上位かという順位ではなく、**作ろうとしている特徴量の単位**を先に決めます。

## 定義・仕組み

| 比較軸 | TF-IDF | Word2Vec | BERT |
| --- | --- | --- | --- |
| 値を取り出す単位 | 文書と語の組 | 単語 | 文中のトークン位置 |
| 値・表現の作り方 | 文書内頻度と文書集合での珍しさ | 周辺語の予測から学習した単語ベクトル | 入力系列の前後関係を反映する表現 |
| 同じ語が別の文に出たら | 文書中の頻度などで重みが変わり得る | 学習済みの語ベクトルは基本的に同じ | 文脈によって内部表現が変わる |

TF-IDFも文書ごとに値が変わりますが、それだけでBERTのような文脈依存の意味表現とはいえません。**頻度による重みの変化と、周囲の語から計算する表現の変化を区別**します。

また、Word2Vecは単語ベクトルです。文書分類に使う場合は、語ベクトルを集約するなど、文書の特徴にする処理も考える必要があります。

## いつ使う？（得意・不得意）

| 必要なもの | 確認する手法 | 注意点 |
| --- | --- | --- |
| 軽量で語の寄与を確認しやすい文書特徴量 | [TF-IDF](/gk/tf-idf/) | 語順や語義を直接学ぶ仕組みではない |
| 単語類似度や軽量な静的Embedding | [Word2Vec](/gk/word2vec/) | 文脈ごとの多義語の表現は苦手 |
| 文脈を踏まえた分類・質問応答・抽出 | [BERT](/gk/bert/) | 計算資源や用途に応じた使い方を考える |

## G検定ひっかけポイント

- 「TF-IDFも値が変わるので文脈の意味を理解する」→ 頻度による重み付けとの違いを確認する。
- 「Word2Vecは文脈を一切使わない」→ 学習時には周辺語を使う。
- 「Word2Vecはそのままで文書ごとに1つのベクトルを返す」→ 基本は単語の表現。集約などの処理とは分ける。
- 「BERTなら常に最適」→ 目的、計算量、データに応じて選ぶ。

## まとめ（試験直前用）

- TF-IDF：**文書ごとの語の重み**
- Word2Vec：**語ごとの静的ベクトル**
- BERT：**文中の位置ごとの文脈表現**
- 新旧の順位ではなく、必要な特徴量の単位で選ぶ

## 参考資料（原論文）

- [Term-Weighting Approaches in Automatic Text Retrieval｜ScienceDirect](https://doi.org/10.1016/0306-4573(88)90021-0)
  - Salton・Buckley（1988）。TF-IDFを含む代表的なterm weightingを比較した一次資料です。
- [Efficient Estimation of Word Representations in Vector Space｜arXiv](https://arxiv.org/abs/1301.3781)
  - MikolovらによるWord2Vecの代表的な原論文です。
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding｜ACL Anthology](https://aclanthology.org/N19-1423/)
  - DevlinらによるBERTの原論文です。

{% include gk_article_footer.html %}
