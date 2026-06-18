---
layout: page
title: Atrous Convolution（拡張畳み込み）とは？受容野と解像度の関係を整理【G検定対策】
description: Atrous Convolutionは、畳み込みカーネルの間隔を広げ、解像度を落とさずに受容野を広げる手法です。DeepLab、セグメンテーション、通常の畳み込み、プーリング、Depthwise Separable Convolutionとの違いをG検定向けに整理します。
permalink: /gk/atrous-convolution/
tags: [gk, cnn, image_recognition]
gk_section: ディープラーニングの要素技術/ネットワークの構成要素
gk_order: 12
last_modified_at: 2026-06-18
---

## まず結論

Atrous Convolution（拡張畳み込み）とは、**畳み込みカーネルの間隔を広げることで、解像度を落とさずに広い受容野を得る畳み込み手法**です。

G検定では、特に **DeepLab やセグメンテーションで使われる理由** が問われます。

| 観点 | Atrous Convolutionのポイント |
|---|---|
| 何をする？ | 畳み込みの間隔を広げる |
| 何が広がる？ | 受容野 |
| 何を保つ？ | 特徴マップの解像度 |
| よく出るタスク | セマンティックセグメンテーション |
| 代表モデル | DeepLab |
| 混同しやすい技術 | プーリング、Depthwise Separable Convolution |

問題文に **「受容野を広げる」「解像度を保つ」「DeepLab」「セグメンテーション」** が出てきたら、Atrous Convolutionを疑います。

---

## 直感的な説明

普通の畳み込みは、画像を近くの画素から順番に見ていくイメージです。

一方、Atrous Convolutionは、カーネルの間にすき間を空けて見ます。

たとえるなら、

> **虫めがねの点を少し離して配置し、同じ回数の観察でより広い範囲を見る**

ようなものです。

通常の畳み込みでは、広い範囲を見るために層を深くしたり、プーリングで画像を小さくしたりします。

しかし、セグメンテーションでは、画像のどの位置がどのクラスかを細かく知りたいので、解像度を下げすぎると困ります。

Atrous Convolutionなら、

- 広い文脈を見る
- 位置情報を保つ
- 特徴マップを小さくしすぎない

ということができます。

---

## 定義・仕組み

Atrous Convolutionは、畳み込みカーネルの要素間に間隔を入れる畳み込みです。

別名で、**Dilated Convolution（膨張畳み込み）** と呼ばれることもあります。

### dilation rateとは

Atrous Convolutionでは、dilation rate（拡張率）が重要です。

| dilation rate | 意味 |
|---|---|
| 1 | 通常の畳み込み |
| 2 | カーネル要素の間に1つ分のすき間を空ける |
| 3以上 | さらに広い間隔で畳み込む |

dilation rate が大きいほど、同じカーネルサイズでも広い範囲を見られます。

### 受容野が広がる

受容野とは、出力の1つの値が入力画像のどの範囲を見ているかを表す考え方です。

Atrous Convolutionでは、カーネルの間隔を空けることで、パラメータ数を大きく増やさずに受容野を広げられます。

| 手法 | 受容野 | 解像度 | 試験での見分け方 |
|---|---|---|---|
| 通常の畳み込み | カーネルサイズに応じる | 保ちやすい | 基本の畳み込み |
| プーリング | 広く見やすい | 下がる | 位置情報が粗くなる |
| Atrous Convolution | 広がる | 保ちやすい | 解像度を落とさず受容野を広げる |

G検定では、細かい計算式よりも、**受容野を広げるが、特徴マップの解像度を下げにくい**という役割を押さえれば十分です。

---

## いつ使う？（得意・不得意）

### 得意な場面

Atrous Convolutionは、画像の位置情報が重要なタスクで使われます。

代表例は、**セマンティックセグメンテーション**です。

セマンティックセグメンテーションでは、画像の各画素に対して、

- 道路
- 空
- 人
- 車
- 建物

のようなクラスを割り当てます。

そのため、画像全体の文脈も見たい一方で、細かい位置情報も残したいです。

Atrous Convolutionは、このバランスに向いています。

### DeepLabとの関係

DeepLab系のモデルでは、Atrous Convolutionが重要な技術として使われます。

DeepLabでは、セグメンテーションで必要な

- 広い文脈情報
- 高い空間解像度

を両立するために、Atrous Convolutionが使われます。

### 注意が必要な場面

Atrous Convolutionは便利ですが、すべてのCNN問題で必須というわけではありません。

次のような場面では、別の技術と混同しないようにします。

| 目的 | よく出る技術 |
|---|---|
| 軽量化したい | Depthwise Separable Convolution |
| 位置のずれに強くしたい | プーリング |
| 深いネットワークを学習しやすくしたい | 残差接続 |
| 解像度を保って受容野を広げたい | Atrous Convolution |

---

## G検定ひっかけポイント

### 誤解1：Atrous Convolutionは軽量化のための技術

これは誤りです。

Atrous Convolutionの主な目的は、**解像度を保ちながら受容野を広げること**です。

軽量化のキーワードが出たら、Depthwise Separable ConvolutionやMobileNetを疑います。

### 誤解2：プーリングと同じ

プーリングも広い範囲の情報を集約できますが、特徴マップの解像度を下げます。

Atrous Convolutionは、解像度を下げすぎずに広い範囲を見たいときに使います。

| 手法 | 役割 |
|---|---|
| プーリング | 解像度を下げて特徴を集約する |
| Atrous Convolution | 解像度を保ちつつ受容野を広げる |

### 誤解3：RNNや自然言語処理の技術

Atrous Convolutionは、CNNの畳み込みに関する技術です。

RNN、LSTM、Transformerの文脈ではなく、画像認識やセグメンテーションの文脈で出ます。

### 誤解4：DeepLabそのもの

Atrous Convolutionはモデル名ではなく、畳み込みの手法です。

DeepLabはセグメンテーションモデルで、その中でAtrous Convolutionが使われます。

### 選択肢の切り方

| 問題文の表現 | 疑う用語 |
|---|---|
| 解像度を落とさず受容野を広げる | Atrous Convolution |
| DeepLabで使われる | Atrous Convolution |
| 軽量化、チャネルごとの畳み込み | Depthwise Separable Convolution |
| Inceptionモジュール | GoogLeNet |
| 残差接続 | ResNet |
| 画素ごとの分類 | セマンティックセグメンテーション |

**「受容野 + 解像度維持 + セグメンテーション」なら Atrous Convolution** と覚えると切りやすいです。

---

## まとめ（試験直前用）

- Atrous Convolution = カーネル間隔を広げる畳み込み
- 受容野を広げられる
- 特徴マップの解像度を下げにくい
- DeepLabやセグメンテーションで重要
- 軽量化手法ではなく、Depthwise Separable Convolutionとは別物

**判断基準：解像度を保ちながら広い範囲を見るなら、Atrous Convolution。**

---

## 確認問題（G検定対策）

Atrous Convolutionの説明として、最も適切なものはどれか。

- ア. 畳み込みカーネルの間隔を広げ、解像度を落とさずに受容野を広げる手法
- イ. チャネルごとの畳み込みと1×1畳み込みを組み合わせ、計算量を削減する手法
- ウ. 出力層の値を次時刻の隠れ層へ戻す再帰型ニューラルネットワーク
- エ. 生成器と識別器を競わせて学習する生成モデル

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：ア**

### 解説

- ア：適切です。Atrous Convolutionは、解像度を保ちながら受容野を広げる畳み込みです。
- イ：Depthwise Separable Convolutionの説明です。
- ウ：Jordan Networkの説明です。
- エ：GANの説明です。

判断ポイントは、**解像度を保つ、受容野を広げる、DeepLabで使われる**です。

</details>

{% include gk_article_footer.html %}
