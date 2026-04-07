---
layout: page
title: 二項分布とベルヌーイ試行とは？（成功回数の確率の考え方）【DS検定】
description: 二項分布とベルヌーイ試行は（成功回数の確率の考え方）を理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/binomial-bernoulli/
categories: [data-science]
tags: [ds, statistics]
prev: /ds/bernoulli-binomial/
next: /ds/chi-square-distribution/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論
- **ベルヌーイ試行＝成功/失敗の2択の試行**
- **二項分布＝その試行をn回繰り返したときの成功回数の確率**

DS検定では  
👉「n回中x回成功」という形が出たら二項分布  
と判断できるかが問われます。


## 直感的な説明
コイン投げで考えるとわかりやすいです。

- 表が出る（成功） or 裏が出る（失敗）
- これが1回の試行 → ベルヌーイ試行

これを何回も繰り返して、

- 10回中3回表が出る確率は？

👉 これが二項分布です。

つまり、

- ベルヌーイ試行：1回の話  
- 二項分布：それを何回やったかの話  

という関係です。


## 定義・仕組み

### ■ ベルヌーイ試行とは
次の条件を満たす試行です：

- 結果が2つ（成功 or 失敗）
- 成功する確率が一定（p）

例：
- コイン（表/裏）
- 合格/不合格
- 購入する/しない


### ■ 二項分布とは
ベルヌーイ試行を **n回繰り返したとき** に、

- 成功回数がx回になる確率

を表すものです。

### ■ 二項分布の公式

P(X=x) = nCx × p^x × (1-p)^(n-x)


### ■ 式の意味（ここが重要）
- nCx：成功する位置のパターン数  
- p^x：成功する確率  
- (1-p)^(n-x)：失敗する確率  

👉 つまり

**「何通りあるか × その確率」**


## どんな場面で使う？

DS検定では以下のような文脈で出ます。

- コイン・サイコロの問題
- 不良品が出る回数
- メールが開封される回数
- A/Bテストの成功数

👉 共通点は

- 回数（n）が決まっている
- 成功確率（p）が一定
- 成功回数（x）を知りたい


## よくある誤解・混同

### ❌ 順列（nPx）を使う
→ 並び順は関係ない  
👉 正しくは「組合せ（nCx）」


### ❌ ポアソン分布と混同
- 二項分布：回数が決まっている
- ポアソン分布：回数が決まっていない（平均で考える）

👉 DS検定ではここをよく混同させてくる


### ❌ ベルヌーイ試行と二項分布を同じと考える
- ベルヌーイ試行：1回
- 二項分布：n回の結果

👉 「1回か複数回か」で切り分ける


### ❌ 確率が毎回変わる場合でも使えると思う
→ 二項分布は **確率が一定であることが前提**


## まとめ（試験直前用）

- ベルヌーイ試行＝成功/失敗の1回の試行
- 二項分布＝それをn回繰り返した成功回数
- 「n回中x回成功」→ 二項分布
- 公式は「組合せ × 成功 × 失敗」
- ポアソン分布との違いに注意


## 対応スキル項目（データサイエンス力シート）
- 数理・統計基礎
- 確率
- ★ 基本的な確率分布（ベルヌーイ分布・二項分布など）を理解している

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>

<div style="margin-top: 16px;">
  🏠 <a href="/ds/">DS検定トップに戻る</a>
</div>

<div style="display:flex;justify-content:space-between;margin-top:12px;">

  {% if page.previous.url %}
    <a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url }}">{{ page.next.title }} →</a>
  {% endif %}

</div>
