---
layout: page
title: Anchor Box / Default Box / RPN
description: Anchor Box / Default Box / RPNは重要ポイントを整理して理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、G検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /gk/anchor-defaultbox-rpn/
tags: [G検定, 画像認識, 物体検出]
gk_section: ディープラーニングの応用例/画像認識/ネオコグニトロンとLeNet
gk_order: 3
---

## まず結論

* **Anchor Box（Default Box）**：
  物体検出で使う「最初から用意しておく四角のひな形（基準の箱）」。
* **RPN（Region Proposal Network）**：
  「物体がありそうな候補領域」をネットワークで作る仕組み。

👉 G検定では、
**SSD/YOLOは1段階（高速）**、**Faster R-CNNは2段階（精度）**の前提の上で、

* SSDは **Default Box（＝Anchor）**
* Faster R-CNNは **RPN**

を結びつけて選択肢を切るのが最重要です。

---

## 直感的な説明

### Anchor / Default Box（ひな形の四角）

画像の上に、最初から

* 小さい四角
* 大きい四角
* 横長・縦長の四角

を**大量に置いておく**イメージです。

🔍「この辺に物体があるかも？」と探すとき、
ゼロから四角を描くのではなく、
**用意済みの四角を“ちょい修正”して当てにいく**感じです。

### RPN（候補領域を作る係）

Faster R-CNNはまず、

* 物体がありそうな場所だけを先に集める

という段階があります。
この「候補を集める担当」が **RPN** です。

---

## 定義・仕組み

### Anchor Box / Default Box

* **Anchor Box**：
  画像上の各位置にあらかじめ配置する「基準のバウンディングボックス」
* **Default Box**：
  SSDでの呼び名（意味はほぼ同じ）

モデルは、各Anchorに対して

* 物体らしさ（ある/なし）
* クラス
* 四角の補正量（位置・大きさのズレ）

を予測します。

👉 ポイントは、**四角を“生成”というより“補正”して作る**ことです。

---

### RPN（Region Proposal Network）

RPNは、Faster R-CNNの第1段階で

* 「物体がありそうな領域（Region Proposal）」を出す

ための小さなネットワークです。

流れとしては

1. 画像から特徴マップを作る
2. RPNが「候補領域」を提案
3. その候補を第2段階で分類・位置補正

👉 **RPNがある＝2段階（Faster R-CNN）**で切れます。

---

## いつ使う？（得意・不得意）

### Anchor / Default Boxが活きる場面

* **SSD系**の高速検出
* 位置とクラスを一気に出す（1段階）

ただし

* Anchorの設計（サイズ・縦横比）が合わないと精度が落ちやすい

というクセもあります。

### RPNが活きる場面

* **Faster R-CNN**のような精度重視
* 「候補を絞ってから丁寧に分類」したい場面

ただし

* 2段階なので計算は重くなりやすい

---

## G検定ひっかけポイント

### ① 「AnchorとDefault Boxは別物」→ ❌

❌ よくある誤解：

> Anchor BoxとDefault Boxは異なる概念である

⭕ 正しくは：

> **ほぼ同じ意味**（呼び方の違い）

👉 試験では **SSDのDefault Box＝Anchorの仲間** と捉えてOKです。

---

### ② 「RPNはSSDやYOLOにもある」→ ❌

❌ よくある誤解：

> 物体検出ならRPNを使う

⭕ 正しくは：

> **RPNはFaster R-CNN系（2段階）で重要**

* SSD / YOLO：1段階（RPNなし）
* Faster R-CNN：2段階（RPNあり）

👉 **RPNが出たらFaster R-CNN側**と即断。

---

### ③ 「Anchor＝候補領域（Proposal）」と混同 → ❌

* Anchor：**ひな形の四角**（最初から大量に置く）
* Proposal：**物体がありそうな候補**（選別された少数）

👉 Anchorは“全候補の土台”、Proposalは“選ばれた候補”です。

---

## まとめ（試験直前用）

* Anchor Box（Default Box）は **ひな形の四角**
* SSDでは **Default Box** と呼ぶ（意味はAnchorとほぼ同じ）
* RPNは **候補領域（Proposal）を作るネットワーク**
* **RPNあり＝2段階＝Faster R-CNN**
* **RPNなし＝1段階＝SSD/YOLO**

📝 選択肢で迷ったら：

> **Default Box＝SSD、RPN＝Faster R-CNN**

これで切れます。
