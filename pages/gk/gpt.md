---
layout: page
title: GPTとは？自己回帰・次トークン予測とDecoder型Transformer【G検定】
description: "GPTを、過去側のトークンを条件に次トークンを予測する自己回帰型のTransformer系言語モデルとして整理します。因果マスク、生成的事前学習、BERTのMLMとの違いを押さえ、「生成専用」と絶対視せず構造と学習目的からG検定の選択肢を切ります。"
permalink: /gk/gpt/
tags: [gk, nlp, transformer, attention]
gk_section: ディープラーニングの応用例/自然言語処理/Transformer・言語モデル
gk_order: 4
last_modified_at: 2026-09-23
---

## まず結論

**GPT（Generative Pre-trained Transformer）**系の基本は、これまでのトークンを条件に**次のトークンを予測する自己回帰型のTransformer**です。

G検定では、

- Decoder型Transformer
- Causal Mask
- 自己回帰
- 次トークン予測

を押さえます。

## 直感的な説明

GPTは、

> ここまでの文章から、次に来そうなトークンを予測する

ことを繰り返します。

次トークンを予測するとき、まだ現れていない未来のトークンを答えとして見ないように**因果マスク**を使います。

## 定義・仕組み

### Decoder型Transformer

GPT系は、TransformerのDecoder型ブロックを基礎にした自己回帰モデルとして整理できます。

ただし原典TransformerのDecoderにあるEncoder側Cross-Attentionを必ず持つわけではなく、**Decoder-only型**として使われます。

### 生成的事前学習

初期GPTでは、大量のラベルなしテキストで言語モデルを事前学習し、その後タスク固有データへ適応する方法が示されました。

その後のGPT系では、promptingやfew-shot in-contextなど、重みを更新せずタスクへ対応する使い方も広がりました。

## いつ使う？（得意・不得意）

GPT系は代表的に、

- 文章生成
- 対話
- 要約
- 質問応答
- コード生成

などへ利用されます。

ただし、

> GPT＝生成しかできない

という理解は避けます。

自己回帰言語モデルでも、プロンプトによって分類・質問応答などさまざまなタスクを実行できます。

## G検定ひっかけポイント

### GPT＝MLM？

❌ 文中を隠して左右から当てる  
⭕ **基本は因果的な次トークン予測**

### GPT＝Encoder型？

❌ BERTと同じTransformer Encoder  
⭕ **代表的にはDecoder-only型**

### GPT＝文章生成専用？

❌ 生成以外のタスクに使えない  
⭕ **学習の基本は自己回帰生成だが、利用タスクは広い**

## まとめ（試験直前用）

- GPT＝**自己回帰型Transformer**
- Decoder-only型が基本
- Causal Mask
- 次トークン予測
- 文章生成が代表用途
- promptingで幅広いタスクへ利用可能
- BERTとは**MLM vs 次トークン予測**で切る

## 参考資料

- [Improving Language Understanding by Generative Pre-Training｜OpenAI](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- [Language Models are Few-Shot Learners｜OpenAI](https://openai.com/index/language-models-are-few-shot-learners/)

{% include gk_article_footer.html %}
