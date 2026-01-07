---
layout: page
title: 画像系頻出用語 一気通貫チェック【G検定対策】
permalink: /gk/image-terms-check/
tags: [gk, cnn, cheatsheet]
---

## まず結論
- **画像系の問題は「処理の種類」と「目的」で切るのが最短ルート**。
- G検定では **用語名より「何を変えているか／何のためか」**が問われる。

## 直感的な説明
- 画像系の用語はすべて、次のどこかに属する：
  1. 入力を整える（前処理）
  2. データを増やす（データ拡張）
  3. 特徴を抜き出す（CNN）
  4. 意味を分ける（タスク）
- どの段階の話か分かれば、選択肢は自然に消える。

## 定義・仕組み
### ① 前処理（Preprocessing）
- **Normalization**
  - 画素値を一定範囲に正規化
- **Standardization**
  - 平均0・分散1に変換
- **Resize**
  - 画像サイズを揃える
- **Grayscale**
  - 色情報を除去

👉 目的：学習の安定化・入力統一

### ② データ拡張（Data Augmentation）
**色系**
- Brightness：明るさ
- Contrast：明暗差
- Saturation：色の濃さ
- Hue：色味

**幾何系**
- Rotation：回転
- Flip：反転
- Crop：切り出し

👉 目的：汎化性能向上・ロバスト性

### ③ CNN 構成要素
- **Convolution**
  - 局所特徴抽出
- **Pooling**
  - 空間情報の圧縮
- **Stride / Padding**
  - 特徴マップサイズ調整
- **ReLU**
  - 非線形性付与

👉 目的：特徴抽出と階層化

### ④ 画像タスク
- **Image Classification**
  - 画像全体に1ラベル
- **Object Detection**
  - 位置＋クラス
- **Semantic Segmentation**
  - ピクセル単位分類
- **Instance Segmentation**
  - 個体単位で分離

👉 目的：何を予測するかの違い

## G検定ひっかけポイント
- **処理カテゴリをまたいで混ぜてくる**
- よくある誤解：
  - ❌ Brightness = 回転
  - ❌ Pooling = データ拡張
  - ❌ Segmentation = 検出
- 即断ルール：
  - 「色・形を変える」→ データ拡張
  - 「畳み込み」→ CNN
  - 「位置を出す」→ Detection
  - 「画素単位」→ Segmentation

## まとめ（試験直前用）
- 画像系は **段階で整理**
- 前処理／拡張／CNN／タスク
- 色が変わる？形が変わる？
- 出力はラベル？位置？画素？
- **「どの段階の話か」で即切る**
