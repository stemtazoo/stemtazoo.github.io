---
layout: page
title: Transformer（概要）
description: "Transformer（概要）について、G検定で問われる自然言語処理・系列データ分野の観点から、系列データを扱う仕組み、学習目的、代表モデルとの関係を整理します。暗記だけでなく、似た概念との混同を避ける見分け方や、選択肢を切るためのポイントも確認します。"
permalink: /gk/transformer/
tags: [gk, neural_network, transformer]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 1
last_modified_at: 2026-07-14
---

## まず結論

* **TransformerはRNNを使わない系列モデル**
* **Self-Attentionを中心に構成** されている
* **並列計算が可能** で、長期依存関係に強い

---

## 直感的な説明

Transformerは、

> 「順番に読むのではなく、全体を一気に見て関係を判断する」

モデルです。

[RNN](/gk/rnn/)のように

* 前から順に処理する

のではなく、
**系列全体を同時に処理** します。

---

## 定義・仕組み

### Transformerの基本構成

Transformerは主に次の要素で構成されます。

* **Self-Attention**
* **Feed Forward Network（全結合層）**
* **残差接続（Skip Connection）**
* **Layer Normalization**

これらをブロックとして積み重ねます。

---

### Encoder / Decoder（概要）

* **Encoder**：入力系列を理解・特徴抽出
* **Decoder**：出力系列を生成

機械翻訳などでは、

* Encoder：入力文（翻訳元）
* Decoder：出力文（翻訳先）

という役割分担になります。

この構造をもとに、Encoder側を中心に使う代表例が[BERT](/gk/bert/)、Decoder側の考え方を使う代表例が[GPT](/gk/gpt/)です。

---

### なぜRNNを使わない？

* 時系列処理による **計算の直列化** を避けたい
* 長期依存関係を直接捉えたい

Self-Attentionにより、
**遠く離れた要素同士も直接関連付け** できます。

---

## いつ使う？（得意・不得意）

### 得意なこと

* 機械翻訳・文章理解
* 長距離依存関係のあるタスク
* GPUによる高速学習

### 注意点

* 計算量・メモリ使用量が大きい
* 非常に長い系列では工夫が必要

---

## G検定ひっかけポイント

* ❌「TransformerはRNNの一種」→ **誤り**
* ❌「Attentionは補助的要素」→ **誤り**
* ✅ Transformerの中核は **Self-Attention**
* ✅ 並列計算が可能
* ✅ [BERT](/gk/bert/)はEncoder側、[GPT](/gk/gpt/)はDecoder側の特徴で見分ける

---

## まとめ（試験直前用）

* Transformerは **RNN不要の系列モデル**
* Self-Attentionが中心
* 並列化・長期依存に強い

次は、意味理解に強い[BERT](/gk/bert/)、文章生成に強い[GPT](/gk/gpt/)、単語の分散表現を学ぶ[Word2Vec](/gk/word2vec/)を確認すると、NLP分野のつながりが見えやすくなります。

{% include gk_article_footer.html %}