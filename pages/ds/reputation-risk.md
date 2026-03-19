---
layout: page
title: レピュテーションリスクとは？企業評価が下がる仕組みを理解する【DS検定】
permalink: /ds/reputation-risk/
categories: [business]
tags: [ds, design]
prev: /ds/report-line-risk-management/
next: /ds/risk-management/
---

## まず結論

レピュテーションリスクとは、企業や組織の評判（信用）が低下することで発生するリスクのことです。

DS検定では、不祥事・情報漏えい・システム障害などが企業評価を下げるリスクとして理解できているかが問われます。




## 直感的な説明

企業は商品やサービスだけでなく、**「信頼」**によって成り立っています。

例えば次のようなニュースを見たことがあるかもしれません。

個人情報が流出した

システム障害でサービス停止

不正なデータ操作が発覚


このような出来事が起きると、

SNSで批判が広がる

顧客が離れる

株価が下がる


といった影響が出ることがあります。

このように、

企業の評判（レピュテーション）が悪化することで生じる損失

を レピュテーションリスク と呼びます。

DS検定では、データやAIの活用においても
企業の社会的信用を損なうリスクがあることを理解しているかが問われます。



## 定義・仕組み

レピュテーションリスク（Reputation Risk）

**企業や組織

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

---

[DS検定 学習まとめトップに戻る]({{ '/ds/' | relative_url }})
