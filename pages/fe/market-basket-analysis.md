---
layout: page
title: マーケットバスケット分析とは？POSデータの同時購入を見つける方法【基本情報技術者試験】
description: マーケットバスケット分析はPOSの購買履歴から一緒に買われやすい商品の組合せを見つける手法です。3C分析・ABC分析・コンジョイント分析との違いを比較し、購入データを操作して科目Aの判断基準を学びます。
permalink: /fe/market-basket-analysis/
tags: [fe, fe-strategy, marketing]
fe_section: ストラテジ系
fe_subsection: 経営戦略
fe_order: 123
date: 2026-10-31
last_modified_at: 2026-10-31
---

## まず結論

**マーケットバスケット分析**は、POS（販売時点情報管理）などの購買履歴から、**一緒に購入されやすい商品の組合せ**を見つけるデータマイニングの手法です。

基本情報技術者試験の科目Aでは、**「POSデータ」「同時購入」「一緒に買われる商品」**というキーワードが判断の決め手になります。

## 直感的な説明

スーパーの買い物かごを5つ調べたとします。

| 会計（1回の取引） | 購入した商品 |
|---|---|
| A | パン、牛乳、卵 |
| B | パン、牛乳 |
| C | パン、コーヒー |
| D | パン、牛乳、卵 |
| E | 牛乳、卵 |

この例では「パンと牛乳」が同じ会計で購入されたのは3回、「パンとコーヒー」は1回です。

このように**同じ会計で一緒に買われる組合せを調べる**ことで、売場の配置や関連商品の提案に役立てられます。

ただし、同時購入が多いだけで「片方の商品がもう片方の購入を引き起こした」とは言えません。

## 定義・仕組み

マーケットバスケット分析は、購買データに含まれる商品同士の**共起（同時に現れること）**を調べます。広い意味ではアソシエーション分析の一例です。

- **POSデータ**：どの商品が、いつ、いくつ売れたかなどの販売記録。
- **取引（バスケット）**：一度の会計で購入した商品の集合。
- **同時購入数**：指定した2商品が両方入っている取引の件数。

例えば、5取引のうち3取引でパンと牛乳が一緒に買われたら、同時購入数は**3件**、全取引に対する割合（支持度）は**3 ÷ 5 = 60%**です。

この割合は、パンを買った人の60%が牛乳も買ったという意味ではありません。分母が**全取引**だからです。

### 触って確認：どの商品が一緒に買われる？

**見るポイント：** 比較する商品を変更すると、同時購入数がどう変わるでしょうか。上の5取引と同じデータを使います。

<link rel="stylesheet" href="{{ '/assets/css/fe-market-basket-demo.css' | relative_url }}">

<div class="fe-basket-demo" id="fe-market-basket-demo">
  <div class="fe-basket-controls">
    <div><label for="fe-basket-first">商品1</label><select id="fe-basket-first"><option value="bread">パン</option><option value="milk">牛乳</option><option value="egg">卵</option><option value="coffee">コーヒー</option></select></div>
    <div><label for="fe-basket-second">商品2</label><select id="fe-basket-second"><option value="milk">牛乳</option><option value="bread">パン</option><option value="egg">卵</option><option value="coffee">コーヒー</option></select></div>
  </div>
  <p class="fe-basket-prompt">予想：この2商品が両方入っている会計は何件でしょうか？</p>
  <div class="fe-basket-prediction" role="group" aria-label="同時購入数の予想">
    <button type="button" data-fe-basket-guess="1">1件</button>
    <button type="button" data-fe-basket-guess="2">2件</button>
    <button type="button" data-fe-basket-guess="3">3件</button>
    <button type="button" data-fe-basket-guess="4">4件</button>
  </div>
  <button type="button" id="fe-basket-reveal">結果を見る（予想なしでもOK）</button>
  <p id="fe-basket-feedback" aria-live="polite">商品を選んで結果を確認しましょう。</p>
  <div id="fe-basket-results" hidden>
    <p><strong>同時購入数：<output id="fe-basket-count">3件</output></strong></p>
    <p>全5取引に対する割合（支持度）：<output id="fe-basket-rate">60%</output></p>
    <table class="fe-basket-table"><caption>5件の購買履歴（「両方あり」の取引を表示）</caption><thead><tr><th scope="col">会計</th><th scope="col">商品</th><th scope="col">判定</th></tr></thead><tbody id="fe-basket-rows"></tbody></table>
    <p class="fe-basket-note">同時購入が多いことと、因果関係があることは別です。商品1と商品2に同じ商品を選んだ場合は、その商品の購入件数を表示します。</p>
  </div>
  <button type="button" id="fe-basket-reset">初期状態に戻す</button>
</div>
<script src="{{ '/assets/js/fe-market-basket-demo.js' | relative_url }}" defer></script>
<noscript><p>JavaScriptが利用できない場合は、上の購買履歴表を使って数えましょう。パンと牛乳が両方あるのはA・B・Dの3件、牛乳と卵が両方あるのはA・D・Eの3件です。</p></noscript>

## 科目Aでどう出る？

次の4つの分析手法を目的で区別しましょう。

| 分析手法 | 何を調べるか | 選択肢のキーワード |
|---|---|---|
| **マーケットバスケット分析** | **一緒に買われる商品の組合せ** | POS、同時購入、買い物かご |
| [ABC分析](/fe/abc-analysis/) | 売上高・在庫金額などの大きい順に重点管理する項目 | 累積構成比、A・B・C、重点管理 |
| 3C分析 | 顧客（Customer）・自社（Company）・競合（Competitor）を整理 | 市場環境、競合、自社 |
| コンジョイント分析 | 商品の価格・機能・デザインなどの属性に対する顧客の選好 | 属性、組合せ、選好、重要度 |

**「どの商品が重要か」ならABC分析、「どの商品が一緒に買われるか」ならマーケットバスケット分析**です。

### 確認問題

ある小売店がPOSの取引履歴を使って、同じ会計で購入される商品の組合せを発見しようとしている。最も適切な分析手法はどれか。

- ア：3C分析
- イ：ABC分析
- ウ：コンジョイント分析
- エ：マーケットバスケット分析

<details markdown="1">
<summary>答えと解説を見る</summary>

**正解：エ。** 取引履歴から同時購入される商品の組合せを発見するためです。ABC分析は重点管理する項目を分類する手法であり、目的が異なります。

</details>

## どんな場面で使う？

- **売場の配置**：一緒に購入されやすい商品を近くに置くか検討する。
- **ECサイト**：関連商品をおすすめする候補を探す。
- **販売施策**：セット販売やキャンペーンの組合せを検討する。

実際の分析では、同時購入数だけでなく、支持度・信頼度・リフト値などを用いて関連の強さを評価することもあります。詳しい計算はDS検定向けの[マーケットバスケット分析](/ds/market-basket-analysis/)で扱っています。

## よくある誤解・混同

### 売上の多い商品を探す手法？

それは主に**ABC分析**です。マーケットバスケット分析は、商品同士の同時購入の関係を調べます。

### 同時購入される商品は、必ず近くに置くべき？

必ずではありません。店舗の動線、利益率、購買目的などを考慮して判断します。

### 同時購入が多いなら、因果関係がある？

いいえ。**関連があることと、原因であることは別**です。また、よく売れる商品は多くの商品と同時購入されやすいため、件数だけで関連の強さを断定できません。

## まとめ（試験直前用）

- マーケットバスケット分析：**POSなどの購買履歴から同時購入の組合せを発見**。
- ABC分析：**重要度の高い項目を重点管理**。
- 3C分析：**顧客・自社・競合**。
- コンジョイント分析：**商品属性に対する選好**。
- 同時購入の関連は分かるが、因果関係までは証明できない。

**「一緒に買われる商品」→ マーケットバスケット分析**と判断しましょう。

{% include fe_article_footer.html %}
