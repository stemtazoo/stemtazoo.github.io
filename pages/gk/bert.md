---
layout: page
title: BERTとは？Transformer Encoder・MLM・双方向文脈【G検定対策】
description: "BERTを、Transformer Encoderを重ね、左右の文脈を利用して各トークンの表現を学ぶ事前学習モデルとして整理します。原版BERTのMLMとNSP、下流タスクへのFine-tuningを押さえ、自己回帰型のGPTとの違いを構造と学習目的から確認します。"
permalink: /gk/bert/
tags: [gk, nlp, transformer, attention]
gk_section: ディープラーニングの応用例/自然言語処理/Transformer・言語モデル
gk_order: 1
last_modified_at: 2026-09-23
---

## まず結論

**BERT（Bidirectional Encoder Representations from Transformers）**は、Transformer **Encoder**を使い、各位置の表現を**左右の文脈から作る**事前学習モデルです。

G検定では、

- Transformer Encoder
- Masked Language Model（MLM）
- 双方向の文脈
- 事前学習→下流タスクへ適応

を押さえます。

## 直感的な説明

たとえば「bank」という語が、

- I deposited money at the bank.
- We sat on the river bank.

に現れた場合、同じ単語でも周囲の文脈によって意味が違います。

BERTは文章中の前後関係を利用し、**その位置での文脈依存表現**を作ります。

## 定義・仕組み

### Transformer Encoder

BERTはTransformer Encoderを積み重ねた構造です。

自己回帰生成モデルのように未来側を常に隠すのではなく、基本的に左右の文脈を利用します。

### Masked Language Model（MLM）

入力中の一部のトークンを予測対象にし、前後の文脈から元のトークンを予測します。

詳しくは[MLM](/gk/mlm/)で整理しています。

### Next Sentence Prediction（NSP）

**原版BERT**では、MLMに加えてNSPも事前学習に使われました。

ただし、後続のBERT系モデルではNSPを使わない設計もあるため、

> BERT系モデルは必ずNSPを使う

とは覚えません。

## いつ使う？（得意・不得意）

BERT系は代表的に、

- 文書分類
- 固有表現抽出
- 質問応答
- 文脈表現の取得

などに利用されます。

BERTを「理解専用」と絶対視するより、**Encoder型・MLM・文脈依存表現**という構造と学習目的で判断するのが安全です。

## G検定ひっかけポイント

### BERT＝次トークン予測？

❌ 左から右へ次の語を順番に予測するのが基本  
⭕ **原版BERTの代表的事前学習はMLM**

### BERT＝NSP必須？

❌ BERT系ならすべてNSPを使う  
⭕ **原版BERTでは使用。後続モデルでは使わない例もある**

### BERT＝固定単語Embedding？

❌ 同じ単語は常に同じ最終表現  
⭕ **文脈に応じて各位置の表現が変わる**

## まとめ（試験直前用）

- BERT＝**Transformer Encoder**
- 左右の文脈を利用
- MLMが代表的事前学習
- 原版BERTではNSPも使用
- 文脈依存表現
- GPTとは**構造と学習目的**で切る

## 参考資料

- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding｜arXiv](https://arxiv.org/abs/1810.04805)

{% include gk_article_footer.html %}
