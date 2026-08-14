---
layout: page
title: IPsec・L2TP・TLSの違いとは？OSI参照モデルでの位置を整理【基本情報技術者試験】
description: VPNで使われるIPsec・L2TP・TLSを、OSI参照モデル上の位置と役割で整理し、L2TPは第2層、IPsecは第3層、TLSは第4層付近という判断軸と、L2TP/IPsecの組合せをFE科目A向けに解説します。
permalink: /fe/ipsec-l2tp-tls/
tags: [fe, fe-technology, network, security]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 35
date: 2026-08-14
last_modified_at: 2026-08-14
---

## まず結論

IPsec・L2TP・TLSは、どれも安全な通信やVPNで関係する技術ですが、**OSI参照モデル上の位置と役割が違います**。

基本情報技術者試験では、まず次の順番で整理すると判断しやすくなります。

```text
上位層

TLS
↓
IPsec
↓
L2TP

下位層
```

対応する層の目安は、次のとおりです。

```text
L2TP
→ 第2層（データリンク層）

IPsec
→ 第3層（ネットワーク層）

TLS
→ 第4層付近（トランスポート層付近）
```

特に、

```text
Layer 2
→ L2TP

IP
→ IPsec

Transport
→ TLS
```

と名前から結び付けると覚えやすくなります。

## 直感的な説明

3つの技術は、通信の「どの位置で働くか」が違います。

イメージすると、次のようになります。

```text
アプリケーション
↓
TLS
↓
TCP / UDP
↓
IPsec
↓
IP
↓
L2TP
↓
データリンク
```

実際のプロトコル構成は用途によって異なりますが、FE試験ではまず**相対的な上下関係**をつかむことが大切です。

一言でまとめると、

```text
L2TP
→ 下の方でトンネルを作る

IPsec
→ IP通信を守る

TLS
→ より上位で通信を暗号化する
```

というイメージです。

## 定義・仕組み

### L2TP

L2TPは、Layer 2 Tunneling Protocolの略です。

名前にあるとおり、**Layer 2（第2層）**に関係するトンネリング技術です。

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

IP通信をネットワーク層で保護します。

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
ネットワーク層
IPパケット
VPN
暗号化
認証
```

といった語が判断材料になります。

詳しくは、[IPsecとは？](/fe/ipsec/)も参照してください。

### TLS

TLSは、Transport Layer Securityの略です。

名前に「Transport Layer」とあるため、FE試験では**トランスポート層付近で通信を保護する技術**として整理すると判断しやすくなります。

TLSは、HTTPSなどで使われます。

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

公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

## 科目Aでどう出る？

科目Aでは、複数のセキュアプロトコルを**OSI参照モデルの層で並べる問題**が考えられます。

### まず名前を見る

```text
L2TP
→ Layer 2
→ 第2層

IPsec
→ IP
→ 第3層

TLS
→ Transport Layer
→ 第4層付近
```

この対応が分かれば、上位から

```text
TLS
IPsec
L2TP
```

と並べられます。

### 判断表

| プロトコル | 層の目安 | 主な役割 |
|---|---|---|
| L2TP | 第2層 | トンネリング |
| IPsec | 第3層 | IP通信の暗号化・認証 |
| TLS | 第4層付近 | HTTPSなどの暗号化通信 |

### 試験中の判断順

```text
1. 名前にLayer 2がある？
→ L2TP

2. IPを守る？
→ IPsec

3. Transport Layer Security？
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

3つとも「安全な通信」に関係しますが、同じ目的・同じ層ではありません。

## よくある誤解・混同

### 全部VPNで使われるなら同じ層？

違います。

```text
VPNで関係する
≠
同じ層で動く
```

FEでは、用途だけでなく**OSI参照モデル上の位置**を見ます。

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

### TLSはアプリケーション層？

実務上の説明ではTLSをアプリケーション層とトランスポート層の間に位置付けることもあります。

ただし、FEの層比較問題では、**L2TPより上、IPsecより上**にある技術として整理できれば十分です。

```text
TLS
↓
IPsec
↓
L2TP
```

### 名前を見ずに全部暗記する必要がある？

ありません。

```text
L2
→ L2TP

IP
→ IPsec

Transport
→ TLS
```

という名前との対応を使うと、かなり覚えやすくなります。

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
TLS
→ 第4層付近

IPsec
→ 第3層

L2TP
→ 第2層
```

したがって、上位層から

```text
TLS → IPsec → L2TP
```

の順になります。

</details>

## まとめ（試験直前用）

- L2TPはLayer 2のトンネリング技術
- IPsecはIP通信をネットワーク層で保護する
- TLSはトランスポート層付近で通信を保護する
- 上位から並べると **TLS → IPsec → L2TP**
- L2TP自体には暗号化機能がない
- L2TPとIPsecは組み合わせて使われることがある
- **「L2」「IP」「Transport」という名前から層を判断する**

{% include fe_article_footer.html %}
