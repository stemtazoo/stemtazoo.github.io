---
layout: default
title: HOME
description: AI・データサイエンス・IT学習ノートのトップページです。G検定、DS検定、基本情報技術者試験、情報セキュリティマネジメント試験の頻出テーマを分野別に整理し、基礎理解、用語の比較、演習前の確認、試験直前の復習まで迷わず進められる学習導線をまとめています。各テーマの記事一覧から、苦手分野をすぐに見直せます。
permalink: /
---

<section>
  <h2>AI・データサイエンス・IT学習ノートへようこそ</h2>
  <p>
    学びの記録や制作メモをまとめたブログです。新しい技術に触れた気づきや
    試行錯誤の過程をシンプルに共有していきます。
  </p>
</section>

<section aria-label="主要な学習エリア">
  <h2>主要な学習エリア</h2>
  <ul>
    <li><a href="{{ '/gk/' | relative_url }}">G検定の記事を見る</a> - AI、機械学習、深層学習、法律・倫理を概念理解と混同防止の視点で整理しています。</li>
    <li><a href="{{ '/sg/' | relative_url }}">SG試験の記事を見る</a> - 情報セキュリティマネジメント試験の判断軸、実務場面、ひっかけポイントを確認できます。</li>
    <li><a href="{{ '/fe/' | relative_url }}">基本情報技術者試験の記事を見る</a> - 科目Aの用語判断と科目Bの読み取りに使う基礎を整理しています。</li>
    <li><a href="{{ '/ds/' | relative_url }}">DS・Pythonの記事を見る</a> - 統計、データ分析、SQL、Python、データ活用の基礎を学べます。</li>
    <li><a href="{{ '/search/' | relative_url }}">サイト内を検索する</a> - SG、FE、G検定、DS・Pythonの記事を横断検索できます。</li>
  </ul>
</section>

<section class="home-card-grid" aria-label="学習まとめ">
  <article class="home-card">
    <h2>📘 G検定 学習まとめ</h2>
    <p>
      G検定の過去問・模擬試験で間違えた内容をもとに、<br>
      用語・概念を体系的に整理しています。
    </p>
    <ul>
      <li>✔ 用語ごとに1ページ完結</li>
      <li>✔ ひっかけポイント重視</li>
      <li>✔ 試験直前の確認にも対応</li>
    </ul>
    <p>
      <a href="{{ '/gk/' | relative_url }}">
        → G検定 学習まとめページへ
      </a>
    </p>
  </article>

  <article class="home-card">
    <h2>📊 DS検定 リテラシー 学習まとめ</h2>
    <p>
      DS検定（リテラシーレベル）の出題範囲をもとに、<br>
      統計・確率・データ活用の考え方を整理しています。
    </p>
    <ul>
      <li>✔ 数式より「意味」と「使い分け」を重視</li>
      <li>✔ よくある誤解・ひっかけポイントを整理</li>
      <li>✔ 実務と試験の両方に役立つ構成</li>
    </ul>
    <p>
      <a href="{{ '/ds/' | relative_url }}">
        → DS検定 リテラシー 学習まとめページへ
      </a>
    </p>
  </article>

  <article class="home-card">
    <h2>💻 基本情報技術者試験 学習まとめ</h2>
    <p>
      基本情報技術者試験（FE）の科目A・科目B対策を、<br>
      用語の切り分けとアルゴリズムのトレース練習に分けて整理しています。
    </p>
    <ul>
      <li>✔ テクノロジ・マネジメント・ストラテジを分野別に確認</li>
      <li>✔ 科目Bの疑似言語・処理の流れを重視</li>
      <li>✔ 情報セキュリティはSG試験の知識とも関連付け</li>
    </ul>
    <p>
      <a href="{{ '/fe/' | relative_url }}">
        → 基本情報技術者試験 学習まとめページへ
      </a>
    </p>
  </article>

  <article class="home-card">
    <h2>情報セキュリティマネジメント試験 まとめ</h2>
    <p>
      情報セキュリティマネジメント試験の試験概要、出題内容、勉強の進め方を整理していくページです。<br>
      セキュリティの基礎、管理、法務、運用などを試験対策の観点から見やすくまとめていきます。
    </p>
    <ul>
      <li>試験概要と対象者像を最初に確認</li>
      <li>科目A・科目Bの出題内容を整理</li>
      <li>頻出テーマを分野ごとに学習</li>
    </ul>
    <p>
      <a href="{{ '/sg/' | relative_url }}">
        → 情報セキュリティマネジメント試験 まとめページへ
      </a>
    </p>
  </article>

  <article class="home-card">
    <h2>サイト内検索</h2>
    <p>
      FE、SG試験、G検定、DS検定の記事を横断して検索できます。<br>
      用語名や比較したいキーワードから、関連する学習ページを探せます。
    </p>
    <ul>
      <li>RADIUS、Cookie、DNSSEC などの用語検索</li>
      <li>教師あり学習、混同行列などの復習</li>
      <li>リスク、CIA、AES などの横断確認</li>
    </ul>
    <p>
      <a href="{{ '/search/' | relative_url }}">
        → サイト内検索へ
      </a>
    </p>
  </article>
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
