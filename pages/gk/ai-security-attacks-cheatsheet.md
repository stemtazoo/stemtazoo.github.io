---
layout: page
title: AIセキュリティ攻撃まとめ｜Poisoning・Evasion・Prompt Injection・窃取【G検定】
description: "AIセキュリティ攻撃を、学習データを汚すPoisoning、推論入力を細工するEvasion、生成AIの命令境界を悪用するPrompt Injection、学習データやモデルを狙うPrivacy・Extraction攻撃という攻撃時点と目的で横断整理します。"
permalink: /gk/ai-security-attacks-cheatsheet/
tags: [gk, security, cheatsheet]
gk_section: AIの法律と倫理/AIセキュリティ・プライバシー攻撃/比較・まとめ
gk_order: 0
last_modified_at: 2026-09-25
---

## まず結論

AIセキュリティ攻撃は、**いつ・何を狙うか**で切ります。

| 攻撃 | 主な時点・対象 |
|---|---|
| Data Poisoning | 学習データ・学習過程 |
| Backdoor Poisoning | 学習時にトリガー挙動を仕込む |
| Adversarial Example / Evasion | 推論入力 |
| Prompt Injection | LLMの指示・コンテキスト |
| Data Extraction | 学習データ由来の情報 |
| Membership Inference | 学習に含まれたか |
| Model Extraction | モデルの挙動・能力 |

## 直感的な説明

- **教科書を汚す** → Poisoning
- **秘密の合図を仕込む** → Backdoor
- **本番入力を細工する** → Evasion
- **LLMへ悪意ある命令を混ぜる** → Prompt Injection
- **覚えているデータを探る** → Data Extraction
- **見たことがあるか聞き出す** → Membership Inference
- **モデルを真似する** → Model Extraction

## 定義・仕組み

### 学習段階

[Data Poisoning](/gk/data-poisoning-attack/)は学習データやラベルを汚染します。

[Backdoor Poisoning](/gk/backdoor-poisoning/)は、特定トリガーに対する攻撃者指定挙動を仕込みます。

### 推論段階

[敵対的サンプル](/gk/adversarial-example/)は入力を意図的に変化させて誤認識を狙います。

[Prompt Injection](/gk/prompt-injection/)は生成AIの命令・データ境界を悪用します。

### 情報窃取

- [Data Extraction](/gk/data-extraction-attack/) → 学習データ由来情報
- [Membership Inference](/gk/membership-inference-attack/) → 学習に含まれたか
- [Model Extraction](/gk/model-extraction-attack/) → モデルの挙動

## いつ使う？（得意・不得意）

試験では攻撃手段の細部より、

1. 学習時か推論時か
2. データかモデルか
3. 誤動作・情報窃取・命令乗っ取りのどれか

を確認すると切り分けやすくなります。

## G検定ひっかけポイント

- 学習データを汚す → **Poisoning**
- 推論入力を細工 → **Evasion**
- LLMの命令境界 → **Prompt Injection**
- 学習に含まれたか → **Membership Inference**
- モデルの代替品を作る → **Model Extraction**

## まとめ（試験直前用）

- **学習時 / 推論時**を最初に見る
- Poisoning＝学習を汚す
- Evasion＝推論入力を細工
- Prompt Injection＝LLMの命令境界
- Privacy attacks＝学習情報を探る
- Model Extraction＝モデル能力を模倣
- **攻撃名より「何を狙う？」で切る**

{% include gk_article_footer.html %}
