---
layout: page
title: ETLとは？（データ統合の基本プロセス）【DS検定リテラシー】
permalink: /ds/etl/
categories: [data-engineering]
tags: [ds, data-processing]
prev: /ds/batch-vs-stream/
next: /ds/hadoop/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論
ETLとは、データを「抽出（Extract）→変換（Transform）→格納（Load）」する一連の処理のことです。  
DS検定では「DWHにデータを入れる前の処理は何か？」という形で問われます。


## 直感的な説明

企業には、

- 販売システム
- 会計システム
- 顧客管理システム

など、別々のデータがあります。

そのままでは形式がバラバラ。

そこで、

① 必要なデータを取り出す  
② 形式をそろえて加工する  
③ 分析基盤（DWHなど）に入れる  

この流れがETLです。

「データを整えてから倉庫に入れる作業」と考えると分かりやすいです。


## 定義・仕組み

ETLは3つの工程から成ります。

### ① Extract（抽出）
各システムからデータを取り出す


### ② Transform（変換）
- データ形式の統一
- 不要データの削除
- 単位の変換
- 欠損値処理

ここが最も重要です。


### ③ Load（格納）
整形済みデータをDWHに保存する


重要ポイント：

ETLは「分析前の前処理プロセス」です。  
分析そのものではありません。


## どんな場面で使う？

### 使う場面

- DWH構築
- 経営ダッシュボード作成
- 部門横断データ統合

特に「複数システムを統合する」場面で使われます。


### 向かない場面

- リアルタイム処理
- 生データをそのまま保存するデータレイク

その場合はELTやストリーム処理が使われます。


## よくある誤解・混同

### ① ETL＝データ分析？

違います。

ETLは分析の前段階です。

DS検定では  
「分析モデルを構築する工程」と混同させてきます。


### ② ELTとの違い

| 項目 | ETL | ELT |
|------|-----|-----|
| 変換タイミング | 格納前 | 格納後 |
| 主な用途 | 従来型DWH | クラウド基盤 |

DS検定では  
「クラウド」「大容量基盤」とあればELT寄りです。


### ③ データレイクとの混同

データレイクは保存の考え方。  
ETLは加工プロセス。

役割がまったく違います。


## まとめ（試験直前用）

- ETL＝抽出→変換→格納  
- DWHに入れる前の整形作業  
- 分析そのものではない  
- 複数システム統合に必須  
- 「変換してから保存」→ ETL


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
