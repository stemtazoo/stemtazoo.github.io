---
layout: page
title: マネジメント系まとめ
description: "サービスマネジメント、システム監査、プロジェクト管理を、管理プロセスの目的という入口とタグ連動の全記事一覧で整理します。新規記事は主分類タグから自動反映し、旧タグの記事も移行期間中は拾います。"
permalink: /sg/category/management/
last_modified_at: 2026-09-09
---

[SGトップへ戻る](/sg/)

## SG試験での見方

マネジメント系では、**どの管理プロセスの話か**を見ると切り分けやすくなります。

- 計画・進捗・成果物を管理する → プロジェクトマネジメント
- ITサービスを安定して提供する → サービスマネジメント
- 運用や統制が適切か確認する → システム監査

## まず読むまとめ記事

- [プロジェクトマネジメントまとめ｜PMBOK・WBS・PERT図を整理【SG試験】](/sg/project-management-summary/)

## テーマ別の入口

### プロジェクトマネジメント

- [WBSとは？](/sg/wbs/)
- [クリティカルパスとは？](/sg/critical-path/)

### サービスマネジメント

- [SLAとは？](/sg/sla/)
- [サービスデスクとは？](/sg/service-desk/)

### システム監査

- [システム監査とは？](/sg/system-audit/)

## 全記事一覧（タグから自動更新）

新規記事では主分類タグ `sg-management` を正とします。既存記事には旧タグだけのものが残っているため、移行期間中は `management`、`project_management`、`service_management`、`system_audit` も自動的に拾います。

{% assign sg_pages = site.pages | sort: "title" %}
{% assign category_count = 0 %}
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" and p.tags %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.tags contains "sg-management" or p.tags contains "management" or p.tags contains "project_management" or p.tags contains "service_management" or p.tags contains "system_audit" %}
- [{{ p.title }}]({{ p.url }})
        {% assign category_count = category_count | plus: 1 %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% if category_count == 0 %}
- 現在、該当記事はありません。
{% endif %}

{% include sg_article_footer.html %}
