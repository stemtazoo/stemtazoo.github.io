---
layout: page
title: DS検定 リテラシー 学習まとめ
permalink: /ds/
categories: [business]
tags: [ds, index]
---

## 📚 学習の進め方

<div style="padding:16px;border-radius:12px;background:#f8fafc;margin-bottom:20px;">
<b>はじめての人</b><br>
→ データサイエンスとは → 統計の基礎
<br><br>
<b>実務を意識</b><br>
→ 前処理 → 可視化 → 分析
<br><br>
<b>試験直前</b><br>
→ チートシート → スキルチェック
</div>

---

## 🔗 公式リンク

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-bottom:24px;">

  <a href="https://www.datascientist.or.jp/dscertification/what/#summary"
     target="_blank"
     style="display:block;padding:18px;border-radius:14px;
     background:linear-gradient(135deg,#1e293b,#3b82f6);
     color:#fff;text-decoration:none;">
    <b>DS検定とは</b><br>
    試験概要・出題範囲
  </a>

  <a href="https://www.datascientist.or.jp/news/n-pressrelease/post-1757/"
     target="_blank"
     style="display:block;padding:18px;border-radius:14px;
     background:linear-gradient(135deg,#065f46,#14b8a6);
     color:#fff;text-decoration:none;">
    <b>スキルチェックリスト</b><br>
    出題範囲の基準
  </a>

</div>

---

## ⭐ まず読む3記事

<ul>
{% assign rec = site.pages | where_exp: "p", "p.tags contains 'statistics'" %}
{% for p in rec limit:3 %}
  {% if p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 🧠 データサイエンス力

### 📊 統計
<ul>
{% for p in site.pages %}
  {% if p.tags contains "statistics" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### ⚙️ 前処理
<ul>
{% for p in site.pages %}
  {% if p.tags contains "preprocessing" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 🛠 データエンジニアリング力

### 🧾 SQL
<ul>
{% for p in site.pages %}
  {% if p.tags contains "sql" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 🗄 データベース
<ul>
{% for p in site.pages %}
  {% if p.tags contains "database" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 📊 ビジネス力

<ul>
{% for p in site.pages %}
  {% if p.categories contains "business" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 🤖 AI利活用

<ul>
{% for p in site.pages %}
  {% if p.categories contains "ai-utilization" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 🧪 試験対策

<ul>
{% for p in site.pages %}
  {% if p.tags contains "skillcheck" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

{% assign shown_urls = "" | split: "" %}

{%- comment -%}
ここで「表示済み記事」を全部記録する
{%- endcomment -%}

{% for p in site.pages %}
  {% if p.tags contains "statistics" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "preprocessing" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "sql" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

---

# 🧩 未分類（あとで整理）

<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% unless shown_urls contains p.url %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>