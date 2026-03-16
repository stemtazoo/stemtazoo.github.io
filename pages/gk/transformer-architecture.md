---
layout: page
title: Transformerの全体構造（Encoder / Decoder）とは？【BERT・GPTとの関係｜G検定対策】
permalink: /gk/transformer-architecture/
tags: [gk, transformer, attention]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 5
---

## まず結論
- **Transformer**は、Self-Attentionを中核としたニューラルネットワーク構造である。
- **Encoder**は「入力を理解する役割」、**Decoder**は「出力を生成する役割」を担う。
- G検定では「**EncoderかDecoderか**」を見抜けるかが最大のポイント。

## 直感的な説明
Transformerは、文章処理を  
**「読むパート」と「書くパート」**に分けた構造です。

- Encoder：  
  👉 文章を読んで、意味を理解する
- Decoder：  
  👉 理解した内容をもとに、文章を生成する

👉 **読む＝Encoder、書く＝Decoder**

## 定義・仕組み
### Transformerの基本構成
- Embedding層
- Self-Attention
- Feed Forward Network
- 残差接続＋正規化

これらを  
- **Encoderブロック**
- **Decoderブロック**  
として積み重ねる。

---

### Encoder
- 入力文全体を同時に処理
- 双方向に文脈を考慮
- 出力は「文脈情報を含んだ表現」

👉 **意味理解が得意**

---

### Decoder
- これまでの出力をもとに次の単語を予測
- 一方向（未来は見ない）
- Encoderの出力を参照する場合もある

👉 **文章生成が得意**

## いつ使う？（得意・不得意）
### Encoder系が向く
- 文書分類
- 感情分析
- 質問応答（理解側）

### Decoder系が向く
- 文章生成
- 要約
- 対話システム

## G検定ひっかけポイント
ここが超重要 👇

### ❌ Encoderは文章を生成する
- **誤り**
- Encoderは理解専用

### ❌ Decoderは双方向に文脈を見る
- **誤り**
- Decoderは一方向

### ⭕ 正しい判断基準
- 「双方向」「理解」→ Encoder
- 「一方向」「生成」→ Decoder

## BERT・GPTとの関係
- **BERT**：Transformer **Encoderのみ**
- **GPT**：Transformer **Decoderのみ**
- **翻訳モデル**：Encoder + Decoder

👉 **どの部分を使うかがモデルの性格を決める**

## まとめ（試験直前用）
- TransformerはAttention中心構造
- Encoder＝理解（双方向）
- Decoder＝生成（一方向）
- BERT＝Encoderのみ
- GPT＝Decoderのみ
- 「理解か生成か」で切る
