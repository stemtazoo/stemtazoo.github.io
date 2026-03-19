---
layout: page
title: 障害・遅延の報告とレポートラインとは？（リスクマネジメントの基本）【DS検定】
permalink: /ds/report-line-risk-management/
categories: [business]
tags: [ds, design]
---

## まず結論

- **レポートラインとは、問題や障害を発見したときに報告する正式な経路（上司・プロジェクトリーダーなど）を指します。**
- DS検定では、**問題を発見したときに「迅速にレポートラインへ報告する」というリスクマネジメントの考え方**が問われます。


## 直感的な説明

例えば、データ分析プロジェクトで次のような状況が起きたとします。

- 分析用データが壊れている  
- システム処理が止まっている  
- モデルの結果がおかしい  

このとき、

- 自分だけで解決しようとする  
- 問題が大きくなってから報告する  

という対応をすると、プロジェクト全体に大きな影響が出る可能性があります。

そのため組織では

**問題を見つけたらすぐに「レポートライン」に報告する**

というルールが作られています。

DS検定でも、

> 「問題を発見したときに適切な行動は何か」

という形で、この考え方が問われることがあります。


## 定義・仕組み

### レポートライン（report line）

**組織において、報告を行う正式な経路のこと**

通常は次のような人を指します。

- 上司  
- プロジェクトリーダー  
- マネージャー  

つまり

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
