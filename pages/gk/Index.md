---
layout: page
title: G検定 用語集
permalink: /gk/
---

## 機械学習 分野別まとめ

<ul>
{% for page in site.pages %}
  {% if page.url contains "/gk/" and page.url != "/gk/" %}
    <li><a href="{{ page.url }}">{{ page.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
