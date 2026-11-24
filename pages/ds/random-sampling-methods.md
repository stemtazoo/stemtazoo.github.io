---
layout: page
title: 無作為抽出法とは？種類と違いを整理【DS検定リテラシー】
permalink: /ds/random-sampling-methods/
categories: [data-science]
tags: [ds, data-preparation, statistics]
ds_area: datascience
ds_section: data-preparation
description: "単純無作為・系統・層別・集落・多段の抽出手続を比較します。各層から取ることと比例配分の違い、精度・コスト・名簿の条件、無作為でも誤差や偏りが残る点を整理します。"
last_modified_at: 2026-11-24
image:
  path: https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/ds/random-sampling-methods.png
  width: 1731
  height: 909
  alt: "単純無作為・系統・層別・集落・多段の5種類を、抽出する対象と手順の違いで比較した図"
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

無作為抽出法とは、調査者の都合や主観で対象を選ばず、**確率的な手続で母集団から標本を選ぶ方法**です。
DS検定では「どの抽出方法かを見抜けるか」「方法の違いを切り分けられるか」が問われます。

無作為抽出をしても、偶然による標本誤差がなくなるわけではありません。狙いは「必ず偏りのない標本を作る」ことではなく、**選び方に意図的な偏りが入りにくく、抽出確率を説明できる状態にすること**です。


<figure style="margin:16px 0 20px;">
  <img src="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/ds/random-sampling-methods.png" width="1731" height="909" alt="無作為抽出法の5種類。単純無作為は個人をランダムに、系統は一定間隔で、層別は各層から、集落は選んだグループ全体を、多段は段階的に対象を選ぶ図" style="display:block;width:100%;max-width:100%;height:auto;" loading="lazy" decoding="async">
  <figcaption style="font-size:0.88em;line-height:1.5;color:#666;margin-top:8px;">5種類の違いは「何を、どの順序で選ぶか」。層別は各層から一部を選び、集落は選んだ集団を丸ごと調べる点に注目しましょう。</figcaption>
</figure>

## 直感的な説明

たとえば、全国の中学生の体力を調べたいとします。

- 1校ずつランダムに選ぶのか  
- 地域ごとに分けてから選ぶのか  
- 男女を分けてから人数を決めて選ぶのか  

取り出し方が違うだけで、データの偏りや精度が変わります。

無作為抽出法は、  
「どうやって公平に取り出すか」の設計ルールです。


## 定義・仕組み

代表的な無作為抽出法は次の5つです。

### ① 単純無作為抽出法

母集団の各対象が同じ確率で選ばれるように、くじ引きや乱数で抽出する基本的な方法です。
例：住民名簿から乱数を使って100人を選ぶ。

→ 「各対象が同じ確率」「くじ引き・乱数」がキーワード。

### ② 系統抽出法
最初の1人をランダムに選び、その後は一定間隔で抽出する方法。  
例：5000人から10人おきに選ぶ。

→ 「間隔」がキーワード。


### ③ 多段抽出法
グループを段階的に絞り込み、最終的に個人を抽出する方法。  
例：都道府県 → 市区町村 → 学校 → 生徒

→ 「段階的に絞る」がポイント。


### ④ 集落抽出法（クラスタ抽出）
母集団をいくつかの集団に分け、選ばれた集団を丸ごと調査する方法。  
例：学校をランダムに選び、その学校の全員を調査。

→ 「選んだグループは全員調査」が特徴。


### ⑤ 層別抽出法
あらかじめ母集団を層（グループ）に分け、各層から人数を決めて抽出する方法。  
例：男女比6:4なら、6人と4人をそれぞれ抽出。

→ 「各層から抽出」が重要。母集団の男女比に合わせるのは比例配分の例です。層化抽出には、層の大きさと同じ比率にしない非比例配分もあります。


### 触って覚える：5種類の抽出方法を比較する

**見るポイント：** 「個人を選ぶ」「各層から選ぶ」「集団を丸ごと選ぶ」「集団の中からさらに選ぶ」の違いを確かめましょう。

この教材では、母集団60人を6グループ（各10人）に分け、全員を層A・B・Cのいずれかに分類しています（各層20人）。**グループは調査対象の集まり、層は比較したい属性による区分**で、同じ分類ではありません。

まず「集落抽出」を選んで「抽出する（もう一度押すと再抽出）」を押し、青くなった人がどのグループにいるか見てください。次に「多段抽出」に切り替えて、同じように確かめましょう。

ほかの方式も選べます。もう一度押すと、同じ方式で抽出し直せます。選び方の予想は省略できます。

<link rel="stylesheet" href="{{ '/assets/css/ds-random-sampling.css' | relative_url }}">

<div id="ds-sampling-demo" class="ds-sampling-demo" aria-label="5つの無作為抽出方法を比較する教材">
  <div class="ds-sampling-demo__controls">
    <label for="ds-sampling-method">① 抽出方法
      <select id="ds-sampling-method" data-method>
        <option value="simple">単純無作為抽出</option>
        <option value="systematic">系統抽出</option>
        <option value="stratified">層別抽出（比例配分の例）</option>
        <option value="cluster">集落抽出</option>
        <option value="multistage">多段抽出</option>
      </select>
    </label>
    <label for="ds-sampling-guess">② 選び方を予想（任意）
      <select id="ds-sampling-guess" data-guess>
        <option value="">予想せずに進む</option>
        <option value="simple">全員から個人を選ぶ</option>
        <option value="systematic">最初を選び一定間隔で選ぶ</option>
        <option value="stratified">各層から一部を選ぶ</option>
        <option value="cluster">選んだ集団の全員を選ぶ</option>
        <option value="multistage">集団を選んでから個人を選ぶ</option>
      </select>
    </label>
  </div>
  <div class="ds-sampling-demo__controls">
    <button type="button" data-draw>③ 抽出する（もう一度押すと再抽出）</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <p class="ds-sampling-demo__legend">青：選ばれた人　白：選ばれていない人。A・B・Cは属性の層、グループ1～6は集団を表します。</p>
  <div class="ds-sampling-demo__population" data-population aria-label="60人の母集団。青いマスが標本です">
    <p>母集団60人を表示します。</p>
  </div>
  <div class="ds-sampling-demo__result">
    <p><strong data-count>未抽出</strong></p>
    <p data-breakdown>抽出ボタンを押すと、選ばれた人を表示します。</p>
    <p role="status" aria-live="polite" aria-atomic="true" data-feedback>どの単位を選ぶ方式か予想してみましょう。</p>
  </div>
</div>
<noscript>
  <p>JavaScriptが無効でも手順は確認できます。60人を6グループ（各10人）、A・B・Cの3層（各20人）に分ける例です。単純無作為は全60人から12人、系統抽出は無作為な開始位置から5人おきに12人、層別は各層から4人ずつ12人を選びます。集落抽出は選んだ2グループの全20人、多段抽出は2グループを選んだ後に各6人ずつ合計12人を選びます。</p>
</noscript>
<script src="{{ '/assets/js/ds-random-sampling.js' | relative_url }}" defer></script>

**注意：** 集落抽出だけ標本サイズは20人で、ほかの4方式は12人です。これは抽出手順を見比べるための例で、人数が異なる標本から精度を直接比較する教材ではありません。抽出が無作為でも、得られた標本が毎回母集団の比率と一致するとは限りません。

## どんな場面で使う？

### 単純無作為抽出法

母集団の一覧があり、各対象を同じ確率で公平に選びたいとき。母集団が大きい場合は、完全な名簿の準備や広範囲の調査が負担になります。

### 系統抽出法
名簿が整っているとき。  
ただし周期性があるデータでは偏る可能性あり。

### 多段抽出法
全国調査など、大規模でコストを抑えたいとき。

### 集落抽出法
移動コストを抑えたいとき。  
ただし集団内の対象がよく似ていると、同じ人数の単純無作為抽出より標本誤差が大きくなる場合があります。

### 層別抽出法
各年代などの層を標本に含めて、推定精度や層ごとの結果を考えたいとき。比例配分を使うかどうかは目的と調査設計で決めます。


### 目的から選ぶ早見表

| 重視すること | 方法の例 | 確認すること |
|---|---|---|
| 全対象から基本的な無作為抽出 | 単純無作為 | 母集団の一覧を準備できるか |
| 名簿から一定間隔で選ぶ | 系統 | 並びに周期性がないか |
| 各属性の層を含める | 層別（層化） | 層ごとの人数配分と推定方法 |
| 移動・調査コストを抑える | 集落 | 集落内の類似性が精度に与える影響 |
| 全国など広範囲を段階的に選ぶ | 多段 | 各段階の抽出手続・確率 |

比率が似て見えることだけで、代表性や誤差の小ささは保証されません。母数の推定と記述の違いは[母分散・標本分散・不偏分散](/ds/population-sample-unbiased-variance/)、データの特徴の読み取りは[四分位](/ds/quartile/)も関連します。

## よくある誤解・混同

### 層別抽出法と集落抽出法の違い

DS検定ではここを混同させてきます。

| 方法 | 何をする？ |
|------|------------|
| 層別抽出 | 各グループから「一部」抽出 |
| 一段の集落抽出の基本例 | 選んだグループを「丸ごと」調査 |

選択肢で  
「グループを選び、その中の全員を調査」  
と書いてあれば → 集落抽出。

「各層から抽出」が層別抽出の判断の軸です。男女比を保つのは、その配分方法の一例です。


### 多段抽出と集落抽出の違い

- 多段抽出：複数段階で抽出する。
- 一段の集落抽出：選んだ集落の全対象を調べる。

集落を選んでからその内部でさらに抽出する設計もあり、「集落」と「多段」が常に相互に排他的というわけではありません。

グループの名前だけでなく、各段階で何を抽出したのかを確認します。

### 無作為抽出なら必ず母集団を正確に代表する

これは誤りです。無作為抽出でも、偶然による標本の偏りや無回答による偏りは起こります。

無作為抽出は偏りを自動的にゼロにする方法ではなく、**標本誤差を確率的に評価できる抽出設計**です。


## まとめ（試験直前用）

- 単純無作為抽出 → 各対象を同じ確率で選ぶ
- 系統抽出 → 一定間隔  
- 多段抽出 → 段階的に絞る  
- 集落抽出 → グループ丸ごと  
- 層別抽出 → 各層から抽出する

DS検定では  
「グループから一部か？全員か？」  
ここを切り分けられるかが勝負です。

## 公式情報・参考リンク

- 総務省統計局：[統計用語辞典「無作為抽出」](https://www.stat.go.jp/naruhodo/13_yougo/ma-gyo.html)
- 総務省統計局 Data StaRt：[標本抽出の諸方法](https://www.stat.go.jp/dstart/point/seminar/02/2-1-2.html)


- [Statistics Canada：Survey Methods and Practices](https://www150.statcan.gc.ca/n1/en/pub/12-587-x/12-587-x2003001-eng.pdf)
  - 7.1節の比例配分・非比例配分の例から、層化と人数配分を区別できます。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：解析技術
- **スキルカテゴリ**：データ準備
- **サブカテゴリ**：サンプリング
- **必須スキル**：◯
- ★ 標本誤差およびサンプリングバイアス、およびそれぞれの違いについて説明できる
- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)
