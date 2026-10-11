---
layout: page
title: GUI部品とは？ラジオボタンとチェックボックスの使い分け【基本情報技術者試験】
description: ラジオボタン・チェックボックス・コンボボックス・ドロップダウンリストの違いを操作例で整理し、単一選択・複数選択・自由入力の条件からFE科目Aの選択肢を見分けます。
permalink: /fe/gui-controls/
tags: [fe, fe-technology, human-interface, gui]
fe_section: テクノロジ系
fe_subsection: ヒューマンインタフェース
fe_order: 30
date: 2026-10-11
last_modified_at: 2026-10-11
---

## まず結論

**GUI部品**は、画面上で選択・入力・操作するための部品です。基本情報技術者試験では、**「一つだけ選ぶ」「複数選ぶ」「一覧から選ぶ」「文字を入力する」**の違いで判断します。

- **ラジオボタン**：同じグループから一つだけ選ぶ
- **チェックボックス**：項目ごとに独立してオン・オフする
- **ドロップダウンリスト**：一覧を開いて候補から選ぶ
- **コンボボックス**：入力欄と候補リストを組み合わせた部品

## 直感的な説明

通販サイトの注文画面を想像してみましょう。

- 配送方法を「通常・速達・店舗受取」から**一つ**選ぶ → ラジオボタン
- 「領収書を発行」「ギフト包装」を**それぞれ**指定する → チェックボックス
- 都道府県を**開いた一覧**から選ぶ → ドロップダウンリスト
- 商品名を入力しながら**候補からも選べる** → 入力可能なコンボボックス

### 実際に操作して違いを確認

次の部品を操作すると、選択方法の違いが分かります。JavaScriptを使わず、ブラウザ標準のHTML部品だけで試せます。

<div style="border:1px solid #cbd5e1;border-radius:12px;padding:16px;margin:16px 0;background:#f8fafc;">
  <fieldset style="border:1px solid #cbd5e1;border-radius:8px;padding:12px;margin:0 0 14px;">
    <legend><strong>① ラジオボタン：配送方法は一つだけ</strong></legend>
    <label style="display:block;margin:8px 0;"><input type="radio" name="fe-gui-delivery" checked> 通常配送</label>
    <label style="display:block;margin:8px 0;"><input type="radio" name="fe-gui-delivery"> 速達</label>
    <label style="display:block;margin:8px 0;"><input type="radio" name="fe-gui-delivery"> 店舗受取</label>
  </fieldset>
  <fieldset style="border:1px solid #cbd5e1;border-radius:8px;padding:12px;margin:0 0 14px;">
    <legend><strong>② チェックボックス：複数選択できる</strong></legend>
    <label style="display:block;margin:8px 0;"><input type="checkbox"> 領収書を発行</label>
    <label style="display:block;margin:8px 0;"><input type="checkbox"> ギフト包装</label>
  </fieldset>
  <div style="margin-bottom:14px;">
    <label for="fe-gui-pref"><strong>③ ドロップダウンリスト：一覧を開いて選ぶ</strong></label>
    <select id="fe-gui-pref" style="display:block;margin-top:8px;padding:8px;max-width:100%;"><option>都道府県を選ぶ</option><option>東京都</option><option>大阪府</option><option>愛媛県</option></select>
  </div>
  <div>
    <label for="fe-gui-item"><strong>④ 入力可能なコンボボックスの例：入力・候補選択</strong></label>
    <input id="fe-gui-item" list="fe-gui-items" placeholder="商品名を入力" style="display:block;margin-top:8px;padding:8px;max-width:100%;box-sizing:border-box;">
    <datalist id="fe-gui-items"><option value="ノート"><option value="ペン"><option value="消しゴム"></datalist>
    <small>※ HTMLのdatalistを使った簡易的な例です。候補の見え方はブラウザによって異なります。</small>
  </div>
</div>

**見るポイント：** ラジオボタンは別の項目を選ぶと前の選択が外れます。一方、チェックボックスは複数を同時に選べます。

## 定義・仕組み

| GUI部品 | 主な用途 | 判断の目印 |
|---|---|---|
| ラジオボタン | グループ内で一つを選択 | 排他的、単一選択 |
| チェックボックス | 各項目を個別に選択 | 複数選択、オン・オフ |
| ドロップダウンリスト | 開いた候補一覧から選択 | 一覧を開く、選択肢を省スペースで表示 |
| コンボボックス | テキスト欄と候補一覧を組み合わせる | 入力欄と選択リスト |
| テキストボックス | 文字や数値を入力 | 文字入力 |
| リストボックス | 候補を一覧表示して選択 | 一覧が表示される |

コンボボックスは実装によって自由入力を許さない場合もあります。試験では、**「入力欄と候補一覧を組み合わせる」**という構造を押さえましょう。

## 科目Aでどう出る？

### 具体例で判断する練習

次の画面には、どのGUI部品が適しているでしょうか。

| 場面 | 適した部品 | 理由 |
|---|---|---|
| A. アンケートで「はい・いいえ」のどちらか一方を選ぶ | ラジオボタン | 同時に二つは選べない |
| B. 希望する通知方法を「メール・SMS・アプリ」から複数選ぶ | チェックボックス | 複数の項目を指定できる |
| C. 国名の候補を必要なときだけ開いて選ぶ | ドロップダウンリスト | 一覧を普段は閉じておける |
| D. 部品番号を直接入力するか、候補から選ぶ | 入力可能なコンボボックス | 入力と候補選択を併用する |

**「選べる数」と「入力の有無」**に注目すれば、似た選択肢を切り分けられます。

## どんな場面で使う？

画面設計では、利用者にどのような操作をしてほしいかでGUI部品を選びます。

例えば「支払い方法を一つだけ指定してほしい」ならラジオボタンが適しています。一方「受け取りたい通知をすべて選んでほしい」ならチェックボックスが適しています。

候補数が多い場合は、ドロップダウンリストなどで画面の場所を節約することもできます。

## よくある誤解・混同

### ラジオボタンは複数選択できる？

**同じグループでは一つだけ**です。複数選択させたいならチェックボックスを検討します。

### ドロップダウンリストとコンボボックスは同じ？

どちらも候補一覧を扱いますが、コンボボックスは入力欄と候補リストを組み合わせた部品です。自由入力できるかどうかは実装によります。

### リストボックスとドロップダウンリストは同じ？

どちらも一覧から選択しますが、**リストボックスは一覧を表示しておく形式**、**ドロップダウンリストは必要に応じて一覧を開く形式**として区別できます。

## まとめ（試験直前用）

- **一つだけ・排他的** → ラジオボタン
- **複数・個別のオン／オフ** → チェックボックス
- **開いて候補を選ぶ** → ドロップダウンリスト
- **入力欄＋候補リスト** → コンボボックス
- GUI問題は、**選択数・一覧の表示方法・文字入力**の三点で切り分ける

{% include fe_article_footer.html %}
