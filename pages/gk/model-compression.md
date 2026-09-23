---
layout: page
title: モデル圧縮まとめ｜Pruning・Quantization・Knowledge Distillation【G検定】
description: "モデル圧縮を、Pruningは重みや構造を削る、Quantizationは数値表現のbit幅を下げる、Knowledge DistillationはTeacherの出力情報をStudentへ移すという役割で整理します。圧縮しても実機速度が必ず上がるとは限らない点も確認します。"
permalink: /gk/model-compression/
tags: [gk, model_compression]
gk_section: ディープラーニングの応用例/モデルの軽量化/モデル圧縮の基本・手法
gk_order: 1
last_modified_at: 2026-09-24
---

## まず結論

モデル圧縮は、モデルの

- サイズ
- メモリ使用量
- 計算量
- 消費電力・遅延

などを抑えるための技術群です。

代表的には、

- [Pruning](/gk/pruning/) → **不要・重要度の低い重みや構造を削る**
- [Quantization](/gk/quantization/) → **数値表現を低精度化**
- [Knowledge Distillation](/gk/knowledge-distillation/) → **Teacherの知識をStudentへ移す**

で整理します。

## 直感的な説明

- 削る → Pruning
- 数値を粗くする → Quantization
- 大きな教師から小さな生徒へ学ばせる → Distillation

と覚えると切り分けやすくなります。

## 定義・仕組み

### Pruning

重み・チャネル・フィルタなどを削減します。

- 非構造化Pruning → 個々の重みを0にする
- 構造化Pruning → チャネル・フィルタ単位で削る

### Quantization

FP32などの数値をINT8など低bit表現へ変換します。

モデルサイズ・メモリ帯域・対応ハードウェアでの演算効率改善が期待できます。

### Knowledge Distillation

Teacherの出力分布や中間表現などをStudentの学習へ利用します。

必ずしもTeacherのパラメータをコピーするわけではありません。

## いつ使う？（得意・不得意）

- モバイル・エッジ
- 低遅延推論
- メモリ制約
- 消費電力制約

などで重要です。

ただし、

> パラメータ数を減らせば必ず実機で高速化する

とは限りません。

実際の速度は、

- ハードウェア
- ランタイム
- 演算形式
- メモリアクセス
- 疎行列サポート

などにも依存します。

## G検定ひっかけポイント

### Dropout

❌ 推論時モデルの重みを恒久的に削除する圧縮  
⭕ **学習時の正則化手法**

### Quantization

❌ 必ずネットワーク構造を変更する  
⭕ **主に数値表現を低精度化**

### Distillation

❌ Teacherの重みをそのままStudentへコピー  
⭕ **Teacherの出力情報などを学習信号として利用**

## まとめ（試験直前用）

- Pruning＝**削る**
- Quantization＝**bit幅を下げる**
- Distillation＝**知識を移す**
- 圧縮＝必ず精度低下ではない
- 圧縮＝必ず実機高速化でもない
- ハードウェアとの組合せも重要

{% include gk_article_footer.html %}
