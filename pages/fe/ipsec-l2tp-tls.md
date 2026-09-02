---
layout: page
title: IPsec・L2TP・TLSの違いとは？OSI参照モデルでの位置を整理【基本情報技術者試験】
description: VPNで使われるIPsec・L2TP・TLSを、OSI参照モデル上の相対的な位置と役割で整理し、L2TPはLayer 2をトンネルする技術、IPsecはIP層を保護する技術、TLSはより上位で通信を保護する技術という判断軸をFE科目A向けに解説します。
permalink: /fe/ipsec-l2tp-tls/
tags: [fe, fe-technology, network, security]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 35
date: 2026-08-14
last_modified_at: 2026-09-02
---

## まず結論

IPsec・L2TP・TLSは、どれも安全な通信やVPNで関係する技術ですが、**働く位置と役割が違います**。

基本情報技術者試験で3つの相対的な位置関係を問われたら、まず次の順番で整理します。

```text
上位層

TLS
↓
IPsec
↓
L2TP

下位層
```

試験では、次の対応で判断すると選択肢を切りやすくなります。

```text
L2TP
→ Layer 2をトンネルする技術

IPsec
→ IP層を保護する技術

TLS
→ IPsecより上位で通信を保護する技術
```

つまり、**「TLS＝必ず第4層」のように層番号だけを固定暗記するより、3つの相対位置と役割で整理する**のが安全です。

## 直感的な説明

3つの技術は、通信の「どのあたりを守る・運ぶか」が違います。

FE試験向けには、次のイメージで十分です。

```text
アプリケーションに近い側
↓
TLS
↓
IPsec
↓
L2TP
↓
ネットワークの下位側
```

一言でまとめると、

```text
L2TP
→ Layer 2の通信をトンネルする

IPsec
→ IP通信を守る

TLS
→ より上位の通信を守る
```

というイメージです。

実際のプロトコルスタックは用途によって異なるため、**OSI参照モデルの層番号を厳密に当てはめることより、FEの比較問題では相対的な上下関係をつかむこと**を優先します。

## 定義・仕組み

### L2TP

L2TPは、Layer 2 Tunneling Protocolの略です。

名前にあるとおり、**Layer 2の通信をトンネルする技術**です。

主な役割は、通信データをカプセル化してトンネルを作ることです。

```text
Layer 2
＋
Tunneling
→ L2TP
```

重要なのは、**L2TP自体には暗号化機能がない**ことです。

そのため、安全なVPN通信ではIPsecと組み合わせて使われることがあります。

```text
L2TP
→ トンネルを作る

IPsec
→ 暗号化・認証する
```

### IPsec

IPsecは、IP Securityの略です。

**IP層でIP通信を保護する仕組み**です。

主な役割は次のとおりです。

- 暗号化
- 認証
- 改ざん検知

```text
IP
＋
Security
→ IPsec
```

FE試験では、

```text
IP
VPN
暗号化
認証
```

といった語が判断材料になります。

詳しくは、[IPsecとは？](/fe/ipsec/)も参照してください。

### TLS

TLSは、Transport Layer Securityの略です。

HTTPSなどで使われ、**IPsecより上位側で通信を保護する技術**として整理すると、FEの比較問題では判断しやすくなります。

主な役割は次のとおりです。

- 通信内容の暗号化
- 改ざん検知
- 通信相手の認証

```text
HTTPS
暗号化通信
証明書
→ TLS
```

TLSをOSI参照モデルのどの層に置くかは説明方法によって表現が異なるため、FE試験では**IPsecより上位**という相対関係を押さえるのがポイントです。

公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

### 一次情報で確認する

仕様そのものを確認したい場合は、IETFのRFCが一次情報です。

- [RFC 2661：Layer Two Tunneling Protocol "L2TP"](https://datatracker.ietf.org/doc/html/rfc2661)
- [RFC 4301：Security Architecture for the Internet Protocol](https://datatracker.ietf.org/doc/html/rfc4301)
- [RFC 8446：The Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/html/rfc8446)

FE対策ではRFCを細かく暗記する必要はありません。**記事の説明の根拠を確認したいときの参照先**として使えば十分です。

## 科目Aでどう出る？

科目Aでは、複数のセキュアプロトコルを**OSI参照モデル上の相対的な位置で並べる問題**が考えられます。

### まず名前と役割を見る

```text
L2TP
→ Layer 2をトンネル

IPsec
→ IPを保護

TLS
→ より上位の通信を保護
```

この対応が分かれば、上位から

```text
TLS
IPsec
L2TP
```

と並べられます。

### 判断表

| プロトコル | FEでの位置の目安 | 主な役割 |
|---|---|---|
| L2TP | 下位 | Layer 2のトンネリング |
| IPsec | 中間 | IP通信の暗号化・認証 |
| TLS | 上位 | HTTPSなどの暗号化通信 |

### 試験中の判断順

```text
1. Layer 2をトンネルする？
→ L2TP

2. IPを守る？
→ IPsec

3. それらより上位で通信を守る？
→ TLS
```

細かい仕様を全部覚えなくても、この3つの対応関係で選択肢をかなり切れます。

## どんな場面で使う？

### L2TP

L2TPは、VPNなどでトンネルを作るために使われます。

ただし、暗号化機能を持たないため、単独で安全なVPNを実現するというより、IPsecと組み合わせることがあります。

### IPsec

IPsecは、拠点間VPNやリモートアクセスVPNなどで、IP通信そのものを保護するときに使われます。

```text
拠点A
↓
暗号化されたIP通信
↓
拠点B
```

### TLS

TLSは、Web通信など、アプリケーションに近い位置で通信を保護します。

代表例はHTTPSです。

```text
HTTP
＋
TLS
→ HTTPS
```

3つとも「安全な通信」に関係しますが、同じ目的・同じ位置ではありません。

## よくある誤解・混同

### 全部VPNで使われるなら同じ層？

違います。

```text
VPNで関係する
≠
同じ位置で動く
```

FEでは、用途だけでなく**相対的な位置関係**も見ます。

### L2TPは暗号化する？

L2TPの主な役割はトンネリングです。

```text
トンネルを作る
→ L2TP

暗号化・認証
→ IPsec
```

L2TP/IPsecという名前で使われることがあるため、L2TP自体が暗号化すると思わないようにします。

### IPsecとTLSは同じ暗号化技術？

どちらも通信を保護しますが、働く位置が違います。

```text
IP通信そのものを守る
→ IPsec

HTTPSなど上位の通信を守る
→ TLS
```

### TLSは必ずOSI第4層？

**「TLS＝第4層」とだけ固定暗記するのは避けます。**

TLSは、OSI参照モデルへ厳密に1対1で対応させにくい技術です。

FEの層比較問題では、

```text
TLS
↓
IPsec
↓
L2TP
```

という**相対的な上下関係**を判断できれば十分です。

### L2TPは必ずOSI第2層で動く？

L2TPは**Layer 2の通信をトンネルするプロトコル**です。

名前の「Layer 2」は強い手掛かりですが、試験対策では「第2層とだけ暗記する」より、

```text
Layer 2をトンネル
→ L2TP
```

と役割までセットで覚えます。

### 名前を見ずに全部暗記する必要がある？

ありません。

```text
Layer 2
→ L2TP

IP
→ IPsec

より上位
→ TLS
```

という対応を使うと、かなり覚えやすくなります。

## 確認問題（基本情報技術者試験対策）

IPsec・L2TP・TLSを、OSI参照モデル上で上位層に近いものから並べた組合せとして、最も適切なものはどれか。

- ア. IPsec → L2TP → TLS
- イ. IPsec → TLS → L2TP
- ウ. TLS → IPsec → L2TP
- エ. TLS → L2TP → IPsec

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：ウ**

FE試験では、次のように整理します。

```text
L2TP
→ Layer 2をトンネル

IPsec
→ IPを保護

TLS
→ より上位で通信を保護
```

したがって、上位から

```text
TLS → IPsec → L2TP
```

の順になります。

</details>

## まとめ（試験直前用）

- L2TPは**Layer 2の通信をトンネルする**
- IPsecは**IP通信を保護する**
- TLSは**IPsecより上位で通信を保護する**
- 上位から並べると **TLS → IPsec → L2TP**
- L2TP自体には暗号化機能がない
- L2TPとIPsecは組み合わせて使われることがある
- **OSIの層番号だけでなく、相対位置と役割で判断する**

{% include fe_article_footer.html %}
