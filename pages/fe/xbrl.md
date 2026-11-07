---
layout: page
title: XBRLとは？財務情報の意味をデータとして交換する仕組み【基本情報技術者試験】
description: XBRLを財務情報などに共通の意味を付けて交換・集計する規格として解説。XMLとの関係、タクソノミ・インスタンス、EDINETでの利用、HTML・PDFとの違いを科目A向けに整理します。
permalink: /fe/xbrl/
tags: [fe, fe-strategy, business-management]
fe_section: ストラテジ系
fe_subsection: 経営戦略
fe_order: 340
date: 2026-11-07
last_modified_at: 2026-11-07
related_articles:
  - /fe/xml/
  - /fe/financial-statements-comparison/
---

## まず結論

**XBRL（eXtensible Business Reporting Language）は、企業の財務情報などをコンピュータが意味を判別できる形で記述し、交換・集計・比較しやすくするための標準規格**です。

基本情報技術者試験の科目Aでは、**「XMLを基礎に財務報告のデータを記述・交換する」→ XBRL** と判断します。

XBRLは文書をきれいに表示するための形式ではありません。**売上高などの数値が何を意味するか**を明確にすることが中心です。

## 直感的な説明

会社の決算資料に次のような数字が書かれているとします。以下は記事独自の架空データです。

| 会社 | 対象期間 | 項目 | 金額 |
|---|---|---|---:|
| A社 | 2025年度 | 売上高 | 100億円 |

人なら表の見出しを読んで「2025年度のA社の売上高が100億円」と理解できます。

しかし、数字の `100` だけを取り出したコンピュータには、それが**売上高なのか、利益なのか、単位が円なのか億円なのか**判断できません。

XBRLでは、数字と一緒に意味を示すための情報を持たせます。

<div class="fe-xbrl-figure" role="group" aria-label="人が読む表とXBRLのデータ構造の比較">
  <div class="fe-xbrl-figure__panel">
    <strong>人が読む表</strong>
    <div class="fe-xbrl-figure__amount">売上高：100億円</div>
    <p>見出しや文脈を読んで意味を理解する</p>
  </div>
  <div class="fe-xbrl-figure__arrow" aria-hidden="true">→</div>
  <div class="fe-xbrl-figure__panel fe-xbrl-figure__panel--data">
    <strong>構造化した財務データ</strong>
    <dl>
      <div><dt>項目</dt><dd>売上高</dd></div>
      <div><dt>企業</dt><dd>A社</dd></div>
      <div><dt>期間</dt><dd>2025年度</dd></div>
      <div><dt>値・単位</dt><dd>100億円</dd></div>
    </dl>
    <p>項目や期間・単位を区別して自動処理しやすくする</p>
  </div>
</div>

<style>
.fe-xbrl-figure{display:grid;grid-template-columns:minmax(0,1fr) 26px minmax(0,1fr);align-items:stretch;gap:8px;margin:1.1rem 0}
.fe-xbrl-figure__panel{min-width:0;padding:14px 12px;border:1px solid #aab9c8;border-radius:10px;background:#f6f8fb;color:#25364a}
.fe-xbrl-figure__panel--data{background:#eaf5ed;border-color:#8cac95}
.fe-xbrl-figure__panel strong{display:block;line-height:1.55;margin-bottom:8px}
.fe-xbrl-figure__amount{background:#fff;border:1px solid #c2ced6;border-radius:6px;padding:10px 6px;text-align:center;font-weight:bold}
.fe-xbrl-figure__arrow{align-self:center;text-align:center;font-size:1.3rem;font-weight:700;color:#405d71}
.fe-xbrl-figure__panel p{font-size:.85rem;margin:10px 0 0;line-height:1.6}
.fe-xbrl-figure__panel dl{margin:0}
.fe-xbrl-figure__panel dl div{display:grid;grid-template-columns:42px minmax(0,1fr);gap:5px;border-bottom:1px solid #bdd6c6;padding:5px 0;font-size:.86rem}
.fe-xbrl-figure__panel dt{font-weight:bold}
.fe-xbrl-figure__panel dd{margin:0;overflow-wrap:anywhere}
@media(max-width:560px){.fe-xbrl-figure{grid-template-columns:minmax(0,1fr)}.fe-xbrl-figure__arrow{transform:rotate(90deg)}}
</style>

上の図は**概念図**です。実際のXBRLデータは規格に沿った要素・識別子・コンテキスト・単位などで表現します。図中の日本語の項目名が、そのままXBRLのタグ名になるわけではありません。

## 定義・仕組み

### XMLとの関係

**XML**は、データの構造をタグなどで記述するための基礎技術です。**XBRL**はその考え方を財務報告などの分野で利用し、項目の意味を共通化するための仕組みを備えています。

```text
XML
└─ タグなどを使ってデータの構造を表現する

XBRL
└─ 財務情報などを共通の定義に沿って
   意味付けし、報告・交換できるようにする
```

FEの用語問題では「XMLを財務情報の交換に応用したもの」と理解すれば十分です。ただし現在のXBRL標準には、XML以外の表現形式もあります。**XBRL＝すべてのデータファイルが必ずXML形式**とは断定しないでください。

XMLそのものの構文は[XMLとは？](/fe/xml/)で学びます。ここでは**財務情報に意味を付けること**に注目します。

### タクソノミとインスタンス

金融庁のEDINETでも使われる重要な2語です。

| 用語 | 初心者向けの意味 |
|---|---|
| **タクソノミ（Taxonomy）** | 財務項目などの**共通の定義・辞書**。「売上高」などの項目が何を意味するか定める |
| **インスタンス（Instance）** | 定義に従って報告した**実際のデータ**。金額、期間、単位などを含む |

```text
タクソノミ：何を報告するかの定義
     ↓
インスタンス：実際に報告する数値・情報
     ↓
ソフトウェアが集計・比較に利用
```

数字の `100` を正しく比較するためには、項目の定義だけでなく、**企業・対象期間・通貨や単位**なども必要です。XBRL Internationalも、データ項目に加えて単位や対象期間などを関連付けることを説明しています。

### XBRLの簡単なデータイメージ

次は、実際のXBRLファイルの構文ではなく、**意味の付け方だけを表す疑似表現**です。

```text
項目 = 売上高
企業 = A社
対象期間 = 2025年度
値 = 10000000000
単位 = JPY（円）
```

実際のファイル例と混同しないため、架空の独自タグを「正式なXBRL構文」として掲載していません。

## 科目Aでどう出る？

問題文に**財務情報の電子的な交換・共通の意味・自動分析**が出てきたらXBRLを考えます。

| 用語 | 判断の手掛かり |
|---|---|
| **XBRL** | **財務報告などのデータの意味を定義し、機械的に交換・比較する** |
| XML | 汎用的な構造化データの記述 |
| HTML | Webページの文書構造や内容の記述 |
| PDF | 文書のレイアウトや見た目を保って配布・表示 |
| RPG | 帳票や事務処理向けのプログラミング言語 |

**「XMLを使う」というだけではXBRLに限定できません。** 財務情報の共通形式という目的が決め手です。

### 独自の確認問題

複数の企業が公開した売上高や利益などの情報を、項目の意味・対象期間・通貨などを区別して機械的に集計・比較しやすくするための規格として最も適切なものはどれか。

- A：Webページの見出しやリンクなどの構造を表すHTML
- B：ページの見た目を保持するPDF
- C：企業の財務報告などに共通の意味を付けるXBRL
- D：帳票処理にも用いられるRPG

<details markdown="1">
<summary>答えと理由を見る（タップして開く）</summary>

**正解：C（XBRL）**

財務情報を共通の定義に沿って意味付けし、交換・比較する目的に最も合うためです。HTMLはWebページの構造、PDFは文書表示、RPGはプログラミング言語なので、目的が異なります。

</details>

## どんな場面で使う？

### EDINETでの企業情報の開示

金融庁の[EDINETタクソノミの公表情報](https://www.fsa.go.jp/search/20251111.html)によると、EDINETではXBRLを利用して有価証券報告書等を作成・提出します。財務報告の電子データを取得・分析する際に役立ちます。

2026年版EDINETタクソノミは正式公表済みです。一方、2026年9月11日に金融庁が公開した[2027年版EDINETタクソノミ](https://www.fsa.go.jp/search/20260911.html)は**案**です。試験対策では版番号の暗記より、**XBRLの目的と利用場面**を押さえましょう。

### Pythonを使った財務データ分析

複数企業の財務指標をPythonで比較する場合は、次の流れを考えます。

```text
EDINETなどから対象データを取得
  ↓
財務項目・企業・期間・単位を確認
  ↓
同じ意味の項目や同じ期間に揃える
  ↓
表にまとめて集計・可視化する
```

ただし、XBRL形式であれば無条件に異なる企業の数値を比較できるわけではありません。**会計基準、連結・個別、期間、項目の定義や単位が一致するか**を確かめる必要があります。

## よくある誤解・混同

### XBRLはWebページを表示するための言語？

違います。Webページの文書構造を記述するのはHTMLです。XBRLの中心的な目的は**報告データを意味付けし、機械処理を可能にすること**です。

### PDFとXBRLはどちらも財務報告だから同じ？

違います。PDFは文書の表示・配布に適し、XBRLは数値や項目の意味を構造化して扱うための仕組みです。両方を利用することもあります。

### タクソノミに売上金額が入っている？

通常は違います。タクソノミは**項目の定義**、インスタンスは**実際に報告される情報**です。

### XBRLデータなら必ず正しく比較できる？

違います。項目定義や会計基準、期間・単位の違いに注意します。機械可読性が高いことと、比較条件が同一であることは別です。

## まとめ（試験直前用）

- **XBRL＝財務情報などに意味を付けて報告・交換する標準規格**
- XMLを基礎に発展したが、現在のXBRLはXML形式だけに限らない
- **タクソノミ＝項目の共通定義／インスタンス＝報告する実データ**
- **EDINET＝XBRLが利用される代表例**
- **HTML＝Webページ／PDF＝文書表示／RPG＝プログラミング言語** と区別する

### 一次情報・参考資料

- [XBRL International：Taxonomies](https://www.xbrl.org/the-standard/what/key-concepts-in-xbrl/taxonomies/) — データ項目の意味や、期間・単位の扱い
- [XBRL International：Reporting Requirements](https://specifications.xbrl.org/reporting-requirements.html) — 報告データと単位・規則の関係
- [金融庁：2026年版EDINETタクソノミの公表](https://www.fsa.go.jp/search/20251111.html) — EDINETにおけるXBRLとタクソノミ・インスタンス
- [金融庁：2027年版EDINETタクソノミ（案）](https://www.fsa.go.jp/search/20260911.html) — 更新案、2026年9月11日公表

{% include fe_article_footer.html %}
