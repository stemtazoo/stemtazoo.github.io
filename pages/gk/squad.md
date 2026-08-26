---
layout: page
title: SQuADとは？抽出型質問応答データセット【G検定対策】
description: "SQuAD（Stanford Question Answering Dataset）を、文章・質問・答えのスパンからなる抽出型質問応答データセットとして整理します。GLUEとの違い、画像データセットではない点、BERTなどの評価で使われる理由をG検定向けに確認します。"
permalink: /gk/squad/
tags: [gk, nlp, dataset]
gk_section: ディープラーニングの応用例/自然言語処理/タスク・評価
gk_order: 3
last_modified_at: 2026-08-26
---

## まず結論

**SQuAD（Stanford Question Answering Dataset）**は、文章を読んで質問に答える**抽出型質問応答（Extractive QA）**の代表的なデータセットです。

G検定では、

```text
文章 + 質問 + 文章中の答え
→ SQuAD
```

と切り分けます。

## 直感的な説明

SQuADは、人が文章を読んで

> 「この質問の答えは、本文のこの部分」

と探す問題をモデルに解かせるイメージです。

画像分類用データセットではありません。

## 定義・仕組み

SQuADでは、基本的に次の情報を扱います。

- Context：答えを含む文章
- Question：その文章についての質問
- Answer：文章中の答えとなる範囲（span）

そのため、代表的な課題は**文章中の開始位置と終了位置を見つける抽出型QA**です。

SQuAD 2.0では、答えが本文中に存在しない質問も追加されています。

## いつ使う？（得意・不得意）

SQuADは、質問応答モデルの学習・評価で使われます。

BERTなどのTransformer系モデルでも広く使われてきましたが、SQuAD自体がBERT専用という意味ではありません。

また、過去にはRNN・Attentionなどを使ったモデルでも取り組まれており、**「CNNは使わない」など特定のモデル構造で限定するのは不適切**です。

## G検定ひっかけポイント

### SQuADとGLUE

- SQuAD → 質問応答データセット
- GLUE → 複数の自然言語理解タスクをまとめた評価ベンチマーク

### SQuADは画像データセット？

違います。NLPの文章・質問応答データセットです。

### SQuADは分類専用？

代表的には、本文から答えの位置を抽出する**抽出型QA**です。

## まとめ（試験直前用）

- SQuAD＝NLPの質問応答データセット
- Context・Question・Answerを扱う
- 代表タスクは抽出型QA
- SQuAD 2.0には回答不能な質問もある
- GLUEは複数タスクの評価ベンチマーク

{% include gk_article_footer.html %}
