---
layout: page
title: "スキルレベル定義2023 総まとめ【Assistant Data Scientist（見習い）】"
description: スキルレベル定義2023の総まとめページです。Assistant Data Scientistに求められるビジネス力、データサイエンス力、データエンジニアリング力の位置づけと学習範囲を整理します。3つの力の役割とDS検定での判断ポイントを短時間で俯瞰できます。
permalink: /ds/skilllevel-2023-summary/
categories: [business]
tags: [ds, skillcheck]
prev: /ds/skilllevel-2023-assistant-ds-datascience/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

このページでは、**スキルレベル定義2023における Assistant Data Scientist（見習い）レベル**の全体像を整理します。（スキルチェックリスト ver5.0）

## まず結論

Assistant Data Scientist（見習い）では、次の3つの力をバランスよく身につけることが重要です。

| 力 | 役割 | 試験での見方 |
|---|---|---|
| ビジネス力 | 課題を整理し、分析を仕事につなげる | 目的・KPI・説明責任 |
| データサイエンス力 | 統計・機械学習を理解して使う | 分析手法・評価・解釈 |
| データエンジニアリング力 | データを安全に扱い、加工する | SQL・API・データ基盤・セキュリティ |

高度な研究開発よりも、**基礎を理解し、適切に判断して仕事を進められること**が中心です。

## 全体構造（3つの力）

### ビジネス力

**目的 → データ → 結論**の流れで考える力です。

できる状態の例：

- 目的を明確にできる
- 必要なデータを判断できる
- データの信頼性を確認できる
- 分析結果を言語化できる
- モニタリングの重要性を理解している

DS検定では、KPI、データの信頼性、仮説検証、説明責任などにつながります。

### データサイエンス力

**統計・機械学習の基礎を理解し、適切に使う力**です。

できる状態の例：

- 平均・分散を説明できる
- 推定と検定の違いが分かる
- 教師あり学習／教師なし学習を区別できる
- 過学習を説明できる
- 基本的な分析結果を解釈できる

DS検定では、統計概念、評価指標、過学習、相関と因果などが中心です。

### データエンジニアリング力

**データを安全に扱い、必要な形に加工する力**です。

できる状態の例：

- 構造化データを理解できる
- SQLで基本操作ができる
- データ結合・集計ができる
- APIの役割を理解している
- セキュリティの基本を理解している

DS検定では、SQL、データ形式、API、クラウド、セキュリティ基礎などにつながります。

## Assistant Data Scientist の立ち位置

Assistant Data Scientist は、高度な研究者やアーキテクトを意味するものではありません。

むしろ重要なのは次の土台です。

- 正しい進め方ができる
- 基礎概念を理解している
- 選択肢や状況を適切に判断できる
- データを安全に扱える

**「高度さ」より「基礎を正しく使えるか」**で捉えると整理しやすくなります。

## モデルカリキュラムとの関係

モデルカリキュラム側の学習内容も、社会・データ・倫理・技術といった複数の領域を横断します。

| 観点 | 主な内容 |
|---|---|
| 社会理解 | データ・AIが社会やビジネスでどう使われるか |
| データ理解 | データの読み方・分析の基礎 |
| 倫理理解 | 法律・倫理・セキュリティ |
| 技術基礎 | 数理・アルゴリズム・データ活用 |

スキルレベル定義と完全に同じ分類ではありませんが、**DS検定で必要な基礎を複数領域から捉える**という点で対応させると理解しやすくなります。

## 試験直前まとめ

判断するときは、次の3点に戻ります。

- **仕事の進め方・課題設定** → ビジネス力
- **統計・機械学習・分析** → データサイエンス力
- **SQL・基盤・安全なデータ取扱い** → データエンジニアリング力

DS検定は、1つの専門だけでなく、**この3つを横断して基礎的な判断ができるか**を見る試験として整理すると学習しやすくなります。

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
