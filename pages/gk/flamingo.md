---
layout: page
title: Flamingoとは？画像・テキストをFew-shotで扱うマルチモーダルモデル【G検定】
description: "Flamingoを、画像とテキストが混在する入力を扱い、少数の例を文脈として与えるfew-shot in-context対応に強みを持つマルチモーダルモデルとして整理します。Perceiver Resampler、Gated Cross-Attention、凍結済み視覚エンコーダと言語モデルの接続を確認します。"
permalink: /gk/flamingo/
tags: [gk, multimodal, attention]
gk_section: ディープラーニングの応用例/マルチモーダル/汎用マルチモーダルモデル
gk_order: 1
last_modified_at: 2026-09-23
---

## まず結論

**Flamingo**は、画像とテキストが混在する入力を扱い、**少数の例をプロンプト内の文脈として与えて新しいタスクへ対応するfew-shot in-context能力**を重視したマルチモーダルモデルです。

G検定では、

- 画像＋テキスト
- Few-shot in-context
- Perceiver Resampler
- Cross-Attention

を押さえます。

## 直感的な説明

Flamingoでは、たとえば、

> 画像A → 回答A  
> 画像B → 回答B  
> 画像C → ？

のように、少数の画像・テキスト例を文脈として与え、新しい画像について応答させることができます。

ここでいうFew-shotは、**その場で重みを再学習することではなく、少数例を入力文脈へ含めて対応する**という意味で捉えるのが重要です。

## 定義・仕組み

原論文のFlamingoは、事前学習済みの視覚モデルと言語モデルを活用し、その間を接続する構造を追加します。

### Perceiver Resampler

可変数の画像特徴を、言語モデルへ渡しやすい固定数の視覚トークンへ変換します。

### Gated Cross-Attention

言語モデル側から視覚情報を参照できるようにするCross-Attention層を挿入します。

これにより、画像・テキストが交互に現れる**interleaved input**を扱えます。

## いつ使う？（得意・不得意）

Flamingoは、

- 画像質問応答
- 画像説明
- 少数例からのタスク適応
- 複数画像と文章が混在する対話

などに向きます。

ただし、

> Flamingo＝Few-shot学習アルゴリズム

ではありません。

モデルの重みを数例だけで更新する手法そのものではなく、**few-shot in-contextで使えるマルチモーダルモデル**です。

## G検定ひっかけポイント

### Few-shot

❌ 数例で必ずモデル重みを更新する  
⭕ **少数例を入力文脈として与える**

### Flamingo＝CLIP？

❌ 画像とテキストの類似度計算が中心  
⭕ **画像・テキストを条件に文章応答を生成できる**

### Flamingo＝音声モデル？

❌ ASR専用  
⭕ **画像・テキストを中心とするマルチモーダルモデル**

## まとめ（試験直前用）

- Flamingo＝**画像＋テキスト**
- few-shot in-context
- Perceiver Resampler
- Gated Cross-Attention
- interleaved image-text input
- **Few-shot＝重み更新とは限らない**

## 参考資料

- [Flamingo: a Visual Language Model for Few-Shot Learning｜arXiv](https://arxiv.org/abs/2204.14198)

{% include gk_article_footer.html %}
