---
layout: page
title: ResNet・DenseNet・EfficientNet 比較（G検定対策）
permalink: /gk/cnn-architectures-comparison/
tags: [gk, cnn, neural_network, cheatsheet]
gk_section: ディープラーニングの応用例/画像認識/ネオコグニトロンとLeNet
gk_order: 10
---

## まず結論（試験はここだけ見ればOK）

* **ResNet**：勾配消失を防ぐ（スキップ接続）
* **DenseNet**：特徴量を再利用（全結合的な接続）
* **EfficientNet**：性能と計算量のバランス最適化

👉 G検定では **「何を解決したモデルか」** が最重要

---

## 直感的な違い

### ResNet

> 近道を作って、学習を楽にする

* 層を飛び越える **スキップ接続**
* 深くしても学習できる

---

### DenseNet

> これまでの情報を全部使う

* 前の層の出力を **すべて結合**
* 特徴量の再利用が得意

---

### EfficientNet

> 同じ計算量で、もっと賢く

* ネットワーク幅・深さ・解像度を **同時に最適化**
* 少ない計算量で高精度

---

## 構造の違い（図なしで理解）

| モデル          | 接続の特徴    | 主な工夫   |
| ------------ | -------- | ------ |
| ResNet       | スキップ接続   | 勾配消失対策 |
| DenseNet     | 全結合的接続   | 特徴量再利用 |
| EfficientNet | スケーリング設計 | 計算効率向上 |

---

## 何が問題で、どう解決した？（頻出）

### ResNet

* 問題：深くすると学習できない
* 解決：**恒等写像（Identity）** による勾配伝播

---

### DenseNet

* 問題：情報が層ごとに失われる
* 解決：**すべての層を結合**

---

### EfficientNet

* 問題：大きくすると計算量が爆増
* 解決：**Compound Scaling**

---

## G検定ひっかけポイント

* ❌「ResNetは正則化手法」→ **誤り**
* ❌「DenseNetはCNNではない」→ **誤り**
* ❌「EfficientNetは層を増やしただけ」→ **誤り**

---

## 超短縮 暗記フレーズ

* ResNet：**近道（Skip）**
* DenseNet：**全部つなぐ**
* EfficientNet：**バランス設計**

---

## まとめ（試験直前用）

* ResNet → 深くする
* DenseNet → 情報を使い切る
* EfficientNet → 効率よく強くする

👉 次は **画像タスク総まとめ（分類・検出・セグメンテーション）** に進むと全体像が完成
