---
layout: page
title: GANの派生モデルまとめ
permalink: /gk/gan-variants/
tags: [gk, neural_network, gan, cheatsheet]
---

## まず結論

* **GANは派生モデル名と用途を結びつける問題が多い**
* G検定では  
  👉「条件付き？」「変換？」「高品質？」  
  のどれかで切る
* **DCGAN / Conditional GAN / CycleGAN / StyleGAN** が頻出

---

## 直感的な整理（超重要）

GAN派生は一言で覚える👇

* **DCGAN** → 画像をきれいに
* **Conditional GAN** → 条件をつけて
* **CycleGAN** → 変換する
* **StyleGAN** → 超高品質

---

## 主要GAN派生モデル

### DCGAN（Deep Convolutional GAN）

* GANに **CNNを導入**
* 画像の空間構造を保持
* 高解像度な画像生成が可能

👉  
**GAN × CNN**

---

### Conditional GAN（cGAN）

* 入力に **条件ラベル** を追加
* 特定クラスの画像を生成可能

例：
* 「数字3の画像を生成」
* 「犬の画像だけ生成」

👉  
**条件付き生成**

---

### CycleGAN

* **画像から画像への変換**
* ペアデータ不要
* 逆変換の一貫性（Cycle Consistency）を利用

例：
* 写真 ↔ 絵画
* 夏 ↔ 冬

👉  
**Image-to-Image Translation**

---

### StyleGAN

* スタイルを制御した画像生成
* 非常に高品質
* 顔画像生成で有名

👉  
**リアルすぎる画像**

---

## 試験向け比較表（ここだけ見ればOK）

| モデル | 主目的 | キーワード |
|---|---|---|
| DCGAN | 高品質生成 | CNN |
| Conditional GAN | 条件付き生成 | ラベル |
| CycleGAN | 画像変換 | ペア不要 |
| StyleGAN | 超高品質 | スタイル |

---

## G検定ひっかけポイント

### ❌ よくある誤解

* ❌ 「YOLOはGANの一種」
* ❌ 「GANは分類モデル」
* ❌ 「CycleGANはペア画像が必要」

---

### ✅ 正しい切り方

* 生成？ → GAN
* 条件付き？ → Conditional GAN
* 変換？ → CycleGAN
* 画質重視？ → StyleGAN

---

## 試験での即断フレーズ

* 「条件付き生成」 → Conditional GAN
* 「ペアなし画像変換」 → CycleGAN
* 「高解像度画像生成」 → DCGAN / StyleGAN
* 「物体検出」 → ❌ GANではない

---

## まとめ（試験直前用）

* GAN派生は **用途で区別**
* DCGAN：CNN導入
* cGAN：条件付き
* C*
