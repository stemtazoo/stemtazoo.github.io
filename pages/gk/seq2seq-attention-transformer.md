---
layout: page
title: Seq2SeqからTransformerへの進化【Attention登場の理由】
permalink: /gk/seq2seq-attention-transformer/
tags: [gk, rnn, attention, transformer, nlp]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 7
---

## まず結論
- **Seq2Seq → Attention → Transformer** は、  
  **「長文が苦手」「並列処理できない」というRNNの限界を克服するための進化の流れ**である。
- G検定では **「何が問題で、何が解決されたか」** が問われる。

## 直感的な説明
- Seq2Seq：  
  👉「全文を一度丸暗記してから話す」
- Attention：  
  👉「話すときに、必要な部分を見返しながら話す」
- Transformer：  
  👉「最初から全部を見渡し、同時に処理する」

つまり  
**記憶頼り → 参照可能 → 並列処理** への進化。

## 定義・仕組み
### Seq2Seq（RNNエンコーダ・デコーダ）
- 入力系列を **1つの固定長ベクトル** に圧縮
- 長文になるほど情報が欠落
- 処理は **時系列順（並列不可）**

### Attention
- デコーダが **入力系列の各部分を重み付きで参照**
- 長文でも重要部分を使える
- ただし **RNN構造自体は残る**

### Transformer
- RNNを完全に廃止
- **Self-Attentionのみ**で系列を処理
- 全トークンを **並列処理** 可能
- 長距離依存関係に強い

## いつ使う？（得意・不得意）
**Seq2Seq**
- 短文の翻訳
- 小規模タスク

**Attention付きSeq2Seq**
- 長文翻訳
- 音声認識・要約

**Transformer**
- 大規模言語モデル（BERT, GPT）
- 高速学習・高精度が必要な場面

## G検定ひっかけポイント
- ❌「Seq2SeqはAttentionを前提としている」
- ❌「TransformerはSeq2Seqの一種」
- ❌「Attention = Transformer」

👉 **Attentionは仕組み**  
👉 **Transformerはモデル構造**

### 判断基準
- 固定長ベクトル → Seq2Seq
- 重み付き参照 → Attention
- RNNなし・並列処理 → Transformer

## まとめ（試験直前用）
- Seq2Seq：RNNで系列→系列
- 問題：長文に弱い・並列不可
- Attention：必要部分を参照
- Transformer：RNNを捨てて完全並列
- 「何を解決したか」を見る
