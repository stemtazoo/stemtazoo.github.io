---
layout: page
title: ResNetとは？残差接続と深層化の仕組み【G検定対策】
description: "ResNet（Residual Network）を、入力を後段へ直接足す残差接続によって深いネットワークを学習しやすくしたCNNとして整理します。勾配消失だけでなく、深くすると学習誤差まで悪化する劣化問題との関係を押さえ、VGG・WideResNet・SENetとの違いを確認します。"
permalink: /gk/resnet/
tags: [gk, cnn]
gk_section: ディープラーニングの応用例/画像認識/物体認識タスク
gk_order: 4
last_modified_at: 2026-09-23
---

## まず結論

**ResNet（Residual Network）**は、入力を後段へ直接つなぐ**残差接続（skip / shortcut connection）**を導入し、非常に深いニューラルネットワークを学習しやすくしたモデルです。

G検定では、

- 残差接続
- F(x) + x
- 深層化
- 劣化問題の緩和

を押さえます。

「ResNet＝勾配消失だけを解決したモデル」と狭く覚えないことが重要です。

## 直感的な説明

深いネットワークでは、層を増やせば必ず学習が良くなるわけではありません。

ResNetは、変換した結果だけを次へ渡すのではなく、

> **元の入力を近道でそのまま後ろへ届ける**

経路を作ります。

これにより、必要なら「大きく変換しない」ことも学びやすくなります。

## 定義・仕組み

代表的な残差ブロックは、

**出力 = F(x) + x**

と表せます。

- x：入力
- F(x)：複数層で学習する変換
- xを直接足す経路：shortcut connection

この設計により、ネットワークが「入力との差分（残差）」を学習しやすくなります。

### 劣化問題

ResNet原論文で重要なのは、深いネットワークで起こる**degradation problem（劣化問題）**です。

これは単なる過学習ではなく、層を追加した深いモデルのほうが**訓練誤差まで悪化する**ことがある問題です。

残差学習は、この深いネットワークの最適化を容易にしました。

## いつ使う？（得意・不得意）

ResNetは、

- 画像分類
- 物体検出のバックボーン
- セグメンテーション
- 特徴抽出

など、多くの画像タスクの基盤として利用されてきました。

一方、モデルサイズや計算量はResNet-18、50、101など構成によって大きく異なります。

> ResNet＝必ず重い

と一括りにしないようにします。

## G検定ひっかけポイント

### ResNet＝勾配消失対策だけ？

❌ 勾配消失だけを目的に作られた  
⭕ **残差接続によって深いネットワークの最適化・劣化問題を改善する**

### skip connection

❌ 層を削除する仕組み  
⭕ **入力を後段へ直接伝える経路**

### VGGとの違い

- VGG → 3×3畳み込みを直列に積む
- ResNet → **残差接続を使う**

### SENetとの違い

- ResNet → shortcut connection
- SENet → チャネル重要度を調整するAttention

## まとめ（試験直前用）

- ResNet＝**Residual Network**
- F(x) + x
- shortcut / skip connection
- 深いネットワークを学習しやすくする
- 劣化問題を緩和
- **「勾配消失だけ」と限定しない**

## 参考資料

- [Deep Residual Learning for Image Recognition｜arXiv](https://arxiv.org/abs/1512.03385)

{% include gk_article_footer.html %}
