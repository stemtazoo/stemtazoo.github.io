---
layout: page
title: ストラテジ系まとめ
description: "経営戦略、業務改善、法務、組織管理を「誰が何を決めるか」で整理し、SG試験で技術対策ではなく経営判断・責任分担・契約上の論点を選ぶ場面を見分けるまとめページです。業務改善や外部委託の事例で、システム構成ではなく経営・管理・法務の選択肢を選ぶ根拠を確認できます。"
permalink: /sg/category/strategy/
---

[SGトップへ戻る](/sg/)

## SG試験での見方

- 経営視点での意思決定と責任範囲で判断する
- 組織・制度・業務設計の違いを切り分ける
- 法務・契約は実務の場面とセットで理解する

## 関連記事一覧

{% assign sg_pages = site.pages | sort: "title" %}
{% assign has_items = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags %}
          {% if p.tags contains 'strategy' or p.tags contains 'sg-strategy' or p.tags contains 'business' or p.tags contains 'business_management' or p.tags contains 'organization' or p.tags contains 'corporate_legal' or p.tags contains 'system_strategy' %}
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
