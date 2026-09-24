---
layout: default
title: 制作記録・お知らせ
description: G検定・DS検定・SG試験の学習ページ公開や、これまでの記事更新についてのお知らせを時系列でまとめています。学習記事は各分野のまとめページやサイト内検索から探せます。
permalink: /posts/
---

<h1>制作記録・お知らせ</h1>
<p>学習ページの公開や、これまでの更新告知をまとめています。学習記事を探す場合は、<a href="{{ '/search/' | relative_url }}">サイト内検索</a>をご利用ください。</p>
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span>（{{ post.date | date: "%Y-%m-%d" }}）</span>
    </li>
  {% endfor %}
</ul>
