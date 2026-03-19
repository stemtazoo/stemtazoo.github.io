---
layout: page
title: 仮説思考とは？データ分析の出発点【DS検定】
permalink: /ds/hypothesis-thinking/
categories: [business]
tags: [ds, design]
prev: /ds/evidence-based/
next: /ds/mece/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

# 仮説思考とは？


## まず結論

**仮説思考（Hypothesis Thinking）**とは、

**最初に仮説（予測や仮の答え）を立ててからデータ分析を行う考え方**です。

DS検定では、

- データ分析
- ビジネス課題解決
- データドリブン意思決定

の基本的な考え方として登場します。


## 直感的な説明

例えば売上が減少したとします。

仮説思考を使わない場合

- とりあえずデータを全部見る
- グラフをたくさん作る
- 何が原因か分からない

となりがちです。

一方、仮説思考では

まず仮説を立てます。

例

- 新しい競合が増えた
- 広告効果が下がった
- 商品価格が高い

その仮説を検証するために

- 売上データ
- 広告データ
- 市場データ

を分析します。

つまり

**仮説 → データ分析 → 検証**

という流れになります。


# 定義・仕組み

仮説思考は次のプロセスで進めます。


## ① 仮説を立てる

問題の原因について

**もっとも可能性が高い説明**

を仮説として設定します。

例

- 売上減少の原因は広告効果の低下


## ② 必要なデータを集める

仮説を検証するために

- 広告クリック率
- アクセス数
- 売上データ

などを収集します。


## ③ 分析する

データを分析して

仮説が正しいか確認します。

例

- CTRの変化
- コンバージョン率


## ④ 仮説を修正

仮説が違っていれば

- 新しい仮説を立てる
- 再度分析する

というプロセスを繰り返します。


# どんな場面で使う？


## データ分析

データ分析では

**目的のない分析**

を避けるために仮説思考を使います。


## ビジネス問題解決

売上低下や顧客離れなどの原因を

効率よく特定できます。


## AI・データサイエンス

機械学習でも

- 特徴量設計
- モデル改善

などで仮説が重要になります。


# よくある誤解・混同


## 仮説は「推測」？

❌ 単なる思いつきではない

仮説は

- 既存データ
- ドメイン知識
- 経験

などをもとに立てます。


## 仮説が間違っていたら失敗？

❌ 仮説が間違うことは普通

重要なのは

**仮説を検証して学習すること**

です。


# まとめ（試験直前用）

仮説思考とは

**仮説を立ててからデータ分析を行う方法**

です。

流れ

- 仮説
- データ収集
- 分析
- 検証

DS検定では

**「仮説を立てて検証する分析プロセス」**

という表現が出たら

**仮説思考**

と判断できることが重要です。


【対応スキル項目（ビジネス力シート）】

- ビジネス課題理解
- データ活用
- 仮説検証型分析

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
