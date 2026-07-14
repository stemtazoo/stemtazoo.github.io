---
layout: page
title: Dilated Convolution（Atrous Convolution）とは？受容野と解像度【G検定】
description: "Dilated Convolution（Atrous Convolution・拡張畳み込み）は、カーネル要素の間隔を広げ、パラメータ数や特徴マップの解像度を大きく変えずに受容野を広げる手法です。dilation rate、DeepLab・ASPPとの関係、プーリングやDepthwise Convolutionとの違いを整理します。"
permalink: /gk/atrous-convolution/
tags: [gk, cnn, image_recognition]
gk_section: ディープラーニングの要素技術/ネットワークの構成要素
gk_order: 12
last_modified_at: 2026-07-14
---

## まず結論

Dilated Convolutionとは、**畳み込みカーネルの要素間にすき間を設け、特徴マップの解像度を保ちながら受容野を広げる手法**です。

**Atrous Convolution、拡張畳み込み、空洞畳み込み**も、基本的には同じ手法を指します。

| 観点 | 判断ポイント |
|---|---|
| 何を変える？ | カーネル要素を配置する間隔 |
| 何が広がる？ | 受容野 |
| 何を保ちやすい？ | 特徴マップの空間解像度 |
| 代表的な用途 | セマンティックセグメンテーション |
| 代表モデル・構造 | DeepLab、ASPP |

G検定では、**「解像度を下げずに受容野を広げる」**という説明を手がかりにします。

## 直感的な説明

通常の3×3畳み込みは、隣り合う9個の位置を見ます。

Dilated Convolutionでは、カーネルの間にすき間を空けます。同じ9個の重みを使いながら、より広い範囲を確認できます。

```text
通常の畳み込み：近い範囲を連続して見る
Dilated Convolution：間隔を空けて広い範囲を見る
```

セマンティックセグメンテーションでは、画像全体の文脈と、画素ごとの細かな位置情報の両方が必要です。プーリングや大きなストライドで特徴マップを小さくしすぎると、境界の位置が粗くなります。

Dilated Convolutionは、**広い文脈を見ることと、位置情報を残すことを両立しやすい**手法です。

## 定義・仕組み

Dilated Convolutionでは、dilation rate（拡張率）によってカーネル要素の間隔を決めます。

| dilation rate | 動き |
|---:|---|
| 1 | 通常の畳み込み |
| 2 | カーネル要素の間に1マス空ける |
| 3 | カーネル要素の間に2マス空ける |

3×3カーネルの場合、dilation rateを大きくすると、重みの数は9個のままでも、入力上で見る範囲が広がります。

### 受容野とは

受容野とは、出力の1点が入力画像のどの範囲から影響を受けるかを表す考え方です。

Dilated Convolutionは、パラメータ数を大きく増やさず、ダウンサンプリングも行わずに、受容野を広げられます。

| 手法 | 受容野 | 特徴マップの解像度 | 主な目的 |
|---|---|---|---|
| 通常の畳み込み | カーネルや層数に応じて広がる | 保ちやすい | 局所特徴の抽出 |
| ストライド・プーリング | 広げやすい | 下がる | ダウンサンプリング |
| Dilated Convolution | 広げられる | 保ちやすい | 広い文脈と位置情報の両立 |

### DeepLab・ASPPとの関係

DeepLab系のモデルでは、Dilated Convolutionがセマンティックセグメンテーションに利用されます。

ASPP（Atrous Spatial Pyramid Pooling）は、**異なるdilation rateの畳み込みを並列に使い、複数の大きさの受容野から特徴を集める構造**です。

- Dilated Convolution：間隔を空けた畳み込み手法
- ASPP：複数の拡張率を組み合わせる構造
- DeepLab：これらを利用するセグメンテーションモデル群

## いつ使う？（得意・不得意）

Dilated Convolutionは、画素の位置を細かく保ちながら、広い範囲の情報も見たい場面に向いています。

- セマンティックセグメンテーション
- 物体境界を保ちたい画像処理
- 複数スケールの文脈を扱う処理
- DeepLab系モデル

一方、Dilated Convolutionの主目的は計算量削減ではありません。軽量化が目的なら、Depthwise Separable ConvolutionやMobileNetの文脈を疑います。

また、dilation rateを大きくしすぎると、入力を飛び飛びに見るため、細かな局所情報を拾いにくくなることがあります。

## G検定ひっかけポイント

### Atrous ConvolutionとDilated Convolutionは別の手法

誤りです。文献や実装によって呼び方が異なりますが、基本的には同じ拡張畳み込みを指します。

### 軽量化のためにチャネルごとに畳み込む

これはDepthwise Convolutionの説明です。Dilated Convolutionが空けるのは、**空間方向のカーネル要素の間隔**です。

### プーリングと同じように解像度を下げる

誤りです。Dilated Convolutionは、ストライドを1に保てば、特徴マップの解像度を保ちながら受容野を広げられます。

### 画像を拡大する畳み込みである

誤りです。画像や特徴マップを拡大するのは、転置畳み込みやアップサンプリングの文脈です。Dilated Convolutionは、出力サイズを拡大することが目的ではありません。

### 選択肢の判断基準

| 問題文の表現 | 疑う技術 |
|---|---|
| カーネルの間隔・dilation rate | Dilated / Atrous Convolution |
| 解像度を保ちながら受容野を拡大 | Dilated / Atrous Convolution |
| 複数の拡張率を並列に利用 | ASPP |
| チャネルごとに畳み込み、軽量化 | Depthwise Separable Convolution |
| 特徴マップを小さくする | プーリング、ストライド |
| 特徴マップを大きくする | 転置畳み込み、アップサンプリング |

## まとめ（試験直前用）

- Dilated ConvolutionとAtrous Convolutionは基本的に同じ手法
- カーネル要素の間隔を広げる
- パラメータ数を大きく増やさずに受容野を広げる
- 特徴マップの解像度を保ちやすい
- DeepLabやASPP、セマンティックセグメンテーションと関係が深い

**「間隔を空ける・受容野を広げる・解像度を保つ」ならDilated Convolutionです。**

## 確認問題（G検定対策）

Dilated Convolutionの説明として、最も適切なものはどれか。

- ア. カーネル要素の間隔を広げ、特徴マップの解像度を保ちながら受容野を広げる。
- イ. チャネルごとに畳み込み、1×1畳み込みと組み合わせて計算量を削減する。
- ウ. 特徴マップの縦横サイズを大きくするために、入力の間へ値を補う。
- エ. 最大値や平均値を選び、特徴マップを小さくする。

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：ア**

### 解説

- ア：適切です。空間方向の間隔を広げることで受容野を広げます。
- イ：Depthwise Separable Convolutionの説明です。
- ウ：アップサンプリングに近い説明です。
- エ：プーリングの説明です。

判断ポイントは、**dilation rate、受容野、解像度維持**です。

</details>

{% include gk_article_footer.html %}
