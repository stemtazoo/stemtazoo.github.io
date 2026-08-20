---
layout: page
title: Accuracy（正解率）とは？クラス不均衡の注意点【G検定対策】
description: Accuracy（正解率）は、全データのうち正しく分類できた割合を表す指標です。TP・TNを使う式、クラス不均衡で高く見える弱点、Precision・Recall・F1-scoreとの使い分けをG検定の選択肢判断に合わせて整理します。
permalink: /gk/accuracy/
tags: [gk, machine_learning, metrics, frequent]
gk_section: 機械学習の概要/モデルの選択・評価
gk_order: 2
last_modified_at: 2026-08-21
---

## まず結論

Accuracy（正解率）は、**全データのうち、正しく分類できた割合**です。

```text
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

G検定では、次の判断が重要です。

> **全体の正解率 → Accuracy**
>
> **クラスが大きく偏る → Accuracyだけで判断しない**

## 直感的な説明

100問中90問正解なら、Accuracyは90%です。

分類でも同じで、陽性・陰性を問わず、**全体で何件正しく分類できたか**を見ます。

ただし、例えば正常99件・異常1件のデータで、全部を「正常」と予測してもAccuracyは99%になります。

```text
Accuracyは高い
でも異常は1件も拾えていない
```

このように、Accuracyは分かりやすい一方で、クラス不均衡では弱点があります。

## 定義・仕組み

混同行列では、正解した **TPとTN** を分子に使います。

|  | 予測：陽性 | 予測：陰性 |
|---|---|---|
| 実際：陽性 | TP | FN |
| 実際：陰性 | FP | TN |

- TP：陽性を陽性と予測
- TN：陰性を陰性と予測
- FP：陰性を陽性と誤予測
- FN：陽性を陰性と誤予測

Accuracyは二値分類だけでなく、多クラス分類でも **正解数 ÷ 全件数** という考え方で使えます。

## いつ使う？（得意・不得意）

### 得意なこと

- クラスの偏りが小さい
- 各クラスの誤りを同程度に扱いたい
- 全体性能をシンプルに比較したい

### 苦手・注意点

- クラスが大きく偏っている
- 少数派クラスの見逃しが重大
- FPとFNのコストが大きく違う

このような場合は、[Precision](/gk/precision/)、[Recall](/gk/recall/)、[F1-score](/gk/f1-score/)なども確認します。

## G検定ひっかけポイント

| 指標 | 判断ワード |
|---|---|
| Accuracy | 全体の正解率 |
| [Precision](/gk/precision/) | 誤検知を減らす・陽性予測の信頼性 |
| [Recall](/gk/recall/) | 見逃しを減らす・実際陽性を拾う |
| [F1-score](/gk/f1-score/) | PrecisionとRecallのバランス |

特に注意するのは次です。

- Accuracyが高くても、少数派クラスを全く検出できないことがある
- Accuracyは「陽性だけの正解率」ではない
- クラス不均衡では、多数派だけを予測する単純なベースラインと比較する
- 「Accuracyが高い＝良いモデル」と無条件に判断しない

## まとめ（試験直前用）

- Accuracy = **全体の正解数 ÷ 全件数**
- 二値分類では `(TP + TN) / 全件数`
- クラス不均衡では高く見えることがある
- 見逃し重視ならRecall、誤検知重視ならPrecision
- 高いAccuracyだけでモデル性能を断定しない

次に読むなら、[Precision](/gk/precision/)と[Recall](/gk/recall/)を確認すると、評価指標の役割が整理しやすくなります。

{% include gk_article_footer.html %}