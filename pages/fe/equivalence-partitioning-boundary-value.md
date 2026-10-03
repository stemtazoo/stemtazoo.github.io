---
layout: page
title: 同値分割と境界値分析とは？代表値と境界値の選び方【基本情報技術者試験】
description: 同値分割は同じように処理される入力のグループから代表値を選び、境界値分析は処理が変わる境目を確かめる方法です。有効範囲内の処理切替も境界として扱い、代表値と境界値を兼用できる条件、重複を除いた最小個数の数え方、比較演算子の誤りを見つける入力を整理します。
permalink: /fe/equivalence-partitioning-boundary-value/
tags: [fe, fe-technology, programming, testing]
fe_section: テクノロジ系
fe_subsection: システム開発技術
fe_order: 22
date: 2026-10-03
last_modified_at: 2026-10-03
---

## まず結論

**同値分割は、同じように処理される入力をグループに分けて代表値を選ぶ方法です。境界値分析（限界値分析）は、そのグループの境界付近を重点的に確認する方法です。**

テストデータの最小個数は、「代表値は何個必要か」「どの境界値が必要か」「同じ値を兼用できるか」の順に考えます。入力が有効か無効かだけでなく、**有効範囲の中で処理が変わる境目**も確認します。

## 直感的な説明

受付番号を判定するシステムを考えます。入力は整数で、仕様は次のとおりです。

| 入力する受付番号 | 期待する処理 |
|---|---|
| 0以下 | 入力エラー |
| 1～40 | 窓口Aへ案内 |
| 41～200 | 窓口Bへ案内 |
| 201以上 | 入力エラー |

窓口Aへ案内されるかを確認するために、1～40をすべて試す代わりに、例えば20を代表として選びます。これが同値分割の考え方です。

ただし、20では正しく動いても、40を誤って窓口Bへ案内する実装かもしれません。そこで40と41を試し、処理が変わる境目を確認します。これが境界値分析です。

## 定義・仕組み

### 同じ処理になる入力を分ける

同値分割で分けたグループを**同値クラス**と呼びます。仕様から、同じように処理されると想定する値をまとめます。

受付番号の例には、有効クラスが2つ、無効クラスが2つあります。どちらの無効範囲もエラーですが、下限側と上限側を別の区間として確認します。

| 同値クラス | 範囲 | 代表値の例 |
|---|---|---:|
| 無効・下限側 | 0以下 | -10 |
| 有効・窓口A | 1～40 | 20 |
| 有効・窓口B | 41～200 | 120 |
| 無効・上限側 | 201以上 | 250 |

代表値は一意には決まりません。20の代わりに10を選んでも、同じクラスの代表になり得ます。また、代表値を試しただけでクラス内のすべての値の正しさが保証されるわけではありません。

### 境界をまたぐ値を選ぶ

ここでは、整数の隣り合うクラスの境目について、**両側の値を1つずつ選ぶ**方法を使います。

| 確認する境目 | 選ぶ値 | 期待する処理 |
|---|---|---|
| 無効から窓口Aへ | 0、1 | エラー、窓口A |
| 窓口Aから窓口Bへ | 40、41 | 窓口A、窓口B |
| 窓口Bから無効へ | 200、201 | 窓口B、エラー |

40も41も有効な値ですが、期待する処理が異なるため、この境目も対象です。

境界値分析には、境界と隣接クラス側の値を見る2値の方法や、境界の両隣まで見る3値の方法があります。[ISTQB Foundation Levelシラバス v4.0.1（英語PDF、4.2.1～4.2.2）](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf)でも区別されています。**必要な値は問題やテスト方針の指定で決め、機械的に前後3個を選ばない**ようにします。

### 代表値と境界値を切り替えて見る

次の図解は、「有効クラスから境界ではない代表値を1個ずつ」「すべての区間境界の両側の値」を選ぶ条件です。無効クラスの代表値を別途追加する条件はありません。

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}">
<div class="fe-learning-demo fe-boundary-demo" data-fe-boundary-demo>
  <p class="fe-learning-demo__title">受付番号：代表値2個と境界値6個</p>
  <div class="fe-learning-demo__controls" role="group" aria-label="テストデータの表示切替">
    <button type="button" class="fe-learning-demo__button" data-boundary-mode="representative" aria-pressed="false" disabled>代表値だけ</button>
    <button type="button" class="fe-learning-demo__button" data-boundary-mode="boundary" aria-pressed="false" disabled>境界値だけ</button>
    <button type="button" class="fe-learning-demo__button" data-boundary-mode="both" aria-pressed="true" disabled>両方を見る</button>
  </div>
  <div class="fe-boundary-demo__classes">
    <div class="fe-boundary-demo__class"><strong>無効：0以下</strong><p>入力エラー</p><span data-boundary-kind="boundary" class="fe-boundary-demo__value is-boundary">0（境界値）</span></div>
    <div class="fe-boundary-demo__class is-valid"><strong>有効：1～40</strong><p>窓口A</p><span data-boundary-kind="boundary" class="fe-boundary-demo__value is-boundary">1（境界値）</span><span data-boundary-kind="representative" class="fe-boundary-demo__value">20（代表値）</span><span data-boundary-kind="boundary" class="fe-boundary-demo__value is-boundary">40（境界値）</span></div>
    <div class="fe-boundary-demo__class is-valid"><strong>有効：41～200</strong><p>窓口B</p><span data-boundary-kind="boundary" class="fe-boundary-demo__value is-boundary">41（境界値）</span><span data-boundary-kind="representative" class="fe-boundary-demo__value">120（代表値）</span><span data-boundary-kind="boundary" class="fe-boundary-demo__value is-boundary">200（境界値）</span></div>
    <div class="fe-boundary-demo__class"><strong>無効：201以上</strong><p>入力エラー</p><span data-boundary-kind="boundary" class="fe-boundary-demo__value is-boundary">201（境界値）</span></div>
  </div>
  <p data-boundary-status aria-live="polite" aria-atomic="true">両方：代表値2個＋境界値6個＝8個。代表値は境界値と重ならない値を選んでいます。</p>
  <p class="fe-learning-demo__hint">区間の幅は数値の大きさに比例していません。文字と枠線で値の役割を区別しています。JavaScriptが使えない場合も全8個を表示します。</p>
</div>
<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}" defer></script>

## 科目Aでどう出る？

最小個数を求めるときは、手法の名前だけでなく、**追加の条件**を確認します。

受付番号の例で、図解と同じ条件なら次のように数えます。

1. 有効クラスは2つなので、境界ではない代表値を2個選ぶ。例：20、120。
2. 区間の境目は3か所。両側の値は0、1、40、41、200、201の6個。
3. 同じ値が重なっていないか確認する。この条件では代表値と境界値は兼用できない。
4. 2個＋6個で、必要な入力値は8個。

一方、代表値を境界値で兼用してよく、同じ6個の境界値をすべて試す条件なら、1や40が窓口A、41や200が窓口Bの代表にもなります。別の代表値を追加する必要はなく、6個で条件を満たせます。

**「同値分割と境界値分析なら必ず8個」ではありません。** クラスの数、必要な境界、兼用の可否から、重複を除いた入力値の集合を作ります。

## 科目Bでどう使う？

仕様から選んだ境界値は、比較演算子の誤りを確認するときに役立ちます。受付番号を判定する疑似言語で、次の誤りがあるとします。

```text
if x < 1 or x > 200
    入力エラー
elseif x < 40
    窓口Aへ案内
else
    窓口Bへ案内
endif
```

仕様では40も窓口Aです。しかし、`x < 40` では40が真にならず、窓口Bへ案内されます。正しくは `x <= 40` です。

| 入力 | 仕様上の期待結果 | 誤ったプログラムの結果 |
|---:|---|---|
| 20 | 窓口A | 窓口A |
| 40 | 窓口A | 窓口B |
| 41 | 窓口B | 窓口B |

代表値20だけでは、この誤りを見つけられません。**仕様から期待結果を決め、境界値を代入して条件式の真偽を追う**のが確認の手順です。テストデータを、誤った実装に合わせて選ばないようにします。

## よくある誤解・混同

| 誤解 | 正しい理解 |
|---|---|
| 有効な入力はすべて1クラス | 期待する処理が変わるなら、有効範囲内も分ける |
| 同値分割は常に3クラス | 仕様に応じてクラス数は変わる |
| 境界は有効・無効の境目だけ | 窓口Aと窓口Bのような処理の切替も対象 |
| 代表値は必ず中央の値 | クラスを代表でき、指定条件を満たす値を選ぶ |
| 代表値数と境界値数を必ず足す | 同じ値を兼用できる場合は、重複して数えない |
| 整数でも小数でも境界の隣は±1 | 隣接する値は入力の単位による。小数や連続値では扱いを確認する |

テストの設計根拠や他の手法の概要は[ブラックボックステスト](/fe/black-box-testing/)で、内部の分岐を基準にするテストとの違いは[ブラックボックスとホワイトボックスの比較](/fe/black-box-vs-white-box-testing/)で整理しています。

## まとめ（試験直前用）

- 同値分割は、同じように処理されるクラスから代表値を選ぶ。
- 境界値分析は、クラスの境界付近を確認する。
- 有効範囲内でも、処理が変われば境界がある。
- 最小個数は指定条件から値を列挙し、兼用と重複を確認して数える。
- 境界値を条件式に代入すると、`<` と `<=` などの誤りを見つけやすい。

{% include fe_article_footer.html %}
