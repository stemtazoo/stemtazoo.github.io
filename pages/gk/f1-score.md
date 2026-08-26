---
layout: page
title: F1-scoreとは？PrecisionとRecallの調和平均【G検定】
description: "F1-scoreを、PrecisionとRecallの調和平均で誤検知と見逃しのバランスを見る分類指標として整理します。どちらか一方だけが高くてもF1は高くなりにくいこと、TNを式に直接含まないこと、クラス不均衡でも常に最適とは限らない点をG検定の判断軸で確認します。"
permalink: /gk/f1-score/
tags: [gk, 機械学習, 評価指標, 頻出]
gk_section: 機械学習の概要/モデルの選択・評価/分類の評価指標
gk_order: 5
last_modified_at: 2026-08-26
---

## まず結論

F1-scoreは、**Precision（適合率）とRecall（再現率）のバランスを、調和平均で1つの値にまとめた指標**です。

```text
Precision → 誤検知を気にする
Recall → 見逃しを気にする
F1-score → 両方をまとめて見る
```

どちらか一方だけが高くても、F1-scoreは高くなりにくいのが特徴です。

## 直感的な説明

異常検知を例にすると、

- Precision：異常だと言ったものは、本当に異常だった？
- Recall：本当に異常だったものを、ちゃんと拾えた？

という違いがあります。

F1-scoreは、この2つを同時に見たいときの指標です。

```text
誤検知も多い → 困る
見逃しも多い → 困る

両方のバランスを見る
→ F1-score
```

## 定義・仕組み

F1-scoreは次の式で表します。

**F1-score = 2 × (Precision × Recall) / (Precision + Recall)**

これは単純平均ではなく、**調和平均**です。

例えば、Precisionが高くてもRecallが非常に低ければ、F1-scoreも高くなりません。

また、

- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)

なので、F1-scoreには主にTP・FP・FNが関係します。

**TN（真陰性）は式に直接入りません。**

## いつ使う？（得意・不得意）

### 得意なこと

- 誤検知と見逃しの両方を気にしたい
- 陽性クラスの性能を中心に評価したい
- Accuracyだけでは実態を捉えにくい場面を補いたい

### 苦手・注意点

F1-scoreがクラス不均衡で有用なことは多いですが、**不均衡なら常にF1-scoreが最適という意味ではありません**。

例えば、

- 誤検知を特に重く見る → [Precision](/gk/precision/)
- 見逃しを特に重く見る → [Recall](/gk/recall/)
- 全体の正解割合を見る → [Accuracy](/gk/accuracy/)

というように、評価目的によって使い分けます。

## G検定ひっかけポイント

### F1-scoreは単純平均ではない

誤りです。**調和平均**です。

### TNを直接使う

誤りです。

```text
F1-score
→ Precision と Recall から求める
→ TN は式に直接入らない
```

### F1-scoreが高い＝全クラスで完璧

誤りです。F1-scoreは、PrecisionとRecallのバランスを見ています。

多クラス分類ではmacro平均やmicro平均など別の集約方法もあるため、「F1-scoreが高い」という一言だけでは、全クラスで均等に高性能とは限りません。

### PrecisionとRecallは必ずトレードオフする

しきい値を動かすと一方が上がり他方が下がることは多いですが、**必ずそうなると決めつける必要はありません**。

試験では、F1-scoreが両者をまとめて評価する指標だと押さえれば十分です。

## まとめ（試験直前用）

- F1-score：PrecisionとRecallの**調和平均**
- どちらか一方だけが高くてもF1は上がりにくい
- TNは式に直接入らない
- 誤検知と見逃しの両方を気にするときに使う
- クラス不均衡でも、目的に応じてPrecision・Recall・Accuracyと使い分ける

{% include gk_article_footer.html %}
