---
layout: page
title: Knowledge Distillation（知識蒸留）とは？TeacherとStudent【G検定】
description: "Knowledge Distillationを、大きなTeacherモデルの出力分布などを学習信号としてStudentモデルへ知識を移す手法として整理します。Soft Targets、Temperature、通常ラベルとの併用を押さえ、Pruning・Quantizationとの違いを確認します。"
permalink: /gk/knowledge-distillation/
tags: [gk, neural_network, model_compression]
gk_section: ディープラーニングの応用例/モデルの軽量化/モデル圧縮の基本・手法
gk_order: 4
last_modified_at: 2026-09-24
---

## まず結論

**Knowledge Distillation（知識蒸留）**は、大きな**Teacher**モデルの出力情報などを使って、**Student**モデルを学習する方法です。

G検定では、

- Teacher / Student
- Soft Targets
- Temperature

を押さえます。

## 直感的な説明

正解ラベルが「猫」だけだと、他クラスとの関係は分かりません。

Teacherが、

- 猫 0.80
- トラ 0.15
- 犬 0.05

のような分布を出せば、Studentは「猫に近いがトラとも少し似ている」といった情報も学べます。

## 定義・仕組み

Teacherのlogitsに**Temperature**を適用し、より滑らかな確率分布を作る方法が代表的です。

この分布を**Soft Targets**としてStudentへ学習させます。

実際には、

- 正解ラベルへの損失
- Teacher出力への蒸留損失

を組み合わせることがあります。

## いつ使う？（得意・不得意）

代表的には、

- 大きなモデルから小さなモデルへ能力を移したい
- 推論コストを下げたい
- Studentの学習を補助したい

場合に使われます。

ただし、Studentが必ずTeacherと同等性能になるわけではありません。

また、蒸留はモデル圧縮だけでなく、知識移転の一般的な学習方法として使われる場合もあります。

## G検定ひっかけポイント

### Distillation＝重みコピー？

❌ Teacherのパラメータをそのままコピー  
⭕ **Teacherの出力情報などを学習信号にする**

### Soft Targets

❌ one-hot正解ラベルだけ  
⭕ **Teacherの確率分布など**

### Temperature

❌ 学習率  
⭕ **Teacher/Studentの出力分布の滑らかさに関係**

## まとめ（試験直前用）

- Distillation＝**Teacher → Student**
- Soft Targets
- Temperature
- 正解ラベルと併用する場合がある
- 重みコピーではない
- Pruning・Quantizationとは別の軽量化アプローチ

## 参考資料

- [Distilling the Knowledge in a Neural Network｜arXiv](https://arxiv.org/abs/1503.02531)

{% include gk_article_footer.html %}
