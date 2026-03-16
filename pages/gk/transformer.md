---
layout: page
title: Transformer（概要）
permalink: /gk/transformer/
tags: [gk, neural_network, transformer]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 1
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

RNNのように

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

---

## まとめ（試験直前用）

* Transformerは **RNN不要の系列モデル**
* Self-Attentionが中心
* 並列化・長期依存に強い

👉 次は **Embedding / Word2Vec** を整理するとNLPが完成します。
