---
layout: page
title: AdaBoundとは？動的な学習率境界を使う最適化手法【G検定】
description: "AdaBoundを、Adam系の実効学習率に時間とともに狭まる上限・下限を設け、学習後半にSGDに近い更新へ移ることを狙う最適化手法として整理します。Adam・AMSBoundとの違いをG検定向けに確認します。"
permalink: /gk/adabound/
tags: [gk, neural_network, optimization]
gk_section: ディープラーニングの概要/最適化手法
gk_order: 10
last_modified_at: 2026-08-21
---

## まず結論

AdaBoundは、**Adam系の実効学習率へ動的な上限・下限を設ける最適化手法**です。

学習が進むにつれて境界を狭め、後半はSGDに近い更新へ移ることを狙います。

## 直感的な説明

最初は状況に応じて歩幅を変え、学習が進むほど歩幅の許容範囲を狭めるイメージです。

```text
学習初期 → Adam系の適応的な更新
学習後半 → 境界が狭まりSGDに近い更新
```

## 定義・仕組み

AdaBoundでは、パラメータごとの実効学習率に**時間とともに変化する下限・上限**を設けます。

重要なのは、途中で最適化手法を突然SGDへ切り替えるのではなく、**境界を狭めることでSGDに近い挙動へ滑らかに移す**点です。

## いつ使う？（得意・不得意）

### 狙い

- Adam系の適応的更新を利用する
- 学習後半の実効学習率を制約する
- SGDに近い更新へ移行する

### 注意点

- 常にAdamやSGDより高性能とは限らない
- 学習率スケジューラそのものではない
- 正則化手法ではない

## G検定ひっかけポイント

- ⭕ 動的な学習率の上限・下限 → AdaBound
- ⭕ Adamを基盤とするBound系 → AdaBound
- ❌ 学習率を一定値へ最初から固定 → AdaBoundではない
- ❌ AMSGradを基盤 → AMSBound側

## まとめ（試験直前用）

- AdaBound＝Adam系＋動的な学習率境界
- 上限・下限は時間とともに変化
- 学習後半はSGDに近い更新を狙う
- AMSBoundはAMSGrad基盤
- 「Bound＝動的な境界」で切る

{% include gk_article_footer.html %}
