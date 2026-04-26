---
layout: page
title: 情報セキュリティ関連法規まとめ
description: 個人情報保護法、不正アクセス禁止法、著作権法、電子署名法など、SG試験で問われる関連法規を整理するまとめページです。
permalink: /sg/category/law/
---

[SGトップへ戻る](/sg/)

## このページで学ぶこと

このページでは、情報セキュリティ関連法規に関する記事をまとめています。  
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
          {% if p.tags contains 'law' or p.tags contains 'security_law' or p.tags contains 'sg-security-law' or p.tags contains 'compliance' or p.tags contains 'personal_information' or p.tags contains 'privacy_law' or p.tags contains 'corporate_legal' or p.tags contains '法務' %}
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
