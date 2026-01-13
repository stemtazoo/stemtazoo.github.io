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
{% comment %} 1. データの収集（ここは変更なし） {% endcomment %}
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

{% comment %} 
  2. 親カテゴリを抽出するための前処理
  各ページオブジェクトに、第一階層のみを取り出した「gk_parent」という仮想プロパティをセットします。
{% endcomment %}
{% for p in gk_all %}
  {% if p.gk_section %}
    {% assign parts = p.gk_section | split: "/" %}
    {% assign p.gk_parent = parts[0] %}
  {% endif %}
{% endfor %}

{% comment %} 3. 親カテゴリがあるものだけ抽出し、親カテゴリ名でグループ化 {% endcomment %}
{% assign gk_section_pages = gk_all | where: "gk_parent" | sort: "gk_section" %}
{% assign gk_top_groups = gk_section_pages | group_by: "gk_parent" %}

---

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
  <h2 id="{{ group.name | slugify }}">{{ group.name }}</h2>
  {% assign group_items = group.items %}
  {% comment %} depth=0 から開始することで tree 側で正しく階層化させます {% endcomment %}
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