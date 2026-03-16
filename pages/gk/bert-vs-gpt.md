---
layout: page
title: BERTとGPTの違い【比較チートシート｜G検定対策】
permalink: /gk/bert-vs-gpt/
tags: [gk, nlp, transformer, cheatsheet]
gk_section: ディープラーニングの応用例/自然言語処理
gk_order: 3
---

## まず結論
- **BERTは「意味理解」向き、GPTは「文章生成」向き**のTransformerモデルである。
- G検定では「**双方向か一方向か**」「**理解か生成か**」を見抜けるかが合否を分ける。

## 直感的な説明
- **BERT**：文章を最初から最後まで一気に読んで意味を理解する「読解の専門家」
- **GPT**：これまでの文章をもとに続きを書く「作家」

同じ Transformer でも、  
👉 **使い方と得意分野が真逆** なのが最大のポイント。

## 定義・仕組み
### BERT（Bidirectional Encoder Representations from Transformers）
- Transformer **Encoderのみ**を使用
- **双方向**に文脈を考慮
- 事前学習タスク
  - Masked Language Model（MLM）
  - Next Sentence Prediction（NSP）

### GPT（Generative Pre-trained Transformer）
- Transformer **Decoder構造**を使用
- **一方向（左→右）**の自己回帰モデル
- 事前学習タスク
  - 次の単語予測のみ

## いつ使う？（得意・不得意）
### BERTが得意
- 文書分類
- 感情分析
- 質問応答
- 文の意味理解

### GPTが得意
- 文章生成
- 要約
- チャットボット
- ストーリー生成

### 注意点
- **文章生成 → GPT**
- **意味理解 → BERT**
と割り切ると迷わない。

## G検定ひっかけポイント
G検定では、次の表現で混同させてくる。

### よくあるひっかけ対応表

| 選択肢の表現 | 正解 |
|---|---|
| 文の前後を同時に考慮 | BERT |
| 次の単語を予測 | GPT |
| 双方向Transformer | BERT |
| 自己回帰モデル | GPT |
| Masked Language Model | BERT |
| 文章生成に強い | GPT |

### 超重要な切り方
- 「**一方向**」と書いてあったら **BERTは切る**
- 「**双方向**」と書いてあったら **GPTは切る**

## まとめ（試験直前用）
- **BERT：双方向・意味理解・Encoder**
- **GPT：一方向・文章生成・自己回帰**
- MLM / NSP → BERT
- 次単語予測 → GPT
- 迷ったら  
  👉 **理解＝BERT、生成＝GPT**
