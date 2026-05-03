---
layout: page
title: マネジメント系まとめ
description: サービスマネジメント、システム監査、プロジェクト管理など、SG試験に関係するマネジメント分野を整理するまとめページです。
permalink: /sg/category/management/
---

[SGトップへ戻る](/sg/)

## SG試験での見方

- 管理プロセスの目的と手順で判断する
- 監査・運用・改善の流れを区別する
- 現場運用に落ちるかどうかで理解する

## 関連するまとめページ

このカテゴリに関連する学習まとめページです。  
はじめに全体像を確認したい場合は、まとめページから読むと理解しやすくなります。

- [プロジェクトマネジメントまとめ｜PMBOK・WBS・PERT図を整理【SG試験】](/sg/project-management-summary/)  
  プロジェクトマネジメントの全体像、PMBOKの管理領域、WBS、アローダイアグラム、クリティカルパスを整理したまとめページです。

## 関連記事一覧

{% assign sg_pages = site.pages | sort: "title" %}
{% assign has_items = false %}
{% assign summary_page_urls = "/sg/project-management-summary/" | split: "," %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags %}
          {% assign is_summary_page = false %}
          {% if p.url contains '-summary/' %}
            {% assign is_summary_page = true %}
          {% endif %}
          {% if p.tags contains 'summary' or p.tags contains 'sg-summary' %}
            {% assign is_summary_page = true %}
          {% endif %}

          {% if is_summary_page == false %}
            {% unless summary_page_urls contains p.url %}
            {% if p.tags contains 'management' or p.tags contains 'sg-management' or p.tags contains 'project_management' or p.tags contains 'service_management' or p.tags contains 'system_audit' %}
              {% assign has_items = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
            {% endif %}
            {% endunless %}
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
