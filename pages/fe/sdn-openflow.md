---
layout: page
title: SDNとは？OpenFlow・NFV・SNMPとの違い【基本情報技術者試験】
description: SDNを「ネットワーク制御機能とデータ転送機能を分離し、コントローラで集中制御する考え方」として整理し、OpenFlow・NFV・SNMP・従来型ルーティングとの違いをFE科目A向けに解説します。
permalink: /fe/sdn-openflow/
tags: [fe, fe-technology, network, sdn, openflow]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 95
date: 2026-09-20
last_modified_at: 2026-09-20
---

## まず結論

SDN（Software-Defined Networking）は、**ネットワークの制御機能とデータ転送機能を論理的に分離し、ソフトウェアによる集中制御を可能にする考え方**です。

基本情報技術者試験では、次の関係を押さえると選択肢を切りやすくなります。

```text
制御する
→ SDNコントローラ

実際にパケットを転送する
→ スイッチなどのネットワーク機器

コントローラとスイッチをつなぐ代表的な仕組み
→ OpenFlow
```

特に、

> **制御プレーンとデータプレーンを分ける**

という説明があれば、SDNを疑います。

## 直感的な説明

従来のネットワーク機器では、各機器が

- 経路をどう決めるか
- どこへ転送するか

をそれぞれ判断します。

イメージすると、

```text
ルータA
→ 自分で判断して転送

ルータB
→ 自分で判断して転送

ルータC
→ 自分で判断して転送
```

です。

SDNでは、この「判断する役割」をネットワーク機器から分離し、コントローラ側へ集めます。

```text
       SDNコントローラ
       ↓ 制御
  ┌────┼────┐
スイッチA スイッチB スイッチC
  ↓転送    ↓転送    ↓転送
```

つまり、

> **考える場所と、実際に転送する場所を分ける**

と理解すると分かりやすいです。

## 定義・仕組み

### SDN

Open Networking Foundation（ONF）は、SDNを動的で管理しやすく、柔軟なネットワークを実現するアーキテクチャとして説明しています。

SDNでは、ネットワーク制御をソフトウェア側へ分離することで、ネットワーク全体をプログラム可能にします。

試験対策では、

```text
Control Plane
→ 経路や転送方針を決める

Data Plane
→ 実際にパケットを転送する
```

という切り分けが重要です。

### OpenFlow

OpenFlowは、**SDNの制御層と転送層の間で情報をやり取りするための標準的なインタフェース／プロトコル**です。

ONFでは、OpenFlowをSDNアーキテクチャにおける制御層と転送層の間の標準通信インタフェースとして説明しています。

```text
SDNコントローラ
↓ OpenFlow
OpenFlowスイッチ
```

コントローラは、スイッチに対して、

- フローテーブルを書き換える
- パケットの転送方法を指示する
- 状態を取得する

といった制御を行います。

OpenFlow Switch Specificationでも、コントローラとスイッチ間で転送テーブルの変更や統計情報の取得などを行うメッセージが定義されています。

### フロー

OpenFlowでは、パケットを「フロー」として扱い、条件に一致した通信へ処理を適用します。

例えば、

```text
送信元IP
宛先IP
TCP/UDPポート番号
など
↓
条件に一致
↓
指定ポートへ転送
破棄
コントローラへ通知
```

といった制御ができます。

FEでは細かなフィールド名を覚えるより、

> **コントローラがフロー単位で転送ルールを管理する**

くらいで十分です。

## 1次情報

SDNとOpenFlowは、Open Networking Foundation（ONF）の公式資料で確認できます。

- [Open Networking Foundation：SDN Definition](https://opennetworking.org/sdn-definition/)
- [Open Networking Foundation：OpenFlow](https://opennetworking.org/sdn-resources/openflow-2/)
- [Open Networking Foundation：OpenFlow Switch Specification](https://opennetworking.org/sdn-resources/openflow-switch-specification/)
- [Open Networking Foundation：OpenFlow Switch Specification Ver. 1.5.1](https://opennetworking.org/wp-content/uploads/2014/10/openflow-switch-v1.5.1.pdf)

ONFはOpenFlowについて、SDNの**control layer と forwarding layer の間の標準通信インタフェース**として説明しています。

NFVとの違いを確認する一次情報としては、ETSI（European Telecommunications Standards Institute）の公式資料が使えます。

- [ETSI：Network Functions Virtualisation (NFV)](https://www.etsi.org/technical-groups/nfv/)
- [ETSI：NFV White Paper](https://portal.etsi.org/nfv/nfv_white_paper2.pdf)

## 科目Aでどう出る？

科目Aでは、SDNそのものの説明を選ばせる問題や、SNMP・NFV・従来型ルーティングとの違いを問う問題が出ます。

### まずキーワードを見る

```text
制御機能と転送機能を分離
→ SDN

MIBから機器情報を取得
→ SNMP

ネットワーク機能を仮想化
→ NFV

各ルータが経路情報を交換して判断
→ 従来型ルーティング
```

### 選択肢を切る比較表

| 問題文の表現 | 判断 |
|---|---|
| 制御プレーンとデータプレーンを分離 | SDN |
| コントローラがスイッチを集中制御 | SDN |
| OpenFlowでコントローラとスイッチが通信 | SDN / OpenFlow |
| MIB情報を取得して監視・管理 | SNMP |
| ルータやファイアウォールなどの機能を仮想化 | NFV |
| 各機器が経路情報を交換して転送経路を決定 | 従来型ルーティング |

既存のSNMP記事では、ネットワーク機器の監視・管理を整理しています。

- [SNMPとは？ネットワーク機器を監視・管理するプロトコル](/fe/snmp/)

## SDNとNFVの違い

SDNとNFVは一緒に使われることがありますが、目的が違います。

### SDN

```text
何を分ける？
→ 制御機能と転送機能

目的
→ ネットワーク制御を柔軟にする
```

### NFV

```text
何を仮想化する？
→ ルータ、FW、ロードバランサなどのネットワーク機能

目的
→ 専用ハードウェアに依存せず
  ソフトウェアとして機能を実行する
```

つまり、

```text
SDN
→ 制御の仕方を変える

NFV
→ ネットワーク機能の実装方法を変える
```

と整理すると混同しにくくなります。

ETSIはNFVを、ネットワーク機能を仮想化し、汎用的なハードウェア／ソフトウェア基盤上で実行するための枠組みとして標準化しています。

## どんな場面で使う？

SDNでは、ネットワーク全体の制御をソフトウェアから変更しやすくなります。

例えば、

- 通信経路を動的に変更する
- 特定の通信だけ別経路へ流す
- 複数のスイッチへ一括してポリシーを適用する
- クラウド環境でネットワーク構成を柔軟に変更する

といった場面です。

従来は各機器を個別に設定していたものを、コントローラからまとめて制御できるのが大きな特徴です。

## よくある誤解・混同

### SDNはネットワーク監視の仕組み？

違います。

```text
機器の状態を監視・管理
→ SNMP

転送ルールを集中制御
→ SDN
```

MIBという言葉が出てきたら、SDNではなくSNMPを疑います。

### SDNとNFVは同じ？

違います。

```text
SDN
→ 制御と転送を分離

NFV
→ ネットワーク機能を仮想化
```

「仮想マシン上でルータやFW機能を動かす」という説明ならNFV寄りです。

### OpenFlow＝SDNそのもの？

完全に同じではありません。

SDNはネットワークアーキテクチャの考え方で、OpenFlowはその実現に使われる代表的な標準インタフェース／プロトコルです。

```text
SDN
→ 考え方・アーキテクチャ

OpenFlow
→ 制御層と転送層をつなぐ仕組み
```

### 各ルータが経路情報を交換するのがSDN？

それは従来型の分散ルーティングの考え方です。

```text
各機器が自律的に判断
→ 従来型ルーティング

コントローラが集中制御
→ SDN
```

### SDNコントローラが実際にパケットを全部転送する？

通常、実際のデータ転送はスイッチなどのデータプレーン側が担当します。

コントローラは、どのように転送するかというルールを決める側です。

## まとめ（試験直前用）

- SDNは、**制御機能とデータ転送機能を分離**する
- 制御は**SDNコントローラ**が担当する
- 実際の転送はスイッチなどの**データプレーン**が担当する
- OpenFlowは、コントローラとスイッチ間の代表的な標準インタフェース
- MIB・監視・管理 → **SNMP**
- ネットワーク機能の仮想化 → **NFV**
- 各機器が経路情報を交換して判断 → **従来型ルーティング**
- **SDN＝制御方法、NFV＝機能の仮想化**

```text
制御と転送を分離
→ SDN

コントローラ ⇔ スイッチ
→ OpenFlow

監視
→ SNMP

仮想化
→ NFV
```

{% include fe_article_footer.html %}
