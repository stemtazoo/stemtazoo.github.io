---
layout: page
title: Quantization（量子化）とは？INT8・PTQ・QAT【G検定対策】
description: "Quantizationを、モデルの重みや活性値をFP32などからINT8など低bit表現へ変換し、モデルサイズやメモリ使用量、対応ハードウェアでの演算効率を改善する手法として整理します。PTQとQAT、Pruningとの違いを確認します。"
permalink: /gk/quantization/
tags: [gk, neural_network, model_compression]
gk_section: ディープラーニングの応用例/モデルの軽量化/モデル圧縮の基本・手法
gk_order: 3
last_modified_at: 2026-09-24
---

## まず結論

**Quantization（量子化）**は、モデルの重みや活性値を、FP32などからINT8などの**低bit表現へ変換する**モデル軽量化手法です。

G検定では、

- 数値精度を下げる
- モデルサイズ・メモリを削減
- PTQ / QAT

を押さえます。

## 直感的な説明

32bitで細かく表していた数値を、8bitなど少ない段階で表すイメージです。

同じ数のパラメータでも、1個あたりの保存bit数を減らせるため、モデルを小さくできます。

## 定義・仕組み

### Post-Training Quantization（PTQ）

学習済みモデルを後から量子化します。

再学習コストを抑えやすい一方、低bit化による誤差で性能が下がる場合があります。

### Quantization-Aware Training（QAT）

学習・Fine-tuning中に量子化誤差を模擬し、低精度での推論を意識してモデルを適応させます。

一般にPTQより手間は増えますが、精度を保ちやすい場合があります。

## いつ使う？（得意・不得意）

- モバイル
- エッジデバイス
- メモリ制約
- 低遅延推論

で使われます。

ただし、低bit演算による高速化は**ハードウェアや推論ランタイムが対応しているか**にも依存します。

## G検定ひっかけポイント

### Quantization＝Pruning？

❌ 重みを削除する  
⭕ **数値表現のbit幅を下げる**

### PTQ

❌ 学習前にだけ行う  
⭕ **学習済みモデルを後処理で量子化**

### QAT

❌ 量子化とは無関係な通常学習  
⭕ **量子化誤差を意識して学習**

## まとめ（試験直前用）

- Quantization＝**低bit化**
- FP32 → INT8など
- PTQ＝学習後
- QAT＝量子化を意識して学習
- モデルサイズ・メモリ削減
- 実機高速化はハードウェア依存

## 参考資料

- [Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference｜arXiv](https://arxiv.org/abs/1712.05877)

{% include gk_article_footer.html %}
