---
layout: page
title: SRAMとDRAMの違いとは？SDRAM・RDRAMも整理【基本情報技術者試験】
description: SRAMとDRAMの違いを、フリップフロップ・コンデンサ・リフレッシュ・用途で整理し、SDRAM・RDRAMとの関係までFE科目A向けに解説します。
permalink: /fe/sram-dram/
tags: [fe, fe-technology, memory, computer-architecture]
fe_section: テクノロジ系
fe_subsection: コンピュータ構成要素
fe_order: 230
date: 2026-08-14
last_modified_at: 2026-08-14
---

## まず結論

SRAMとDRAMの違いは、**1ビットをどう記憶するか**です。

```text
フリップフロップで記憶
→ SRAM

コンデンサの電荷で記憶
→ DRAM
```

基本情報技術者試験では、この違いから、

```text
SRAM
→ 高速
→ リフレッシュ不要
→ キャッシュメモリ

DRAM
→ 大容量
→ リフレッシュ必要
→ 主記憶
```

と切り分けられるようにしておくと強いです。

## 直感的な説明

SRAMは、電気回路の状態そのもので0と1を保持します。

イメージとしては、

```text
回路がこの状態
→ 0

回路が別の状態
→ 1
```

のように、状態を保ち続けることで記憶します。

一方、DRAMはコンデンサに電気をためて記憶します。

```text
電荷あり
→ 1

電荷なし
→ 0
```

というイメージです。

ただし、コンデンサの電荷は少しずつ失われるため、DRAMでは定期的に内容を書き直す必要があります。

これが **リフレッシュ** です。

## 定義・仕組み

### SRAM

SRAMは Static Random Access Memory の略です。

1ビットの記憶にフリップフロップ回路を使います。

特徴は、

- 高速
- リフレッシュ不要
- 回路規模が大きい
- 高価
- 大容量化しにくい

です。

そのため、CPUに近い高速メモリである**キャッシュメモリ**に使われます。

### DRAM

DRAMは Dynamic Random Access Memory の略です。

1ビットの記憶にコンデンサの電荷を使います。

特徴は、

- SRAMより低速
- リフレッシュが必要
- 回路が単純
- 安価
- 大容量化しやすい

です。

そのため、コンピュータの**主記憶**に使われます。

### なぜDRAMにはリフレッシュが必要？

コンデンサにためた電荷は、そのままでは少しずつ失われます。

そのため、

```text
電荷を保持
↓
時間がたつ
↓
電荷が減る
↓
再び書き直す
```

という処理が必要です。

この定期的な書き直しがリフレッシュです。

### SDRAM

SDRAMは Synchronous DRAM の略です。

ここでの **SはStaticではなくSynchronous** です。

SDRAMは、システムクロックに同期して動作するDRAMです。

```text
SDRAM
→ DRAMの一種
→ クロック同期で動作
```

と覚えます。

### RDRAM

RDRAMは Rambus DRAM の略です。

Rambus社が開発した高速なDRAM方式です。

試験では、

```text
RDRAM
→ DRAM系
```

と整理できれば十分です。

## 科目Aでどう出る？

科目Aでは、メモリの構造や特徴から用語を選ぶ問題が出ます。

### 判断表

| 問題文のキーワード | 判断 |
|---|---|
| フリップフロップ | SRAM |
| リフレッシュ不要 | SRAM |
| キャッシュメモリ | SRAM |
| コンデンサ | DRAM |
| リフレッシュ必要 | DRAM |
| 主記憶 | DRAM |
| クロック同期 | SDRAM |
| Rambus | RDRAM |

### 試験中の切り分け

```text
フリップフロップ？
→ SRAM

コンデンサ？
→ DRAM

クロック同期のDRAM？
→ SDRAM

Rambus方式？
→ RDRAM
```

## どんな場面で使う？

### SRAM

高速性が重要な場所で使われます。

代表例は、

```text
CPU
↓
キャッシュメモリ
↓
主記憶
```

のキャッシュ部分です。

CPUに近い場所ほど高速性が求められるため、SRAMが向いています。

### DRAM

大容量とコストが重要な場所で使われます。

代表例は主記憶です。

```text
大容量
＋
比較的安価
→ DRAM
```

という特徴が主記憶に向いています。

## よくある誤解・混同

### SDRAMのSはStatic？

違います。

```text
SRAM
→ Static RAM

SDRAM
→ Synchronous DRAM
```

です。

ここは非常に間違えやすいポイントです。

### SRAMは主記憶に使われる？

一般的には違います。

SRAMは高速ですが高価で大容量化しにくいため、

```text
キャッシュ
→ SRAM

主記憶
→ DRAM
```

という組合せで覚えます。

### DRAMはフリップフロップで記憶する？

違います。

```text
SRAM
→ フリップフロップ

DRAM
→ コンデンサ
```

です。

### リフレッシュが必要なのはSRAM？

違います。

リフレッシュが必要なのはDRAMです。

```text
SRAM
→ リフレッシュ不要

DRAM
→ リフレッシュ必要
```

### RDRAMとSDRAMはSRAMの仲間？

違います。

どちらもDRAM系です。

```text
DRAM
├ SDRAM
└ RDRAM
```

というイメージで整理すると分かりやすいです。

## 確認問題（基本情報技術者試験対策）

フリップフロップ回路を使って情報を保持し、リフレッシュ動作を必要としないメモリはどれか。

- ア. DRAM
- イ. RDRAM
- ウ. SDRAM
- エ. SRAM

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：エ**

SRAMは、フリップフロップ回路で1ビットの状態を保持します。

そのため、DRAMのような定期的なリフレッシュ動作は不要です。

- DRAM：コンデンサで記憶し、リフレッシュが必要
- RDRAM：DRAM系
- SDRAM：クロック同期で動作するDRAM
- SRAM：フリップフロップで記憶

</details>

## まとめ（試験直前用）

- SRAMはフリップフロップで記憶する
- DRAMはコンデンサで記憶する
- SRAMはリフレッシュ不要
- DRAMはリフレッシュ必要
- SRAMは高速・高価でキャッシュ向け
- DRAMは大容量・安価で主記憶向け
- SDRAMのSはStaticではなくSynchronous
- RDRAMとSDRAMはDRAM系
- **フリップフロップ → SRAM、コンデンサ → DRAM**

{% include fe_article_footer.html %}
