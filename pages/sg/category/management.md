---
layout: page
title: マネジメント系まとめ
description: "サービスマネジメント、システム監査、プロジェクト管理を、管理プロセスの目的という入口とタグ連動の全記事一覧で整理します。新規記事も主分類タグから自動で反映されます。"
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

以下は、主分類タグ `sg-management` が付いた記事をタイトル順に自動表示しています。

**今後は新規記事に正しい主分類タグを付ければ、このカテゴリページへの手動追記は不要です。**

{% assign category_pages = site.pages | where: "tags", "sg-management" | sort: "title" %}
{% assign category_count = 0 %}
{% for p in category_pages %}
  {% if p.permalink %}
- [{{ p.title }}]({{ p.permalink }})
    {% assign category_count = category_count | plus: 1 %}
  {% endif %}
{% endfor %}
{% if category_count == 0 %}
- 現在、該当記事はありません。
{% endif %}

{% include sg_article_footer.html %}
