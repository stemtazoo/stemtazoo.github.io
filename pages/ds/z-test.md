---
layout: page
title: z検定とは？t検定との違いまで整理【DS検定リテラシー】
description: "z検定を、検定統計量を標準正規分布で評価する方法として整理します。母平均の検定では母分散既知などの条件、比率では正規近似の条件を確認し、サンプルサイズだけでt検定と切り分けない判断軸を押さえます。"
permalink: /ds/z-test/
categories: [data-science]
tags: [ds, statistics]
ds_area: datascience
ds_section: statistics
prev: /ds/welch-t-test/
next: /ds/causal-inference/
last_modified_at: 2026-09-26
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

z検定とは、**標準化した検定統計量を標準正規分布で評価する検定**です。母平均の検定では、母分散が既知など標準誤差を正規分布として扱える条件で使います。  

DS検定では「z検定とt検定をどう切り分けるか」が問われることが多いです。


## 直感的な説明

例えば、ある商品の平均売上が「本当に100個なのか？」を確かめたいとします。

サンプルをたくさん集めて平均を出したとき、

- 100個からどれくらいズレているか？
- そのズレは「偶然」なのか？
- それとも「意味のある差」なのか？

を判断するのが検定です。

母平均のz検定では、  
**母分散が既知で標準誤差を計算できる場合**などに、  
ズレがどれくらい極端かを標準化して判断します。

大標本では正規近似を利用できる場面もありますが、**「大標本なら必ずz検定」ではありません**。


## 定義・仕組み

z検定は、母平均に関する仮説を検証する方法です。

基本の考え方はシンプルです。

1. まず「差はない」という前提（帰無仮説）を立てる  
2. サンプル平均と仮説平均との差を計算する  
3. その差を「標準誤差」で割って、どれくらい極端かを見る  

この「標準化した値」が z値 です。

z値が大きいほど  
「偶然では説明しにくい差」と判断します。

DS検定では、式そのものよりも、

- なぜ標準化するのか  
- なぜ正規分布を前提にするのか  

を理解しているかが重要です。


## どんな場面で使う？

### 使うべき場面

- 母平均の検定で、母分散が既知の場合
- 標本比率など、条件を満たして正規近似を使う場合
- 大標本で正規近似が妥当と判断できる場合

### 注意が必要な場面

母分散が未知で、標本標準偏差から標準誤差を推定する母平均の検定では、一般にt分布を使います。

DS検定では、**サンプルサイズだけでz検定とt検定を決めない**ことが重要です。


## よくある誤解・混同

### ① z検定とt検定の混同

最も多いひっかけです。

母平均の検定では、まず

- 母分散が既知か
- 標準誤差を何から求めるか
- 正規近似を使える条件か

を確認します。

単純に「大標本ならz、小標本ならt」とだけ覚えない方が安全です。

DS検定では  
「標本分散を使っているのにz検定と書いてある」  
といった選択肢が出ることがあります。

### ② p値との混同

z検定そのものは「方法」です。  
p値は「結果の指標」です。

z値をもとにp値を求めます。

「z値＝有意差」ではありません。  
有意かどうかは、あらかじめ決めた有意水準との比較です。


## まとめ（試験直前用）

- z検定は「母平均の検定」  
- 母平均のz検定では、母分散既知など標準正規分布で評価できる条件を確認する
- 大標本は正規近似を使える材料になるが、サンプルサイズだけでz/tを決めない  
- z値は差を標準化したもの  
- 検定とp値を混同しない  

DS検定では  
「どの条件ならどの検定を使うか」を判断できることが最重要です。


## 公式情報・参考リンク

- [NIST/SEMATECH e-Handbook｜What are statistical tests?](https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm)
  - 仮説検定、帰無仮説、有意水準の基本を確認できます。
- [NIST/SEMATECH e-Handbook｜Two-Sample t-Test for Equal Means](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)
  - 母分散を標本から推定するt検定との違いを確認する比較資料として使えます。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：基礎技術
- **スキルカテゴリ**：科学的解析の基礎
- **サブカテゴリ**：推定・検定
- **必須スキル**：—
- ★ 検定する対象となるデータの対応の有無を考慮した上で適切な検定手法（t検定, z検定など）を選択し、適用できる
- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)
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
