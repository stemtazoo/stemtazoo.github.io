---
layout: page
title: エビデンスベースドとは？（Evidence-Basedの考え方）【DS検定】
permalink: /ds/evidence-based/
categories: [business]
tags: [ds, design]
prev: /ds/data-literacy-practice/
next: /ds/hypothesis-thinking/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

エビデンスベースド（Evidence-Based）とは、勘や思い込みではなく、データや根拠に基づいて判断する考え方です。

DS検定では、 「データを根拠に意思決定する姿勢を理解しているか」 が問われることが多いです。



## 直感的な説明

例えば新しい商品を発売するかどうかを考えるとします。

次の2つの判断方法があります。

判断方法	例

勘や経験	「なんとなく売れそう」
データに基づく判断	「過去の売上データから需要が高い」


このとき

データや事実を根拠にして判断する考え方

がエビデンスベースドです。

医療、政策、ビジネスなど、さまざまな分野で

「データに基づいて判断する」

という考え方が重要になっています。



## 定義・仕組み

エビデンスベースドとは

客観的な根拠（エビデンス）に基づいて意思決定を行うこと

を意味します。

ここでいうエビデンスには、

売上データ

アンケート結果

実験結果

論文や公的統計


などが含まれます。

重要なのは、

「なんとなく正しそう」ではなく、

確認できる根拠に基づいて判断する

ことです。



## どんな場面で使う？

エビデンスベースドは次のような場面で使われます。

商品企画

施策効果の検証

営業判断

医療・政策判断


データ活用の現場では、

仮説を立てる
↓
データを集める
↓
結果を確認する
↓
意思決定する

という流れで使われます。



## よくある誤解・混同

混同①：経験や勘はすべて不要

実際には、

経験から仮説を立てること自体は重要

です。

ただし最終判断は、

根拠で確認する

必要があります。



混同②：データがあれば必ず正しい

データにも、

偏り

不足

測定ミス


があるため、

データの質を確認すること

も大切です。



## まとめ（試験直前用）

エビデンスベースド＝根拠に基づく意思決定

勘や思い込みだけで判断しない

データの質や信頼性も確認する

DS検定では「データを根拠に判断する姿勢」が重要

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
