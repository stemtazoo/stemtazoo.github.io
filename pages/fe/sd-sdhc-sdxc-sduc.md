---
layout: page
title: SD・SDHC・SDXC・SDUCの違いとは？容量とファイルシステムで見分ける【基本情報技術者試験】
description: SD・SDHC・SDXC・SDUCを、容量上限とFAT16・FAT32・exFATの違いから整理します。microSDとの違い、SDIOとの混同も含めてFE科目A向けに解説します。
permalink: /fe/sd-sdhc-sdxc-sduc/
tags: [fe, fe-technology, computer-system, storage, sd-card]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 52
date: 2026-09-27
last_modified_at: 2026-09-27
---

## まず結論

SDメモリカードの規格は、**容量の範囲と標準ファイルシステム**で切り分けると分かりやすくなります。

| 規格 | 容量 | 標準ファイルシステム |
|---|---:|---|
| SD | 最大2GB | FAT12 / FAT16 |
| SDHC | 2GB超～32GB | FAT32 |
| SDXC | 32GB超～2TB | exFAT |
| SDUC | 2TB超～128TB | exFAT |

基本情報技術者試験では、特に次の対応を押さえます。

~~~text
HC
→ High Capacity
→ 32GBまで
→ FAT32

XC
→ eXtended Capacity
→ 2TBまで
→ exFAT

UC
→ Ultra Capacity
→ 128TBまで
→ exFAT
~~~

> **SDXCなら「32GB超～2TB・exFAT」をまず思い出す。**

## 直感的な説明

SDカードは、同じ形に見えても容量規格が異なります。

イメージとしては、

~~~text
SD
↓ 容量を拡張
SDHC
↓ さらに拡張
SDXC
↓ さらに拡張
SDUC
~~~

です。

ここで大切なのは、

> **SD / SDHC / SDXC / SDUCは「容量規格」**

だということです。

一方、

~~~text
SD
microSD
~~~

は主に**カードの外形サイズ**の違いです。

したがって、

~~~text
microSDXC
microSDUC
~~~

のような組合せもあります。

「microだからSDHC」という意味ではありません。

## 定義・仕組み

### SD

SDは、初期の容量規格です。

~~~text
容量
→ 最大2GB

ファイルシステム
→ FAT12 / FAT16
~~~

と整理します。

### SDHC

SDHCは **SD High Capacity** の略です。

~~~text
容量
→ 2GB超～32GB

ファイルシステム
→ FAT32
~~~

です。

試験では、

> **HC → High Capacity → 32GBまで**

とつなげます。

### SDXC

SDXCは **SD eXtended Capacity** の略です。

~~~text
容量
→ 32GB超～2TB

ファイルシステム
→ exFAT
~~~

です。

SDXCの問題では、

> **exFAT・最大2TB**

が強い判断材料になります。

### SDUC

SDUCは **SD Ultra Capacity** の略です。

~~~text
容量
→ 2TB超～128TB

ファイルシステム
→ exFAT
~~~

です。

古い過去問ではSDUCが登場しない場合がありますが、現在のSD規格を整理するときはSDUCまで含めて覚えておくと混乱しにくくなります。

### 公式規格で確認する

SD Associationでは、現在の容量規格を次の4区分として整理しています。

~~~text
SD
SDHC
SDXC
SDUC
~~~

容量範囲とファイルシステムも公式に対応付けられています。

- [SD Association：容量（SD/SDHC/SDXC/SDUC）](https://www.sdcard.org/ja/developers-2/sd-standard-overview/capacity-sd-sdhc-sdxc-sduc/)

## 科目Aでどう出る？

科目Aでは、SDXCなどの特徴を選ばせる問題として出ます。

### 「exFAT・2TB」ならSDXC

~~~text
exFAT
＋
最大2TB
↓
SDXC
~~~

と判断できます。

### 「FAT32・32GB」ならSDHC

~~~text
FAT32
＋
最大32GB
↓
SDHC
~~~

です。

### 「小型サイズ」は容量規格ではない

「SDカードより小さい」という説明は、microSDなどの**外形サイズ**の話です。

~~~text
カードの大きさ
→ SD / microSD

容量規格
→ SD / SDHC / SDXC / SDUC
~~~

と分けます。

### 「GPS・無線LANなどをカード化」はSDIO

GPSや無線LANなどの入出力機能をSDカード形状で実現する仕組みは、SDIO（SD Input/Output）です。

これはSDXCの容量規格とは別です。

~~~text
容量を表す
→ SDXC

入出力機能を追加する
→ SDIO
~~~

### 著作権保護技術だけでSDXCとは決めない

SDカードには著作権保護に関する仕組みもありますが、SDXCを見分ける最優先の判断軸は、

~~~text
容量
＋
ファイルシステム
~~~

です。

問題文に

~~~text
exFAT
2TB
~~~

があれば、まずSDXCを疑います。

## どんな場面で使う？

### デジタルカメラや動画撮影

写真や動画では大容量の記憶媒体が必要になるため、SDXCなどの大容量規格が使われます。

ただし、カードを選ぶときは容量だけでなく、機器側がその規格に対応しているか確認する必要があります。

~~~text
SDHC対応機器
→ SDHCまで

SDXC対応機器
→ SDXCまで

SDUC対応機器
→ SDUCまで
~~~

というように、ホスト機器側の対応規格が重要です。

### フラッシュメモリとの関係

SDカードの記憶媒体にはフラッシュメモリが使われます。

~~~text
フラッシュメモリ
→ 記憶素子の種類

SD / SDHC / SDXC / SDUC
→ SDカードの容量規格
~~~

つまり、分類の軸が違います。

フラッシュメモリそのものの特徴は、[フラッシュメモリとは？](/fe/flash-memory/)で整理しています。

## よくある誤解・混同

### SDXCはカードサイズの名前

違います。

SDXCは容量規格です。

~~~text
SDXC
→ 容量規格

microSD
→ 外形サイズ
~~~

そのため、microSDXCというカードがあります。

### microSDHCとSDHCは容量が違う

基本となる容量規格は同じです。

~~~text
SDHC
microSDHC
↓
どちらもHC規格
↓
2GB超～32GB
~~~

違うのは主に外形サイズです。

### SDXCなら必ず2TBある

違います。

SDXCは、

~~~text
32GB超～2TB
~~~

という**容量範囲の規格**です。

「最大2TBまで対応できる」という意味で、すべてのSDXCカードが2TBという意味ではありません。

### exFATなら必ずSDXC

SDUCでもexFATを使用します。

~~~text
SDXC
→ exFAT

SDUC
→ exFAT
~~~

したがって、exFATだけでなく容量範囲も合わせて判断します。

### SDHCは32GBを超える

SDHCの上限は32GBです。

~~~text
32GBまで
→ SDHC

32GB超
→ SDXC
~~~

と境界を確認します。

## まとめ（試験直前用）

- SD：最大2GB、FAT12 / FAT16
- SDHC：2GB超～32GB、FAT32
- SDXC：32GB超～2TB、exFAT
- SDUC：2TB超～128TB、exFAT
- **HC → 32GBまで・FAT32**
- **XC → 2TBまで・exFAT**
- **UC → 128TBまで・exFAT**
- SD / SDHC / SDXC / SDUCは容量規格
- SD / microSDは主に外形サイズの違い
- GPS・無線LANなどの入出力機能はSDIOと切り分ける

~~~text
～2GB
→ SD

～32GB
→ SDHC

～2TB
→ SDXC

～128TB
→ SDUC
~~~

> **容量とファイルシステムを見る。SDXCなら「2TB・exFAT」。**

{% include fe_article_footer.html %}
