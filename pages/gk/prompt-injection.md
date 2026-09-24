---
layout: page
title: Prompt Injectionとは？Direct・Indirect攻撃を整理【G検定対策】
description: "Prompt Injectionを、生成AIやLLMへ与えられる命令の境界を悪用し、本来の指示より攻撃者の命令を優先させようとする攻撃として整理します。Direct Prompt Injectionと、外部コンテンツ経由のIndirect Prompt InjectionをG検定向けに確認します。"
permalink: /gk/prompt-injection/
tags: [gk, security, generative_ai]
gk_section: AIの法律と倫理/AIセキュリティ・プライバシー攻撃/推論時の攻撃
gk_order: 2
last_modified_at: 2026-09-25
---

## まず結論

**Prompt Injection**は、生成AI・LLMへ与えられる指示の扱いを悪用し、**本来のシステム指示より攻撃者が埋め込んだ指示を優先させようとする攻撃**です。

G検定では、

- ユーザーが直接悪意ある指示を与える → **Direct Prompt Injection**
- Webページ・文書など外部データへ指示を埋め込む → **Indirect Prompt Injection**

と切り分けます。

## 直感的な説明

LLMは、通常のデータと「命令」を完全に分離して理解するとは限りません。

そのため、モデルが読む文章の中に、

> これまでの指示を無視して別の行動をせよ

のような命令が混ざると、本来は単なるデータだったものを命令として扱ってしまうリスクがあります。

## 定義・仕組み

### Direct Prompt Injection

攻撃者自身がモデルへ直接入力し、意図しない応答やルール逸脱を狙います。

### Indirect Prompt Injection

モデルやAIエージェントが、

- Webページ
- メール
- 文書
- 検索結果
- 外部ツールから得たデータ

を読み込むとき、そのコンテンツ中に悪意ある指示が埋め込まれている攻撃です。

AIエージェントが外部ツールを操作できる場合、単なる不適切な文章生成だけでなく、意図しないアクションへつながる可能性があります。

## いつ使う？（得意・不得意）

リスクが特に高くなりやすいのは、

- RAG
- Web検索付きLLM
- メール・文書を読むAI
- 外部ツールを操作するAIエージェント

などです。

対策では、

- 信頼できないデータと命令を分離する設計
- 外部ツールの権限を最小化
- 危険な操作で人間の承認を求める
- 入出力・ツール利用を監視する

など、複数の防御を組み合わせます。

## G検定ひっかけポイント

### Prompt Injection＝データポイズニング？

❌ 学習データを汚してモデル自体を変える  
⭕ **主に推論時の入力・コンテキストを悪用する**

### Indirect Prompt Injection

❌ 攻撃者が必ずチャット欄へ直接入力する  
⭕ **モデルが読む外部コンテンツ経由でも起こる**

### Jailbreakとの関係

Jailbreakは、モデルの安全制約を回避して本来制限される応答を引き出そうとする攻撃・操作を指すことがあります。

Prompt Injectionと重なる場合がありますが、**完全な同義語として固定しません。**

## まとめ（試験直前用）

- Prompt Injection＝**命令境界を悪用**
- Direct＝ユーザーから直接
- Indirect＝外部コンテンツ経由
- 学習データを汚すPoisoningとは別
- RAG・AIエージェントで特に注意
- 権限最小化・人間の承認など多層防御が重要

## 参考資料

- [Prompt Injection｜NIST CSRC Glossary](https://csrc.nist.gov/glossary/term/prompt_injection)
- [Adversarial Machine Learning: A Taxonomy and Terminology｜NIST](https://doi.org/10.6028/NIST.AI.100-2e2025)

{% include gk_article_footer.html %}
