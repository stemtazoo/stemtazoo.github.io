---
layout: page
title: AutoAugment・RandAugment・TrivialAugmentの違い【画像データ拡張 完全比較｜G検定対策】
permalink: /gk/auto-rand-trivial-augment/
tags: [gk, cnn, cheatsheet]
---

## まず結論
- **AutoAugment／RandAugment／TrivialAugment の違いは「最適化するか・指定するパラメータ数」だけ**である。
- G検定では「**探索する？ランダム？1回だけ？**」で即切る。

## 直感的な説明
3つは「画像をどう拡張するか」を決める**考え方の違い**です。

- **AutoAugment**  
  👉 一番よくなる拡張方法を「探す」
- **RandAugment**  
  👉 強めの拡張を「ランダムに振る」
- **TrivialAugment**  
  👉 1つだけ「ランダムにかける」

つまり、

> **考える → Auto**  
> **振る → Rand**  
> **1発 → Trivial**

です。

## 定義・仕組み
### AutoAugment
- 拡張操作の **種類・順序・強度** を自動探索
- 強化学習・探索アルゴリズムを使用
- データセットごとに最適なポリシーを学習

特徴：
- メタ学習的
- 高性能だが計算コスト大

### RandAugment
- 事前定義された拡張セットを使用
- 指定するのは **回数（N）と強度（M）だけ**
- 拡張の種類や順序はランダム

特徴：
- シンプル
- パラメータが少ない
- 最適化はしない

### TrivialAugment
- 事前定義された拡張セットから
- **1つの操作をランダムに1回だけ適用**
- 強度もランダム

特徴：
- 最小構成
- 実装が非常に簡単

## いつ使う？（得意・不得意）
### AutoAugmentが向く場面
- 計算資源が豊富
- 最高性能を狙いたい

### RandAugmentが向く場面
- 実務・研究のバランス
- 再現性と性能を両立したい

### TrivialAugmentが向く場面
- ベースライン
- 実装コストを最小にしたい

## G検定ひっかけポイント（最重要）
### よくある誤解
- ❌「全部ランダムだから同じ」
- ❌「RandAugmentは最適化する」
- ❌「正規化手法である」

### 正しい判断基準
- **拡張方法を探索 → AutoAugment**
- **回数と強度だけ指定 → RandAugment**
- **1回だけ適用 → TrivialAugment**

## 完全比較表（これだけ見ればOK）
| 項目 | AutoAugment | RandAugment | TrivialAugment |
|---|---|---|---|
| 拡張の選び方 | 探索・最適化 | ランダム | ランダム |
| 最適化 | する | しない | しない |
| 指定パラメータ | 多い | 回数N・強度M | なし |
| 適用回数 | 複数 | 複数 | 1回 |
| 計算コスト | 高い | 低い | 非常に低い |
| G検定キーワード | 自動探索 | 強度と回数 | 1つだけ |

## まとめ（試験直前用）
- AutoAugment：拡張を探す
- RandAugment：強く振る
- TrivialAugment：1発だけ
- 最適化するのはAutoだけ
- 「探索／ランダム／1回」で切る
