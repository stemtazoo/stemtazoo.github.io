---
layout: page
title: 情報セキュリティ全般まとめ
description: 情報セキュリティ分野の入口として、CIA、脅威、脆弱性、リスク、攻撃、暗号などの基本概念を学習用の入口とタグ連動の全記事一覧で整理します。新規記事も主分類タグから自動で反映されます。
permalink: /sg/category/security-overview/
last_modified_at: 2026-09-09
---

[SGトップへ戻る](/sg/)

## SG試験での見方

情報セキュリティ全般では、用語名を暗記するより、**何を守る話か、何が原因か、何をする対策か**で整理すると判断しやすくなります。

- 守る性質を見る → 機密性・完全性・可用性など
- 弱点そのものを見る → 脆弱性
- 起こり得る危険を見る → 脅威
- 脅威と脆弱性から影響を考える → リスク
- 実際の攻撃手法を見る → マルウェア・不正アクセス・各種攻撃

## まず読む

- [情報セキュリティマネジメント試験とは？](/sg/information-security-management-exam/)
- [情報セキュリティマネジメント試験の出題内容とは？](/sg/sg-exam-outline-study/)
- [SG試験 ケース問題の解き方テンプレ](/sg/case-solving-template/)
- [脆弱性とは？攻撃される原因を理解する](/sg/vulnerability/)
- [リスクマネジメントとは？全体像と実務の流れを整理](/sg/risk-management/)

## テーマ別の入口

### 基本概念

- [情報資産台帳とは？リスク管理の出発点を整理](/sg/asset-register/)
- [稼働率とは？可用性の考え方とSLAでの判断基準](/sg/availability/)
- [情報セキュリティ事象とは？インシデントとの違いを整理](/sg/security-event/)
- [情報セキュリティインシデントとは？事象との違いで理解](/sg/security-incident/)

### 脅威・攻撃

- [攻撃者の種類とは？目的と特徴で整理する](/sg/attacker-types/)
- [マルウェアとは？種類と見分け方を整理](/sg/malware/)
- [不正アクセスとは？攻撃の流れと対策の考え方](/sg/unauthorized-access/)
- [ソーシャルエンジニアリングとは？なりすまし・のぞき見・トラッシングの違い](/sg/social-engineering/)

### 脆弱性・評価

- [脆弱性対策まとめ｜JVN・CVSS・検査・ペンテスト・ファジングの違い](/sg/vulnerability-cheatsheet/)
- [CVSSとは？脆弱性の深刻度を共通スコアで判断する](/sg/cvss/)
- [JVNとは？脆弱性情報の見方とJVN iPediaとの違い](/sg/jvn/)

### 暗号・認証

- [共通鍵暗号方式とは？高速だが鍵管理が課題の仕組み](/sg/symmetric-key-cryptography/)
- [公開鍵暗号方式とは？鍵の受け渡し問題を解決する仕組み](/sg/public-key-cryptography/)
- [電子署名とは？本人証明と改ざん検知を整理](/sg/digital-signature/)
- [PKIとは？公開鍵基盤の役割をやさしく整理](/sg/pki/)

## 全記事一覧（タグから自動更新）

以下は、主分類タグ `sg-security-overview` が付いた記事をタイトル順に自動表示しています。

**今後は新規記事に正しい主分類タグを付ければ、このカテゴリページへの手動追記は不要です。**

{% assign category_pages = site.pages | where: "tags", "sg-security-overview" | sort: "title" %}
{% assign category_count = 0 %}
{% for p in category_pages %}
  {% if p.permalink %}
- [{{ p.title }}]({{ p.permalink }})
    {% assign category_count = category_count | plus: 1 %}
  {% endif %}
{% endfor %}
{% if category_count == 0 %}
- 現在、該当記事はありません。
{% endif %}

{% include sg_article_footer.html %}
