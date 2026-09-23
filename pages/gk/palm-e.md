---
layout: page
title: PaLM-Eとは？ロボットのセンサ情報を言語モデルへ統合【G検定対策】
description: "PaLM-Eを、画像やロボット状態などの連続的なセンサ入力を言語モデルへ取り込むEmbodied Multimodal Language Modelとして整理します。PaLMとの違い、ロボット計画・視覚質問応答などのタスク、EはEnvironmentではなくEmbodiedと捉える点を確認します。"
permalink: /gk/palm-e/
tags: [gk, multimodal, transformer, embodied_ai]
gk_section: ディープラーニングの応用例/マルチモーダル/汎用マルチモーダルモデル
gk_order: 2
last_modified_at: 2026-09-23
---

## まず結論

**PaLM-E**は、テキストだけでなく、画像やロボットの状態などの**連続的なセンサ入力を言語モデルへ取り込むEmbodied Multimodal Language Model**です。

G検定では、

- PaLMを基盤にしたマルチモーダル化
- 画像・センサ・ロボット状態
- embodied（身体化された）タスク

を押さえます。

**Eを単純にEnvironmentの略と覚えない**ことが重要です。

## 直感的な説明

通常の言語モデルが文章だけを読んで答えるのに対し、PaLM-Eは、

> カメラで見えているもの  
> ロボットの現在状態  
> テキスト指示

などを同じモデルへ入力して、現実世界のタスクに利用します。

## 定義・仕組み

PaLM-Eでは、画像や状態などの連続的な入力を埋め込みへ変換し、**言語トークンと同じように言語モデルへ入力**します。

これにより、

- ロボット計画
- 視覚質問応答
- 画像説明

など複数のembodied・視覚言語タスクを1つのモデルで扱います。

重要なのは、単なる「ロボット制御器」ではなく、**大規模言語モデルへマルチモーダルな実世界入力を統合する**設計です。

## いつ使う？（得意・不得意）

PaLM-Eは、

- ロボットへの自然言語指示
- 視覚情報を含む計画
- センサ状態を踏まえた応答
- 視覚言語タスク

などの研究で使われました。

ただし、

> PaLM-E＝ロボット専用モデル

と限定しません。

論文では一般的な視覚言語タスクでも評価されています。

## G検定ひっかけポイント

### E＝Environment？

❌ EnvironmentのEと暗記  
⭕ **Embodied Multimodal Language Modelとして整理する**

### PaLMとの違い

- PaLM → 言語モデル
- PaLM-E → **画像・センサ等を言語モデルへ統合**

### PaLM-E＝ルールベース制御？

❌ 人がIF-THENルールを記述する  
⭕ **マルチモーダル入力を扱う大規模モデル**

## まとめ（試験直前用）

- PaLM-E＝**Embodied Multimodal Language Model**
- テキスト＋画像＋センサ状態
- 実世界・ロボットタスクへ利用
- 連続入力を埋め込みとして言語モデルへ投入
- PaLM単体とは入力モダリティが異なる
- **E＝Environmentと決めつけない**

## 参考資料

- [PaLM-E: An Embodied Multimodal Language Model｜arXiv](https://arxiv.org/abs/2303.03378)

{% include gk_article_footer.html %}
