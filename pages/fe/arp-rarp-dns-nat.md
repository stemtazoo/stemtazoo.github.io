---
layout: page
title: ARPとRARPの違いとは？DNS・NATとの見分け方も整理【基本情報技術者試験】
description: ARP・RARP・DNS・NATの違いを、何から何へ変換するのかという視点で整理します。基本情報技術者試験で選択肢を切る判断基準を初心者向けに解説します。
permalink: /fe/arp-rarp-dns-nat/
tags: [fe, fe-technology, network]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 36
date: 2026-09-18
last_modified_at: 2026-09-18
---

## まず結論

ARP・RARP・DNS・NATは、**何から何へ変換するのか**で切り分けると覚えやすくなります。

- **ARP**：IPアドレス → MACアドレス
- **RARP**：MACアドレス → IPアドレス
- **DNS**：ホスト名・ドメイン名 → IPアドレス
- **NAT**：IPアドレス → 別のIPアドレス

試験では、変換元と変換先を見ればかなり選択肢を切れます。

## 直感的な説明

ネットワークでは、同じ「住所」のように見えても、役割の違う情報を使います。

- IPアドレス：ネットワーク上の場所を示す
- MACアドレス：同一ネットワーク内で機器を識別する
- ホスト名・ドメイン名：人が覚えやすい名前

そのため、場面によって「名前からIPへ」「IPからMACへ」といった変換が必要になります。

## 定義・仕組み

### ARP

ARP（Address Resolution Protocol）は、**IPアドレスからMACアドレスを調べる**ための仕組みです。

```text
IPアドレス
↓
ARP
↓
MACアドレス
```

同一ネットワーク内で、宛先機器へフレームを届けるために使われます。

### RARP

RARP（Reverse Address Resolution Protocol）は、その名のとおりARPの逆方向で、**MACアドレスからIPアドレスを求める**仕組みです。

```text
MACアドレス
↓
RARP
↓
IPアドレス
```

試験では、**Reverse＝逆**と考えると判断しやすくなります。

### DNS

DNS（Domain Name System）は、**ホスト名やドメイン名からIPアドレスを求める**仕組みです。

```text
example.com
↓
DNS
↓
IPアドレス
```

### NAT

NAT（Network Address Translation）は、**IPアドレスを別のIPアドレスに変換する**仕組みです。

代表例は、プライベートIPアドレスとグローバルIPアドレスの変換です。

## どんな場面で使う？

ARPはLAN内で宛先MACアドレスを知りたいとき、DNSは名前から通信先IPアドレスを知りたいとき、NATは内部ネットワークとインターネットの間でIPアドレスを変換するときに使います。

RARPは古い仕組みですが、基本情報技術者試験ではARPとの対応関係を問う形で出題されることがあります。

## よくある誤解・混同

一番混同しやすいのはARPとRARPです。

```text
ARP
IP → MAC

RARP
MAC → IP
```

また、DNSもIPアドレスを求めるため混同しやすいですが、出発点が違います。

```text
名前 → IP
= DNS

MAC → IP
= RARP
```

NATは「何かからIPを調べる」のではなく、**IPアドレスそのものを別のIPアドレスへ変換する**点が違います。

## 科目Aでどう出る？

次のように、機能説明から用語を選ばせる問題が典型です。

- IPアドレスからMACアドレスを求める → ARP
- MACアドレスからIPアドレスを求める → RARP
- ドメイン名からIPアドレスを求める → DNS
- プライベートIPとグローバルIPを変換する → NAT

## まとめ

試験直前は、次の4行で十分です。

```text
IP → MAC
= ARP

MAC → IP
= RARP

名前 → IP
= DNS

IP → 別のIP
= NAT
```

**「何から何へ変換するのか」**を見るのが、最も確実な判断基準です。
