---
layout: page
title: DS検定 リテラシー 学習まとめ
permalink: /ds/
categories: [business]
tags: [ds, index]
---

## 📚 学習の進め方

### はじめての人
- データサイエンスとは
- 統計（平均・分散・相関）

### 実務を意識
- 前処理 → 可視化 → 分析

### 試験直前
- チートシート
- スキルチェック

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

### 🧮 数学
<ul>
{% for p in site.pages %}
  {% if p.tags contains "math" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 🤖 機械学習
<ul>
{% for p in site.pages %}
  {% if p.tags contains "machine-learning" and p.url contains "/ds/" %}
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

### 🗄 データベース
<ul>
{% for p in site.pages %}
  {% if p.tags contains "database" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 🧾 SQL
<ul>
{% for p in site.pages %}
  {% if p.tags contains "sql" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 🔄 データ処理
<ul>
{% for p in site.pages %}
  {% if p.tags contains "data-processing" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 📊 ビジネス力

### 🧠 思考・設計
<ul>
{% for p in site.pages %}
  {% if p.tags contains "design" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 📈 分析
<ul>
{% for p in site.pages %}
  {% if p.tags contains "analysis" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 🤖 AI利活用

### ⚠️ 倫理・ガバナンス
<ul>
{% for p in site.pages %}
  {% if p.tags contains "ethics" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 🚀 活用
<ul>
{% for p in site.pages %}
  {% if p.tags contains "ai-use" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 🧪 試験対策

### 📝 スキルチェック
<ul>
{% for p in site.pages %}
  {% if p.tags contains "skillcheck" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 📄 チートシート
<ul>
{% for p in site.pages %}
  {% if p.tags contains "cheatsheet" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

# 🧩 未分類（あとで整理）

<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" and p.tags %}
    {% unless p.tags contains "statistics"
      or p.tags contains "math"
      or p.tags contains "machine-learning"
      or p.tags contains "preprocessing"
      or p.tags contains "sql"
      or p.tags contains "database"
      or p.tags contains "data-processing"
      or p.tags contains "design"
      or p.tags contains "analysis"
      or p.tags contains "ethics"
      or p.tags contains "ai-use"
      or p.tags contains "skillcheck"
      or p.tags contains "cheatsheet" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>