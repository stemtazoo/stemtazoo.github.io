---
layout: page
title: Vision Transformer（ViT）とは？画像パッチとCNNの違い【G検定】
description: "Vision Transformer（ViT）を、画像を固定サイズのパッチへ分割し、トークン列としてTransformer Encoderへ入力する画像認識モデルとして整理します。Patch Embedding、位置埋め込み、CLSトークン、Self-Attentionを押さえ、CNNとの違いをG検定向けに確認します。"
permalink: /gk/vit/
tags: [gk, transformer, attention, image_recognition]
gk_section: ディープラーニングの応用例/画像認識/物体認識タスク
gk_order: 11
last_modified_at: 2026-09-23
---

## まず結論

**Vision Transformer（ViT）**は、画像を小さな**パッチ**に分割し、それぞれをトークンのように扱ってTransformer Encoderへ入力する画像認識モデルです。

G検定では、

- 画像 → パッチ
- Patch Embedding
- 位置埋め込み
- Self-Attention
- Transformer Encoder

という流れを押さえます。

## 直感的な説明

CNNは、小さなフィルタを使って局所的な特徴を積み重ねます。

ViTは、画像をタイル状のパッチへ分け、

> **各パッチを単語のようなトークンとしてTransformerへ入力する**

イメージです。

そのため、離れたパッチ同士の関係もSelf-Attentionで直接扱えます。

## 定義・仕組み

代表的なViTの流れは次のとおりです。

1. 画像を固定サイズのパッチへ分割
2. 各パッチをベクトルへ変換
3. 位置埋め込みを加える
4. Transformer Encoderで処理
5. 分類ではCLSトークンなどの表現からクラスを予測

### なぜ位置埋め込みが必要？

TransformerのAttentionだけでは、パッチが画像のどの位置にあったかを自動では表せません。

そのため**位置情報を別途加える**ことが重要です。

### CNNとの違い

| 観点 | CNN | ViT |
|---|---|---|
| 基本処理 | 畳み込み | Self-Attention |
| 入力の扱い | 画像の局所領域 | パッチをトークン化 |
| 局所性 | 構造として強く持つ | 学習から関係を獲得 |
| 長距離関係 | 層を重ねて広げる | Attentionで直接扱える |

## いつ使う？（得意・不得意）

原論文では、大規模データで事前学習して転移することで、ViTが高い画像認識性能を示しました。

ただし、

> ViTは必ず大規模データがないと使えない

と絶対視するのは避けます。

ViT以降、データ拡張や学習方法の改良も進んでいます。

G検定では、**「大規模事前学習と相性がよいTransformer系画像モデル」**という位置付けを押さえれば十分です。

## G検定ひっかけポイント

### ViT＝CNN？

❌ 畳み込みフィルタを中心に画像を処理  
⭕ **画像パッチをTransformer Encoderで処理**

### パッチ＝クラス？

❌ 各パッチがそのまま分類結果になる  
⭕ **各パッチをトークン表現へ変換してAttentionで関係を学ぶ**

### Decoderを使う？

❌ 基本ViTはTransformer Decoder中心  
⭕ **原典ViTはEncoderを使う**

### ViTは常にCNNより高精度？

❌ どんなデータ・条件でも必ず上  
⭕ **性能はデータ量・学習方法・モデル規模などに依存する**

## まとめ（試験直前用）

- ViT＝**画像パッチをトークン化**
- Patch Embedding＋位置情報
- Transformer Encoderを利用
- Self-Attentionでパッチ同士の関係を扱う
- CNNは畳み込み、ViTはAttentionが中心
- **「ViTが常にCNNより優れる」とは覚えない**

## 参考資料

- [An Image is Worth 16x16 Words｜arXiv](https://arxiv.org/abs/2010.11929)

{% include gk_article_footer.html %}
