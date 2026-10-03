---
layout: page
title: 文字コード表の読み方｜上位4ビット・下位4ビットとJISコード【基本情報技術者試験】
description: JISコード表などの文字コード表を、列＝上位4ビット、行＝下位4ビットとして読む方法を解説します。2進数・16進数との対応と、FE試験で選択肢を切る判断基準も整理します。
permalink: /fe/character-code-table/
tags: [fe, fe-technology, basic-theory]
fe_section: テクノロジ系
fe_subsection: 基礎理論
fe_order: 36
date: 2026-10-03
last_modified_at: 2026-10-03
---

<style>
.code-rule {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: .6rem;
  align-items: center;
  max-width: 620px;
  margin: 1rem auto;
}
.code-half {
  padding: 1rem .7rem;
  border: 1px solid #c9d2d8;
  border-radius: 10px;
  text-align: center;
  background: #f7f9fa;
}
.code-half strong {
  display: block;
  font-size: 1.25rem;
  letter-spacing: .12em;
  margin-top: .3rem;
}
.code-plus {
  font-weight: bold;
}
.code-example {
  max-width: 620px;
  margin: 1rem auto;
  border: 1px solid #d7dde1;
  border-radius: 10px;
  overflow: hidden;
}
.code-row {
  display: grid;
  grid-template-columns: 4rem 1fr 1fr 1.2fr;
  text-align: center;
}
.code-row > div {
  padding: .65rem .35rem;
  border-bottom: 1px solid #e4e8eb;
}
.code-row:last-child > div {
  border-bottom: 0;
}
.code-row.head {
  font-weight: bold;
  background: #f3f5f6;
}
@media (max-width: 520px) {
  .code-rule { gap: .3rem; }
  .code-half { padding: .8rem .35rem; font-size: .9rem; }
  .code-half strong { font-size: 1.05rem; }
  .code-row { grid-template-columns: 3rem 1fr 1fr 1.15fr; font-size: .88rem; }
}
</style>

## まず結論

文字コード表を読む問題では、まず**表の見出しに示されたビットの対応**を確認します。

**列番号＝上位4ビット、行番号＝下位4ビット**

今回のJISコード表では、文字があるマスを見つけたら、**列の4ビットを先、行の4ビットを後**につなぎます。表によって配置の示し方は異なるため、列・行を暗記するのではなく、上位・下位の表示を確認するのが安全です。

<div class="code-rule">
  <div class="code-half">列＝上位4ビット<strong>0100</strong></div>
  <div class="code-plus">＋</div>
  <div class="code-half">行＝下位4ビット<strong>0001</strong></div>
</div>

たとえば、列4・行1にある文字なら、

```text
0100 + 0001 = 01000001
```

です。

試験では文字コードそのものを丸暗記するより、**表のどこを前半・後半にするか**を判断できることが重要です。

## 直感的な説明

8ビットを、4ビットずつ二つの箱に分けるイメージです。

```text
8ビット
┌────────┬────────┐
│ 上位4bit │ 下位4bit │
│   列     │   行     │
└────────┴────────┘
```

たとえば「A」が列4・行1にあるなら、

```text
列4 → 0100
行1 → 0001

A → 0100 0001
```

となります。

ここで大切なのは、**表を「行→列」の順に読まないこと**です。見た目では行と列を探しますが、ビット列にするときは問題の表が示す **上位→下位** の順です。

## 定義・仕組み

### 1. 上位4ビットと下位4ビット

8ビットのデータは、次のように分けて考えられます。

```text
b8 b7 b6 b5 | b4 b3 b2 b1
───────────┼───────────
 上位4bit  | 下位4bit
```

今回のようなコード表では、

- 上位4ビット：列番号
- 下位4ビット：行番号

に対応します。

### 2. 4ビットは16進数1桁に対応する

4ビットで表せる値は0～15です。これは16進数1桁とちょうど対応します。

| 2進数 | 16進数 |
|---|---|
| 0001 | 1 |
| 0010 | 2 |
| 0011 | 3 |
| 0100 | 4 |

そのため、

```text
0100 0001
  4    1

→ 0x41
```

のように、8ビットを4ビットずつ区切ると16進数でも読みやすくなります。

### 3. 表から文字を読む

たとえば、表で次の位置に文字があるとします。

<div class="code-example">
  <div class="code-row head"><div>文字</div><div>列</div><div>行</div><div>8ビット</div></div>
  <div class="code-row"><div>A</div><div>4<br>0100</div><div>1<br>0001</div><div>01000001</div></div>
  <div class="code-row"><div>2</div><div>3<br>0011</div><div>2<br>0010</div><div>00110010</div></div>
</div>

「A」「2」の順に並べるなら、

```text
A  → 01000001
2  → 00110010

01000001 00110010
```

となります。

## 科目Aでどう出る？

このタイプの問題では、次の順番で処理すると迷いにくくなります。

1. 指定された文字を表から探す
2. その文字の列番号を確認する
3. 列番号を上位4ビットにする
4. 行番号を下位4ビットにする
5. 「列＋行」の順につなぐ
6. 複数文字なら、問題文に書かれた文字順につなぐ

特に最後の「文字順」はひっかけになりやすいポイントです。

```text
A → 01000001
2 → 00110010
```

が分かっていても、

```text
00110010 01000001
```

とすると「2A」になってしまいます。

## どんな場面で使う？

コンピュータ内部では、文字も最終的には数値として扱われます。

文字コードは、文字と数値を対応付けるルールです。FEでは、文字コードの名称だけでなく、**表からビット列を読み取れるか**を問われることがあります。

現在はUnicodeが広く使われていますが、試験ではJISコードやASCIIなど、文字コードの基本的な考え方を理解するための問題も出題対象になります。

## よくある混同

### 「列」と「行」の順番を逆にする

今回の表では、

**列＝上位4ビット → 行＝下位4ビット**

です。

「行・列」という日本語の語順につられて、行を先にしないようにします。

### 文字そのものの順番を逆にする

各文字のコードが正しくても、並べる順番を逆にすると別の文字列になります。

問題文が「Aと2をこの順に」と指定していれば、

```text
Aのコード → 2のコード
```

です。

### 2進数を全部暗記しようとする

文字コードをすべて2進数で覚える必要はありません。

**表の位置 → 列と行 → 4ビットずつ結合**

という手順で求められます。

## まとめ

- 文字コード表では、まず列と行がどのビットに対応するか確認する
- 今回の形式では **列＝上位4ビット、行＝下位4ビット**
- 8ビットは「上位4bit＋下位4bit」と考える
- 4ビットは16進数1桁と対応する
- 複数文字では、最後に**文字の並び順**も確認する

試験中は、まず表の **「上位」「下位」** の表示を確認し、今回の形式なら **「列を前、行を後」** と置いてから選択肢を見ると、入れ替えのひっかけを切りやすくなります。
