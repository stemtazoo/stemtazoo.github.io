---
layout: page
title: BLIPとは？画像理解とキャプション生成を両立する事前学習【G検定】
description: "BLIP（Bootstrapping Language-Image Pre-training）を、画像・テキストの理解タスクと生成タスクを統合するマルチモーダル事前学習手法として整理します。画像キャプション、VQA、画像テキスト検索、CaptionerとFilterによるデータブートストラップを押さえ、CLIPとの違いを確認します。"
permalink: /gk/blip/
tags: [gk, multimodal, attention]
gk_section: ディープラーニングの応用例/マルチモーダル/画像と言語の表現・理解
gk_order: 2
last_modified_at: 2026-09-23
---

## まず結論

**BLIP（Bootstrapping Language-Image Pre-training）**は、画像とテキストを使い、**理解タスクと生成タスクの両方へ使えるマルチモーダル事前学習手法**です。

代表的には、

- 画像・テキスト検索
- 画像キャプション生成
- Visual Question Answering（VQA）

などを扱います。

G検定では、CLIPと比べて**対応付けだけでなく、文章生成を含む複数タスクへ対応する設計**であることを押さえます。

## 直感的な説明

CLIPは、

> この画像と、この文章は意味的に合っているか？

を学ぶのが中心です。

BLIPはそれに加えて、

> この画像を文章で説明する  
> この画像について質問に答える

といった理解・生成タスクまで扱えるように設計されています。

## 定義・仕組み

BLIPでは、画像とテキストの表現を学ぶだけでなく、生成にも利用できるよう複数の学習目的を組み合わせます。

また原論文では、Web上の画像・テキストデータに含まれるノイズへ対処するため、**CapFilt（Captioning and Filtering）**を使います。

- Captioner：画像から新しいキャプションを生成
- Filter：ノイズの多い画像・テキストペアを選別

この**データを生成・選別して学習データを改善する仕組み**がBootstrappingの重要な点です。

## いつ使う？（得意・不得意）

BLIPは、

- 画像キャプション
- VQA
- 画像・テキスト検索
- 画像と言語をまたぐ表現学習

などに利用できます。

ただし、

> BLIPはCLIPの上位互換

と覚えるのは避けます。

CLIPとBLIPは学習目的・設計・得意な利用方法が異なります。

## G検定ひっかけポイント

### BLIP＝CLIP？

❌ 画像とテキストの類似度だけを学ぶ  
⭕ **理解＋生成を含む複数タスクを扱う**

### Bootstrapping

❌ 少数例学習の別名  
⭕ **キャプション生成・フィルタリングで学習データを改善する仕組み**

### BLIP＝画像生成モデル？

❌ Text-to-Imageで画像を生成するモデル  
⭕ **画像を入力してテキスト生成・理解などを扱うマルチモーダルモデル**

## まとめ（試験直前用）

- BLIP＝**Bootstrapping Language-Image Pre-training**
- 画像＋テキスト
- 理解タスク＋生成タスク
- キャプション生成
- VQA
- CapFiltで学習データを改善
- CLIPとは役割・学習目的が異なる

## 参考資料

- [BLIP: Bootstrapping Language-Image Pre-training｜arXiv](https://arxiv.org/abs/2201.12086)
- [CLIP](/gk/clip/)

{% include gk_article_footer.html %}
