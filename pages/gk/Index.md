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

{% comment %} 1. データの収集（クォーテーションをシンプルに） {% endcomment %}
{% assign gk_pages = site.pages | where_exp: "p", "p.url contains '/gk/'" %}
{% assign gk_posts = site.posts | where_exp: "p", "p.url contains '/gk/'" %}
{% assign gk_all = gk_pages | concat: gk_posts %}

{% comment %} 2. gk_section があるものだけ抽出し、ソート {% endcomment %}
{% assign gk_section_pages = gk_all | where_exp: "p", "p.gk_section != nil" | sort: "gk_section" %}

{% comment %} 
   3. group_by_exp のエラー回避策
   フィルタ (| split: '/' | first) を使わず、プロパティ名だけでグループ化します。
{% endcomment %}
{% assign gk_top_groups = gk_section_pages | group_by: "gk_section" %}

## まずどこから？

- はじめて：**人工知能とは → 機械学習の概要 → ディープラーニングの概要**
- 画像まわり：**ディープラーニングの要素技術 → 応用例（物体検出・セグメンテーション）**
- 試験直前：**チートシート → ひっかけ問題集**

---

## 目次

<ul>
  {% for group in gk_top_groups %}
    {% comment %} gk_section の最初の階層だけを取り出す処理をループ内で行う {% endcomment %}
    {% assign display_name = group.name | split: '/' | first %}
    <li><a href="#{{ display_name | slugify }}">{{ display_name }}</a></li>
  {% endfor %}
</ul>

---

{% for group in gk_top_groups %}
  {% assign display_name = group.name | split: '/' | first %}
  ## {{ display_name }}
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
