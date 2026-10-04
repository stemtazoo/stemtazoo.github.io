---
layout: page
title: arp・ipconfig・netstat・pingの違い｜ネットワーク確認コマンドの見分け方【基本情報技術者試験】
description: arp、ipconfig、netstat、pingの違いを「何を知りたいか」で整理します。IPアドレスからMACアドレスを調べるARPを中心に、FE試験で選択肢を切る判断基準を解説します。
permalink: /fe/network-diagnostic-commands/
tags: [fe, fe-technology, network]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 6
date: 2026-10-05
last_modified_at: 2026-10-05
---

## まず結論

`arp`・`ipconfig`・`netstat`・`ping`は、**「何を知りたいか」**で切り分けると迷いにくくなります。

| 知りたいこと | コマンド |
|---|---|
| IPアドレスとMACアドレスの対応 | `arp` |
| 自分のIP設定 | `ipconfig` |
| 現在の通信・接続状況 | `netstat` |
| 相手と通信できるか | `ping` |

> **MACなら arp、自分の設定なら ipconfig、接続状況なら netstat、疎通なら ping。**

---

## 直感的な説明

たとえば、同じLANにあるプリンタのIPアドレスが分かっていて、対応するMACアドレスを知りたいとします。

<div class="net-command-flow">
  <div><strong>IPアドレス</strong><span>192.168.1.20</span></div>
  <b>↓ arp</b>
  <div><strong>MACアドレス</strong><span>00-11-22-33-44-55</span></div>
</div>

この場合に見るのは、**IPアドレスとMACアドレスの対応関係**です。したがって `arp` が候補になります。

問題文に「プリンタ」「PC」と書かれていても、機器名から選ぶのではありません。

> **問題文で何を調べたいのかを先に探す。**

これが科目Aでの基本的な判断方法です。

---

## 定義・仕組み

### arp｜IPアドレスとMACアドレスの対応

ARP（Address Resolution Protocol）は、同一LAN内で、IPアドレスに対応するMACアドレスを解決するための仕組みです。

PCは一度得た対応関係をARPキャッシュ（ARPテーブル）に一時的に保持します。そのため、直前に通信した相手であれば、その対応が残っていることがあります。

```text
IPアドレス
ネットワーク層
     ↓ ARP
MACアドレス
データリンク層
```

試験では、**「IPは分かる。MACを知りたい」→ ARP** と判断できれば十分です。

※「直前に通信した」からといって、必ずARPキャッシュに残っていると断定する必要はありません。試験では、対応情報を確認する手掛かりとして捉えます。

### ipconfig｜自分のネットワーク設定

`ipconfig` は、Windowsで自端末のTCP/IP設定を確認するときに使います。

代表的には、IPアドレス、サブネットマスク、デフォルトゲートウェイなどを確認します。

```text
自分のIPアドレスは？
自分のデフォルトゲートウェイは？
→ ipconfig
```

### netstat｜現在の通信・接続状況

`netstat` は、ネットワーク接続や待受け状態などを確認するためのコマンドです。

試験では細かなオプションより、

```text
今、どんな通信・接続がある？
→ netstat
```

と役割を押さえるのが先です。

### ping｜相手まで通信できるか

`ping` は、IPネットワーク上で対象との疎通を確認するときに使います。

```text
サーバまで届く？
プリンタと通信できる？
→ ping
```

ただし、**pingはMACアドレスを調べるためのコマンドではありません。**

---

## 科目Aでどう出る？

4つをコマンド名だけで覚えると、`arp` と `ping` などで迷いやすくなります。

<div class="net-command-grid">
  <div><strong>MAC</strong><span>arp</span></div>
  <div><strong>自分の設定</strong><span>ipconfig</span></div>
  <div><strong>接続状況</strong><span>netstat</span></div>
  <div><strong>疎通</strong><span>ping</span></div>
</div>

問題文では、まず目的語を探します。

```text
MACアドレスを知りたい
→ arp

IP設定を確認したい
→ ipconfig

接続状況を確認したい
→ netstat

通信できるか確認したい
→ ping
```

---

## どんな場面で使う？

ネットワーク障害を調べる場合も、目的によって使うコマンドが変わります。

たとえば「PCのIP設定がおかしいかもしれない」なら `ipconfig`、「相手まで届くか」を確認するなら `ping`、「IPとMACの対応を確認したい」なら `arp` というように使い分けます。

重要なのは、**ネットワークを調べるコマンドという共通点ではなく、それぞれ何を見るコマンドなのか**です。

---

## よくある混同

### 「相手の機器を調べる」なら ping？

違います。

`ping` が確認する中心は**疎通**です。相手のMACアドレスを確認したいなら、目的が異なります。

```text
つながる？ → ping
IPとMACの対応は？ → arp
```

### arpとipconfigの違い

どちらもIPアドレスが関係しますが、見る対象が違います。

- `arp`：**IPアドレスとMACアドレスの対応**
- `ipconfig`：**自分自身のIP設定**

### IPアドレスとMACアドレスを同じものとして考える

IPアドレスとMACアドレスは役割が異なります。

OSI基本参照モデルとの位置付けを整理したい場合は、[OSI基本参照モデル](/fe/osi-reference-model/)も確認してください。

---

## まとめ

- **IP ↔ MACの対応**を確認するなら `arp`
- **自分のIP設定**を確認するなら `ipconfig`
- **通信・接続状況**を確認するなら `netstat`
- **疎通確認**なら `ping`
- 試験ではコマンド名より、**「何を知りたいのか」から選ぶ**

> **MAC → arp / 設定 → ipconfig / 接続 → netstat / 疎通 → ping**

この4つの対応が思い出せれば、似た選択肢をかなり切りやすくなります。

{% include fe_article_footer.html %}

<style>
.net-command-flow{max-width:520px;margin:1.4rem auto;text-align:center}.net-command-flow div{border:1px solid #bbb;border-radius:10px;padding:.75rem 1rem;background:#fafafa}.net-command-flow div strong,.net-command-flow div span{display:block}.net-command-flow b{display:block;padding:.45rem}.net-command-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.7rem;margin:1.4rem 0}.net-command-grid div{border:1px solid #ccc;border-radius:10px;padding:.8rem;text-align:center;background:#fafafa}.net-command-grid strong,.net-command-grid span{display:block}.net-command-grid span{margin-top:.3rem;font-weight:700}@media(max-width:520px){.net-command-grid{grid-template-columns:1fr}}
</style>
