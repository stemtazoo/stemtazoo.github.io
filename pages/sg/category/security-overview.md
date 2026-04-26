---
layout: page
title: 情報セキュリティ全般まとめ
description: 情報セキュリティの基本概念、脅威、脆弱性、暗号、リスクの考え方を整理するSG試験向けまとめページです。
permalink: /sg/category/security-overview/
---

## このページで学ぶこと

このページでは、情報セキュリティ全般に関する記事をまとめています。  
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
          {% if p.tags contains 'security_general' or p.tags contains 'threat_vulnerability' or p.tags contains 'cryptography' or p.tags contains 'crypto_auth' or p.tags contains 'sg-security-overview' %}
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
