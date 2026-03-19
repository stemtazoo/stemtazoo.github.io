---
layout: page
title: エビデンスベースドとは？（Evidence-Basedの考え方）【DS検定】
permalink: /ds/evidence-based/
categories: [business]
tags: [ds, design]
prev: /ds/data-literacy-practice/
next: /ds/hypothesis-thinking/
---

## まず結論

エビデンスベースド（Evidence-Based）とは、勘や思い込みではなく、データや根拠に基づいて判断する考え方です。

DS検定では、 「データを根拠に意思決定する姿勢を理解しているか」 が問われることが多いです。



## 直感的な説明

例えば新しい商品を発売するかどうかを考えるとします。

次の2つの判断方法があります。

判断方法	例

勘や経験	「なんとなく売れそう」
データに基づく判断	「過去の売上データから需要が高い」


このとき

データや事実を根拠にして判断する考え方

がエビデンスベースドです。

医療、政策、ビジネスなど、さまざまな分野で

「データに基づいて判断する」

という考え方が重要になっています。



## 定義・仕組み

エビデンスベースドとは

客観的な根拠（エビデンス）に基づいて意思決定を行うこと

を意味します。

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>
