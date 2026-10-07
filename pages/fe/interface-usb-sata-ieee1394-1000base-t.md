---
layout: page
title: USB・SATA・IEEE 1394・1000BASE-Tの違いとは？特徴語で切り分ける【基本情報技術者試験】
description: USB 3.0、SATA、IEEE 1394、1000BASE-Tを、SuperSpeed、ATAのシリアル化、FireWire、4対のツイストペアという特徴語から基本情報技術者試験向けに切り分けます。
permalink: /fe/interface-usb-sata-ieee1394-1000base-t/
tags: [fe, fe-technology, hardware, network]
fe_section: テクノロジ系
fe_subsection: ハードウェア
fe_order: 152
date: 2026-10-06
last_modified_at: 2026-10-07
---

## まず結論

USB、SATA、IEEE 1394、1000BASE-Tは、どれもデータをやり取りする技術ですが、**何を接続するか・どんな特徴語が出るか**で切り分けます。

基本情報技術者試験では、まず次の対応を押さえます。

| 特徴語 | 疑う規格 |
|---|---|
| SuperSpeed、5 Gbit/s | USB 3.0 |
| ATAをシリアル化 | SATA |
| FireWire | IEEE 1394 |
| 4対のツイストペア、1 Gbit/s | 1000BASE-T |

最も大切なのは、**「シリアル」という言葉だけでUSBを選ばないこと**です。USB、SATA、IEEE 1394はいずれもシリアル通信に関係します。

## 直感的な説明

4つを「何をつなぐ技術か」で見ると整理しやすくなります。

```text
PC ─ 周辺機器
   → USB

PC ─ HDD・SSDなど
   → SATA

PC ─ 音声・映像機器など（FireWire接続）
   → IEEE 1394

PC ─ LAN
   → 1000BASE-T
```

試験では細かな仕様を全部覚えるより、**その規格だけを強く示す特徴語**を拾います。

## 定義・仕組み

### USB 3.0

USBは、PCとさまざまな周辺機器を接続するために広く使われるシリアルインタフェースです。

USB 3.0では、USB 2.0のHigh-Speedより高速な**SuperSpeed**が導入され、5 Gbit/sの信号速度が規定されました。

```text
USB 2.0
→ High-Speed
→ 480 Mbit/s

USB 3.0
→ SuperSpeed
→ 5 Gbit/s
```

USBの仕様はUSB-IFの公式資料で確認できます。

- [USB-IF：USB 3.2 Specification](https://www.usb.org/document-library/usb-32-revision-10-june-12-2022)
- [USB-IF：USB 2.0 Specification](https://www.usb.org/document-library/usb-20-specification)

### SATA

**SATA（Serial ATA）**は、ATAをシリアル方式へ発展させたストレージ接続用のインタフェースです。

```text
ATA
↓ シリアル化
SATA
```

問題文に「ATA仕様をシリアル化」とあれば、USBではなくSATAを疑います。

### IEEE 1394

IEEE 1394は、高速なシリアルバス規格で、音声・映像など時間的な連続性が重要なデータを扱う**アイソクロナス転送**をサポートします。

```text
FireWire
↓
IEEE 1394
↓
音声・映像などの転送に利用
```

**アイソクロナス転送はUSBでも利用されるため、この語だけでIEEE 1394とは確定できません。** IEEE 1394の別名である**FireWire**や、問題文に示された他の特徴と組み合わせて判断します。

[Microsoft Learn：USBのアイソクロナス転送](https://learn.microsoft.com/en-us/windows-hardware/drivers/usbcon/transfer-data-to-isochronous-endpoints)でも、USBで音声・映像など時間に依存するデータを転送できることが説明されています。

### 1000BASE-T

1000BASE-Tは、ツイストペアケーブルを使うGigabit Ethernetの規格です。

```text
4対のツイストペア
＋
1 Gbit/s
↓
1000BASE-T
```

これはPCの周辺機器インタフェースではなく、**LANの通信規格**です。

## 科目Aでどう出る？

このタイプの問題では、最初に「何の種類の規格か」を見ます。

```text
周辺機器を接続
→ USB

ストレージ接続
→ SATA

FireWire
→ IEEE 1394

Ethernet・LAN
→ 1000BASE-T
```

次に固有の特徴語を確認します。

| 問題文の表現 | 判断 |
|---|---|
| SuperSpeed、5 Gbit/s | USB 3.0 |
| High-Speed、480 Mbit/s | USB 2.0 |
| ATAをシリアル化 | SATA |
| FireWire | IEEE 1394 |
| 4対、1 Gbit/s、Ethernet | 1000BASE-T |

「シリアルインタフェース」という共通点よりも、**SuperSpeed、ATA、FireWire、Ethernetといった特徴語を優先**すると切りやすくなります。

## どんな場面で使う？

USBは、キーボード、マウス、ストレージなど幅広い周辺機器の接続に使われます。

SATAは、主にコンピュータ内部でHDDやSSDなどのストレージを接続する規格として使われてきました。

IEEE 1394は、デジタルビデオ機器などで利用されたシリアルバス規格です。

1000BASE-Tは、LANで1 Gbit/sのEthernet通信を行うための規格です。

実際の利用状況は時代とともに変わりますが、FEでは**規格名と代表的な特徴の対応**を判断できることが重要です。

## よくある誤解・混同

### シリアルインタフェースならUSB？

違います。

```text
USB
SATA
IEEE 1394
↓
いずれもシリアル通信に関係する
```

そのため、「シリアル」だけでは決められません。

### USB 3.0は1 Gbit/s？

違います。

```text
1 Gbit/s
＋
4対のツイストペア
→ 1000BASE-T

SuperSpeed
＋
5 Gbit/s
→ USB 3.0
```

速度だけでなく、**何の規格か**も一緒に確認します。

### 音声・映像ならUSBではなく必ずIEEE 1394？

そうとは限りません。

USBでも音声・映像データを扱え、アイソクロナス転送にも対応します。**音声・映像やアイソクロナス転送は、IEEE 1394だけの特徴ではありません。**

FireWireという別名があればIEEE 1394と判断できます。それ以外では、接続方式や他の特徴も確認します。

### USB 3.xのコネクタは必ず青色？

色だけで規格を断定しない方が安全です。

USBの実機では青色のコネクタがUSB 3.xの目印として使われる例がありますが、試験では**SuperSpeedや転送速度など仕様上の特徴**を判断基準にします。

### USB 3.0と現在のUSB表記は同じ？

USBの名称・表記は後に整理されており、現在の製品表記と古い試験問題の「USB 3.0」がそのまま同じ呼び方とは限りません。

過去問では、問題が作られた時点の表記として**USB 3.0 = SuperSpeed 5 Gbit/s**を読み取り、現在の製品選びとは分けて考えます。

## まとめ（試験直前用）

- **SuperSpeed・5 Gbit/s → USB 3.0**
- **ATAをシリアル化 → SATA**
- **FireWire → IEEE 1394**
- **4対のツイストペア・1 Gbit/s → 1000BASE-T**
- アイソクロナス転送はUSBでも利用されるため、それだけでは規格を確定できない
- 「シリアル」だけではUSB・SATA・IEEE 1394を区別できない
- まず規格の種類を見て、その後に固有の特徴語で確定する
- USBコネクタの色ではなく、仕様上の特徴で判断する

試験直前は、次の対応を思い出してください。

```text
SuperSpeed → USB
ATA → SATA
FireWire → IEEE 1394
4対・1 Gbit/s → 1000BASE-T
```

{% include fe_article_footer.html %}
