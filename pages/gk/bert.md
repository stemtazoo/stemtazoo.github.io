---
layout: page
title: BERT（双方向Transformer）とは？G検定対策
description: BERTをTransformer Encoderを使う双方向の自然言語処理モデルとして整理します。MLM、NSP、文脈依存表現、GPTとの違い、G検定での見分け方を確認できます。
permalink: /gk/bert/
tags: [gk, nlp, transformer, attention]
gk_section: ディープラーニングの応用例/自然言語処理
gk_order: 1
last_modified_at: 2026-07-14
---

## まず結論

- **BERT（Bidirectional Encoder Representations from Transformers）**は、[Transformer](/gk/transformer/)の**Encoder**を使い、文の前後を同時に考慮する双方向の自然言語処理モデルです。
- G検定では「**双方向の意味理解はBERT、一方向の生成は[GPT](/gk/gpt/)**」と切り分けるのが最重要です。

## 直感的な説明
BERTは、文章を**左から右だけでなく、右から左も同時に読む**モデルです。

たとえば  
> 「私は **銀行** に行った」

という文で、「銀行」が  
- 川の銀行なのか  
- お金の銀行なのか  

を判断するには、**前後の文脈の両方**が必要です。  
BERTはこのように、**文全体を一度に見て単語の意味を決める**のが特徴です。

一方、文章を左から右へ順に生成する用途では[GPT](/gk/gpt/)系が代表的です。BERTは「次の単語をどんどん生成するモデル」というより、**文の意味を理解して分類・抽出・質問応答に使うモデル**と考えると覚えやすいです。

## 定義・仕組み
- BERTは [Transformer](/gk/transformer/) の Encoder 部分のみを使ったモデル
- 特徴は **双方向（Bidirectional）** に文脈を処理すること

BERTの事前学習では、主に次の2つのタスクを用いる。

### Masked Language Model（MLM）
- 文中の単語をランダムに隠し（[MASK]）、元の単語を当てる
- → **前後の文脈を使わないと解けない**

### Next Sentence Prediction（NSP）
- 2文を与え、「文Bは文Aの続きか？」を判定
- → 文同士の関係性を学習する

また、BERTの事前学習は  
**ラベルの付いていない大量のテキスト（自己教師あり学習）**で行われる。

## いつ使う？（得意・不得意）
### 得意
- 文書分類
- 質問応答
- 感情分析
- 文の意味理解が重要なタスク

### 不得意・注意点
- 文章生成（[GPT](/gk/gpt/)系のほうが得意）
- 計算量・メモリ消費が大きい
- リアルタイム処理には不向きな場合がある

## G検定ひっかけポイント
G検定では、次のような混同を狙ってくる。

### ❌ 一方向Transformer
- 「文章の冒頭から末尾にかけ、一方向にTransformerを適用」
→ **これはGPT系の説明**
→ **BERTは双方向なので誤り**

### ❌ 事前学習は教師あり学習
- 「ラベル付きデータで事前学習する」
→ **誤り**
→ BERTは **ラベルなしデータで事前学習**

### ⭕ 正しい判断基準

| キーワード | 判断 |
| --- | --- |
| 双方向、Encoder、MLM | BERT |
| 一方向、Decoder、文章生成 | [GPT](/gk/gpt/) |
| Attentionを使う基盤構造 | [Transformer](/gk/transformer/)全般 |
| 単語の固定的な分散表現 | [Word2Vec](/gk/word2vec/)など |

- **双方向** → BERT
- **Masked Language Model + NSP** → BERT
- **生成が得意** → GPT
- **Encoderのみ使用** → BERT

## まとめ（試験直前用）
- BERTは **双方向Transformer（Encoderのみ）**
- 文全体を同時に見て単語の意味を理解する
- 事前学習は **MLM と NSP**
- **一方向処理と書いてあったらBERTではない**
- 「意味理解特化」＝BERT と覚える

次に読むなら、基盤構造を確認する[Transformer](/gk/transformer/)と、生成向きの[GPT](/gk/gpt/)がおすすめです。

{% include gk_article_footer.html %}