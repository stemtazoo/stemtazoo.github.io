---
layout: gk_index
title: G検定 学習まとめ
permalink: /gk/
tags: [gk]
gk_section: 人工知能（AI）とは/人工知能（AI）とは
gk_order: 15
---

{% comment %} 1. データの収集 {% endcomment %}
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

{% comment %} 2. 親カテゴリ（第一階層）のリストを重複なしで作成 {% endcomment %}
{% assign parent_names = "" %}
{% for p in gk_all %}
  {% if p.gk_section %}
    {% assign parts = p.gk_section | split: "/" %}
    {% capture parent_names %}{{ parent_names }}|{{ parts[0] }}{% endcapture %}
  {% endif %}
{% endfor %}
{% assign unique_parents = parent_names | remove_first: "|" | split: "|" | uniq | sort %}

---

## まずどこから？
- はじめて：**人工知能とは → 機械学習の概要 → ディープラーニングの概要**
- 画像まわり：**ディープラーニングの要素技術 → 応用例（物体検出・セグメンテーション）**

---

## 目次
<ul>
  {% for name in unique_parents %}
    <li><a href="#{{ name | slugify }}">{{ name }}</a></li>
  {% endfor %}
</ul>

---

{% for name in unique_parents %}
  <h2 id="{{ name | slugify }}">{{ name }}</h2>
  
  {% comment %} その親カテゴリに属するアイテムだけを抽出 {% endcomment %}
  {% assign group_items = "" | split: "" %}
  {% for p in gk_all %}
    {% assign parts = p.gk_section | split: "/" %}
    {% if parts[0] == name %}
      {% assign group_items = group_items | push: p %}
    {% endif %}
  {% endfor %}
  
  {% comment %} 抽出したアイテムを tree に渡す {% endcomment %}
  {% include gk_section_tree.html items=group_items depth=0 %}
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