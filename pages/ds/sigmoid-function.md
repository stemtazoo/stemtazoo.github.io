---
layout: page
title: シグモイド関数とは？（確率に変換する関数）【DS検定】
permalink: /ds/sigmoid-function/
categories: [business]
tags: [ds, modeling, design]
prev: /ds/replication-vs-backup/
next: /ds/symmetric-difference/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論
- シグモイド関数とは、**任意の値を0〜1の確率のような値に変換する関数**
- DS検定では「出力の範囲」「確率として解釈できるか」を判断させる問題がよく出る


## 直感的な説明
シグモイド関数は、  
**「どんなに大きな値でも、0〜1の範囲に押し込む関数」**です。

例えば：
- 売上スコア → 「購入する確率」
- 信用スコア → 「返済できる確率」

のように、**数値を“確率っぽく”扱える形に変換する**ときに使います。

イメージとしては、
- 小さい値 → 0に近づく  
- 大きい値 → 1に近づく  
- 真ん中（0付近） → 0.5あたり  

という、**なめらかなS字カーブ**になります。


## 定義・仕組み
シグモイド関数は、入力された値を次のように変換します：

- 小さい値 → ほぼ0
- 大きい値 → ほぼ1
- 0付近 → 約0.5

重要なのは「計算式」よりも、

👉 **出力が必ず0〜1に収まること**

です。

この性質により、
- 「確率」として解釈できる
- 「分類問題（YES/NO）」に使える

という特徴があります。

DS検定では、  
**「出力の範囲」と「確率として扱えるか」**が問われることが多いです。


## どんな場面で使う？
主に以下のような場面で使われます。

### ① 二値分類（ロジスティック回帰）
- 購入する / しない
- 合格 / 不合格
- 異常 / 正常

👉 モデルの出力を「確率」に変換するために使う


### ② AI・機械学習モデルの出力層
- ニューラルネットワークの最終層
- 「確率として出したい」とき


### 注意が必要な場面
- 3クラス以上の分類 → ソフトマックス関数を使う
- 回帰問題 → シグモイドは使わない

👉 **「確率にしたいか？」が判断基準**


## よくある誤解・混同

### ❌ 誤解①：出力は0や1をとる
→ ⭕ **実際には0や1にはならない（近づくだけ）**


### ❌ 誤解②：どんな分類でも使える
→ ⭕ **二値分類専用（多クラスはソフトマックス）**


### ❌ 誤解③：x→∞で0になる
→ ⭕ **xが大きいほど1に近づく**

👉 DS検定ではここがよくひっかけになります


### ❌ 誤解④：ロジット関数と同じ
→ ⭕ **ロジット関数の「逆関数」がシグモイド**

👉 「どっちが入力でどっちが出力か」を問われることが多い


## まとめ（試験直前用）
- シグモイド関数＝**値を0〜1に変換する関数**
- 出力は**確率として解釈できる**
- 二値分類で使用（ロジスティック回帰）
- **x→∞で1、x→-∞で0に近づく**
- 「ロジット関数の逆」「0〜1に収まるか」が判断ポイント


## 対応スキル項目（AI利活用スキルシート）
- AIの基礎理解
- 機械学習の基礎
- ★ 機械学習の基本的な仕組み（教師あり学習・分類・回帰）を理解している

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
