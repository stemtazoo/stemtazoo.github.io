---
layout: page
title: ELSIとは？AI時代に重要な倫理・法・社会問題を理解する【DS検定】
description: ELSIはAI時代に重要な倫理・法・社会問題を理解するを理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/elsi/
categories: [ai-utilization]
tags: [ds, ethics]
next: /ds/ccpa/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

- **ELSI（Ethical, Legal and Social Issues）とは、科学技術の発展によって生じる「倫理・法・社会」に関する問題を考える枠組みです。**
- DS検定では、**AIやデータ活用の技術的な可能性だけでなく「社会への影響をどう考えるか」**を問う問題として出題されます。


## 直感的な説明

AIやデータ分析の技術はとても便利ですが、  
「技術ができること」と「社会として許されること」は必ずしも同じではありません。

例えば次のような場面です。

- AIが顔認識で犯罪者を特定できる  
- 企業が個人の購買履歴を分析できる  
- AIが採用候補者を自動で選別する  

技術的には可能でも、

- プライバシーは守られているか  
- 差別につながらないか  
- 法律に違反していないか  

といった問題が生まれます。

このように  
**技術の社会的影響を考える枠組みが ELSI** です。


## 定義・仕組み

ELSI は次の3つの観点から構成されます。

### Ethical（倫理）

社会的に正しいかどうかを考える問題です。

例

- AIの判断は公平か  
- アルゴリズムによる差別はないか  
- AIの判断は説明可能か  

近年は  
**AI倫理（AI Ethics）** として議論されることが多い領域です。


### Legal（法）

法律との関係です。

例

- 個人情報保護法  
- GDPR  
- 著作権  
- AI責任問題  

AIが誤った判断をした場合  
**誰が責任を持つのか** という問題もここに含まれます。


### Social（社会）

社会への影響です。

例

- AIによる雇用への影響  
- 社会格差の拡大  
- AI監視社会

技術が社会にどんな変化をもたらすのかを考えます。


つまり ELSI とは

**「技術を作る」だけではなく  
「社会の中でどう使うべきか」を考える視点**

と言えます。


## どんな場面で使う？

ELSIは特に次のような分野で重要です。

### AI・データ活用

- AIの公平性
- AIの透明性
- AIの説明可能性

例  
採用AIが特定の性別を不利にしていないか。


### 医療データ

- 遺伝情報
- 医療データ
- 個人健康情報

例  
遺伝子データを誰が利用できるのか。


### 個人データ活用

- SNSデータ
- 位置情報
- 購買履歴

例  
企業がどこまでデータを利用してよいのか。


DS検定では

**「技術的に可能でも社会的に問題がある場合がある」**

という視点を理解しているかが問われます。


## よくある誤解・混同

### 誤解①  
ELSIは倫理だけの話

これは誤りです。

ELSIは

- 倫理  
- 法律  
- 社会  

の **3つをまとめた概念** です。


### 誤解②  
ELSIはAIだけの問題

これも誤りです。

もともとELSIは  
**ヒトゲノム計画（遺伝子研究）** で議論された概念です。

現在は

- AI
- ビッグデータ
- バイオテクノロジー

など広い技術分野で使われています。


### DS検定でのひっかけ

DS検定では次のような形で出題されます。

- 技術の説明 → **ELSIの観点を問う**
- AIの社会問題 → **ELSIという用語を選ばせる**

選択肢で

- 倫理問題
- 社会問題
- 法律問題

が並んでいた場合、

**これらをまとめた概念が ELSI**  
と判断できると正解しやすくなります。


## まとめ（試験直前用）

- **ELSI = Ethical・Legal・Social Issues**
- 技術の社会的影響を考える枠組み
- AI・遺伝子研究・データ活用などで重要
- 技術の「できること」と「社会的に許されること」は別
- DS検定では **AIの社会的課題の文脈で出題される**


## 対応スキル項目（AI利活用スキルシート）

- AI利活用  
- AI倫理・社会

★ AIの利活用における社会的影響や倫理的課題を理解している
★ AIの活用に伴う法的・社会的リスクを理解している

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
