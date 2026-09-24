---
layout: page
title: 敵対的サンプルとは？Evasion Attackと学習時攻撃の違い【G検定】
description: "敵対的サンプルを、学習済みモデルへの入力を攻撃者が意図的に変化させ、推論時に誤認識を引き起こすEvasion Attackの代表例として整理します。データポイズニング、データ窃取、モデル窃取との違いを攻撃時点と目的で確認します。"
permalink: /gk/adversarial-example/
tags: [gk, security, neural_network]
gk_section: AIの法律と倫理/AIセキュリティ・プライバシー攻撃/推論時の攻撃
gk_order: 1
last_modified_at: 2026-09-24
---

## まず結論

**敵対的サンプル（Adversarial Example）**は、学習済みモデルへの入力へ意図的な変化を加え、**推論時に誤った予測をさせる入力**です。

NISTの分類では、このような推論時の回避攻撃を**Evasion Attack**として整理します。

G検定では、

> 学習時にデータを汚す → Poisoning  
> 推論時に入力を細工する → Evasion / Adversarial Example

で切ります。

## 直感的な説明

人にはほぼ同じ画像に見えても、モデルには別クラスとして認識されるよう、入力へ小さな変化を加えるイメージです。

重要なのは、モデルの重みを直接書き換えるのではなく、**入力側を攻撃する**ことです。

## 定義・仕組み

攻撃者はモデルの弱点を利用し、

- 画像へ摂動を加える
- 音声へ人が気づきにくい信号を加える
- 特徴量を意図的に変更する

などして予測を変えようとします。

攻撃には、

- 特定クラスへ誤分類させるTargeted Attack
- 正解クラスから外せればよいUntargeted Attack

などがあります。

## いつ使う？（得意・不得意）

敵対的サンプルは、

- 画像認識
- 音声認識
- セキュリティ判定

などで重要な安全性・ロバストネス問題です。

対策にはAdversarial Trainingなどがありますが、すべての未知攻撃を完全に防げるとは限りません。

## G検定ひっかけポイント

### Adversarial Example＝Poisoning？

❌ 学習データへ不正例を混ぜる  
⭕ **学習済みモデルへの推論入力を細工する**

### モデル窃取？

❌ 代替モデルを作る  
⭕ **誤予測を引き起こす入力を作る**

### ノイズなら全部敵対的？

❌ 偶然入ったノイズもすべて敵対的サンプル  
⭕ **攻撃者がモデル誤動作を狙って作る入力**

## まとめ（試験直前用）

- 敵対的サンプル＝**推論時の細工入力**
- Evasion Attackの代表例
- 学習データを汚すPoisoningとは別
- モデル窃取とも別
- Targeted / Untargetedがある
- **攻撃時点＝推論時**が判断軸

## 参考資料

- [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations｜NIST](https://doi.org/10.6028/NIST.AI.100-2e2025)
- [AIガバナンスとその評価 研究会資料｜JDLA](https://www.jdla.org/wp-content/uploads/2021/06/20210422_%E9%96%8B%E5%82%AC%E5%A0%B1%E5%91%8A%E3%80%8CAI%E3%82%AC%E3%83%90%E3%83%8A%E3%83%B3%E3%82%B9%E3%81%A8%E3%81%9D%E3%81%AE%E8%A9%95%E4%BE%A1%E3%80%8D%E7%A0%94%E7%A9%B6%E4%BC%9A12.pdf)

{% include gk_article_footer.html %}
