---
layout: page
title: データウェアハウス（DWH）とは？データマートとの違いを理解する【DS検定】
permalink: /ds/data-warehouse-vs-datamart/
categories: [data-engineering]
tags: [ds, data-storage, data-structure, database]
prev: /ds/data-warehouse/
next: /ds/database-constraints/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

- **データウェアハウス（DWH）とは、企業のデータを分析のために統合して保存するデータベースです。**
- BIツールやOLAP分析は、このデータウェアハウスに蓄積されたデータを利用します。

DS検定では

- **DWH**
- **データマート**
- **BI**
- **OLAP**

の関係を理解しているかがよく問われます。

---

## 直感的な説明

企業にはさまざまなシステムがあります。

例えば

- 販売管理システム  
- 顧客管理システム  
- 在庫管理システム  

これらのシステムにはそれぞれデータが保存されています。

しかし、そのままでは

- 売上分析  
- 顧客分析  
- マーケティング分析  

を行うことが難しい場合があります。

そこで、これらのデータを

**分析用にまとめて保存する場所**

として作られるのが

**データウェアハウス（DWH）**

です。

---

## 定義・仕組み

データウェアハウスとは

**企業のさまざまなシステムからデータを集めて、分析用に統合したデータベース**

です。

一般的な構成は次のようになります。

```
業務システム （販売・顧客・在庫など）
↓
データウェアハウス（DWH）
↓
BIツール OLAP分析 レポート
```

DWHでは

- データ統合  
- 長期間データ保存  
- 分析の高速化  

が重視されます。

---

## どんな場面で使う？

データウェアハウスは

**企業のデータ分析基盤**

として使われます。

### 経営分析

- 売上推移  
- 利益率  
- KPI分析  

---

### マーケティング分析

- 顧客の購買傾向  
- 商品の人気分析  

---

### BIツール分析

BIツールは

**DWHのデータを使って分析**

を行います。

---

## よくある誤解・混同

### DWH vs データマート

DS検定でよく問われる違いです。

| 用語 | 意味 |
|---|---|
| データウェアハウス | 企業全体の分析データ |
| データマート | 部門ごとの分析データ |

イメージ

```
DWH ├ 営業データマート ├ マーケデータマート └ 財務データマート
```

---

### DWH vs 業務データベース

| 種類 | 目的 |
|---|---|
| 業務DB | 日常業務処理 |
| DWH | データ分析 |

業務DBは

- 注文処理  
- 在庫更新  

などの **処理速度** が重要です。

一方DWHは

**分析のしやすさ**

が重要になります。

---

## まとめ（試験直前用）

- **DWH＝企業データを分析のために統合したデータベース**
- BIツールやOLAPは **DWHのデータを使う**
- **データマート＝部門別DWH**
- 業務DBは **業務処理用**、DWHは **分析用**

DS検定では  
**DWH → BI → OLAP → データ分析**

という流れを理解しておくことが重要です。

---

## 対応スキル項目（データエンジニアリング力シート）

- データ基盤  
- データ管理  

★ データベースやデータウェアハウスなどのデータ管理基盤の基本概念を理解している

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
