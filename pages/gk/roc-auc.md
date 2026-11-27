---
layout: page
title: ROC曲線・AUCとは？TPRとFPRで分類性能を比較【G検定】
description: "ROC曲線を「しきい値を動かしたときのTPRとFPRの関係」として整理し、AUCがその曲線全体を1つの値で要約する指標であることをG検定向けに解説します。Precision-Recall曲線との使い分けや、AUCが高くても特定しきい値で誤検知が少ないとは限らない点も確認します。"
permalink: /gk/roc-auc/
tags: [gk, 機械学習, 評価指標, 頻出]
gk_section: 機械学習の概要/モデルの選択・評価/分類の評価指標
gk_order: 6
last_modified_at: 2026-11-27
image:
  path: "https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/gk/roc-auc.png"
  width: 1200
  height: 630
  alt: "横軸FPR（偽陽性率）、縦軸TPR（真陽性率）のROC曲線と、その下を塗りつぶしたAUC。対角線はランダムな分類の基準"
---

## まず結論

ROC曲線は、**分類のしきい値を変えたときの TPR（真陽性率）と FPR（偽陽性率）の関係を見るグラフ**です。

AUCは、そのROC曲線の下の面積で、**しきい値全体を通した識別性能を1つの値で要約**します。

試験ではまず、

- **縦軸：** TPR（Recall）
- **横軸：** FPR
- **曲線全体を要約：** AUC

と切り分けます。

<figure class="gk-eyecatch" style="margin:16px 0 20px;">
  <picture>
    <source media="(max-width: 640px)" srcset="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/gk/roc-auc-mobile.png" width="1122" height="1402">
    <img src="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/gk/roc-auc.png" width="1200" height="630" alt="横軸FPR（偽陽性率）、縦軸TPR（真陽性率）のROC曲線と、その下を塗りつぶしたAUC。対角線はランダムな分類の基準" loading="lazy" decoding="async" style="display:block;width:100%;max-width:100%;height:auto;">
  </picture>
</figure>

## 直感的な説明

陽性と判定するしきい値を緩くすると、多くの陽性を拾いやすくなりますが、陰性を誤って陽性とするケースも増えやすくなります。

```text
しきい値を緩くする
→ TPR は上がりやすい
→ FPR も上がりやすい
```

逆に、しきい値を厳しくすると誤検知は減りやすい一方、見逃しが増えることがあります。

ROC曲線は、この**拾いやすさと誤検知のトレードオフを、しきい値全体で見る**ためのものです。

## 定義・仕組み

ROC曲線の軸は次のとおりです。

| 指標 | 式 | 意味 |
| --- | --- | --- |
| TPR | TP / (TP + FN) | 実際の陽性をどれだけ拾えたか。Recallと同じ |
| FPR | FP / (FP + TN) | 実際の陰性をどれだけ誤って陽性にしたか |

AUC（Area Under the Curve）はROC曲線の下の面積です。

```text
AUC = 1.0 に近い
→ 陽性と陰性をうまく順位付けできている

AUC = 0.5 付近
→ ランダムな順位付けに近い
```

AUCは、**1つの固定しきい値でのAccuracyやPrecisionではなく、スコアの順位付け性能をしきい値全体で要約する指標**と考えると分かりやすいです。

### 数値例：しきい値を変えるとROC曲線の点はどう動く？

ある二値分類モデルが、4件に対して「陽性らしさ」のスコアを出したとします。以下は説明用に作ったデータです。

| データ | 実際のクラス | 陽性スコア |
|---|---|---:|
| A | 陽性 | 0.9 |
| B | 陰性 | 0.7 |
| C | 陽性 | 0.6 |
| D | 陰性 | 0.2 |

**スコアがしきい値以上なら陽性と判定**します。実際の陽性2件・陰性2件という分母は変えず、判定だけを切り替えます。

| しきい値 | TP | FN | FP | TN | TPR = TP/2 | FPR = FP/2 |
|---|---:|---:|---:|---:|---:|---:|
| 0.95 | 0 | 2 | 0 | 2 | 0 | 0 |
| 0.8 | 1 | 1 | 0 | 2 | 0.5 | 0 |
| 0.5 | 2 | 0 | 1 | 1 | 1 | 0.5 |
| 0.2 | 2 | 0 | 2 | 0 | 1 | 1 |

例えばしきい値0.8では、Aだけが陽性判定です。Cを見逃すのでTPRは1/2、陰性のB・Dを誤検知しないのでFPRは0/2です。

しきい値を0.5に下げるとCも拾えますが、陰性のBまで陽性判定になります。このとき **TPRは0.5→1、FPRは0→0.5** に変わります。

これらの点を **横軸FPR・縦軸TPR** に順に配置したものがROC曲線です。AUCはその下の面積であり、表のどれか一行の正解率ではありません。ROC曲線の定義としきい値の扱いは[scikit-learn公式ドキュメント](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)でも確認できます。

> 数値例は仕組みの理解用です。4件だけで実際のモデル性能を評価するのは適切ではありません。

## いつ使う？（得意・不得意）

### 得意なこと

- 複数モデルの識別性能を、しきい値を固定する前に比較する
- しきい値全体での傾向を見る
- TPRとFPRの関係を確認する

### 苦手・注意点

AUCが高くても、実運用で使う**特定のしきい値**において誤検知が十分少ないとは限りません。

また、陽性クラスが非常に少なく、陽性予測の質を重視したい場合は、ROC曲線だけでなく[Precision-Recall曲線](/gk/precision-recall-curve/)も確認します。

```text
ROC
→ TPR と FPR

PR曲線
→ Precision と Recall
```

クラス不均衡だから必ずROCが不適切、または必ずPRが優れる、と機械的に決めるのではなく、**何を評価したいか**を見ることが大切です。

## G検定ひっかけポイント

### ROC曲線の横軸をPrecisionとしない

誤りです。

```text
縦軸 → TPR（Recall）
横軸 → FPR
```

### AUCが高い＝特定しきい値で誤検知が少ない

誤りです。AUCはしきい値全体を要約した指標です。

### AUCはAccuracyと同じ

違います。

- Accuracy：1つの判定結果で、全体の正解割合を見る
- ROC-AUC：しきい値全体で、陽性と陰性の識別性能を見る

### 「しきい値に依存しない」の意味

AUCは複数のしきい値を通した曲線全体を要約するので、**1つのしきい値だけに固定された指標ではない**という意味です。

## まとめ（試験直前用）

- ROC曲線：**TPR と FPR** の関係
- 縦軸は TPR＝Recall、横軸は FPR
- AUC：ROC曲線全体を1つの値で要約
- AUCが高くても特定しきい値の誤検知率までは分からない
- 陽性クラス重視ではPR曲線との使い分けも確認する

{% include gk_article_footer.html %}
