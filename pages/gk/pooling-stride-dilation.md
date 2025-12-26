---
layout: page
title: Pooling・Stride・Dilated Convolution の違い
permalink: /gk/pooling-stride-dilation/
tags: [gk, neural_network, cnn, cheatsheet]
---

## まず結論

* **Pooling**：サイズを小さくして情報を要約する
* **Stride**：畳み込みの移動間隔を広げてサイズを小さくする
* **Dilated Convolution**：サイズを保ったまま受容野を広げる

👉 **「サイズがどうなるか」** が最重要。

---

## 直感的な説明

### 一言イメージ

* Pooling  
  → **間引いて圧縮**
* Stride  
  → **飛ばしながら進む**
* Dilation  
  → **手を広げて見る**

---

## 定義・仕組み

### Pooling（Max Poolingなど）

* 一定領域の代表値を取る
* 情報を要約
* **空間サイズが小さくなる**

---

### Stride

* 畳み込みカーネルの移動幅
* Stride > 1 にすると
  * 計算量削減
  * **空間サイズが小さくなる**

---

### Dilated Convolution（空洞畳み込み）

* カーネルの間隔を広げる
* パラメータ数は増えない
* **空間サイズは変わらない**
* 受容野が広がる

---

## サイズと情報の違い（超重要）

| 手法 | サイズ | 受容野 | 主目的 |
|---|---|---|---|
| Pooling | 小さくなる | 広がるが粗い | 圧縮 |
| Stride | 小さくなる | やや広がる | 計算削減 |
| Dilation | **変わらない** | **広がる** | 文脈理解 |

---

## いつ使う？（得意・不得意）

### Pooling が向く場面

* 分類タスク
* 多少の位置ずれを許容したい場合

---

### Stride が向く場面

* モデルを軽くしたい
* リアルタイム処理

---

### Dilated Convolution が向く場面

* セマンティックセグメンテーション
* 境界情報を保ちたい場合
* DeepLab 系モデル

---

## G検定ひっかけポイント

### ❌ よくある誤解

* ❌ 「Dilationは学習を速くする」
* ❌ 「StrideとPoolingは同じ」
* ❌ 「受容野を広げる＝サイズが小さくなる」

---

### ✅ 正しい理解

* サイズを小さくする → **Pooling / Stride**
* サイズを保つ → **Dilation**
* 広い文脈を取る → **Dilation**

---

## 試験での即断フレーズ

* **「サイズを小さくしない」**  
  → Dilated Convolution
* **「要約・圧縮」**  
  → Pooling
* **「計算量削減」**  
  → Stride

---

## まとめ（試験直前用）

* Pooling・Stride → サイズが小さくなる
* Dilation → サイズを保つ
* Dilationの目的は **受容野拡大**
* 学習速度UPではない

👉 次は **ASPP（Atrous Spatial Pyramid Pooling）** に進むと理解が完成します。
