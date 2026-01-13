---
layout: gk_index
title: G検定 学習まとめ
permalink: /gk/
tags: [gk]
gk_section: 人工知能（AI）とは/人工知能（AI）とは
gk_order: 15
---

{% comment %}
  /gk/配下の全ページ（pages + posts）を集める
{% endcomment %}

{% assign gk_pages = site.pages | where_exp: "p", "p.url contains '/gk/'" | where_exp: "p", "p.url != '/gk/'" %}
{% comment %}
{% assign gk_posts = site.posts | where_exp: "p", "p.url contains '/gk/'" %}
{% assign gk_all = gk_pages | concat: gk_posts %}
{% assign gk_section_pages = gk_all | where_exp: "p", "p.gk_section" | sort: "gk_section" %}
{% assign gk_top_groups = gk_section_pages | group_by_exp: "p", "p.gk_section | split: '/' | first" %}
{% endcomment %}

## まずどこから？

- はじめて：**人工知能とは → 機械学習の概要 → ディープラーニングの概要**
- 画像まわり：**ディープラーニングの要素技術 → 応用例（物体検出・セグメンテーション）**
- 試験直前：**チートシート → ひっかけ問題集**

---

## 目次

<ul>
  {% for group in gk_top_groups %}
    <li><a href="#{{ group.name | slugify }}">{{ group.name }}</a></li>
  {% endfor %}
</ul>

---

{% for group in gk_top_groups %}
## {{ group.name }}
{% assign group_items = group.items %}
{% include gk_section_tree.html items=group_items depth=1 %}

{% endfor %}

---

## 未分類（gk_section未設定）

{% assign unclassified = gk_all | where_exp: "p", "p.gk_section == nil or p.gk_section == ''" %}


{% if unclassified.size == 0 %}
<p>✅ gk_section未設定ページはありません。</p>
{% else %}
<ul>
  {% for p in unclassified %}
    <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>（{{ p.url }}）</li>
  {% endfor %}
</ul>
{% endif %}
