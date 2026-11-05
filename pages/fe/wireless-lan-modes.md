---
layout: page
title: 無線LANの通信モードとは？インフラストラクチャ・アドホック・Wi-Fi Direct【基本情報技術者試験】
description: 無線LANのインフラストラクチャモード・アドホックモード・Wi-Fi Directを、アクセスポイントの有無と接続の仕組みで比較。3方式を切り替える教材で科目Aの判断を練習します。
permalink: /fe/wireless-lan-modes/
tags: [fe, fe-technology, network, wireless-lan]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 67
date: 2026-11-05
last_modified_at: 2026-11-05
related_articles:
  - /fe/ssid-bssid/
  - /fe/csma-ca/
  - /fe/wireless-lan-security/
---

## まず結論

無線LANの通信モードは、**どの機器を経由して通信するか**で区別します。

| 方式 | 通信の特徴 | 既設のアクセスポイントは必要？ |
|---|---|---|
| インフラストラクチャモード | 端末が無線LANアクセスポイント（AP）を介して通信する | 必要 |
| アドホックモード | 端末同士が直接通信する、従来のIEEE 802.11のIBSS方式 | 不要 |
| Wi-Fi Direct | 専用の無線LANルータを使わず機器同士を接続し、グループ内で役割を分担する | 不要 |

**Wi-Fi Directは単なる従来のアドホックモードの別名ではありません。** グループ内の端末が「Group Owner」というAPに似た役割を担う仕組みです。

## 直感的な説明

会社のWi-FiにPCやスマートフォンを接続するときは、通常、APを経由する**インフラストラクチャモード**です。

一方、昔ながらのアドホックモードでは、端末同士がAPなしで直接ネットワークを構成します。

Wi-Fi Directも既設APなしで機器同士を接続できますが、接続した機器のうち1台が**Group Owner**として接続を管理する点が従来のアドホックモードと異なります。プリンタとスマートフォンの直接接続などに使われます。

## 定義・仕組み

### インフラストラクチャモード

```text
PC ─────┐
        ├── 無線LANアクセスポイント ── ネットワーク
スマホ ──┘
```

端末はAPに接続します。同じ無線LANの端末間でも、通常APを介してデータをやり取りします。自宅や会社のWi-Fiでよく使う構成です。**SSIDは接続先ネットワークを識別する名前**です。詳細は[SSIDとBSSID](/fe/ssid-bssid/)で確認してください。

### アドホックモード

```text
端末A ←── 直接通信 ──→ 端末B
         （従来のIBSS）
```

従来のIEEE 802.11のアドホックモード（IBSS：Independent Basic Service Set）は、APを設置せず端末同士で無線ネットワークを構成する方式です。**既設APを使わない＝すべてWi-Fi Direct、ではありません。**

### Wi-Fi Direct

```text
スマホ（Group Owner）
        │
  Wi-Fi Directのグループ
        │
      プリンタ
```

Wi-Fi Directは、従来のAPを経由せず、対応機器同士を接続できる仕組みです。機器の1台が**Group Owner**となってグループを管理します。このため、従来のアドホック（IBSS）のように各端末が対等な立場で直接接続する構造とは異なります。

なお、Wi-Fi Directに対応していない端末も参加できるかなどは機器や接続設定によって異なります。

### 触って覚える：3方式の構成を切り替える

先に予想してください。**Wi-Fi Directは「既設APが不要」でも、グループを管理する機器は必要でしょうか？**

<link rel="stylesheet" href="{{ '/assets/css/fe-wireless-lan-modes.css' | relative_url }}">

<div id="fe-wireless-modes-demo" class="fe-wireless-modes-demo">
  <p><strong>① 通信モードを選ぶ</strong></p>
  <div class="fe-wireless-modes-demo__modes" role="group" aria-label="無線LANの通信モード">
    <button type="button" data-mode="infra" aria-pressed="true">インフラストラクチャ</button>
    <button type="button" data-mode="adhoc" aria-pressed="false">アドホック</button>
    <button type="button" data-mode="direct" aria-pressed="false">Wi-Fi Direct</button>
  </div>
  <p><strong>② 既設APなしで構成できますか？</strong></p>
  <fieldset class="fe-wireless-modes-demo__guess">
    <legend>予想（省略もできます）</legend>
    <label><input type="radio" name="fe-wireless-modes-guess" value="yes"> できる</label>
    <label><input type="radio" name="fe-wireless-modes-guess" value="no"> できない</label>
  </fieldset>
  <div class="fe-wireless-modes-demo__actions">
    <button type="button" data-reveal>構成と理由を見る</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <div data-result hidden class="fe-wireless-modes-demo__result">
    <p data-feedback role="status" aria-live="polite"></p>
    <div data-diagram class="fe-wireless-modes-demo__diagram" aria-label="選択した方式の接続構成"></div>
    <p data-explanation></p>
  </div>
  <p class="fe-wireless-modes-demo__note">機器と接続の関係を簡略化した概念図です。Wi-Fi DirectのGroup Ownerは機器内でAPに似た役割を担いますが、別途設置する無線LANルータではありません。</p>
</div>
<noscript><p>JavaScript無効時も本文の静的な構成図で比較できます。インフラストラクチャはAPを使用、アドホックはIBSSで直接接続、Wi-Fi DirectはGroup Ownerが接続を管理します。</p></noscript>
<script src="{{ '/assets/js/fe-wireless-lan-modes.js' | relative_url }}" defer></script>

### IEEE 802.11、Wi-Fi、SSID、CSMA/CAはそれぞれ別の概念

- **IEEE 802.11**：無線LANの通信技術に関する標準規格群。
- **Wi-Fi**：Wi-Fi Allianceによる相互接続性の認証・ブランド。802.11を使うすべての製品が自動的にWi-Fi認証済みというわけではありません。
- **SSID**：無線LANネットワークを識別する名称。複数のAPが同じSSIDを用いることもあります。
- **CSMA/CA**：無線LANで送信前に通信路を確認して衝突をできるだけ避ける媒体アクセス制御の考え方。衝突を完全にゼロにする保証ではありません。

CSMA/CAの送信前待機や再送については[CSMA/CAの記事](/fe/csma-ca/)で、暗号化などは[無線LANセキュリティ](/fe/wireless-lan-security/)で説明しています。

## 科目Aでどう出る？

| 出題文の手掛かり | 判断 |
|---|---|
| APを中心に複数端末を接続する | インフラストラクチャ |
| APなし、従来のIBSSで端末同士が通信 | アドホック |
| 対応機器同士で直接接続、Group Owner | Wi-Fi Direct |
| 無線LANのネットワーク名 | SSID |
| 無線LANで送信衝突を回避する | CSMA/CA |

### 確認問題

スマートフォンとプリンタを、既設の無線LANアクセスポイントを使わず接続する。接続した機器の一方がGroup Ownerとして接続を管理する方式はどれか。

- ア：インフラストラクチャモード
- イ：従来のアドホックモード（IBSS）
- ウ：Wi-Fi Direct

<details markdown="1">
<summary>正解と解説を見る（タップして開く）</summary>

**正解：ウ。** Wi-Fi Directは既設APなしで接続でき、Group Ownerがグループを管理します。APなしという条件だけではアドホックと区別できないため、**Group Owner**に注目します。

</details>

## どんな場面で使う？

会社や家庭でWi-Fiルータ／APに複数の端末をつなぐならインフラストラクチャが一般的です。アドホックは従来型の直接接続の説明として登場します。Wi-Fi Directは対応プリンタや映像機器などへの直接接続で利用されます。具体的な対応状況は製品仕様を確認します。

## よくある誤解・混同

### 「Wi-Fi Directはアドホックモードと同じ」？

異なります。**直接接続できる点は共通**しますが、Wi-Fi DirectはGroup Ownerを中心に接続を管理する方式です。

### 「SSIDが同じなら物理的に同じAP」？

違います。複数APが同じSSIDを持つ場合があります。AP側の識別にはBSSIDが関わります。

### 「CSMA/CAなら衝突は完全に起きない」？

違います。CSMA/CAは衝突を避ける仕組みであり、衝突が絶対に起きないことを保証しません。

## まとめ（試験直前用）

- **インフラストラクチャ**：既設APを介する。
- **アドホック（IBSS）**：APを使わず端末同士で直接通信。
- **Wi-Fi Direct**：既設APなしで接続でき、Group Ownerが接続管理。
- IEEE 802.11は標準規格群、Wi-Fiは認証・ブランド。
- SSIDはネットワークの識別、CSMA/CAは衝突回避。役割を混同しない。

{% include fe_article_footer.html %}
