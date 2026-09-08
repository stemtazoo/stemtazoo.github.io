---
layout: page
title: ストラテジ系まとめ
description: "経営戦略、業務改善、組織管理、契約・法務を、誰が何を決めるかという入口とタグ連動の全記事一覧で整理します。新規記事も主分類タグから自動で反映されます。"
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

以下は、主分類タグ `sg-strategy` が付いた記事をタイトル順に自動表示しています。

**今後は新規記事に正しい主分類タグを付ければ、このカテゴリページへの手動追記は不要です。**

{% assign category_pages = site.pages | where: "tags", "sg-strategy" | sort: "title" %}
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
