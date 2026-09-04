---
layout: page
title: ETLとは？（データ統合の基本プロセス）【DS検定リテラシー】
description: "ETLは、データをExtract（抽出）→Transform（変換）→Load（格納）の順で処理するデータ統合プロセスです。DWHへ格納する前に整形する点、ELTやデータレイクとの違い、DS検定での判断基準を整理します。"
permalink: /ds/etl/
categories: [data-engineering]
tags: [ds, data-collection, data-processing]
ds_area: dataengineering
ds_section: data-collection
prev: /ds/batch-vs-stream/
next: /ds/hadoop/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**ETL = Extract（抽出）→ Transform（変換）→ Load（格納）** です。

DS検定では、**「変換してからDWHなどへ格納する」**という順番を押さえるのがポイントです。

## 直感的な説明

企業には販売・会計・顧客管理など、別々のシステムがあります。

それぞれのデータは形式が異なるため、そのままでは分析しにくいことがあります。

そこで、

1. 必要なデータを取り出す
2. 形式をそろえて加工する
3. DWHなどの分析基盤へ格納する

という流れでデータを整えます。これがETLです。

## 定義・仕組み

| 工程 | 意味 | 例 |
|---|---|---|
| Extract | 抽出 | 販売・会計システムからデータ取得 |
| Transform | 変換 | 型・単位の統一、欠損処理、不要列削除 |
| Load | 格納 | 整形済みデータをDWHへ保存 |

### Extract（抽出）

各システムから必要なデータを取り出します。

### Transform（変換）

分析しやすい形へ整えます。

- データ形式の統一
- 不要データの削除
- 単位の変換
- 欠損値処理

### Load（格納）

整形済みデータをDWHなどへ格納します。

**ETLは分析そのものではなく、分析に使うデータを準備する工程**です。

## どんな場面で使う？

### DWHを作るとき

複数システムのデータを統合して、分析用データとして蓄積するときに使います。

### 経営ダッシュボードを作るとき

販売・顧客・会計などのデータ形式をそろえてから可視化します。

### 部門横断でデータを統合するとき

異なるシステム間の表記や単位を合わせる処理が必要になります。

## よくある誤解・混同

### ❌ ETL = データ分析

ETLは**分析前のデータ統合・準備プロセス**です。

### ETLとELTの違い

| 項目 | ETL | ELT |
|---|---|---|
| 順番 | 抽出 → 変換 → 格納 | 抽出 → 格納 → 変換 |
| 変換する時点 | 格納前 | 格納後 |
| 判断の軸 | 整えてから入れる | まず入れてから整える |

### データレイクとの違い

- **ETL**：データを移動・加工するプロセス
- **データレイク**：さまざまなデータを蓄積する考え方・保存基盤

「処理の流れ」なのか「保存先・保存の考え方」なのかで切り分けます。

## まとめ（試験直前用）

- ETL = **抽出 → 変換 → 格納**
- Transformは格納前に行う
- DWH向けのデータ統合で使われる
- 分析モデルを作る工程ではない
- **格納前に変換 = ETL / 格納後に変換 = ELT**

## 対応スキル項目（データエンジニアリング力シート）

- データ基盤
- データ統合
- ★ データ統合プロセス（ETL）の基本を理解している
- ★ 複数システムのデータを統合する考え方を理解している

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}
{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}
    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}{% assign matched = true %}{% endif %}
    {% endfor %}
    {% if matched %}
      <li style="margin-bottom: 6px;"><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% assign count = count | plus: 1 %}
    {% endif %}
    {% if count >= 5 %}{% break %}{% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>
<div style="margin-top: 16px;">🏠 <a href="/ds/">DS検定トップに戻る</a></div>
<div style="display:flex;justify-content:space-between;margin-top:12px;">
  {% if page.previous.url %}<a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>{% endif %}
  {% if page.next.url %}<a href="{{ page.next.url }}">{{ page.next.title }} →</a>{% endif %}
</div>
