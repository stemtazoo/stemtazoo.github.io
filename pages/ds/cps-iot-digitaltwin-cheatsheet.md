---
layout: page
title: CPS・IoT・デジタルツインの違い：接続・モデル・システム【DS検定】
description: "工場のポンプを例に、IoTの接続、デジタルツインの現実に対応するモデル、CPSの物理と計算が連携するシステムを比較します。制御の有無だけで分類せず、三つの概念が重なる関係を整理します。"
permalink: /ds/cps-iot-digitaltwin-cheatsheet/
categories: [business]
tags: [ds, design]
ds_area: value-creation
ds_section: technology-social-trends
prev: /ds/cps/
next: /ds/data-driven/
last_modified_at: 2026-10-19
---

<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**IoTはモノのネットワーク接続、デジタルツインは現実の対象とデータで結び付くモデル、CPSは物理と計算・通信が連携するシステムに着目します。** 三つは重なり合う概念です。

「デジタルツインは再現だけ、CPSは制御」という二択で分けないようにしましょう。

## 直感的な説明

工場のポンプを例に、同じ設備を違う視点から見ます。

| 着目する部分 | 例 | 対応する概念 |
|---|---|---|
| 接続 | 温度や振動をネットワーク経由で送る | IoT |
| モデル | 実機のデータで劣化モデルを更新し、残りの寿命を予測する | デジタルツイン |
| 連携する全体 | センサー、計算、制御装置、ポンプが連携して運転を調整する | CPS |

この例ではCPSがデジタルツインを利用しています。必ずこの三段階の順番で導入する、という意味ではありません。

## 定義・仕組み

| 観点 | IoT | デジタルツイン | CPS |
|---|---|---|---|
| 中心 | モノの接続とデータ交換 | 特定の現実に対応するデジタル表現・モデル | 物理と計算などが相互作用するシステム |
| 主な問い | 何をどうつなぐか | 実機の状態をどう表し、予測に使うか | 計算結果と物理的な動作をどう連携するか |
| 注意 | 収集だけでなく機器への働きかけにも使う | 更新頻度は目的次第。制御にも利用できる | デジタルツインを必ず持つわけではない |

モデルの更新や通常のシミュレーションとの違いは、[デジタルツインの仕組み](/ds/digital-twin/)で詳しく説明しています。

## どんな場面で使う？

- 遠隔でデータを受け取る接続を説明するなら、IoTの視点。
- 特定の設備に対応し、実測で更新するモデルを説明するなら、デジタルツインの視点。
- 計算・通信・物理プロセスが連携する全体を説明するなら、CPSの視点。

スマート工場、建物のエネルギー管理、交通などで、これらを組み合わせて利用できます。選択肢では「何を説明しているか」を読みます。

## よくある誤解・混同

### IoTは制御に使えない？

ネットワーク越しの機器への指示にも使えます。接続だけで高度な分析や最適化まで実現するとは限らない、という区別です。

### デジタルツインは必ず瞬時に同期する？

必要な頻度・精度は用途によります。保守計画での定期更新と高速な制御で、同じ同期条件を要求するとは限りません。

### 制御があればCPSで、デジタルツインではない？

排他的ではありません。デジタルツインを使うCPSもあり、モデルを予測や制御に利用できます。すべてのCPSに詳細な分身モデルがあるわけでもありません。

## まとめ（試験直前用）

- IoTは接続とデータ交換に着目。
- デジタルツインは現実の対象に対応するモデルに着目。
- CPSは計算・通信と物理が連携するシステムに着目。
- 制御の有無だけで二者択一にせず、構成要素と全体の関係を見る。

## 公式情報・参考リンク

- [NIST：Digital Twin Core Conceptual Models and Services](https://www.nist.gov/publications/digital-twin-core-conceptual-models-and-services)
  - 現実の対象の診断・予測・最適化・制御へのモデル利用を確認できます。
- [NIST：Framework for Cyber-Physical Systems: Volume 1, Overview](https://www.nist.gov/publications/framework-cyber-physical-systems-volume-1-overview)
  - CPSを物理・デジタルなどの要素が連携するシステムとして捉えます。

## 対応スキル項目（ver.6 価値創造）

- **フェーズ**：構想・探索 （Visioning）
- **スキルカテゴリ**：技術・社会潮流の洞察 （Trend Sensing & Technological Foresight）
- **サブカテゴリ**：技術・社会潮流の洞察
- **必須スキル**：◯
- ★ 主要な技術・社会トレンドを理解し、基本的な因果関係を説明できる
- [ver.6 ★1スキルチェックで確認する](/ds/value-creation-skillcheck/)
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
