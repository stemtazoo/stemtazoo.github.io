---
layout: page
title: MobileNetとは？Depthwise Separable Convolutionで軽量化【G検定】
description: "MobileNetを、Depthwise Convolutionと1×1 Pointwise Convolutionを分けるDepthwise Separable Convolutionで計算量を削減した軽量CNNとして整理します。モバイル・エッジ向けという目的と、精度・遅延のトレードオフをG検定向けに確認します。"
permalink: /gk/mobilenet/
tags: [gk, cnn, model_compression]
gk_section: ディープラーニングの応用例/画像認識/物体認識タスク
gk_order: 8
last_modified_at: 2026-09-23
---

## まず結論

**MobileNet**は、モバイル端末や組み込み機器など計算資源が限られる環境を意識した軽量CNNです。

最大の判断キーワードは、

**Depthwise Separable Convolution**

です。

## 直感的な説明

通常の畳み込みでは、空間方向とチャネル方向の処理をまとめて行います。

MobileNetではこれを、

1. チャネルごとに空間方向を処理
2. 1×1畳み込みでチャネルを混ぜる

の2つへ分け、計算を効率化します。

## 定義・仕組み

### Depthwise Convolution

入力チャネルごとに独立して空間方向の畳み込みを行います。

### Pointwise Convolution

1×1畳み込みでチャネル間の情報を組み合わせます。

この2つを組み合わせたものが**Depthwise Separable Convolution**です。

原典MobileNetでは、さらにモデルサイズや計算量を調整するため、

- width multiplier
- resolution multiplier

も導入されています。

## いつ使う？（得意・不得意）

代表的な用途は、

- スマートフォン
- エッジAI
- 組み込み機器
- リアルタイム画像処理

です。

MobileNetは**精度を捨てるモデル**ではなく、制約に応じて**精度と遅延・計算量のバランスを調整する**設計です。

比較対象やモデル世代によって精度は変わるため、

> MobileNetは必ずResNetより低精度

とは覚えません。

## G検定ひっかけポイント

### MobileNetの鍵

❌ 残差接続が最大の特徴  
⭕ **Depthwise Separable Convolution**

### Depthwiseだけ？

❌ チャネルごとの畳み込みだけで終わる  
⭕ **Depthwise + Pointwiseで構成**

### 軽量＝精度が低い？

❌ 軽量モデルは必ず精度が低い  
⭕ **精度・計算量のトレードオフを設計する**

## まとめ（試験直前用）

- MobileNet＝**軽量CNN**
- モバイル・エッジ向け
- Depthwise Convolution
- Pointwise Convolution（1×1）
- 2つを合わせてDepthwise Separable Convolution
- **精度と計算量の固定順位で覚えない**

## 参考資料

- [MobileNets｜arXiv](https://arxiv.org/abs/1704.04861)

{% include gk_article_footer.html %}
