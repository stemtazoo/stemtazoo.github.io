---
layout: page
title: "コンパイラ・リンカ・ローダ・デバッガの違い｜プログラム実行までの流れ【基本情報技術者試験】"
description: "コンパイラ・リンカ・ローダ・デバッガの違いを、ソースプログラムから実行までの流れで整理します。相互参照の解決、ロードモジュール、主記憶への読込みなどFE科目Aで迷いやすい役割を判断基準で解説します。"
permalink: /fe/compiler-linker-loader-debugger/
tags: [fe, fe-technology, software]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 50
date: 2026-10-06
last_modified_at: 2026-10-06
---

<style>
.program-flow{display:flex;align-items:stretch;gap:.45rem;margin:1.2rem 0;flex-wrap:wrap}
.program-step{flex:1 1 125px;border:1px solid #d8dee4;border-radius:10px;padding:.8rem;text-align:center;background:#f6f8fa}
.program-step strong,.program-step span{display:block}
.program-step span{margin-top:.35rem;font-size:.9em}
.program-arrow{display:flex;align-items:center;font-weight:700}
.role-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.7rem;margin:1rem 0}
.role-card{border:1px solid #d8dee4;border-radius:10px;padding:.85rem;background:#f6f8fa}
.role-card strong{display:block;margin-bottom:.35rem}
@media(max-width:600px){.program-flow{flex-direction:column}.program-arrow{justify-content:center;transform:rotate(90deg)}}
</style>

## まず結論

**リンカ（linker）**は、複数の目的モジュールやライブラリを結合し、**相互参照を解決してロードモジュールを作る**ソフトウェアです。

FE科目Aでは、リンカだけを単独で暗記するより、次の4つを役割で切り分けると解きやすくなります。

| 用語 | 判断キーワード |
|---|---|
| コンパイラ | ソースプログラムを翻訳 |
| **リンカ** | **結合・相互参照を解決** |
| ローダ | 主記憶へロード |
| デバッガ | 実行を追跡・デバッグ |

特に、**「複数の目的モジュール」「相互参照の解決」「一つのロードモジュール」**が出たらリンカを疑います。

## 直感的な説明

プログラムが実行されるまでを「翻訳 → 結合 → 読込み → 実行」と考えると分かりやすくなります。

<div class="program-flow" aria-label="プログラムが実行されるまでの流れ">
  <div class="program-step"><strong>ソース</strong><span>人が書いたプログラム</span></div>
  <div class="program-arrow">→</div>
  <div class="program-step"><strong>コンパイラ</strong><span>翻訳する</span></div>
  <div class="program-arrow">→</div>
  <div class="program-step"><strong>目的モジュール</strong><span>翻訳後</span></div>
  <div class="program-arrow">→</div>
  <div class="program-step"><strong>リンカ</strong><span>つなぐ</span></div>
  <div class="program-arrow">→</div>
  <div class="program-step"><strong>ロードモジュール</strong><span>実行可能な形へ</span></div>
  <div class="program-arrow">→</div>
  <div class="program-step"><strong>ローダ</strong><span>主記憶へ</span></div>
</div>

英語のイメージも役立ちます。

- **compile**：翻訳・まとめる
- **link**：つなぐ
- **load**：読み込む
- **debug**：不具合を調べる

とくに **link = つなぐ** を覚えておくと、リンカの役割を思い出しやすくなります。

## 定義・仕組み

プログラムは、ソースコードを書いただけでは、そのまま実行できるとは限りません。

コンパイラ方式では、まずコンパイラがソースプログラムを機械が扱える形式へ翻訳し、目的モジュール（オブジェクトモジュール）を作ります。

しかし、プログラムが複数のモジュールに分かれていたり、ライブラリ中の処理を利用したりする場合、それらの参照関係をまとめる必要があります。

そこで働くのが**リンカ**です。

    目的モジュールA ─┐
    目的モジュールB ─┼→ リンカ → ロードモジュール
    ライブラリ      ─┘
                       ↑
                 相互参照を解決

リンカは、別のモジュールにある関数やデータなどの参照を解決し、必要なモジュールを結び付けます。

その後、**ローダ**がロードモジュールを主記憶へ読み込み、実行できる状態にします。

## 科目Aでどう出る？

FEでは、それぞれのソフトウェアの役割を入れ替えた選択肢がよく迷いどころになります。

<div class="role-cards">
  <div class="role-card"><strong>コンパイラ</strong>ソースプログラムを翻訳する</div>
  <div class="role-card"><strong>リンカ</strong>目的モジュールなどを結合し、参照を解決する</div>
  <div class="role-card"><strong>ローダ</strong>ロードモジュールを主記憶へ読み込む</div>
  <div class="role-card"><strong>デバッガ</strong>プログラムを追跡し、不具合の原因を調べる</div>
</div>

問題文では、動詞を見るのがコツです。

| 問題文の表現 | 優先して考えるもの |
|---|---|
| 翻訳する | コンパイラ |
| 結合する・相互参照を解決する | **リンカ** |
| 主記憶に読み込む | ローダ |
| ステップ実行・実行結果を確認する | デバッガ |

「プログラムに関係するソフトウェア」という共通点だけで判断せず、**何をしているか**を読みます。

## どんな場面で使う？

複数のソースファイルから一つのプログラムを作る場合を考えてみます。

例えば、メイン処理から別のモジュールに定義された関数を呼び出している場合、翻訳しただけでは「その関数がどこにあるか」という参照関係を最終的に解決する必要があります。

その役割を担うのがリンカです。

流れを短くすると、次のようになります。

    ソース
      ↓ 翻訳
    目的モジュール
      ↓ 結合・参照解決
    ロードモジュール
      ↓ 主記憶へ読込み
    実行

試験では、この**処理の順番**から役割を判断できるようにしておくと応用しやすくなります。

## よくある誤解・混同

### リンカ＝コンパイラ？

違います。

- コンパイラ：**翻訳**
- リンカ：**結合・参照解決**

「ソースコードを翻訳する」とあれば、リンカではなくコンパイラです。

### リンカ＝ローダ？

違います。

- リンカ：ロードする前に、モジュールを**つなぐ**
- ローダ：できたロードモジュールを**主記憶へ読み込む**

**link → load** の順番で覚えると切り分けやすくなります。

### 「ロードモジュール」という言葉が出たらローダ？

ここはひっかけポイントです。

「ロードモジュールを**生成する**」ならリンカ、「ロードモジュールを主記憶へ**読み込む**」ならローダです。

名前だけでなく、**生成なのか読込みなのか**を確認します。

### デバッガはプログラムを作るソフトウェア？

主な役割は違います。

デバッガは、ブレークポイントやステップ実行などを使ってプログラムの動作を確認し、不具合の原因を調べるためのソフトウェアです。

## まとめ（試験直前用）

- **翻訳** → コンパイラ
- **結合・相互参照の解決** → リンカ
- **主記憶へ読込み** → ローダ
- **ステップ実行・不具合調査** → デバッガ
- 「ロードモジュールを生成」ならリンカ、「ロードモジュールを主記憶へ読み込む」ならローダ
- 流れは **翻訳 → 結合 → 読込み → 実行**

{% include fe_article_footer.html %}
