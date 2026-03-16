---
layout: page
title: 最適化手法まとめ（SGD / Adam / AdaGrad / RMSprop / AMSGrad / AdaBound / AMSBound / Adadelta）【G検定対策】
permalink: /gk/optimizer-comparison/
tags: [gk, cheatsheet, neural_network]
gk_section: ディープラーニングの概要/最適化手法
gk_order: 21
---

## まず結論
- G検定の最適化手法は **「学習率をどう扱うか」** で一発で切り分ける。
- 覚えるべき軸は **固定か／自動調整か／途中で性質が変わるか** の3つだけ。

## 直感的な説明
最適化手法は、全部「坂を下る方法」ですが、  
**どれくらい慎重に下るか** が違います。

- SGD：一定の歩幅で下る
- Adaptive系：地形に応じて歩幅を変える
- Bound系：最初は賢く、最後は堅実に

👉 名前ではなく **性格** を見るのがコツです。

## 定義・仕組み（まずは分類）
最適化手法は、次の3グループに分けると一気に楽になります。

### ① 学習率固定系
- SGD

### ② 学習率自動調整系（Adaptive系）
- AdaGrad
- RMSprop
- Adadelta
- Adam
- AMSGrad

### ③ 性質が切り替わる系（Bound系）
- AdaBound
- AMSBound

## いつ使う？（得意・不得意）

### 学習率固定系
| 手法 | 特徴 |
|---|---|
| SGD | シンプル・汎化性能が高いが収束は遅い |

### Adaptive系（学習率を自動調整）
| 手法 | 何が特徴？ |
|---|---|
| AdaGrad | 頻出特徴の学習率が小さくなりすぎる |
| RMSprop | AdaGradの欠点を改善 |
| Adadelta | 学習率を明示的に設定しない |
| Adam | モーメント＋RMSpropの組み合わせ |
| AMSGrad | Adamの収束性問題を改善 |

### Bound系（前半と後半で性格が変わる）
| 手法 | 狙い |
|---|---|
| AdaBound | Adam → SGD に近づく |
| AMSBound | AMSGrad → SGD に近づく |

## G検定ひっかけポイント（最重要）
G検定では **ここだけ** を見ています。

### 超重要キーワード対応表
| 問題文の表現 | 正解候補 |
|---|---|
| 学習率固定 | SGD |
| 勾配の二乗和 | AdaGrad |
| AdaGradの改良 | RMSprop |
| 学習率を明示的に設定しない | Adadelta |
| モーメント＋適応的学習率 | Adam |
| Adamの収束性改善 | AMSGrad |
| Adam＋SGDの良さ | AdaBound |
| AMSGrad＋SGDの良さ | AMSBound |

### よくある間違い
- ❌ RMSprop＝Adam  
- ❌ AdaBound＝AMSGrad  
- ❌ AMSBound＝Adam  
- ❌ TF-IDFと混同（最適化ですらない）

## 最終まとめ表（これだけ見ればOK）
| 手法 | 一言で |
|---|---|
| SGD | 学習率固定・堅実 |
| AdaGrad | 学習率が減りすぎる |
| RMSprop | AdaGrad改良 |
| Adadelta | 学習率不要 |
| Adam | 高速・不安定 |
| AMSGrad | Adamの安定版 |
| AdaBound | Adam → SGD |
| AMSBound | AMSGrad → SGD |

## まとめ（試験直前用）
- まず「学習率固定か？」を見る
- 次に「Adaptive系か？」を見る
- 最後に「途中でSGDに近づくか？」を見る
- Adamが出たらAdaBound
- AMSGradが出たらAMSBound
- 名前より **挙動** で判断する
