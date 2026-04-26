---
layout: page
title: ストラテジ系まとめ
description: 経営戦略、業務改善、法務、組織管理など、SG試験に関係するストラテジ分野を整理するまとめページです。
permalink: /sg/category/strategy/
---

## このページで学ぶこと

このページでは、ストラテジ分野に関する記事をまとめています。  
SG試験では、単なる用語暗記ではなく、どの場面で使う考え方か、どの選択肢を切れるかを意識して整理します。

## SG試験での見方

- 用語の定義だけでなく、役割で判断する
- 似た用語との違いを押さえる
- 実務上の目的とセットで理解する

## 関連記事一覧

{% assign sg_pages = site.pages | sort: "title" %}
{% assign has_items = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags %}
          {% if p.tags contains 'strategy' or p.tags contains 'sg-strategy' or p.tags contains 'business' or p.tags contains 'business_management' or p.tags contains 'corporate_legal' or p.tags contains 'organization' or p.tags contains 'system_strategy' %}
            {% assign has_items = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
          {% endif %}
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% if has_items == false %}
該当記事は今後追加予定です。
{% endif %}
