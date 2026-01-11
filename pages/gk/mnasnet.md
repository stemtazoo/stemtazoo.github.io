---
layout: page
title: "MnasNetとは？AutoML時代のモバイル向けCNN【G検定対策】"
permalink: /gk/mnasnet/
tags: [gk, cnn, neural_network]
gk_section: ディープラーニングの応用例/画像認識/物体認識タスク
gk_order: 9
---

## まず結論

* **MnasNet（Mobile Neural Architecture Search Network）とは、AutoML（NAS）によって設計された、モバイル端末向けの高効率CNNモデル**である。
* G検定では「Inception（GoogLeNet）との混同」や「速度を報酬に含める点」が頻出。

## 直感的な説明

* 人がネットワーク構造を考えるのではなく、**コンピュータ自身に“速くて賢い形”を探させたCNN**。
* スマホで使う前提なので、「精度だけでなく速さも評価」されている。

## 定義・仕組み

* Googleが提案した **NAS（Neural Architecture Search）ベースのCNN**。
* 特徴は、

  * **推論レイテンシ（実機での速度）を報酬関数に含めて探索**
  * 精度と速度のトレードオフを同時に最適化
* NASNetをベースに、**モバイル端末向けに改良**されている。

## いつ使う？（得意・不得意）

**得意**

* スマートフォン・組み込み端末での画像認識
* 精度と処理速度の両立が必要な場面

**不得意・注意点**

* サーバー向けの超高精度モデルが必要な場合
* NAS自体の探索コストは高い（設計段階）

## G検定ひっかけポイント

* ❌「Inceptionモジュールで深さと幅を広げた」→ **GoogLeNet**
* ❌「人が手動で設計したモバイルCNN」→ **MobileNet系**
* ✅「AutoML（NAS）で自動設計」「速度を報酬に含める」→ **MnasNet**
* 選択肢で

  * 「モバイル動作時の反応速度」
  * 「報酬関数に速度を組み込む」
    という表現があれば MnasNet を疑う。

## まとめ（試験直前用）

* MnasNet＝AutoML（NAS）で設計されたモバイル向けCNN
* 精度＋実機速度を同時に最適化
* Inception（GoogLeNet）とは別物
* 「速度を報酬に含める」が最重要キーワード
* 
