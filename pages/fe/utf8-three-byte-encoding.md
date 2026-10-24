---
layout: page
title: UTF-8の3バイト符号化とは？6ビットずつ取り出す仕組み【基本情報技術者試験】
description: UTF-8の3バイト表現を商と余りで分解する仕組みを初心者向けに解説。64で割る意味、配列を逆順に埋める理由、科目Bのトレースを独自データとPythonで確認します。
permalink: /fe/utf8-three-byte-encoding/
tags: [fe, fe-technology, programming, pseudocode, trace]
fe_section: 科目B対策
fe_subsection: 疑似言語
fe_order: 63
date: 2026-10-25
last_modified_at: 2026-10-25
related_articles:
  - /fe/character-encoding/
  - /fe/decimal-to-binary-div-mod/
  - /fe/shift-operation/
---

## まず結論

UTF-8の**3バイト符号化**は、Unicodeの符号位置（文字に割り当てた番号）を、次の形で表します。

~~~text
1110xxxx 10xxxxxx 10xxxxxx
   4 bit    6 bit    6 bit
~~~

右端から**6ビットずつ**取り出すために使う数は、`2^6 = 64` です。

- `cp mod 64`：いまの下位6ビットを取り出す
- `cp div 64`：使った下位6ビットを取り除き、残りを次に処理する

科目Bでは**「余りを保存してから、商で変数を更新する」**と判断します。

## 直感的な説明

10進数の整数を下の桁から分けるとき、10で割った余りを使います。同じように、2進数を6ビットずつ区切るなら、`2^6` である64で割ります。

~~~text
元の符号位置
  ↓ 64で割った余り → 一番右の6ビット
残りの商
  ↓ 64で割った余り → 真ん中の6ビット
残りの商
  ↓                → 最初の4ビット
~~~

UTF-8の3バイトは左から並びますが、**値の取り出しは右側から**行います。

## 定義・仕組み

### UnicodeとUTF-8の役割

Unicodeは文字の符号位置を決める規格、UTF-8はその符号位置を実際のバイト列にする符号化方式です。

| 符号位置 | UTF-8の形 |
|---|---|
| U+0000〜U+007F | `0xxxxxxx`（1バイト） |
| U+0080〜U+07FF | `110xxxxx 10xxxxxx`（2バイト） |
| U+0800〜U+FFFF | `1110xxxx 10xxxxxx 10xxxxxx`（3バイト） |
| U+10000〜U+10FFFF | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`（4バイト） |

ただし、**U+D800〜U+DFFFはサロゲート領域で、UTF-8に直接符号化できません。**

このページでは3バイト形式を扱います。後ろの2バイトは先頭の`10`が固定され、各バイトの残り6ビットに情報が入ります。

### 例：「あ」（U+3042）を符号化

「あ」の符号位置は16進数で`3042`、10進数で**12354**です。3バイトの初期値を次のように用意します。

~~~text
utf8Bytes ← {224, 128, 128}
224 = 11100000₂ （先頭の 1110 を固定）
128 = 10000000₂ （先頭の 10 を固定）
128 = 10000000₂ （先頭の 10 を固定）
~~~

`cp = 12354`として、64で割った余りを**3バイト目から順に**加算します。

| 回 | 格納先 | 処理前cp | 64で割った余り | 加算後 | 次のcp（商） |
|---:|---|---:|---:|---:|---:|
| 1 | 3バイト目 | 12354 | 2 | 130 | 193 |
| 2 | 2バイト目 | 193 | 1 | 129 | 3 |
| 3 | 1バイト目 | 3 | 3 | 227 | 0 |

最終的に**`{227, 129, 130}`**、16進数で**`E3 81 82`**です。

最初のバイトは`1110xxxx`なので、符号位置として入れられるのは**4ビットだけ**です。有効な3バイト用の符号位置なら、最後に残る値は0〜15です。

### Pythonで確認する

~~~python
char = "あ"
print(ord(char))                    # 12354
print(list(char.encode("utf-8")))   # [227, 129, 130]
print(char.encode("utf-8").hex(" ")) # e3 81 82
~~~

`ord`は符号位置を、`encode("utf-8")`はUTF-8のバイト列を返します。

## 科目Aでどう出る？

| 問題文の手掛かり | 判断 |
|---|---|
| Unicode | 文字に符号位置を割り当てる規格 |
| UTF-8 | その番号を可変長のバイト列で表す |
| `10xxxxxx` | 固定の2ビット以外に6ビット入る |
| 下位6ビットを取り出す | `mod 64` |
| 次の6ビットへ移る | `div 64` |

**UTF-8の文字がすべて3バイトとは限らない**ことも大切です。

## 科目Bでどう使う？

### 配列を後ろから埋める疑似コード

入力は、3バイト形式に入る有効なUnicode符号位置とします。添字は1から始まります。

~~~text
encode3(整数型: codePoint)
    utf8Bytes ← {224, 128, 128}
    cp ← codePoint
    for (i を3から1まで1ずつ減らす)
        utf8Bytes[i] ← utf8Bytes[i] + (cp mod 64)
        cp ← cp div 64
    endfor
    return utf8Bytes
~~~

`i = 3`から始まるので、最初に**末尾に下位6ビットを保存**します。次のループでは商を使うため、より上位のビットを取り出せます。

### 1回ずつ動かして確かめる

以下は独自データです。文字を選んで「次の処理」を押すと、**どのバイトに余りが加算されたか**と**cpがいくつになったか**を確認できます。

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}?v=20261025-utf8-3">
<div class="fe-learning-demo fe-utf8-trace" data-fe-utf8-trace>
  <p class="fe-learning-demo__title">UTF-8：下位6ビットから3バイトに分配</p>
  <div class="fe-utf8-trace__choices" role="group" aria-label="符号化する文字">
    <button type="button" data-fe-utf8-point="12354" aria-pressed="true">あ（U+3042）</button>
    <button type="button" data-fe-utf8-point="28450" aria-pressed="false">漢（U+6F22）</button>
    <button type="button" data-fe-utf8-point="8364" aria-pressed="false">€（U+20AC）</button>
  </div>
  <p class="fe-utf8-trace__status" data-fe-utf8-status role="status" aria-live="polite">開始前：cp＝12354。右端の3バイト目から進めます。</p>
  <p class="fe-utf8-trace__step">処理：<strong data-fe-utf8-step>0 / 3</strong>　次のcp：<strong data-fe-utf8-cp>12354</strong></p>
  <div class="fe-utf8-trace__bytes" aria-label="生成中の3バイト">
    <div data-fe-utf8-cell="0"><span>1バイト目</span><strong data-fe-utf8-byte="0">E0</strong><small data-fe-utf8-binary="0">11100000</small></div>
    <div data-fe-utf8-cell="1"><span>2バイト目</span><strong data-fe-utf8-byte="1">80</strong><small data-fe-utf8-binary="1">10000000</small></div>
    <div data-fe-utf8-cell="2"><span>3バイト目</span><strong data-fe-utf8-byte="2">80</strong><small data-fe-utf8-binary="2">10000000</small></div>
  </div>
  <p class="fe-utf8-trace__calculation" data-fe-utf8-calculation>64で割った余りを右端から保存します。</p>
  <div class="fe-utf8-trace__controls" data-fe-utf8-controls hidden>
    <button type="button" data-fe-utf8-prev disabled>一つ戻る</button>
    <button type="button" data-fe-utf8-next>次の処理</button>
    <button type="button" data-fe-utf8-reset disabled>最初から</button>
  </div>
  <p class="fe-learning-demo__hint">JavaScriptが使えなくても、直前のトレース表で余りと商の更新を確認できます。</p>
</div>
<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}?v=20261025-utf8-3" defer></script>

### 選択肢を効率よく絞る

- `10xxxxxx` の`x`は6桁 → **`2^6 = 64`**
- 配列の末尾から処理 → **下位ビットから保存**
- `mod` → **余りを格納**
- `div` → **商でcpを更新**

実際のバイト値を全て計算しなくても、空欄の定数を判断できる場合があります。

## よくある誤解・混同

### 3バイトだから24ビットすべてが文字の情報？

違います。先頭の固定ビットを除くと、情報を入れる場所は**4＋6＋6＝16ビット**です。

### 64で割ると下位64ビットが得られる？

違います。64は`2^6`です。余りは0〜63で、**下位6ビット**を表します。

### 余りを保存する前に商で更新してもよい？

違います。先に商へ更新すると、最初に取り出すべき下位6ビットを失います。

### 先頭バイトにも6ビット入る？

違います。先頭は`1110xxxx`で、符号位置を入れられるのは4ビットです。

### サロゲート領域もUTF-8でそのまま符号化できる？

違います。U+D800〜U+DFFFはUTF-8では符号化できません。

## まとめ（試験直前用）

- 3バイト形式は **`1110xxxx 10xxxxxx 10xxxxxx`**
- **`mod 64`は下位6ビットを取得、`div 64`は次のビットへ進む**
- **3→2→1の順で配列を埋める**
- **余りを保存した後で商へ更新する**
- 最初のバイトは4ビット分だけ符号位置を格納する

関連記事：[文字コードの違い](/fe/character-encoding/)・[divとmodの使い分け](/fe/decimal-to-binary-div-mod/)・[シフト演算](/fe/shift-operation/)

一次情報：[IETF RFC 3629（UTF-8）](https://www.rfc-editor.org/rfc/rfc3629.html)（3節：ビット配置と符号化順序／4節：有効な符号列）

{% include fe_article_footer.html %}
