---
layout: page
title: k匿名性とは？データ匿名化の基本をわかりやすく解説【DS検定】
permalink: /ds/k-anonymity/
categories: [ai-utilization]
tags: [ds, ethics]
prev: /ds/anonymized-information/
next: /ds/pseudonymized-information/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

- **k匿名性（k-anonymity）とは、データの中で同じ属性を持つ人が最低k人存在するようにする匿名化手法です。**
- DS検定では **「個人が特定されないようにするデータ加工の考え方」**として問われることがあります。

簡単に言うと

**「このデータだけでは個人を特定できない状態にする仕組み」**

です。


## 直感的な説明

例えば次のようなデータがあるとします。

|年齢|地域|性別|病気|
|---|---|---|---|
|32|松山市|男性|A|

このままだと、

- 年齢
- 地域
- 性別

の組み合わせで  
**誰のデータか特定できてしまう可能性**があります。

そこで次のように加工します。

|年齢|地域|性別|病気|
|---|---|---|---|
|30代|愛媛県|男性|A|
|30代|愛媛県|男性|B|
|30代|愛媛県|男性|C|

この場合

**同じ属性の人が3人います。**

つまり

**k = 3**

の **3匿名性（3-anonymity）**になります。

これにより

**特定の個人を識別することが難しくなります。**


## 定義・仕組み

k匿名性とは

**データの準識別子（年齢・地域など）の組み合わせが  
少なくともk人以上存在するように加工する匿名化手法**

です。

ここで重要なのが

**準識別子（quasi identifier）**

という概念です。

準識別子とは

- 年齢
- 郵便番号
- 性別
- 地域

など

**単体では個人を特定できないが  
組み合わせると特定できる可能性がある情報**

です。

k匿名性では

これらを

- 範囲化（30代など）
- 集約（県レベルなど）

することで

**同じ属性を持つ人を増やします。**


## どんな場面で使う？

k匿名性は主に

### 医療データ公開

例えば

- 病院の統計データ
- 疫学研究データ

などです。

患者データを公開する際に

**個人が特定されないようにする必要**があります。


### 公共データ公開

政府が公開する

- 人口統計
- 交通データ
- 健康データ

などでも使われます。

DS検定では

**データ公開とプライバシー保護**

という文脈で出題されることがあります。


## よくある誤解・混同

### 誤解①  
**k匿名性 = 完全匿名**

これは誤りです。

k匿名性でも

**外部データと組み合わせると  
個人が特定される可能性**

があります。


### 誤解②  
**匿名化すれば安全**

これも誤りです。

実際には

- l多様性  
- t近接性  

などの改良手法があります。

DS検定では

**匿名化にも限界がある**

という理解が重要です。


### 誤解③  
**匿名加工情報との関係**

k匿名性は

**匿名化を実現する技術の一例**

です。

つまり

- 匿名加工情報 → 法律の概念  
- k匿名性 → 技術的手法

という違いがあります。


## まとめ（試験直前用）

- k匿名性は **同じ属性の人がk人以上になるようにする匿名化手法**
- 年齢・地域など **準識別子** を加工して匿名化する
- 医療データや公共データ公開で利用される
- 完全匿名ではなく **匿名化にも限界がある**

DS検定では

**匿名化技術の基本概念**

として理解しておくと  
選択肢を判断しやすくなります。


## 対応スキル項目（ビジネス力シート）

- ビジネスにおけるデータ活用  
- 法律・倫理  

★ 個人情報保護やプライバシー保護に関する法制度を理解している

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
