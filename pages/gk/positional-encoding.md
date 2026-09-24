---
layout: page
title: 位置エンコーディングとは？Transformerに順序情報を与える【G検定】
description: "位置エンコーディングを、Self-Attentionだけではトークン順序を区別できないTransformerへ位置情報を与える仕組みとして整理します。原典のsin/cos固定表現、学習可能な位置埋め込み、相対位置表現などを区別します。"
permalink: /gk/positional-encoding/
tags: [gk, attention, transformer]
gk_section: ディープラーニングの要素技術/トランスフォーマー (Transformer)
gk_order: 6
last_modified_at: 2026-09-24
---

## まず結論

**位置エンコーディング（Positional Encoding）**は、Transformerへ**トークンの順序・位置情報**を与える仕組みです。

重要なのは、

> Self-Attentionそのものには、入力順序を自動的に区別する仕組みがない

という点です。

## 直感的な説明

同じ単語集合でも、

- 犬が人を追う
- 人が犬を追う

では意味が変わります。

Attentionだけでは「何番目にあるか」を別途与える必要があるため、位置情報を追加します。

## 定義・仕組み

原典Transformerでは、sin/cosを使う固定Positional Encodingをトークン埋め込みへ加えました。

その後、

- 学習可能な位置Embedding
- 相対位置表現
- Rotary Position Embedding（RoPE）

など、さまざまな方法が使われています。

したがって、

> Transformerの位置情報＝必ずsin/cos

ではありません。

## いつ使う？（得意・不得意）

Transformer系で順序や相対位置を扱うために重要です。

RNNは再帰によって順序を構造的に持ちますが、Transformerでは位置情報を別の形で与えます。

## G検定ひっかけポイント

### Transformerは順序を一切扱えない？

❌ 順序情報を利用できない  
⭕ **位置情報を与えることで扱う**

### 位置情報＝必ずsin/cos？

❌ 全Transformerで固定  
⭕ **原典ではsin/cos。学習型や相対位置などもある**

## まとめ（試験直前用）

- 位置エンコーディング＝**順序・位置情報**
- Self-Attentionだけでは順序を区別できない
- 原典Transformerはsin/cos
- 学習可能・相対位置などもある
- **「順序を補う仕組み」で切る**

## 参考資料

- [Attention Is All You Need｜arXiv](https://arxiv.org/abs/1706.03762)

{% include gk_article_footer.html %}
