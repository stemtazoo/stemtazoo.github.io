---
layout: page
title: Adam / RMSProp / AdaDelta / AdaBound の違い【4点比較｜G検定対策】
permalink: /gk/optimizer-compare-4/
tags: [gk]
gk_section: ディープラーニングの概要/最適化手法
gk_order: 12
---

## まず結論

Adam・RMSProp・AdaDelta・AdaBoundはいずれも**学習率を自動調整する最適化手法**だが、G検定では特に**「モーメントの使い方」と「学習率の制御方法（境界の有無）」の違い**を正確に区別できるかが問われる。

## 直感的な説明

4つの手法を人の運転にたとえると次のようになります。

* **RMSProp**：

  * 路面状況を見ながらアクセルを細かく調整
* **AdaDelta**：

  * 過去の運転履歴を見て、アクセル量そのものを決める
* **Adam**：

  * 進行方向（勢い）と路面状況の両方を考慮
* **AdaBound**：

  * Adamの運転に「速度制限」をかける

## 定義・仕組み（4点比較）

| 手法       | 主な特徴       | モーメント  | 学習率の境界 |
| -------- | ---------- | ------ | ------ |
| RMSProp  | 勾配の分散で調整   | 2次のみ   | なし     |
| AdaDelta | 学習率を不要に設計  | 2次＋更新量 | なし     |
| Adam     | 1次＋2次モーメント | 両方     | なし     |
| AdaBound | Adam＋境界制御  | 両方     | **あり** |

## いつ使う？（得意・不得意）

### RMSProp

* 非定常な問題
* RNNなどで利用される

### AdaDelta

* 学習率の初期値調整を省きたい場合

### Adam

* 多くの深層学習でデフォルト
* 高速に収束

### AdaBound

* Adamの不安定さを避けたい場合
* 汎化性能を重視

## G検定ひっかけポイント

G検定では、**AdamとAdaBoundの混同**が最頻出です。

### よくある誤解

* AdaBoundはAdamと同じ → ✕
* AdaDeltaは学習率に上限・下限がある → ✕

### 正誤を切る判断基準

* **1次＋2次モーメント？** → Adam系
* **学習率に上限・下限？** → AdaBound
* **学習率が不要？** → AdaDelta

## まとめ（試験直前用）

* RMSProp：2次モーメント
* AdaDelta：学習率不要
* Adam：1次＋2次
* AdaBound：Adam＋学習率境界
* 境界が出たら即AdaBound
