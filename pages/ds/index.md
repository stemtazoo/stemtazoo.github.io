---
layout: page
title: DS検定 リテラシー 学習まとめ
description: DS検定リテラシー対策の学習まとめページです。スキルチェックリストver.6と2026年の試験範囲に合わせ、基盤、データサイエンス、データエンジニアリング、価値創造の4領域を軸に、基礎用語、比較ポイント、試験直前の復習まで整理します。
permalink: /ds/
categories: [business]
tags: [ds, index]
last_modified_at: 2026-09-04
---

<div class="portal-card-grid">
  <section class="portal-card">
    <h3>DS検定 ver.6 の全体像</h3>
    <p>2026年からの試験範囲である4領域を先に確認します。</p>
    <a class="portal-card__button" href="#ds-ver6">全体像を見る</a>
  </section>
  <section class="portal-card">
    <h3>データ分析の基礎</h3>
    <p>統計、前処理、可視化、モデル化などを順番に確認します。</p>
    <a class="portal-card__button" href="/ds/data-literacy/">学習開始</a>
  </section>
  <section class="portal-card">
    <h3>試験直前チェック</h3>
    <p>チートシートと既存スキルチェックで、弱点を短時間で見直します。</p>
    <a class="portal-card__button" href="/ds/skillcheck/">学習開始</a>
  </section>
  <section class="portal-card">
    <h3>サイト内検索</h3>
    <p>SG試験、G検定、DS検定の記事をキーワードで横断検索できます。</p>
    <a class="portal-card__button" href="{{ '/search/' | relative_url }}">検索する</a>
  </section>
</div>

<a id="ds-ver6"></a>
## 🧭 DS検定 ver.6 の試験範囲

2026年のDS検定は、**スキルチェックリスト ver.6 の★1（見習いレベル）**をもとに、次の4領域を中心に出題されます。

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:18px 0 24px;">
  <div style="padding:16px;border:1px solid #e2e8f0;border-radius:12px;">
    <b>🧱 基盤</b><br>
    <span style="font-size:0.95em;">行動規範、論理的思考、課題の定義、データ理解、ITセキュリティなど</span>
  </div>
  <div style="padding:16px;border:1px solid #e2e8f0;border-radius:12px;">
    <b>🧠 データサイエンス</b><br>
    <span style="font-size:0.95em;">数学・統計、データ準備、可視化、モデル化、非構造化データ、LLMなど</span>
  </div>
  <div style="padding:16px;border:1px solid #e2e8f0;border-radius:12px;">
    <b>🛠 データエンジニアリング</b><br>
    <span style="font-size:0.95em;">環境構築、データ収集・蓄積・加工、SQL、セキュリティ、MLOpsなど</span>
  </div>
  <div style="padding:16px;border:1px solid #e2e8f0;border-radius:12px;">
    <b>💡 価値創造</b><br>
    <span style="font-size:0.95em;">課題の再定義、事業設計、AI設計、ガバナンス、PoC、効果測定など</span>
  </div>
</div>

> **ver.5 からの大きな変更**：従来の「ビジネス力」の多くは「基盤」へ移り、「価値創造」が新しい試験領域として加わりました。サイト内の既存記事は順次 ver.6 の分類へ整理します。

---

## 📚 学習の進め方

<div style="padding:16px;border-radius:12px;background:#f8fafc;margin-bottom:20px;">
<b>はじめての人</b><br>
→ 基盤 → 統計・数学の基礎
<br><br>
<b>分析を学ぶ</b><br>
→ データサイエンス → データエンジニアリング
<br><br>
<b>試験で差がつきやすい新領域</b><br>
→ 価値創造 → ver.6で追加・変更された論点
<br><br>
<b>試験直前</b><br>
→ チートシート → スキルチェック
</div>

---

## 🔗 公式リンク

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-bottom:24px;">

  <a href="https://www.datascientist.or.jp/dscertification/what/"
     target="_blank"
     rel="noopener noreferrer"
     style="display:block;padding:18px;border-radius:14px;
     background:linear-gradient(135deg,#1e293b,#3b82f6);
     color:#fff;text-decoration:none;">
    <b>DS検定とは</b><br>
    現在の試験概要・試験範囲
  </a>

  <a href="https://www.datascientist.or.jp/news/n-pressrelease/post-4959/"
     target="_blank"
     rel="noopener noreferrer"
     style="display:block;padding:18px;border-radius:14px;
     background:linear-gradient(135deg,#065f46,#14b8a6);
     color:#fff;text-decoration:none;">
    <b>スキルチェックリスト ver.6</b><br>
    2025年度版の改訂内容・Excel
  </a>

  <a href="https://www.datascientist.or.jp/news/n-dskentei/post-5204/"
     target="_blank"
     rel="noopener noreferrer"
     style="display:block;padding:18px;border-radius:14px;
     background:linear-gradient(135deg,#7c2d12,#c2410c);
     color:#fff;text-decoration:none;">
    <b>2026年の試験範囲</b><br>
    ver.6対応で何が変わったか
  </a>

</div>

---

## スキルチェック

> 現在のサイト内スキルチェックページには、ver.5の分類をもとに作成したものが含まれます。ver.6の4領域への再整理を進めています。

<ul>
{% for p in site.pages %}
  {% if p.tags contains "skillcheck" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

## ⭐ まず読む3記事

<ul>
{% assign rec = site.pages | where_exp: "p", "p.tags contains 'statistics'" %}
{% for p in rec limit:3 %}
  {% if p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

## 🧱 基盤

現行の試験範囲では、従来のビジネス力の多くが基盤へ移っています。まずは、既存記事のうち基盤と重なる「データ理解」「ITセキュリティ」を確認できます。

### データ理解・検証
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "foundation" and p.ds_section == "data-understanding" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "data-understanding" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### ITセキュリティ
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "foundation" and p.ds_section == "security" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "security" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

---

## 🧠 データサイエンス

### 線形代数
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "linear-algebra" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "linear-algebra" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### 微分・積分
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "calculus" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "calculus" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### 集合論
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "set-theory" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "set-theory" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### 📊 統計
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "statistics" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "statistics" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### データの理解・検証
<ul>
{% for p in site.pages %}
  {% if p.tags contains "data-understanding" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### データ準備
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "data-preparation" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "data-preparation" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### データ可視化
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "visualization" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "visualization" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### ⚙️ モデル化
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "modeling" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "modeling" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### 非構造化データ処理
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "unstructured-data" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "unstructured-data" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

---

## 🛠 データエンジニアリング

### 環境構築
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "dataengineering" and p.ds_section == "environment-setup" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "environment-setup" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### データ収集
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "dataengineering" and p.ds_section == "data-collection" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "data-collection" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### データ構造
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "dataengineering" and p.ds_section == "data-structure" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "data-structure" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### データ蓄積
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "dataengineering" and p.ds_section == "data-storage" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "data-storage" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### データ加工
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "dataengineering" and p.ds_section == "data-processing" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "data-processing" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### 🧾 SQL
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "dataengineering" and p.ds_section == "sql" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "sql" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### 🗄 データベース
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "dataengineering" and p.ds_section == "database" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "database" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### 🗄 ITセキュリティ
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "dataengineering" and p.ds_section == "security" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "security" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

---

## 💡 価値創造

ver.6で新たに試験領域として加わった分野です。課題の再定義、事業・モデル設計、AI設計、ガバナンス、PoC、効果測定などが含まれます。

> 既存の `business` 分類には、旧スキルチェックリストに基づく記事が多数含まれるため、未分類の記事だけを暫定表示しています。`ds_area` を付与した記事は、基盤・データサイエンス・データエンジニアリング・価値創造の各領域を優先します。

<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "value-creation" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.categories contains "business" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

---

## 🤖 AI利活用・生成AI（補助学習）

AI利活用はver.6全体にまたがるテーマです。現行の試験4領域とは別に、既存のAI利活用記事を補助学習用としてまとめています。

<ul>
{% for p in site.pages %}
  {% if p.categories contains "ai-utilization" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

## 🧪 試験対策

<ul>
{% for p in site.pages %}
  {% if p.tags contains "cheatsheet" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

---

{% assign shown_urls = "" | split: "" %}

{%- comment -%}
ver.6 の分類済み記事は、旧タグに関係なく表示済みとして扱う。
その後、未移行の記事を旧タグ・カテゴリで補完する。
{%- endcomment -%}

{% for p in site.pages %}
  {% if p.ds_area and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "linear-algebra" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "calculus" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "set-theory" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "statistics" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "data-understanding" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "data-preparation" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "data-collection" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "data-structure" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "data-storage" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "data-processing" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "environment-setup" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "visualization" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "modeling" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "unstructured-data" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "security" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "sql" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "database" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.categories contains "business" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.categories contains "ai-utilization" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "skillcheck" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

{% for p in site.pages %}
  {% if p.tags contains "cheatsheet" and p.url contains "/ds/" %}
    {% assign shown_urls = shown_urls | push: p.url %}
  {% endif %}
{% endfor %}

---

## 🧩 未分類（あとで整理）

<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" and p.url != "/ds/" and p.path contains "pages/ds/" %}
    {% unless shown_urls contains p.url %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>

---

<footer style="margin-top:24px; text-align:right;">
  <a href="{{ '/' | relative_url }}">🏠 AI・データサイエンス・IT学習ノート トップへ</a>
</footer>