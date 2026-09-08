---
layout: page
title: 情報セキュリティ管理まとめ
description: "情報セキュリティポリシー、ISMS、リスク管理、インシデント対応、ログ管理、委託先管理を学習用の入口とタグ連動の全記事一覧で整理します。新規記事も主分類タグから自動で反映されます。"
permalink: /sg/category/security-management/
last_modified_at: 2026-09-09
---

[SGトップへ戻る](/sg/)

## SG試験での見方

情報セキュリティ管理では、**誰が・何を・どの手順で管理するか**を見ると切り分けやすくなります。

- 組織の方針を決める → ポリシー・ISMS
- リスクを見つけて対応する → リスク管理
- 事故発生後に動く → インシデント対応
- 証跡を残して追跡する → ログ管理
- 外部事業者を管理する → 委託先管理

## まず読むまとめ記事

- [情報セキュリティ管理とは？](/sg/security-management-overview/)
- [ISMS・セキュリティポリシー・組織管理まとめ｜主要用語を整理](/sg/isms-security-policy-summary/)
- [リスク管理・リスク対応まとめ｜主要用語を整理](/sg/risk-management-summary/)
- [脆弱性管理・診断運用まとめ｜主要用語を整理](/sg/vulnerability-management-summary/)
- [インシデント対応まとめ｜検知・初動対応・外部連携を整理](/sg/incident-response-summary/)
- [委託先・契約・再委託管理まとめ｜主要用語を整理](/sg/vendor-outsourcing-summary/)

## テーマ別の入口

### 組織・ポリシー

- [情報セキュリティポリシーとは？](/sg/security-policy/)
- [ISMSとは？](/sg/isms/)
- [情報セキュリティ委員会とは？](/sg/security-committee/)
- [情報セキュリティ教育・訓練とは？](/sg/security-training/)

### リスク管理

- [リスクマネジメントとは？](/sg/risk-management/)
- [リスクアセスメントとは？](/sg/risk-assessment/)
- [リスク対応とは？基本概念と4つの分類を整理](/sg/risk-treatment/)
- [情報資産台帳とは？](/sg/asset-register/)

### インシデント・運用

- [情報セキュリティインシデントとは？](/sg/security-incident/)
- [インシデント対応とは？](/sg/incident-response/)
- [ログ管理とは？](/sg/log-management/)
- [シャドーITとは？](/sg/shadow-it/)

### 外部組織・委託先

- [CSIRTとは？](/sg/csirt/)
- [SOC・CSIRT・JPCERT/CCの違い](/sg/soc-csirt-jpcert/)
- [委託先管理とは？](/sg/vendor-management/)

## 全記事一覧（タグから自動更新）

以下は、主分類タグ `sg-security-management` が付いた記事をタイトル順に自動表示しています。

**今後は新規記事に正しい主分類タグを付ければ、このカテゴリページへの手動追記は不要です。**

{% assign category_pages = site.pages | where: "tags", "sg-security-management" | sort: "title" %}
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
