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
  <div class="tag-filter">
    <p class="tag-filter__label">タグで絞り込む:</p>
    <div class="tag-filter__buttons">
      <button class="tag-button active" data-tag="all">すべて</button>

      {% assign tag_list = site.posts | map: "tags" | join: "," | split: "," | uniq | sort_natural %}
      {% assign tag_list = tag_list | reject: "" %}
      {% for tag_name in tag_list %}
        <button class="tag-button" data-tag="{{ tag_name }}">{{ tag_name }}</button>
      {% endfor %}
    </div>
  </div>
  <ul class="post-list">
    {% for post in site.posts limit: 5 %}
      <li class="post-item" data-tags="{{ post.tags | join: ',' }}">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span>（{{ post.date | date: "%Y-%m-%d" }}）</span>
        {% if post.tags %}
          <span class="post-tags">
            {% for tag in post.tags %}
              <span class="post-tag">{{ tag }}</span>
            {% endfor %}
          </span>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
  <p><a href="{{ "/posts/" | relative_url }}">すべての記事を見る</a></p>
</section>

<section>
  <h2>更新情報</h2>
  <p>このサイトはGitHub PagesとJekyllで構築しています。気になる点や改善案があれば、Issuesまでお知らせください。</p>
</section>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".tag-button");
    const items = document.querySelectorAll(".post-item");

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        buttons.forEach((btn) => btn.classList.remove("active"));
        button.classList.add("active");

        const selected = button.dataset.tag;
        items.forEach((item) => {
          if (selected === "all") {
            item.style.display = "list-item";
            return;
          }

          const tags = item.dataset.tags.split(",").filter(Boolean);
          item.style.display = tags.includes(selected) ? "list-item" : "none";
        });
      });
    });
  });
</script>
