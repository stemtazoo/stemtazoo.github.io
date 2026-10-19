---
layout: page
title: DWHとデータマートの違い：全社・部門とBI・OLAPの関係【DS検定】
description: "DWHとデータマートを、全社横断の売上・在庫データと営業向けの集計で比較します。対象範囲と指標の共有、DWHに依存しないマート、BI・OLAPとの役割の違いを整理します。"
permalink: /ds/data-warehouse-vs-datamart/
categories: [data-engineering]
tags: [ds, data-storage, data-structure, database]
ds_area: dataengineering
ds_section: data-storage
prev: /ds/data-warehouse/
next: /ds/database-constraints/
last_modified_at: 2026-10-19
---

<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**DWHは広い範囲のデータを統合して分析する基盤、データマートは部門や目的などの範囲に焦点を絞った分析用データ基盤**です。このページでは「誰が、どの範囲を見るか」を比較します。

保存時の整理とデータレイクとの違いは、[DWHの基本とSchema on Write](/ds/data-warehouse/)で確認できます。

## 直感的な説明

販売・顧客・在庫の各システムを持つ会社を考えます。経営企画は全社の売上と在庫を横断して分析したい一方、営業部は担当商品・地域ごとの月次売上をすばやく見たいとします。

| 使う人・目的 | 用意するデータの例 | 捉え方 |
|---|---|---|
| 経営企画が複数部門を横断する | 共通の商品・顧客コードにそろえた売上・在庫履歴 | DWH |
| 営業部が販売状況を見る | 月・地域・商品別の売上に絞ったデータ | 営業データマート |
| マーケティングが購買傾向を見る | キャンペーン・顧客層別の集計 | マーケティングデータマート |

DWHではデータの統合・過去の履歴・分析のしやすさが重要です。マートでは利用目的に合った範囲や集計を用意します。

## 定義・仕組み

### DWHから作る場合と、直接作る場合

DWHの一部を取り出すマートは、共通の定義を再利用しやすくなります。一方、業務システムなどから直接作る独立型のマートもあります。**マートは必ずDWHの物理的なコピー、というわけではありません。**

### BI・OLAPは別の役割

| 用語 | 役割 | この例で行うこと |
|---|---|---|
| DWH | 広い範囲の分析用データを統合・蓄積 | 全社の売上・在庫履歴をそろえる |
| データマート | 特定の利用目的・対象範囲に絞る | 営業向けのデータを用意する |
| BI | 判断に使う集計・可視化・レポートなど | 売上ダッシュボードを表示する |
| OLAP | 軸を変えて多次元的に分析する | 月別から地域別へ切り替え、商品へ掘り下げる |

BIはDWHやマートなどを利用でき、OLAP的な分析を提供する場合もあります。**DWH → BI → OLAPという必須の直列工程ではありません。**

## どんな場面で使う？

- 全社の利益率やKPIを同じ基準で比較したいときは、統合と指標の共通化を重視する。
- 営業やマーケティングの定型分析では、利用者に必要な範囲をマートとして提供する。
- 部門ごとに「売上」の定義が違うときは、マートを増やす前に、返品・値引き・計上時点をそろえる。

部門だけの集計ができても、共通キーや粒度が異なるままでは全社の横断分析には使いにくくなります。

## よくある誤解・混同

### 小さいDWHならすべてデータマート？

容量よりも対象範囲・利用目的に着目します。特定の業務やテーマに焦点を絞ることがポイントです。

### 部門ごとに作れば指標は自動でそろう？

共通の定義・粒度・更新タイミングを管理する必要があります。独立型のマートではデータの分断にも注意します。

### 業務DBも同じ分析基盤？

注文登録や在庫更新を正しく処理する業務DBと、履歴を横断して分析する基盤では主な目的が異なります。BIやOLAPも保存基盤と同義ではありません。

## まとめ（試験直前用）

- DWHは広い範囲を統合、マートは部門・テーマなどに焦点を絞る。
- マートにはDWHを使うものと、独立して作るものがある。
- BIは分析・可視化の利用側、OLAPは多次元分析の考え方。
- 全社と部門で指標の定義をそろえる。

## 公式情報・参考リンク

- [AWS：What is a Data Mart?](https://aws.amazon.com/what-is/data-mart/)
  - 対象範囲の違いと、DWHに依存するマート・独立したマートを確認できます。

## 対応スキル項目（ver.6 データエンジニアリング）

- **分類**：データエンジニアリング
- **スキルカテゴリ**：データ蓄積
- **サブカテゴリ**：データ蓄積技術
- **必須スキル**：—
- ★ データマートやDWHなどの集中型データ基盤と、データファブリックやデータメッシュなどの分散型データ基盤の設計思想の違いを理解し、ユースケースや組織構造に応じて適切に選択できる
- [ver.6 ★1スキルチェックで確認する](/ds/engineering-skillcheck/)
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
