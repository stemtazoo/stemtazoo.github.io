---
layout: default
title: HOME
permalink: /
---

<section>
  <h1>STEMTAZOO Blogへようこそ</h1>
  <p>
    学びの記録や制作メモをまとめたブログです。新しい技術に触れた気づきや
    試行錯誤の過程をシンプルに共有していきます。
  </p>
</section>

<section>
  <h2>最新記事</h2>
  <ul>
    {% for post in site.posts limit: 5 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span>（{{ post.date | date: "%Y-%m-%d" }}）</span>
      </li>
    {% endfor %}
  </ul>
  <p><a href="{{ "/posts/" | relative_url }}">すべての記事を見る</a></p>
</section>

<section>
  <h2>更新情報</h2>
  <p>このサイトはGitHub PagesとJekyllで構築しています。気になる点や改善案があれば、Issuesまでお知らせください。</p>
</section>
