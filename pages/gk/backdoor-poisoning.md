---
layout: page
title: Backdoor Poisoningとは？トリガーで特定挙動を起こす攻撃【G検定】
description: "Backdoor Poisoningを、学習データなどを汚染してモデルへ隠れたトリガー条件を埋め込み、通常入力では正常でも特定パターンを含む入力で攻撃者指定の挙動を起こさせる攻撃として整理します。通常のPoisoningやEvasionとの違いを確認します。"
permalink: /gk/backdoor-poisoning/
tags: [gk, security]
gk_section: AIの法律と倫理/AIセキュリティ・プライバシー攻撃/学習データを狙う攻撃
gk_order: 4
last_modified_at: 2026-09-25
---

## まず結論

**Backdoor Poisoning**は、モデルへ特定の**トリガー**に反応する隠れた挙動を埋め込むPoisoning攻撃です。

通常の入力では正常に見えても、

> 特定のパターンが入った入力だけ、攻撃者が狙った出力をさせる

ことを目的とします。

## 直感的な説明

普段のテストでは正常に動くモデルへ、

> 特定のマークが付いたときだけ別のクラスとして判定する

という秘密の条件を学習させるイメージです。

通常性能が高いままでも、トリガー入力だけ異常挙動する可能性があるため発見が難しい場合があります。

## 定義・仕組み

NISTではBackdoor Poisoningを、**特定のbackdoor patternを含む入力に対して、攻撃者が選んだ挙動を起こすようモデルを汚染するPoisoning攻撃**として整理しています。

代表的には、

- 一部の学習例へトリガーパターンを追加
- 攻撃者が望むラベル・挙動と結び付ける
- モデルにその対応を学習させる

という形です。

## いつ使う？（得意・不得意）

リスクを考える場面は、

- 外部から学習データを集める
- 事前学習済みモデルを第三者から取得する
- 学習パイプラインの供給網を信頼しきれない

場合です。

対策では、データ・モデルの出所確認、完全性検証、異常なパターンの検査などが重要になります。

## G検定ひっかけポイント

### Backdoor＝通常のPoisoningと完全に同じ目的？

❌ 必ず全体性能を下げる  
⭕ **通常時は正常に見せ、トリガー時だけ標的挙動を狙う場合がある**

### Evasionとの違い

- Backdoor Poisoning → **学習段階でトリガー挙動を仕込む**
- Evasion → **学習済みモデルへの推論入力を細工する**

### トリガー

❌ どんな入力でも攻撃挙動  
⭕ **特定パターンで攻撃者指定の挙動**

## まとめ（試験直前用）

- Backdoor＝**Poisoningの一種**
- 特定トリガーに反応
- 通常入力では正常な場合がある
- 学習段階で仕込む
- 推論時だけ細工するEvasionとは別
- **トリガー＋標的挙動**が判断キーワード

## 参考資料

- [Backdoor Poisoning Attack｜NIST CSRC Glossary](https://csrc.nist.gov/glossary/term/backdoor_poisoning_attack)
- [Adversarial Machine Learning: A Taxonomy and Terminology｜NIST](https://doi.org/10.6028/NIST.AI.100-2e2025)

{% include gk_article_footer.html %}
