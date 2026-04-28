---
layout: page
title: テクノロジ系まとめ
description: ネットワーク、データベース、システム構成、暗号技術など、SG試験に関係するテクノロジ分野を技術要素と利用目的の観点で整理するまとめページです。
permalink: /sg/category/technology/
---

[SGトップへ戻る](/sg/)

## SG試験での見方

- 技術名だけでなく、どの層で効く対策かで判断する
- 構成要素と通信経路を意識して整理する
- 暗号・認証は利用目的とセットで理解する

## 関連記事一覧

{% assign sg_pages = site.pages | sort: "title" %}
{% assign has_items = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags %}
          {% if p.tags contains 'technology' or p.tags contains 'sg-technology' or p.tags contains 'network' or p.tags contains 'database' or p.tags contains 'system_architecture' or p.tags contains 'cryptography' or p.tags contains 'crypto_auth' %}
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
