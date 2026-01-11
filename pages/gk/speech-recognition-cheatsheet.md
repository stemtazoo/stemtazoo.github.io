---
layout: page
title: 音声認識まとめ（WaveNet・CTC・RNN）
permalink: /gk/speech-recognition-cheatsheet/
tags: [gk, cheatsheet]
gk_section: チートシート（試験直前）/チートシート（試験直前）
gk_order: 5
---

## まず結論（この1ページで即断）

**音声認識は「音声という時系列データ」をどう扱うかがすべてです。**

G検定では、
👉 **「音声のどの段階を扱っているか」**
を見抜けるかが問われます。

---

## 直感的な全体像

| 手法                  | 何をする？       | 典型用途     |
| ------------------- | ----------- | -------- |
| **RNN**             | 時系列を順に処理    | 音声特徴量の処理 |
| **Encoder-Decoder** | 音→文字列変換     | 音声認識・翻訳  |
| **CTC**             | 時系列とラベル対応付け | 音声→文字    |
| **WaveNet**         | 波形を直接生成     | 音声生成     |

👉 **画像用CNN（EfficientNetなど）は対象外**

---

## 各手法の役割

### RNN / LSTM / GRU

* 音声特徴量（MFCCなど）を時系列として処理
* 音声認識の基礎構造

👉 「時系列処理」と言われたらまず RNN

---

### Encoder-Decoder

* 入力：音声系列
* 出力：文字系列
* 入力長と出力長が異なってもOK

👉 **seq2seq 構造**

---

### CTC（Connectionist Temporal Classification）

* 音声フレームと文字の対応を自動で学習
* アラインメント不要

👉 音声認識で超頻出

---

### WaveNet

* 音声波形を直接モデル化
* 高品質な音声生成が可能

👉 **認識ではなく生成が主用途**

---

## G検定ひっかけポイント

### ① 音声＝WaveNet と思わせる

❌ 不正解。

* WaveNet：生成向き
* 認識：RNN / CTC / Encoder-Decoder

---

### ② 画像モデルを混ぜる

* EfficientNet
* AlexNet

👉 **音声には不適切**

---

### ③ CTC の役割を誤解

* CTC = 分類器ではない
* **対応付け（アラインメント）手法**

---

## まとめ（試験直前用）

* 音声は **時系列データ**
* 認識：RNN / Encoder-Decoder / CTC
* 生成：WaveNet
* **画像CNNは使わない**

👉 迷ったら

> **音声 = 時系列**
