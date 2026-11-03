---
layout: page
title: 絶対パスと相対パスとは？カレントディレクトリと親ディレクトリのたどり方【基本情報技術者試験】
description: 絶対パスと相対パスを、ルートディレクトリ、カレントディレクトリ、親ディレクトリの考え方で整理し、. と .. を含むパスをFE試験で順番にたどる判断軸を解説します。
permalink: /fe/absolute-relative-path/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 52
date: 2026-07-05
last_modified_at: 2026-11-03
---

## まず結論

絶対パスとは、**ルートディレクトリから目的のファイルまでをすべて書いたパス**です。

相対パスとは、**今いる場所であるカレントディレクトリを基準にして、目的のファイルまでを表したパス**です。

基本情報技術者試験では、次のように切り分けると分かりやすいです。

```text
先頭が ¥
→ ルートディレクトリから始める絶対パス

先頭が . またはディレクトリ名
→ カレントディレクトリから始める相対パス

.
→ 今いるディレクトリ

..
→ 1階層上のディレクトリ
```

相対パスが出たら、**カレントディレクトリから左から順にたどる** のが基本です。

## 直感的な説明

パスは、ファイルの場所を表す住所のようなものです。

絶対パスは、住所を最初から全部書くイメージです。

```text
¥a¥a¥b¥c
```

一方、相対パスは、今いる場所から見てどこにあるかを書くイメージです。

```text
.¥..¥..¥a¥b¥file
```

ここで、`.` と `..` が大事です。

```text
.  → 今いる場所
.. → 1つ上の場所
```

英語では、次のように整理できます。

```text
absolute path：絶対パス
relative path：相対パス
current directory：カレントディレクトリ
parent directory：親ディレクトリ
root directory：ルートディレクトリ
```

特に `parent directory` は「親ディレクトリ」、つまり1階層上のディレクトリです。

## 定義・仕組み

パスに関する用語を整理すると、次のようになります。

| 用語 | 英語表記 | 意味 |
|---|---|---|
| 絶対パス | absolute path | ルートディレクトリから目的の場所までを表すパス |
| 相対パス | relative path | カレントディレクトリを基準にしたパス |
| カレントディレクトリ | current directory | 今いるディレクトリ |
| 親ディレクトリ | parent directory | 1階層上のディレクトリ |
| ルートディレクトリ | root directory | 階層構造の一番上のディレクトリ |

例えば、カレントディレクトリが次だとします。

```text
¥a¥a¥b¥c
```

ここで、相対パスが次のように与えられた場合を考えます。

```text
.¥..¥..¥a¥b¥file
```

これは、左から順番に処理します。

```text
開始地点：¥a¥a¥b¥c

.    → 今の場所のまま        → ¥a¥a¥b¥c
..   → 1階層上へ             → ¥a¥a¥b
..   → さらに1階層上へ       → ¥a¥a
a    → aディレクトリへ       → ¥a¥a¥a
b    → bディレクトリへ       → ¥a¥a¥a¥b
file → fileを指定            → ¥a¥a¥a¥b¥file
```

したがって、絶対パスは次のようになります。

```text
¥a¥a¥a¥b¥file
```

公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。絶対パスと相対パスは、OSやファイル管理の基本として出題されることがあります。

### 触って覚える：相対パスを左から1要素ずつたどる

**「今いるフォルダ」から `.` と `..` を処理したら、最終的にどこへ着くでしょうか？**

1. 相対パスの例を選び、次の要素がどのような移動を表すか予想します。
2. 「次へ」を押して1要素ずつ処理し、フォルダツリーと現在地を確認します。
3. 「1要素戻る」でやり直し、最後の絶対パスを確かめます。

**この教材の前提：** カレントディレクトリは `¥a¥a¥b¥c` です。フォルダ名が同じ `a` でも、階層が違えば別のフォルダです。教材では、この記事の例と同じフォルダ構造を使います。

<link rel="stylesheet" href="{{ '/assets/css/fe-relative-path.css' | relative_url }}">

<div class="fe-path-demo" id="fe-path-demo" aria-label="絶対パスと相対パスを順にたどる教材">
  <p class="fe-path-demo__step">① 相対パスを選ぶ</p>
  <div class="fe-path-demo__controls">
    <label for="fe-path-case">調べる相対パス
      <select id="fe-path-case">
        <option value="example">.¥..¥..¥a¥b¥file（記事の例）</option>
        <option value="parent">..¥..（2階層上へ）</option>
        <option value="same">.（今の場所のまま）</option>
      </select>
    </label>
  </div>
  <div class="fe-path-demo__tree" aria-label="教材のフォルダ構造。現在地は青で強調">
    <strong>フォルダツリー</strong>
    <ul>
      <li><span class="fe-path-demo__node" data-path-node="root">¥（ルート）</span>
        <ul><li><span class="fe-path-demo__node" data-path-node="a1">a</span>
          <ul><li><span class="fe-path-demo__node" data-path-node="a2">a</span>
            <ul>
              <li><span class="fe-path-demo__node" data-path-node="b1">b</span>
                <ul><li><span class="fe-path-demo__node" data-path-node="c">c（開始位置）</span></li></ul>
              </li>
              <li><span class="fe-path-demo__node" data-path-node="a3">a</span>
                <ul><li><span class="fe-path-demo__node" data-path-node="b2">b</span>
                  <ul><li><span class="fe-path-demo__node" data-path-node="file">file（ファイル）</span></li></ul>
                </li></ul>
              </li>
            </ul>
          </li></ul>
        </li></ul>
      </li>
    </ul>
    <p class="fe-path-demo__hint">青：現在地　薄青：通った場所。フォルダ名だけでなく階層を確認しましょう。</p>
  </div>
  <p class="fe-path-demo__step">② 次の要素の意味を予想する</p>
  <p>次に読む要素：<strong id="fe-path-upcoming">.</strong></p>
  <div class="fe-path-demo__controls">
    <label for="fe-path-guess">次の要素は何を意味する？
      <select id="fe-path-guess">
        <option value="">予想しなくても進められます</option>
        <option value="same">今の場所のまま</option>
        <option value="up">親ディレクトリへ戻る</option>
        <option value="down">子ディレクトリへ進む</option>
        <option value="file">ファイルを指定する</option>
      </select>
    </label>
  </div>
  <p class="fe-path-demo__step">③ 進めて現在地を確認する</p>
  <div class="fe-path-demo__actions">
    <button type="button" id="fe-path-next" class="fe-path-demo__primary">次へ（1要素進む）</button>
    <button type="button" id="fe-path-back">1要素戻る</button>
    <button type="button" id="fe-path-reset">最初から</button>
  </div>
  <div class="fe-path-demo__result">
    <p id="fe-path-progress">0 / 6 要素</p>
    <p>現在の絶対パス：<output id="fe-path-current">¥a¥a¥b¥c</output></p>
    <p>処理済みの要素：<span id="fe-path-history">まだ処理していません。</span></p>
    <p class="fe-path-demo__notice" id="fe-path-feedback" role="status" aria-live="polite">次の要素の意味を予想しましょう。</p>
    <p id="fe-path-reason">まずカレントディレクトリから始めます。各要素を左から一つずつ解釈します。</p>
  </div>
</div>
<noscript>
  <p>JavaScriptが無効でも、本文の例からたどれます。開始 ¥a¥a¥b¥c → 「.」で変化なし → 「..」で ¥a¥a¥b → 「..」で ¥a¥a → 「a」→「b」→「file」で ¥a¥a¥a¥b¥file になります。</p>
</noscript>
<script src="{{ '/assets/js/fe-relative-path.js' | relative_url }}" defer></script>

## 科目Aでどう出る？

科目Aでは、カレントディレクトリと相対パスが与えられ、対応する絶対パスを選ぶ問題が出やすいです。

選択肢を切るときは、次の順番で考えます。

```text
1. カレントディレクトリを開始地点にする
2. 相対パスを左から順に読む
3. . はそのまま
4. .. は1階層上へ戻る
5. ディレクトリ名やファイル名は順に進む
```

例えば、次のように、

```text
カレントディレクトリ：¥a¥a¥b¥c
相対パス：.¥..¥..¥a¥b¥file
```

であれば、まず `.` は現在地なので変わりません。

その後、`..` が2回あるので、2階層上へ戻ります。

```text
¥a¥a¥b¥c
→ ¥a¥a¥b
→ ¥a¥a
```

そこから `a¥b¥file` に進みます。

```text
¥a¥a
→ ¥a¥a¥a
→ ¥a¥a¥a¥b
→ ¥a¥a¥a¥b¥file
```

したがって、絶対パスは `¥a¥a¥a¥b¥file` になります。

## どんな場面で使う？


ファイル操作やプログラムの入出力を読むときに、パスの考え方は役立ちます。

例えば、次のような場面です。

- 設定ファイルを読み込む
- ログファイルを出力する
- カレントディレクトリを基準にファイルを指定する
- 親ディレクトリにあるファイルへ移動する

このとき、相対パスを絶対パスと同じ感覚で読むと間違えやすくなります。

```text
相対パスは、必ず今いる場所から見る
```

この感覚を持っておくと、ファイルの場所を追いやすくなります。

## よくある誤解・混同

一番多い誤解は、`.` と `..` を混同することです。

| 混同しやすい点 | 正しい理解 |
|---|---|
| `.` は1階層上へ戻る | `.` は今いる場所のまま |
| `..` は今いる場所を表す | `..` は1階層上へ戻る |
| 先頭が `¥` でないパスもルートから読む | 先頭が `¥` でないならカレントディレクトリ基準 |
| 相対パスは右から読む | 左から順番に処理する |

このような相対パスでは、`..` の回数を数えるだけでなく、戻った後にどのディレクトリへ進むかも見ます。

```text
.¥..¥..¥a¥b¥file
```

この場合、2階層戻ったあと、`a`、`b`、`file` の順に進みます。

```text
戻るだけでは終わらない
戻ったあとに進む部分も処理する
```

ここを忘れると、選択肢を間違えやすくなります。

## まとめ（試験直前用）

- 絶対パスは、ルートディレクトリから目的の場所までを表す
- 相対パスは、カレントディレクトリを基準に目的の場所を表す
- `.` は今いるディレクトリ、`..` は1階層上のディレクトリ
- 先頭が `¥` なら絶対パス、そうでなければ相対パスとして考える
- 相対パスは、カレントディレクトリから左から順にたどる

{% include fe_article_footer.html %}
