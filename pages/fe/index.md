---
layout: page
title: 基本情報技術者試験 学習まとめ
description: 基本情報技術者試験（FE）の学習記事を、科目Aのテクノロジ・マネジメント・ストラテジ・情報セキュリティと、科目Bのアルゴリズム・データ構造・疑似言語・トレースに分けた総合索引です。用語の選択肢判断からプログラム読解へ進む学習順、分野別の頻出テーマ、苦手論点の関連記事を一覧から探し、試験対策に活用できます。
permalink: /fe/
tags: [fe]
last_modified_at: 2026-08-15
---

# 基本情報技術者試験 学習まとめ

<div class="portal-card-grid">
  <section class="portal-card">
    <h3>はじめてのFE試験</h3>
    <p>試験の全体像をつかみ、科目Aと科目Bで何を意識して学ぶかを整理します。</p>
    <a class="portal-card__button" href="#基本情報技術者試験とは">学習開始</a>
  </section>
  <section class="portal-card">
    <h3>科目Aの基礎固め</h3>
    <p>用語を丸暗記するのではなく、テクノロジ・マネジメント・ストラテジの違いを切り分けます。</p>
    <a class="portal-card__button" href="#科目a対策">科目Aを見る</a>
  </section>
  <section class="portal-card">
    <h3>科目Bの考え方</h3>
    <p>アルゴリズムや疑似言語は、いきなりコードを書く前に処理の流れを追う練習から始めます。</p>
    <a class="portal-card__button" href="#科目b対策">科目Bを見る</a>
  </section>
  <section class="portal-card">
    <h3>サイト内検索</h3>
    <p>FE、SG試験、G検定、DS検定の記事をキーワードで横断検索できます。</p>
    <a class="portal-card__button" href="{{ '/search/' | relative_url }}">検索する</a>
  </section>
</div>

## 基本情報技術者試験とは

[IPA「試験要綱 Ver.5.6」](https://www.ipa.go.jp/shiken/syllabus/rcu1hd00000141gq-att/youkou_ver5_6.pdf)では、基本情報技術者試験（FE）の対象者像を、ITを活用したサービス、製品、システム、ソフトウェアを作る人材に必要な「基本的知識・技能」をもち、実践的な活用能力を身に付けた人としています。FEは、IT用語の暗記だけでなく、システムの企画・設計・開発・運用に知識を活用できるかを確認する試験です。

現在はCBT方式で随時実施され、科目Aと科目Bの2つの試験で構成されています。[IPAの試験要綱](https://www.ipa.go.jp/shiken/syllabus/rcu1hd00000141gq-att/youkou_ver5_6.pdf)では、科目Aは90分・60問、科目Bは100分・20問で、両科目とも多肢選択式とされています。実施方式や出題範囲は改訂されることがあるため、学習時には最新版の公式資料も確認してください。

科目Aでは、テクノロジ、マネジメント、ストラテジ、情報セキュリティなどの幅広い用語を整理します。科目Bでは、アルゴリズム、プログラミング、情報セキュリティの問題を通して、文章や処理手順を読み取り、流れを追って判断する力が問われます。

このページでは、FE対策を「用語の切り分け」と「処理の流れを追う練習」に分けて整理します。

## このページの使い方

- はじめて学ぶ人は、まず科目Aの全体像を確認してから、苦手分野を1つずつ整理します。
- 科目Aは、似た用語の違いを説明できることを目標にします。
- 科目Bは、疑似言語の文法暗記だけでなく、変数の値、条件分岐、繰返し、配列の変化を表や図で追う練習を重視します。
- SG試験やITパスポートからステップアップする人は、情報セキュリティで重なる部分を活用しつつ、FEで問われるシステム開発・ネットワーク・アルゴリズムの文脈に慣れていきます。

## 科目A対策

[IPAの試験要綱](https://www.ipa.go.jp/shiken/syllabus/rcu1hd00000141gq-att/youkou_ver5_6.pdf)では、科目Aは「知識を問う」試験とされています。また、[「基本情報技術者試験（レベル2）」シラバス Ver.9.2](https://www.ipa.go.jp/shiken/syllabus/omgdg50000005kpe-att/syllabus_fe_ver9_2.pdf)には、必要な知識・技能の幅と深さが分野ごとに整理されています。そのため、科目A対策では広い範囲の用語をただ覚えるだけではなく、「何のための技術か」「似た用語と何が違うか」を切り分けることが大切です。

### テクノロジ系

基礎理論、アルゴリズム、コンピュータ構成、OS、データベース、ネットワーク、システム開発技術などを扱います。

FEでは、用語の意味だけでなく、仕組みや処理の流れを問われることがあります。たとえば、データベースなら正規化やSQL、ネットワークならプロトコルやIPアドレス、アルゴリズムなら探索・整列の考え方を確認します。

### マネジメント系

プロジェクトマネジメント、サービスマネジメント、システム監査などを扱います。

開発や運用の現場で、進捗、品質、コスト、サービス提供、監査をどう管理するかを整理します。単語だけでなく、「誰が何を管理するのか」「どの場面で使う考え方か」を押さえると選択肢を切りやすくなります。

### ストラテジ系

システム戦略、経営戦略、企業と法務などを扱います。

経営や業務改善の目的と、ITをどう結び付けるかを確認します。法律・契約・会計・標準化などは細かい暗記に寄りすぎず、何を守るためのルールかを意識して整理します。

### 情報セキュリティ

情報セキュリティ分野は、SG試験の学習内容とも重なる部分があります。

FEでは、セキュリティの考え方に加えて、ネットワーク、データベース、システム開発、運用管理の文脈で問われる点に注意します。認証、暗号、アクセス制御、マルウェア、脆弱性、ログ管理などを、実際のシステムでどう使うかと結び付けて学びます。

## 科目B対策

[IPAの試験要綱](https://www.ipa.go.jp/shiken/syllabus/rcu1hd00000141gq-att/youkou_ver5_6.pdf)では、科目Bは「技能を問う」試験とされ、20問の内訳はアルゴリズムとプログラミングが16問、情報セキュリティが4問です。出題範囲には、要求仕様の把握、既存プログラムの解読、処理の流れや変数の変化の想定などが含まれるため、科目B対策では問題文に書かれた処理を読み、順番に追って判断する力が重要です。

### アルゴリズムとプログラミング

アルゴリズムは、いきなりコードを書こうとせず、入力、処理、出力を分けて考えます。

条件分岐、繰返し、配列、関数の呼び出し、探索、整列などは、1行ずつ値がどう変わるかを表にして確認すると理解しやすくなります。

### データ構造

配列、リスト、スタック、キュー、木構造などは、「どの順番でデータを入れるか」「どの順番で取り出すか」を意識して整理します。

科目Bでは、データ構造の名前を覚えるだけでなく、処理の途中で中身がどう変化するかを追えることが大切です。

### 情報セキュリティ

科目Bの情報セキュリティでは、攻撃名や対策名を選ぶだけでなく、問題文の状況から適切な管理策や技術的対策を判断します。

SGで学んだリスク、認証、アクセス制御、ログ、インシデント対応の考え方はFEでも役立ちます。ただし、FEでは開発・ネットワーク・運用の流れの中で問われることがあるため、システム全体の文脈も確認します。

### 疑似言語・トレース練習

疑似言語は、文法だけを覚えるよりも、変数や配列の値を追跡する練習が重要です。

苦手な場合は、次の順番で進めます。

1. 入力値と初期値を確認する
2. 条件分岐でどちらに進むかを決める
3. 繰返しごとに変数や配列の値を表に書く
4. 最後に出力される値を確認する

## 分野別の記事一覧

<style>
.fe-index-subsection {
  background: #fff;
  border: 1px solid #d3e6ff;
  border-radius: 8px;
  margin: 0.65rem 0;
  overflow: hidden;
}

.fe-index-subsection summary {
  background: #f7fbff;
  box-sizing: border-box;
  color: #0b6fae;
  cursor: pointer;
  display: block;
  font-weight: 700;
  list-style: none;
  padding: 0.75rem 3rem 0.75rem 1rem;
  position: relative;
}

.fe-index-subsection summary::-webkit-details-marker {
  display: none;
}

.fe-index-subsection summary::after {
  align-items: center;
  background: #0b6fae;
  border-radius: 50%;
  color: #fff;
  content: "＋";
  display: inline-flex;
  height: 1.65rem;
  justify-content: center;
  line-height: 1;
  position: absolute;
  right: 0.85rem;
  top: 50%;
  transform: translateY(-50%);
  width: 1.65rem;
}

.fe-index-subsection[open] summary {
  border-bottom: 1px solid #d3e6ff;
}

.fe-index-subsection[open] summary::after {
  content: "−";
}

.fe-index-subsection summary:hover {
  background: #eef6ff;
}

.fe-index-subsection summary:focus-visible {
  outline: 3px solid rgba(30, 144, 255, 0.3);
  outline-offset: -3px;
}

.fe-index-subsection > ul {
  margin: 0;
  padding: 0.75rem 1rem 0.9rem 2.2rem;
}
</style>

<nav class="fe-index-jump" aria-label="FE分野別記事一覧">
  <p><strong>分野から探す</strong></p>
  <ul>
    <li><a href="#fe-technology">テクノロジ系</a></li>
    <li><a href="#fe-management">マネジメント系</a></li>
    <li><a href="#fe-strategy">ストラテジ系</a></li>
    <li><a href="#fe-subject-b">科目B対策</a></li>
    <li><a href="#fe-security">情報セキュリティ</a></li>
  </ul>
</nav>

{% assign fe_pages = site.pages | sort: "fe_order" %}
{% assign fe_total = 0 %}
{% for p in fe_pages %}
  {% if p.url != page.url %}
    {% if p.tags %}
      {% if p.tags contains "fe" %}
        {% assign fe_total = fe_total | plus: 1 %}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}

{% if fe_total == 0 %}
現在、FE記事を順次追加中です。<br>
まずは科目Aの基礎用語と、科目Bのアルゴリズム問題から整備していきます。
{% endif %}

{% assign fe_sections = "テクノロジ系|マネジメント系|ストラテジ系|科目B対策|情報セキュリティ" | split: "|" %}
{% assign fe_section_ids = "fe-technology|fe-management|fe-strategy|fe-subject-b|fe-security" | split: "|" %}
{% assign fe_subsections = "基礎理論|アルゴリズムとプログラミング|コンピュータ構成要素|システム構成要素|ソフトウェア|ハードウェア|データベース|ネットワーク|システム開発技術|プロジェクトマネジメント|サービスマネジメント|システム監査|システム戦略|経営戦略|企業と法務|アルゴリズム|データ構造|疑似言語|トレース|情報セキュリティ問題" | split: "|" %}

{% for section in fe_sections %}
{% assign section_index = forloop.index0 %}
{% assign section_id = fe_section_ids[section_index] %}
{% assign section_count = 0 %}
{% for p in fe_pages %}
  {% if p.url != page.url %}
    {% if p.tags %}
      {% if p.tags contains "fe" %}
        {% if p.fe_section == section %}
          {% assign section_count = section_count | plus: 1 %}
        {% endif %}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}

<h3 id="{{ section_id }}">{{ section }}（{{ section_count }}記事）</h3>

{% if section_count == 0 %}
- 準備中です。
{% else %}
{% for subsection in fe_subsections %}
{% assign subsection_count = 0 %}
{% for p in fe_pages %}
  {% if p.url != page.url %}
    {% if p.tags %}
      {% if p.tags contains "fe" %}
        {% if p.fe_section == section %}
          {% if p.fe_subsection == subsection %}
            {% assign subsection_count = subsection_count | plus: 1 %}
          {% endif %}
        {% endif %}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}
{% if subsection_count > 0 %}
<details class="fe-index-subsection">
  <summary><strong>{{ subsection }}</strong>（{{ subsection_count }}記事）</summary>
<ul>
{% for p in fe_pages %}
  {% if p.url != page.url %}
    {% if p.tags %}
      {% if p.tags contains "fe" %}
        {% if p.fe_section == section %}
          {% if p.fe_subsection == subsection %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
          {% endif %}
        {% endif %}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>
</details>
{% endif %}
{% endfor %}

{% assign no_subsection_count = 0 %}
{% for p in fe_pages %}
  {% if p.url != page.url %}
    {% if p.tags %}
      {% if p.tags contains "fe" %}
        {% if p.fe_section == section %}
          {% unless p.fe_subsection %}
            {% assign no_subsection_count = no_subsection_count | plus: 1 %}
          {% endunless %}
        {% endif %}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}
{% if no_subsection_count > 0 %}
<details class="fe-index-subsection">
  <summary><strong>その他</strong>（{{ no_subsection_count }}記事）</summary>
<ul>
{% for p in fe_pages %}
  {% if p.url != page.url %}
    {% if p.tags %}
      {% if p.tags contains "fe" %}
        {% if p.fe_section == section %}
          {% unless p.fe_subsection %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
          {% endunless %}
        {% endif %}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>
</details>
{% endif %}
{% endif %}
{% endfor %}

## 学習の進め方

1. **科目Aの全体像をつかむ**<br>
   まずはテクノロジ系、マネジメント系、ストラテジ系の位置づけを確認します。

2. **似た用語を切り分ける**<br>
   FEは範囲が広いため、用語を1つずつ暗記するよりも、似た概念を比較して違いを説明できるようにします。

3. **科目Bは処理を表で追う**<br>
   アルゴリズムや疑似言語は、変数・配列・条件分岐・繰返しを表にして、処理の流れを追う練習をします。

4. **セキュリティは他分野と結び付ける**<br>
   情報セキュリティは単独の知識としてだけでなく、ネットワーク、開発、運用、リスク管理とつなげて確認します。

## 公式情報

最新の試験情報、出題範囲、受験案内は公式ページで確認してください。

- [IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)
- [IPA：試験要綱・シラバスについて](https://www.ipa.go.jp/shiken/syllabus/gaiyou.html)
- [IPA：試験要綱 Ver.5.6（PDF）](https://www.ipa.go.jp/shiken/syllabus/rcu1hd00000141gq-att/youkou_ver5_6.pdf)
- [IPA：基本情報技術者試験 シラバス Ver.9.2（PDF）](https://www.ipa.go.jp/shiken/syllabus/omgdg50000005kpe-att/syllabus_fe_ver9_2.pdf)

<footer style="margin-top:24px; text-align:right;">
  <a href="{{ '/' | relative_url }}">🏠 AI・データサイエンス・IT学習ノート トップへ</a>
</footer>
