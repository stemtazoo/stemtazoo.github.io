---
layout: default
title: 記事一覧
description: 学習記録・更新情報の一覧ページです。G検定・DS検定・SG試験対策の新着記事を時系列で確認できます。
permalink: /posts/
---

<h1>記事一覧</h1>
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span>（{{ post.date | date: "%Y-%m-%d" }}）</span>
    </li>
  {% endfor %}
</ul>
