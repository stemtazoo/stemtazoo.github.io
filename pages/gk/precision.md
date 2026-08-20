---
layout: page
title: Precision（適合率）とは？FPとの関係で覚える【G検定】
description: "Precision（適合率）を、陽性と予測したもののうち実際に陽性だった割合として整理し、分母がTP＋FPであること、FP（誤検知）が増えるとPrecisionが下がることをG検定の判断軸として解説します。RecallやAccuracyとの違いも、何を分母に見るかで切り分けます。"
permalink: /gk/precision/
tags: [gk, 機械学習, 評価指標, 頻出]
gk_section: 機械学習の概要/モデルの選択・評価
gk_order: 3
last_modified_at: 2026-08-21
---

## まず結論

Precision（適合率）は、**陽性と予測したものの中で、実際に陽性だった割合**です。

式は次のとおりです。

**Precision = TP / (TP + FP)**

G検定では、まず

> **分母は「予測で陽性にしたもの」**

と覚えると、Recallとの混同を防ぎやすくなります。

## 直感的な説明

異常検知で「異常です」とアラートを出したとします。

Precisionが見ているのは、

> **そのアラート、本当に異常だった割合はどれくらい？**

ということです。

```text
本当に異常 → TP
正常なのに異常と警告 → FP
```

FPが増えるほど、無駄なアラートが増えるのでPrecisionは下がります。

## 定義・仕組み

混同行列との関係は次のとおりです。

|  | 予測：陽性 | 予測：陰性 |
| --- | --- | --- |
| 実際：陽性 | TP | FN |
| 実際：陰性 | FP | TN |

Precisionでは、**予測陽性の列**だけを見ます。

```text
予測陽性
= TP + FP

そのうち正解
= TP
```

したがって、

**Precision = TP / (TP + FP)**

です。

この「どこを分母にするか」が、評価指標を切り分ける重要ポイントです。

## いつ使う？（得意・不得意）

### 得意なこと

- 誤検知（FP）を減らしたい
- アラートや通知の信頼性を重視したい
- 陽性と判定した結果の確からしさを見たい

例：

- スパム判定
- 不正検知
- 異常検知のアラート

### 苦手・注意点

Precisionが高くても、見逃し（FN）が多い可能性があります。

そのため、

- **Precision**：予測陽性の信頼性
- [**Recall**](/gk/recall/)：実際の陽性をどれだけ拾えたか

を使い分けます。

両方のバランスを見たい場合は、[F1-score](/gk/f1-score/)を使います。

## G検定ひっかけポイント

### Precisionは「実際の陽性」を分母にする

誤りです。それはRecallの考え方です。

```text
Precision
→ TP / (TP + FP)
→ 予測陽性が分母

Recall
→ TP / (TP + FN)
→ 実際の陽性が分母
```

### Precisionが高い＝見逃しが少ない

誤りです。

見逃しに直接関係するのはFNで、Recallが重視する誤りです。

### PrecisionはAccuracyと同じ

違います。

- [Accuracy](/gk/accuracy/)：全体のうち正しく予測できた割合
- Precision：陽性と予測したものの中で正しかった割合

### 「Precisionが高い＝モデル全体が良い」と決めない

評価したい目的によって、Recall、F1-score、ROC-AUCなど他の指標も確認します。

## まとめ（試験直前用）

- Precision = **TP / (TP + FP)**
- 分母は**予測陽性**
- FP（誤検知）が増えるとPrecisionは下がる
- Recallは実際の陽性を分母にする
- 「誤検知を抑えたい」ならPrecisionを疑う

{% include gk_article_footer.html %}
