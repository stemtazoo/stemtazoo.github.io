---
layout: page
title: SegNet vs U-Net 比較チートシート【G検定頻出】
permalink: /gk/segnet-vs-unet/
tags: [gk, cnn, cheatsheet]
---

## まず結論
- **SegNet と U-Net の最大の違いは「Decoder に何を渡すか」**。
- G検定では **skip connection（特徴マップ）か、pooling インデックスか**を混同させてくる。

## 直感的な説明
- **U-Net**  
  👉 「縮小前の情報を、そのままコピーして後半に渡す」  
  👉 情報量が多く、境界がきれい
- **SegNet**  
  👉 「縮小時に、どこが代表だったかだけをメモして渡す」  
  👉 メモリ節約・軽量

イメージ的には：
- U-Net：📦 中身ごと渡す  
- SegNet：📍 位置メモだけ渡す

## 定義・仕組み
### U-Net
- Encoder-Decoder 型 CNN
- **Encoder の特徴マップを skip connection で Decoder に結合**
- 高解像度情報を保持しやすい

### SegNet
- Encoder-Decoder 型 CNN
- **Max Pooling 時のインデックスのみを保存**
- Decoder はそのインデックスを使ってアップサンプリング
- 特徴マップは直接渡さない

## いつ使う？（得意・不得意）
### U-Net
**得意**
- 医用画像など細かい境界が重要
- 精度重視のセマンティックセグメンテーション

**注意**
- メモリ消費が大きい

### SegNet
**得意**
- メモリ制約がある環境
- 軽量・リアルタイム性重視

**注意**
- 境界精度は U-Net に劣ることがある

## G検定ひっかけポイント
- **「skip connection」という単語が出たら U-Net**
- **「pooling インデックス」「位置情報」という単語が出たら SegNet**
- よくある誤り：
  - ❌ SegNet も特徴マップを Decoder に渡す  
  - ⭕ SegNet は **位置情報のみ**
- 選択肢での判断基準：
  - 「特徴量を結合」→ U-Net
  - 「インデックスを保存」→ SegNet

## まとめ（試験直前用）
- 比較軸は **Decoder に何を渡すか**
- U-Net：**特徴マップ（skip connection）**
- SegNet：**Pooling インデックス**
- 精度重視 → U-Net
- メモリ重視 → SegNet
- この二択は **G検定の定番ひっかけ**
- 
