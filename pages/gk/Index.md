---
layout: gk_index
title: G検定 学習まとめ
permalink: /gk/
tags: [gk]
gk_section: 人工知能（AI）とは/人工知能（AI）とは
gk_order: 15
---

{% comment %} 
  1. 配列を初期化し、ループで条件に合うものだけを手動で追加する
  where_exp を使わないことで構文エラーを回避します。
{% endcomment %}
{% assign gk_all = "" | split: "" %}
{% for p in site.pages %}
  {% if p.url contains "/gk/" and p.url != "/gk/" %}
    {% assign gk_all = gk_all | push: p %}
  {% endif %}
{% endfor %}
{% for p in site.posts %}
  {% if p.url contains "/gk/" %}
    {% assign gk_all = gk_all | push: p %}
  {% endif %}
{% endfor %}

{% comment %} 2. gk_section が設定されているページのみ抽出 {% endcomment %}
{% assign gk_section_pages = "" | split: "" %}
{% for p in gk_all %}
  {% if p.gk_section %}
    {% assign gk_section_pages = gk_section_pages | push: p %}
  {% endif %}
{% endfor %}

{% comment %} 3. gk_section でグループ化（フィルタを使わない） {% endcomment %}
{% assign gk_top_groups = gk_section_pages | group_by: "gk_section" %}

## まずどこから？

- はじめて：**人工知能とは → 機械学習の概要 → ディープラーニングの概要**
- 画像まわり：**ディープラーニングの要素技術 → 応用例（物体検出・セグメンテーション）**
- 試験直前：**チートシート → ひっかけ問題集**

---

## 目次

<ul>
  {% for group in gk_top_groups %}
    {% assign display_name = group.name | split: '/' | first %}
    <li><a href="#{{ display_name | slugify }}">{{ display_name }}</a></li>
  {% endfor %}
</ul>

---

{% for group in gk_top_groups %}
  {% assign display_name = group.name | split: '/' | first %}
  <h2 id="{{ display_name | slugify }}">{{ display_name }}</h2>
  {% assign group_items = group.items %}
  {% include gk_section_tree.html items=group_items depth=1 %}
{% endfor %}

---

## 未分類（gk_section未設定）

<ul>
  {% for p in gk_all %}
    {% unless p.gk_section %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>（{{ p.url }}）</li>
    {% endunless %}
  {% endfor %}
</ul>