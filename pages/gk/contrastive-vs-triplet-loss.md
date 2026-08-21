---
layout: page
title: Contrastive LossとTriplet Lossの違い【G検定対策】
description: "Contrastive LossとTriplet Lossを、ペアで距離を調整するか、Anchor・Positive・Negativeの三つ組で相対距離を学ぶかという軸で比較します。margin、埋め込み学習、Cross Entropyとの違いをG検定の判断基準として整理します。"
permalink: /gk/contrastive-vs-triplet-loss/
tags: [gk, neural_network, metrics]
gk_section: ディープラーニングの概要/誤差関数
gk_order: 4
last_modified_at: 2026-08-22
---

## まず結論

Contrastive LossとTriplet Lossは、どちらも**埋め込み空間で距離関係を学ぶ損失関数**です。

最大の違いは入力の組です。

- **Contrastive Loss**：類似・非類似の**ペア**
- **Triplet Loss**：Anchor・Positive・Negativeの**三つ組**

G検定では、**ペアか三つ組か**を最初に見ると切り分けやすくなります。

## 直感的な説明

Contrastive Lossは、

> 「この2つは近づける？ 離す？」

と判断するイメージです。

Triplet Lossは、

> 「AnchorはNegativeよりPositiveに近くあるべき」

という**相対関係**を学びます。

```text
Contrastive
A ↔ B

Triplet
Positive ← Anchor → Negative
   近く        遠く
```

## 定義・仕組み

### Contrastive Loss

主に2つのデータをペアとして扱います。

- 類似ペア → 距離を小さくする
- 非類似ペア → 距離が近すぎるとペナルティ

標準的な形では、非類似ペアにmarginを設けることがあります。

### Triplet Loss

3つのデータを使います。

- **Anchor**：基準
- **Positive**：Anchorと近づけたいデータ
- **Negative**：Anchorから遠ざけたいデータ

目標は、概念的には次の関係です。

```text
距離(Anchor, Positive) + margin
<
距離(Anchor, Negative)
```

つまり、絶対的な距離だけではなく、**PositiveとNegativeの相対的な位置関係**を学びます。

## いつ使う？（得意・不得意）

| 観点 | Contrastive Loss | Triplet Loss |
|---|---|---|
| 入力 | 2点のペア | 3点の三つ組 |
| 代表語 | 類似・非類似 | Anchor / Positive / Negative |
| 学習の中心 | ペア間距離 | 相対距離 |
| 共通点 | 埋め込み・距離学習 | 埋め込み・距離学習 |

どちらも、顔認識・類似検索などで使われます。

性能は損失の名前だけで決まらず、**どのペア・三つ組を学習に選ぶか**も重要です。

## G検定ひっかけポイント

- ❌「Triplet Lossは2点のペアだけで学習する」
  - Anchor・Positive・Negativeの三つ組が基本です。
- ❌「Contrastive LossとTriplet Lossは分類クラス確率を直接最大化する」
  - 中心は埋め込み空間の距離関係です。
- ❌「Contrastive Lossは必ず絶対距離そのものを最小化するだけ」
  - 類似・非類似とmarginを使って距離関係を調整します。
- ❌「Triplet Lossならデータの選び方は重要ではない」
  - 三つ組の作り方は学習に大きく影響します。
- ⭕「Anchor / Positive / Negative」→ Triplet Loss
- ⭕「類似ペア / 非類似ペア」→ Contrastive Loss

### Cross Entropyとの違い

- 正解クラスの確率を高くする → **Cross Entropy**
- ペア・三つ組の距離関係を学ぶ → **Contrastive / Triplet Loss**

ただし実際のモデルでは、距離学習の損失と分類損失を**組み合わせて使う場合もあります**。

## まとめ（試験直前用）

- Contrastive Loss＝**ペア**
- Triplet Loss＝**Anchor・Positive・Negative**
- どちらも埋め込み・距離学習
- Tripletは相対距離が中心
- 「Anchor」が出たらTripletを疑う

{% include gk_article_footer.html %}
