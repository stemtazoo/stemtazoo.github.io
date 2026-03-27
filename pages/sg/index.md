---
layout: page
title: 情報セキュリティマネジメント試験 学習まとめ
permalink: /sg/
categories: [business]
tags: [sg, index]
---

## 📚 学習の進め方

<div style="padding:16px;border-radius:12px;background:#f8fafc;margin-bottom:20px;">
<b>はじめての人</b><br>
→ 試験概要 → 出題範囲 → 基本用語
<br><br>
<b>全体像をつかむ</b><br>
→ セキュリティの基礎 → 管理 → 技術
<br><br>
<b>試験直前</b><br>
→ 頻出用語 → 重要テーマの見直し
</div>

---

## 🔗 公式リンク

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-bottom:24px;">

  <a href="https://www.ipa.go.jp/shiken/kubun/sg/index.html"
     target="_blank"
     style="display:block;padding:18px;border-radius:14px;
     background:linear-gradient(135deg,#1e293b,#2563eb);
     color:#fff;text-decoration:none;">
    <b>情報セキュリティマネジメント試験</b><br>
    IPA 公式トップ
  </a>

  <a href="https://www.ipa.go.jp/shiken/kubun/sg/about.html"
     target="_blank"
     style="display:block;padding:18px;border-radius:14px;
     background:linear-gradient(135deg,#0f766e,#14b8a6);
     color:#fff;text-decoration:none;">
    <b>試験の対象者像</b><br>
    求められる役割とレベル
  </a>

  <a href="https://www.ipa.go.jp/shiken/kubun/sg/outline.html"
     target="_blank"
     style="display:block;padding:18px;border-radius:14px;
     background:linear-gradient(135deg,#7c2d12,#f97316);
     color:#fff;text-decoration:none;">
    <b>試験概要・出題範囲</b><br>
    形式と学習の入口
  </a>

</div>

---

## ⭐ まず読む3記事

{% assign sg_intro = site.pages | where_exp: "p", "p.url contains '/sg/' and p.tags and (p.tags contains 'sg-security-overview' or p.tags contains 'security_general' or p.tags contains 'security')" %}
<ul>
{% for p in sg_intro limit:3 %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

---

# 🧩 出題分野別まとめ

### 情報セキュリティ全般
{% assign sg_security_overview = site.pages | where_exp: "p", "p.url contains '/sg/' and p.tags and (p.tags contains 'sg-security-overview' or p.tags contains 'security_general' or p.tags contains 'security')" %}
<ul>
{% for p in sg_security_overview %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

### 情報セキュリティ管理
{% assign sg_security_management = site.pages | where_exp: "p", "p.url contains '/sg/' and p.tags and (p.tags contains 'sg-security-management' or p.tags contains 'security_management')" %}
<ul>
{% for p in sg_security_management %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

### 情報セキュリティ対策
{% assign sg_security_measures = site.pages | where_exp: "p", "p.url contains '/sg/' and p.tags and (p.tags contains 'sg-security-measures' or p.tags contains 'crypto_auth' or p.tags contains 'access_control' or p.tags contains 'unauthorized_access')" %}
<ul>
{% for p in sg_security_measures %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

### 情報セキュリティ関連法規
{% assign sg_security_law = site.pages | where_exp: "p", "p.url contains '/sg/' and p.tags and (p.tags contains 'sg-security-law' or p.tags contains 'security_law')" %}
<ul>
{% for p in sg_security_law %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

### テクノロジ
{% assign sg_technology = site.pages | where_exp: "p", "p.url contains '/sg/' and p.tags and (p.tags contains 'sg-technology' or p.tags contains 'technology' or p.tags contains 'network' or p.tags contains 'system_architecture')" %}
<ul>
{% for p in sg_technology %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

### マネジメント
{% assign sg_management = site.pages | where_exp: "p", "p.url contains '/sg/' and p.tags and (p.tags contains 'sg-management' or p.tags contains 'risk_assessment' or p.tags contains 'incident_management' or p.tags contains 'isms')" %}
<ul>
{% for p in sg_management %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

### ストラテジ
{% assign sg_strategy = site.pages | where_exp: "p", "p.url contains '/sg/' and p.tags and (p.tags contains 'sg-strategy' or p.tags contains 'strategy')" %}
<ul>
{% for p in sg_strategy %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>
