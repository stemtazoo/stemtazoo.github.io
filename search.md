---
layout: search
title: サイト内検索
description: SG試験、G検定、DS検定の記事をキーワードで検索できます。
permalink: /search/
sitemap: true
---

<p class="search-page-description">SG試験、G検定、DS検定の記事をキーワードで検索できます。</p>

<div class="search-panel" data-pagefind-ignore>
  <div id="search"></div>
</div>

<link href="{{ '/pagefind/pagefind-ui.css' | relative_url }}" rel="stylesheet">
<script src="{{ '/pagefind/pagefind-ui.js' | relative_url }}"></script>
<script>
  window.addEventListener('DOMContentLoaded', function () {
    new PagefindUI({
      element: "#search",
      showSubResults: true,
      showImages: false
    });
  });
</script>
