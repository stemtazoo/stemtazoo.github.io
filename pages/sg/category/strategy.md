---
layout: page
title: ストラテジ系まとめ
description: "経営戦略、業務改善、組織管理、契約・法務を、誰が何を決めるかという入口とタグ連動の全記事一覧で整理します。新規記事は主分類タグから自動反映し、旧タグの記事も移行期間中は拾います。"
permalink: /sg/category/strategy/
last_modified_at: 2026-09-09
---

[SGトップへ戻る](/sg/)

## SG試験での見方

ストラテジ系では、**技術そのものではなく、経営・業務・制度のどの判断か**を見ると切り分けやすくなります。

- 経営方針や競争戦略を見る → 経営戦略
- 業務の流れや改善を見る → 業務改善
- 組織や責任分担を見る → 組織管理
- 契約や権利関係を見る → 法務・契約

## まず読む

- [法令・知的財産・委託契約まとめ｜責任と保護対象で整理【SG試験】](/sg/law-ip-contract-summary/)
- [委託契約の責任分界まとめ｜成果物・再委託・権利帰属を整理【SG試験】](/sg/legal-contract-ip-summary/)

## テーマ別の入口

### 経営・業務

- [DXとは？](/sg/digital-transformation/)
- [BPRとは？](/sg/bpr/)

### 組織・責任

- [職務分掌とは？](/sg/separation-of-duties/)
- [委託先管理とは？](/sg/vendor-management/)

### 契約・法務

- [秘密保持契約（NDA）とは？](/sg/nda/)

## 全記事一覧（タグから自動更新）

新規記事では主分類タグ `sg-strategy` を正とします。既存記事には旧タグだけのものが残っているため、移行期間中は `strategy`、`business`、`business_management`、`organization`、`corporate_legal`、`system_strategy` も自動的に拾います。

{% assign sg_pages = site.pages | sort: "title" %}
{% assign category_count = 0 %}
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" and p.tags %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.tags contains "sg-strategy" or p.tags contains "strategy" or p.tags contains "business" or p.tags contains "business_management" or p.tags contains "organization" or p.tags contains "corporate_legal" or p.tags contains "system_strategy" %}
- [{{ p.title }}]({{ p.url }})
        {% assign category_count = category_count | plus: 1 %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% if category_count == 0 %}
- 現在、該当記事はありません。
{% endif %}

{% include sg_article_footer.html %}
