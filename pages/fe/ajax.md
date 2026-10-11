---
layout: page
title: Ajaxとは？非同期通信でWeb画面を部分更新する仕組み【基本情報技術者試験】
description: Ajaxを「ブラウザとWebサーバの間で非同期通信し、ページ全体を再読み込みせずに必要な部分だけ更新する仕組み」として整理し、HTTP・SOAP・CSSとの違いをFE試験向けに解説します。
permalink: /fe/ajax/
tags: [fe, fe-technology, web, network]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 420
date: 2026-08-31
last_modified_at: 2026-10-11
---

## まず結論

Ajax（Asynchronous JavaScript and XML）は、**ブラウザとWebサーバの間で非同期通信を行い、ページ全体を再読み込みせずに必要な部分だけ更新する仕組み**です。

基本情報技術者試験では、次のキーワードが出たらAjaxを候補にします。

```text
非同期通信
＋
ページ全体を再読み込みしない
＋
必要な部分だけ更新
→ Ajax
```

特に重要なのは、**Ajax = XMLを使う技術**と覚えないことです。

名前にはXMLが入っていますが、現在はJSONなどの形式も広く使われます。

## 直感的な説明

通常のWebページでは、操作のたびにページ全体を読み込み直すことがあります。

```text
ボタンを押す
↓
サーバへ要求
↓
ページ全体を受信
↓
画面全体を再表示
```

Ajaxでは、必要なデータだけをサーバとやり取りし、画面の一部だけを更新できます。

```text
ボタンを押す
↓
必要なデータだけを非同期で要求
↓
必要なデータだけ受信
↓
画面の一部を更新
```

たとえば、検索欄へ文字を入力したときに候補が自動表示される処理をイメージすると分かりやすいです。

ページ全体を開き直さなくても、候補部分だけが変わります。

<style>
.ajax-compare { display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:1rem 0; }
.ajax-panel { border:1px solid #cbd5e1;border-radius:10px;padding:12px;min-width:0; }
.ajax-panel h3 {font-size:1rem;margin:0 0 10px;}
.ajax-screen {border:2px solid #94a3b8;border-radius:7px;padding:10px;background:#f8fafc;min-height:120px;}
.ajax-screen .ajax-head {font-weight:700;border-bottom:1px solid #cbd5e1;padding-bottom:5px;}
.ajax-screen .ajax-fixed {font-size:.85rem;margin:9px 0;}
.ajax-screen .ajax-result {background:#dbeafe;border-radius:5px;padding:9px;font-weight:600;min-height:44px;}
.ajax-panel button {margin-top:10px;padding:9px 12px;border:1px solid #64748b;border-radius:7px;background:#f1f5f9;color:#172033;cursor:pointer;width:100%;}
.ajax-panel button:focus-visible {outline:3px solid #2563eb;outline-offset:2px;}
.ajax-status {font-size:.85rem;min-height:3em;margin-top:8px;}
.ajax-updated {background:#dcfce7!important;}
.ajax-screen.ajax-full-refresh { animation:ajax-page-refresh .85s ease-in-out; }
.ajax-screen.ajax-full-refresh .ajax-head,.ajax-screen.ajax-full-refresh .ajax-fixed,.ajax-screen.ajax-full-refresh .ajax-result { animation:ajax-repaint .85s ease-in-out; }
.ajax-result.ajax-part-refresh { animation:ajax-result-refresh .85s ease-in-out; }
@keyframes ajax-page-refresh { 0%,40% {opacity:.25;background:#cbd5e1;} 100% {opacity:1;background:#f8fafc;} }
@keyframes ajax-repaint { 0%,40% {opacity:0;} 100% {opacity:1;} }
@keyframes ajax-result-refresh { 0% {opacity:.45;} 100% {opacity:1;} }
@media(prefers-reduced-motion:reduce){.ajax-screen.ajax-full-refresh,.ajax-screen.ajax-full-refresh .ajax-head,.ajax-screen.ajax-full-refresh .ajax-fixed,.ajax-screen.ajax-full-refresh .ajax-result,.ajax-result.ajax-part-refresh{animation:none;}}
@media(max-width:560px){.ajax-compare{grid-template-columns:1fr;}}
</style>

<div class="ajax-compare" id="ajax-compare-demo">
  <div class="ajax-panel">
    <h3>① ページ全体を再読み込みする例</h3>
    <div class="ajax-screen" id="ajax-full-screen" aria-label="ページ全体の更新例">
      <div class="ajax-head">商品検索</div>
      <div class="ajax-fixed">検索欄：りんご</div>
      <div class="ajax-result" id="ajax-full-result">検索結果：未取得</div>
    </div>
    <button type="button" id="ajax-full-button">全体を更新</button>
    <div class="ajax-status" id="ajax-full-status" aria-live="polite">画面全体を作り直すイメージです。</div>
  </div>
  <div class="ajax-panel">
    <h3>② Ajaxによる部分更新の例</h3>
    <div class="ajax-screen" aria-label="部分更新例">
      <div class="ajax-head">商品検索</div>
      <div class="ajax-fixed">検索欄：りんご</div>
      <div class="ajax-result" id="ajax-part-result">検索結果：未取得</div>
    </div>
    <button type="button" id="ajax-part-button">結果だけ更新</button>
    <div class="ajax-status" id="ajax-part-status" aria-live="polite">見出しと検索欄はそのままです。</div>
  </div>
</div>
<script>
(function () {
  var root = document.getElementById('ajax-compare-demo');
  if (!root) return;
  var fullCount = 0;
  var partCount = 0;
  var fullScreen = root.querySelector('#ajax-full-screen');
  var full = root.querySelector('#ajax-full-result');
  var part = root.querySelector('#ajax-part-result');
  root.querySelector('#ajax-full-button').addEventListener('click', function () {
    fullCount += 1;
    fullScreen.classList.remove('ajax-full-refresh');
    void fullScreen.offsetWidth;
    fullScreen.classList.add('ajax-full-refresh');
    full.textContent = '検索結果：りんご（' + fullCount + '回目）';
    full.classList.add('ajax-updated');
    root.querySelector('#ajax-full-status').textContent = '画面の見出し・検索欄・結果欄をまとめて再表示するイメージです。';
  });
  root.querySelector('#ajax-part-button').addEventListener('click', function () {
    partCount += 1;
    part.classList.remove('ajax-part-refresh');
    void part.offsetWidth;
    part.classList.add('ajax-part-refresh');
    part.textContent = '検索結果：りんご（' + partCount + '回目）';
    part.classList.add('ajax-updated');
    root.querySelector('#ajax-part-status').textContent = '結果欄だけ変化。見出し・検索欄は変わりません。';
  });
}());
</script>

**見るポイント：** ①は画面全体が一度薄くなって再表示され、②は結果欄だけが変化します。スマートフォンでは上下に並ぶ2つのボタンを順に押して比べてください。

※これは表示の違いを示す**疑似デモ**です。実際のサーバ通信やページ再読み込みは行っていません。AjaxではJavaScriptからHTTP要求を送信し、受け取ったデータで必要な箇所を更新します。

## 定義・仕組み

### Ajaxの基本的な流れ

Ajaxでは、JavaScriptなどを使ってブラウザからWebサーバへ非同期に要求を送り、戻ってきたデータを使って画面の一部を書き換えます。

```text
ブラウザ
  ↓ 非同期で要求
Webサーバ
  ↓ データを返す
ブラウザ
  ↓
必要な部分だけ更新
```

ここでいう**非同期**とは、サーバからの応答を待っている間も、ブラウザ側で別の処理を進められるという意味です。

### Ajaxは通信プロトコルではない

AjaxはHTTPのような通信プロトコルそのものではありません。

Ajaxは、既存のWeb技術を組み合わせて、**非同期にデータを取得し、画面を動的に更新する考え方・仕組み**です。

試験では、

```text
HTTP
→ ブラウザとWebサーバが通信するための基本的な仕組み

Ajax
→ その通信を非同期に使い、画面の一部を更新する
```

と分けて考えると迷いにくくなります。

### XMLでなくてもよい

Ajaxは「Asynchronous JavaScript and XML」の略です。

ただし、通信するデータはXMLに限定されません。

現在は、たとえばJSON形式のデータもよく利用されます。

したがって、FE試験では、

> XMLを使っているからAjax

ではなく、

> 非同期通信で、ページ全体を再読み込みせずに一部を更新している

という特徴で判断します。

## 科目Aでどう出る？

Ajaxは、Web関連の似た用語と一緒に選択肢へ出ることがあります。

| 選択肢の表現 | 判断 |
|---|---|
| ブラウザとWebサーバが非同期通信し、画面の一部を動的に更新する | **Ajax** |
| ブラウザからの要求に対してWebサーバが応答する通信方式 | HTTP |
| XMLを用いたメッセージ交換の仕組み | SOAP |
| Webページの見た目やレイアウトを指定する | CSS |

判断の中心は、

```text
非同期
＋
部分更新
→ Ajax
```

です。

## どんな場面で使う？

### 検索候補の自動表示

検索欄に文字を入力するたびに、候補だけが更新される場合です。

```text
文字入力
↓
候補データだけ取得
↓
候補部分だけ更新
```

### ボタン操作で一部だけ内容を変更する

「お気に入り」ボタンなどを押したときに、ページ全体を読み込み直さずボタン表示だけが変わる処理にも使われます。

### 定期的に情報を更新する

画面を開いたまま、サーバから新しい情報を取得して一部を更新するような用途でも使われます。

ただし、FE試験では具体的なJavaScriptの書き方まで覚えるよりも、**非同期通信と部分更新という役割**を押さえることを優先します。

## よくある誤解・混同

### AjaxとHTTP

```text
HTTP
→ Web通信の基本ルール

Ajax
→ HTTPなどを利用して非同期に通信し、画面を部分更新する仕組み
```

HTTPそのものがAjaxではありません。

### AjaxとSOAP

SOAPは、構造化されたメッセージを交換するための仕組みです。

試験では、

```text
XML形式のメッセージ交換
→ SOAP

非同期通信＋画面の部分更新
→ Ajax
```

と切り分けます。

「XML」という単語だけでAjaxを選ばないことがポイントです。

### AjaxとCSS

CSSはWebページの見た目を指定します。

```text
見た目・レイアウト
→ CSS

通信して内容を動的に変える
→ Ajax
```

役割がまったく異なります。

### 非同期 = 必ずAjaxではない

「非同期通信」という言葉だけでAjaxと決めるのも危険です。

Ajaxで重要なのは、**WebブラウザとWebサーバの通信を使って、ページ全体を再読み込みせずに画面を更新する**という文脈です。

## まとめ（試験直前用）

- **非同期通信＋画面の部分更新 → Ajax**
- **HTTP → Web通信の基本**
- **SOAP → メッセージ交換**
- **CSS → 見た目・レイアウト**
- Ajaxという名前にXMLが入っていても、**XMLは必須ではない**

試験中は、

> 「ページ全体を再読み込みせず、必要な部分だけ更新しているか？」

を確認すると、Ajaxの選択肢を見つけやすくなります。

- [IPA：試験要綱・シラバスについて](https://www.ipa.go.jp/shiken/syllabus/index.html)

{% include fe_article_footer.html %}
