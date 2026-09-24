---
layout: page
title: Attention・Transformer・BERTの関係とは？【G検定対策】
description: "Attention・Transformer・BERTを、Attentionは入力要素間の重み付き参照を行う仕組み、TransformerはAttentionを主要構成要素とするアーキテクチャ、BERTはTransformer Encoderを用いた具体的な事前学習モデルとして整理します。単純な包含関係として覚えない判断軸を確認します。"
permalink: /gk/attention-transformer-bert/
tags: [gk, neural_network, attention, transformer]
gk_section: ディープラーニングの応用例/自然言語処理
gk_order: 22
last_modified_at: 2026-09-24
---

## まず結論

3つは役割が違います。

- **Attention** → 情報を重み付きで参照する仕組み
- **Transformer** → Attentionを主要構成要素とするアーキテクチャ
- **BERT** → Transformer Encoderを使う具体的な事前学習モデル

G検定では、**仕組み・構造・モデル**で切ります。

## 直感的な説明

Attentionは「どの情報をどれだけ参照するか」を決める部品です。

Transformerは、そのAttentionを中心に、

- FFN
- 正規化
- 残差接続
- 位置情報

などを組み合わせたアーキテクチャです。

BERTはそのTransformer Encoderを使って作られた具体的なモデルです。

## 定義・仕組み

### Attention

RNNなどTransformer以外の構造でも利用できます。

### Transformer

Self-Attentionを中心に系列要素間の関係を扱います。

### BERT

原版BERTはTransformer Encoderを積み重ね、MLMなどで事前学習します。

したがって、

> Attention ⊂ Transformer ⊂ BERT

という集合の包含関係として覚えるのは不正確です。

## いつ使う？（得意・不得意）

問題文で、

- 重み付き参照 → Attention
- Encoder / Decoder・Self-Attention中心の構造 → Transformer
- MLM・双方向文脈・Encoder型 → BERT

を見ます。

## G検定ひっかけポイント

### Attention＝モデル？

❌ 必ず単独モデル名  
⭕ **仕組み・構成要素**

### Transformer＝BERT？

❌ 同義  
⭕ **Transformerはアーキテクチャ、BERTは具体モデル**

### BERT＝Attentionだけ？

❌ Attentionのみで構成  
⭕ **FFN・残差接続・正規化なども含む**

## まとめ（試験直前用）

- Attention＝**仕組み**
- Transformer＝**アーキテクチャ**
- BERT＝**具体モデル**
- AttentionはTransformer以外でも利用可能
- 単純な包含関係で覚えない
- **役割の粒度で切る**

{% include gk_article_footer.html %}
