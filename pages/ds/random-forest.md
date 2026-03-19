---
layout: page
title: ランダムフォレストとは？（特徴量重要度の考え方まで理解する）【DS検定】
permalink: /ds/random-forest/
categories: [data-science]
tags: [ds, modeling]
prev: /ds/pooling/
next: /ds/feature-importance/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論
- ランダムフォレストとは、複数の決定木を組み合わせて予測することで精度と安定性を高めるモデル  
- DS検定では「1本の木ではなく全体で判断する」「特徴量重要度は不純度減少で見る」が問われる


## 直感的な説明
1人の判断だと間違えることがありますが、  
**複数人の多数決**なら安定した判断ができます。

ランダムフォレストはまさにこれで、

- 決定木1本 → 判断が偏りやすい
- 決定木100本 → 多数決で安定

というイメージです。

さらに重要なのは、

> 「どの特徴量が役に立ったかも全員の意見で判断する」

という点です。


## 定義・仕組み
ランダムフォレストは、

- 複数の決定木を作る
- それぞれ異なるデータ・特徴量で学習する
- 最後に多数決（分類）や平均（回帰）で予測する

というモデルです。

### 特徴量重要度の考え方（ここが試験ポイント）

各決定木では、分岐のたびに

- データのバラつき（不純度）が減る

ように特徴量が使われます。

このとき、

- よく使われて
- 大きく不純度を減らした特徴量

ほど「重要」とされます。

つまり、

> **全ての決定木での「不純度減少の合計」で重要度を判断する**

という仕組みです。


## どんな場面で使う？
### 使う場面
- 精度の高い分類・予測をしたいとき
- 過学習（過度な当てはめ）を抑えたいとき
- どの特徴量が効いているか知りたいとき

### 注意する場面
- 「1本の木を見て解釈したい」場合  
→ ランダムフォレストは不向き（全体で判断するモデル）


## よくある誤解・混同
### ❌ 1本の決定木を見ればモデルが理解できる
→ ⭕ ランダムフォレストは「全体」で判断するモデル


### ❌ 情報利得が小さい特徴量ほど重要
→ ⭕ **情報利得（不純度減少）が大きいほど重要**

DS検定ではここを逆にした選択肢がよく出ます。


### ❌ 多数決で勝った木で使われた特徴量が重要
→ ⭕ **各分岐でどれだけ不純度を減らしたかで判断**


### ❌ 1つの木の構造を解釈すればよい
→ ⭕ **全ての木をまとめて評価する**


## まとめ（試験直前用）
- ランダムフォレスト＝「決定木の多数決モデル」
- 1本ではなく「全体」で判断する
- 特徴量重要度＝不純度減少の合計で見る
- 「情報利得が小さいほど重要」は誤り
- DS検定では「1本だけ見る系の選択肢」は基本NG


## 対応スキル項目（AI利活用スキルシート）
- AI利活用の理解
- 機械学習の基礎
- ★ 代表的な機械学習手法の特徴を理解している

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
