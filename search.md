---
layout: search
title: サイト内検索
description: SG試験、G検定、DS検定の記事をキーワードで検索できます。
permalink: /search/
sitemap: true
---

<p class="search-page-description">SG試験、G検定、DS検定の記事をキーワードで検索できます。</p>

<div class="search-panel" data-search-root data-search-index="{{ '/search-index.json' | relative_url }}">
  <label class="search-panel__label" for="site-search-input">検索キーワード</label>
  <input
    id="site-search-input"
    class="site-search__input"
    type="search"
    autocomplete="off"
    placeholder="例：DNSSEC、RADIUS、過学習"
    data-search-input
  >
  <p class="site-search__status" data-search-status>キーワードを入力してください。</p>
  <div class="site-search__results" data-search-results></div>
</div>

<script src="{{ '/assets/js/site-search.js' | relative_url }}" defer></script>
