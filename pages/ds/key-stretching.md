---
layout: page
title: ストレッチングとは？（ハッシュ強化の仕組み）【DS検定】
description: ストレッチングは（ハッシュ強化の仕組み）を理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/key-stretching/
categories: [business]
tags: [ds, security, design]
prev: /ds/japanese-morphological-analysis-tools/
next: /ds/managed-service/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

ストレッチングとは、**ハッシュ計算を何度も繰り返して、計算コストを意図的に高くすることで攻撃を困難にする技術**です。  
DS検定では「ソルトとの違い」や「何を防ぐのか」を判断させる問題が出やすいです。


## 直感的な説明

攻撃者がパスワードを破る方法の一つは「総当たり攻撃」です。

コンピュータは1秒間に何百万回も計算できます。  
そこで防御側はこう考えます。

> 1回のハッシュ計算を重くすればよい。

例えば、

- 通常のハッシュ → 一瞬で終わる
- ストレッチング → 何千回も繰り返す

すると、攻撃者の試行回数が激減します。

つまり、

**攻撃を“できなくする”のではなく、“時間的に現実的でなくする”技術**です。


## 定義・仕組み

ストレッチングは、

- ハッシュ関数を繰り返し適用する
- 計算回数を増やす
- CPUやメモリ負荷を高める

ことで安全性を高めます。

代表的な仕組み：

- PBKDF2
- bcrypt
- Argon2

これらは「ソルト＋ストレッチング」をまとめて実装しています。


## どんな場面で使う？

### 使う場面

- パスワード保存
- 認証システム
- セキュリティ重視のデータ管理

### 使わない場面

- 高速処理が最優先の場面
- 単なるデータ識別用途

ストレッチングは「わざと遅くする」技術なので、  
用途を間違えると性能問題になります。


## よくある誤解・混同

### ① ソルトとの違い

DS検定で最も狙われる混同ポイントです。

- ソルト → 同じパスワードでも違うハッシュにする
- ストレッチング → 計算を重くする

❌ ソルトは計算を重くする  
⭕ それはストレッチング


### ② レインボーテーブルとの関係

- レインボーテーブル対策 → ソルト
- 総当たり対策 → ストレッチング

ここを整理できるかが判断ポイントです。


### ③ 暗号化との混同

❌ ストレッチングは暗号化  
⭕ あくまでハッシュの強化

復号はできません。


## まとめ（試験直前用）

- ストレッチング＝計算を何度も繰り返す
- 目的は総当たり攻撃の遅延
- ソルトは別技術（役割が違う）
- 暗号化ではない
- 「計算を重くする」と書いてあれば正解方向


## 対応スキル項目（AI利活用スキルシート）

- AIを支えるデータと技術の理解
- セキュリティ・リスク理解  
★ AI・データ活用に伴うセキュリティリスクを理解している  
★ データの適切な管理・保護の重要性を理解している

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
