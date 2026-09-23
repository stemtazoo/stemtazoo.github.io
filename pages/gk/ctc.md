---
layout: page
title: CTCとは？フレーム単位の正解位置なしで系列を学ぶ【G検定】
description: "CTC（Connectionist Temporal Classification）を、音声フレームと文字などの正解ラベルの位置合わせを事前に与えず、blankと重複を含む複数のアラインメントをまとめて学習する目的関数として整理します。Encoder-Decoderとの違いも確認します。"
permalink: /gk/ctc/
tags: [gk, speech, neural_network]
gk_section: ディープラーニングの応用例/音声処理/音声認識・系列モデル
gk_order: 1
last_modified_at: 2026-09-24
---

## まず結論

**CTC（Connectionist Temporal Classification）**は、入力系列と出力ラベル系列の**フレーム単位の正解位置合わせを事前に与えなくても学習できる目的関数・仕組み**です。

音声認識では、長い音声フレーム列から短い文字列を学習する代表的方法です。

## 直感的な説明

「CAT」という文字列を出したいとき、音声の何フレーム目がC・A・Tに対応するかを人手で指定するのは大変です。

CTCでは、blankや同じラベルの繰り返しを含む複数の経路を考え、それらをまとめて正解文字列の確率として扱います。

## 定義・仕組み

CTCでは出力系列に**blank**という特別な記号を追加します。

たとえば C - - A A - T のような経路から、

1. 連続する同じラベルをまとめる
2. blankを除く

ことでCATを得ます。

同じCATへ対応する複数経路の確率を合計し、その確率を高めるよう学習します。

### 単調な対応

標準的なCTCでは、入力と出力の順序が入れ替わらない**単調なアラインメント**を前提とします。

## いつ使う？（得意・不得意）

CTCは、

- 音声認識
- 手書き文字認識
- 時系列ラベリング

などに使われます。

出力順序を大きく並べ替えるタスクには、その前提が合わない場合があります。

## G検定ひっかけポイント

### CTC＝モデル構造？

❌ RNNやTransformerのようなネットワークそのもの  
⭕ **系列対応を扱う目的関数・学習方式**

### アラインメント

❌ 位置合わせを一切考えない  
⭕ **正解フレーム位置を与えず、複数アラインメントをまとめて扱う**

### blank

❌ 空白文字そのもの  
⭕ **CTC専用の特別なラベル**

## まとめ（試験直前用）

- CTC＝**Connectionist Temporal Classification**
- フレーム単位の正解位置が不要
- blankを使う
- 複数アラインメントをまとめて扱う
- 単調な系列対応
- RNN / Transformerとは役割が違う

## 参考資料

- [Connectionist Temporal Classification｜ICML 2006](https://www.cs.toronto.edu/~graves/icml_2006.pdf)

{% include gk_article_footer.html %}
