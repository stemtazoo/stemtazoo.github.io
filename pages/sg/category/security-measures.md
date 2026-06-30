---
layout: page
title: 情報セキュリティ対策まとめ
description: "認証、アクセス制御、マルウェア対策、ネットワーク対策、物理的対策を目的別に整理するまとめページです。侵入防止、検知、被害拡大防止、情報漏えい防止のどれに当たるかを比較して、対策選択の判断軸を学べます。"
permalink: /sg/category/security-measures/
---

[SGトップへ戻る](/sg/)

## SG試験での見方

- 用語の定義だけでなく、役割で判断する
- 似た用語との違いを押さえる
- 実務上の目的とセットで理解する

## まず読むまとめ記事

- [認証・アクセス制御まとめ｜主要用語を整理](/sg/auth-access-control-summary/)
  - 認証・認可・アクセス制御を学習順で読む入口です。
- [認証・アクセス制御まとめ｜SSO・MFA・ゼロトラストを体系整理](/sg/auth-access-summary/)
  - 短時間で全体像を復習する補助的なまとめです。
- [技術的セキュリティ対策まとめ](/sg/security-measures-overview/)
- [物理的セキュリティ対策まとめ](/sg/physical-security-summary/)
- [セキュリティ対策の違いまとめ](/sg/security-measures-comparison/)
- [脆弱性対策まとめ](/sg/vulnerability-cheatsheet/)
- [Webアプリ攻撃まとめ｜SQLインジェクション・XSS・CSRFを整理](/sg/web-application-attacks-summary/)
- [DNS・メールなりすまし対策まとめ｜SPF・DKIM・S/MIMEを整理](/sg/dns-mail-security-summary/)
- [ネットワーク防御と通信保護まとめ｜主要用語を整理【SG試験】](/sg/network-defense-summary/)
- [マルウェアまとめ｜種類・感染後の動き・解析方法を整理](/sg/malware-threats-summary/)
- [暗号と認証の基本まとめ｜秘密にする・確認するを整理【SG試験】](/sg/crypto-auth-summary/)
- [改ざん検知・電子署名・証明書まとめ｜完全性と真正性で整理【SG試験】](/sg/crypto-certificate-integrity-summary/)
- [暗号・証明書・認証基盤まとめ｜証明書運用まで整理【SG試験】](/sg/crypto-auth-platform-summary/)

## 分野別に読む

### 認証・アクセス制御

試験では、「本人確認」なのか「操作権限の制御」なのかで切り分けます。

- [認証・認可・アクセス制御の違いとは？役割の切り分けを整理](/sg/authentication-authorization-access-control/)
- [ID管理（アカウント管理）とは？運用の基本を整理](/sg/id-management/)
- [認証方式とは？3要素と多要素認証を整理](/sg/authentication-methods/)
- [パスワード管理とは？強度とロックアウトの考え方を整理](/sg/password-management/)
- [HDDパスワードとは？BIOSパスワード・OSログインとの違い](/sg/hdd-password/)
- [パスワードのハッシュ保存とは？認証時の比較方法を整理](/sg/password-hash-authentication/)
- [多要素認証（MFA）とは？認証強化の仕組みと判断ポイント](/sg/multi-factor-authentication/)
- [多要素認証と多段階認証の違いとは？混同しやすい認証方式を整理](/sg/mfa-vs-step-auth/)
- [リスクベース認証とは？状況に応じて強化する認証の仕組み](/sg/risk-based-authentication/)
- [チャレンジレスポンス認証とは？パスワードを送らない認証の仕組み](/sg/challenge-response-authentication/)
- [シングルサインオン（SSO）とは？利便性とリスクを整理](/sg/sso/)
- [IdP（認証サーバ）とは？SSOの中核とリスクを整理](/sg/idp/)
- [トークン認証とは？SAML・OAuth・OIDCの違いを整理](/sg/token-authentication/)
- [アクセス制御（認可）とは？認証との違いを整理](/sg/authorization/)
- [アクセス管理とは？特権IDとneed-to-knowで権限を適切に制御](/sg/access-control/)
- [アクセス制御モデルとは？RBAC・ABAC・DAC・MACの違いを整理](/sg/access-control-model/)
- [最小権限の原則とは？権限管理の基本を理解](/sg/least-privilege/)
- [特権ID管理とは？管理者権限のリスクと対策を整理](/sg/privileged-id/)
- [ゼロトラストとは？境界防御との違いを整理](/sg/zero-trust/)
- 関連： [識別符号とは？ID・パスワードとの関係を整理](/sg/identification-code/) / [本人拒否率と他人受入率とは？生体認証の重要指標を整理](/sg/frr-far/) / [境界防御とは？ゼロトラストとの違いを整理](/sg/perimeter-security/)

### パスワード・ログイン攻撃

試験では、「1つのIDを狙う攻撃」か「多くのIDに同じパスワードを試す攻撃」かで切り分けます。

- [ブルートフォース攻撃とは？総当たり攻撃の仕組みと対策](/sg/brute-force-attack/)
- [リバースブルートフォース攻撃とは？逆総当たりの仕組みと対策](/sg/reverse-brute-force-attack/)
- [辞書攻撃とは？効率的なパスワード破解の仕組み](/sg/dictionary-attack/)
- [パスワードリスト攻撃とは？使い回しを狙う不正ログイン](/sg/password-list-attack/)
- [パスワード管理とは？強度とロックアウトの考え方を整理](/sg/password-management/)
- [パスワードのハッシュ保存とは？認証時の比較方法を整理](/sg/password-hash-authentication/)
- [レインボーテーブルとは？パスワード解析の仕組みを理解](/sg/rainbow-table/)
- [ソルトとは？パスワードハッシュ強化の仕組み](/sg/salt/)
- [CAPTCHAとは？ボット対策の仕組みをやさしく理解](/sg/captcha/)

### ネットワーク対策

試験では、「通信を遮断する対策」か「検知・監視する対策」かで切り分けます。

- [ファイアーウォールとは？通信を制御する基本対策](/sg/firewall/)
- [パケットフィルタリングとは？通信を制御する基本技術](/sg/packet-filtering/)
- [IPSとは？不正侵入を検知して遮断する仕組み](/sg/ips/)
- [WAFとは？Webアプリを守る仕組みを理解する](/sg/waf/)
- [DMZとは？外部公開サーバを安全に配置する仕組み](/sg/dmz/)
- [VPNとは？安全な通信を実現する仕組み](/sg/vpn/)
- [セキュアプロトコルとは？代表例と使い分けを整理](/sg/secure-protocol/)
- [SSHとは？安全な遠隔操作の仕組み](/sg/ssh/)
- [Telnetとは？安全でない遠隔操作の仕組み](/sg/telnet/)
- [SSL/TLSとは？通信を守る暗号化の仕組み](/sg/ssl-tls/)
- [EDoS攻撃とは？クラウド従量課金を狙う経済的DoS攻撃](/sg/edos-attack/)
- [HTTPとHTTPSの違いとは？安全な通信の判断ポイント](/sg/http-https/)
- [HTTPステータスコードとは？404 Not Foundの見分け方](/sg/http-status-code/)
- [ポート番号とは？通信先サービスの識別を理解する](/sg/port-number/)
- [SMTPのポート番号とは？パケットフィルタリングでの見方を整理](/sg/smtp-port-packet-filtering/)

### DNS・メール対策

試験では、「名前解決の悪用」か「送信元のなりすまし対策」かで切り分けます。

- [DNSとは？名前解決の仕組みとセキュリティのポイント](/sg/dns/)
- [DNSゾーン転送とは？許可先を制限する理由をやさしく解説](/sg/dns-zone-transfer/)
- [DNSキャッシュポイズニングとは？偽サイトへ誘導する攻撃](/sg/dns-cache-poisoning/)
- [DNSリフレクター攻撃とは？仕組みと対策の考え方](/sg/dns-reflector-attack/)
- [ドメイン名ハイジャックとは？DNSを悪用したなりすましの仕組み](/sg/domain-hijacking/)
- [SPFとは？送信元IPでなりすましを防ぐ仕組み](/sg/spf/)
- [SPF・DKIMとは？なりすましメール対策の仕組み](/sg/spf-dkim/)
- [SMTP-AUTHとは？メール送信時の認証方式](/sg/smtp-auth/)
- [OP25Bとは？外向き25番ポート遮断とスパム対策](/sg/op25b/)
- [スパムメールとは？メーリングリスト・チェーンメールとの違い](/sg/spam-mail/)
- [ベイジアンフィルタリングとは？迷惑メールを学習して判定する仕組み](/sg/bayesian-filtering/)
- [S/MIMEとは？メールの暗号化と電子署名の仕組み](/sg/smime/)
- [メールヘッダーインジェクションとは？改行を悪用する攻撃](/sg/mail-header-injection/)
- [メールヘッダの読み方とは？迷惑メール調査の判断軸](/sg/mail-header-analysis/)

### Webアプリ攻撃対策

試験では、「入力値を悪用する攻撃」か「利用者の操作を悪用する攻撃」かで切り分けます。

- [SQLインジェクションとは？仕組みと対策をやさしく理解](/sg/sql-injection/)
- [クロスサイトスクリプティングとは？スクリプト実行の仕組み](/sg/xss/)
- [クロスサイトリクエストフォージェリとは？なりすまし操作の仕組み](/sg/csrf/)
- [クリックジャッキングとは？見えない操作誘導の仕組み](/sg/clickjacking/)
- [ディレクトリトラバーサルとは？不正ファイルアクセスの仕組みと対策](/sg/directory-traversal/)
- [セッションハイジャックとは？ログイン乗っ取りの仕組みと対策](/sg/session-hijacking/)
- [中間者攻撃とは？通信を盗み見る仕組みと対策](/sg/man-in-the-middle-attack/)
- [Man-in-the-Browserとは？ブラウザ内改ざん攻撃の仕組み](/sg/man-in-the-browser/)

### マルウェア対策

試験では、「感染後に何をするか」と「どの情報を盗むか」で切り分けます。

- [マルウェアとは？種類と見分け方を整理](/sg/malware/)
- [ランサムウェアとは？身代金要求型攻撃の仕組み](/sg/ransomware/)
- [スパイウェアとは？情報を盗むマルウェアの特徴](/sg/spyware/)
- [キーロガーとは？入力情報を盗む仕組みを理解する](/sg/keylogger/)
- [バックドアとは？攻撃者が仕込む裏口を見分ける](/sg/backdoor/)
- [ルートキットとは？管理者権限で隠蔽する仕組み](/sg/rootkit/)
- [マクロウイルスとは？Officeファイル経由の感染を理解する](/sg/macro-virus/)
- [Bagleワームとは？メール拡散型マルウェアの判断ポイント](/sg/bagle-worm/)
- [SQL Slammerとは？SQL Serverの脆弱性を悪用するワーム](/sg/sql-slammer/)
- [VBS.LoveLetterとは？VBScript添付ファイルで広がるワーム](/sg/vbs-loveletter/)
- [ボットとは？遠隔操作される仕組みを理解する](/sg/bot/)
- [ボットネットとは？踏み台化とDDoSの関係を理解する](/sg/botnet/)
- [C&Cサーバとは？ボットネットを操る指令の仕組み](/sg/command-and-control/)
- [クリプトジャッキングとは？不正マイニングの仕組みを理解する](/sg/cryptojacking/)
- [サンドボックスとは？安全にプログラムを実行する仕組み](/sg/sandbox/)
- [マルウェア解析とは？静的解析と動的解析の違い](/sg/malware-analysis/)
- [RLOとは？文字の表示順を悪用した拡張子偽装の手口](/sg/rlo-extension-spoofing/)

### 無線LAN対策

試験では、「暗号化方式」か「接続する端末の制御」かで切り分けます。

- [Wi-Fiのセキュリティ方式を比較！WEP・WPA・WPA2・WPA3の違い](/sg/wifi-security-protocols/)
- [WPA2・WPA3・802.1Xとは？無線LAN認証の違いを整理](/sg/wifi-auth-wpa2-wpa3-8021x/)
- [事前共有鍵（PSK）とは？無線LANの接続制御の基本](/sg/psk-wireless-auth/)
- [プライバシーセパレータとは？無線LANで端末同士を隔離する仕組み](/sg/privacy-separator/)
- [MACアドレスとは？機器を識別する番号の役割](/sg/mac-address/)

### 物理的セキュリティ対策

試験では、「人の入退室」か「機器・画面・紙の保護」かで切り分けます。

- [入退室管理とは？物理アクセス制御の基本](/sg/access-control-physical/)
- [アンチパスバックとは？不正な入退室を防ぐ仕組み](/sg/anti-passback/)
- [セキュリティワイヤとは？機器盗難を防ぐ基本対策](/sg/security-wire/)
- [監視カメラとは？抑止と証跡の役割を整理](/sg/surveillance-camera/)
- [クリアデスク・クリアスクリーンとは？情報漏えい防止の基本ルール](/sg/clear-desk-screen/)
- [物理的セキュリティ対策まとめ｜出題パターンと切り分け一覧](/sg/physical-security-summary/)

### バックアップ・可用性対策

試験では、「データを戻す対策」か「サービスを止めない対策」かで切り分けます。

- [遠隔バックアップとは？災害時のデータ保護の基本](/sg/remote-backup/)
- [RAIDとは？冗長化による信頼性向上の仕組み](/sg/raid/)
- [UPSとは？停電時の業務継続を支える仕組み](/sg/ups/)
- [稼働率とは？可用性の考え方とSLAでの判断基準](/sg/availability/)

### 検知・分析・脆弱性対策

試験では、「弱点を見つける」か「攻撃後の証拠を調べる」かで切り分けます。

- [脆弱性対策まとめ｜JVN・CVSS・検査・ペンテスト・ファジングの違い](/sg/vulnerability-cheatsheet/)
- [脆弱性スキャンとは？自動検査で弱点を見つける仕組み](/sg/vulnerability-scan/)
- [ファジングとは？脆弱性を見つけるテスト手法を整理](/sg/fuzzing/)
- [CVSSとは？脆弱性の深刻度を共通スコアで判断する](/sg/cvss/)
- [JVNとは？脆弱性情報の見方とJVN iPediaとの違い](/sg/jvn/)
- [ポートスキャンとは？攻撃と対策の両面から理解する](/sg/port-scan/)
- [ハニーポットとは？攻撃者をおびき寄せる仕組み](/sg/honeypot/)
- [デジタルフォレンジックとは？証拠としてのデータ活用](/sg/digital-forensics/)
- [ログ管理とは？証跡と異常検知の役割を整理](/sg/log-management/)
- [監査ログとは？不正検知と追跡の基本](/sg/audit-log/)


## その他の関連記事（タグ基準・未掲載分）

以下は `sg-security-measures` タグが付いているものの、上記セクションには未掲載だった関連記事です。新規記事に同タグを付ければ、この一覧に自動で表示されます。

{% assign curated_slugs = "auth-access-summary,auth-access-control-summary,crypto-certificate-integrity-summary,crypto-auth-platform-summary,security-measures-overview,physical-security-summary,security-measures-comparison,vulnerability-cheatsheet,web-application-attacks-summary,dns-mail-security-summary,network-defense-summary,malware-threats-summary,authentication-methods,frr-far,identification-code,authorization,access-control,access-control-model,authentication-authorization-access-control,multi-factor-authentication,mfa-vs-step-auth,sso,idp,token-authentication,risk-based-authentication,challenge-response-authentication,privileged-id,least-privilege,zero-trust,perimeter-security,brute-force-attack,reverse-brute-force-attack,dictionary-attack,password-list-attack,password-management,hdd-password,password-hash-authentication,rainbow-table,salt,captcha,firewall,packet-filtering,ips,waf,dmz,vpn,secure-protocol,ssh,telnet,ssl-tls,edos-attack,http-https,port-number,smtp-port-packet-filtering,dns,dns-zone-transfer,dns-cache-poisoning,dns-reflector-attack,domain-hijacking,spf,spf-dkim,smtp-auth,bayesian-filtering,smime,mail-header-injection,sql-injection,xss,csrf,clickjacking,directory-traversal,session-hijacking,man-in-the-middle-attack,man-in-the-browser,malware,ransomware,spyware,keylogger,backdoor,rootkit,macro-virus,bot,botnet,command-and-control,cryptojacking,sandbox,malware-analysis,rlo-extension-spoofing,wifi-security-protocols,wifi-auth-wpa2-wpa3-8021x,psk-wireless-auth,privacy-separator,mac-address,access-control-physical,anti-passback,security-wire,surveillance-camera,clear-desk-screen,remote-backup,raid,ups,availability,vulnerability-scan,fuzzing,cvss,jvn,port-scan,honeypot,digital-forensics,log-management,audit-log" | split: "," %}
{% assign auto_related = site.pages | where: "tags", "sg-security-measures" | sort: "title" %}
{% assign auto_count = 0 %}
{% for p in auto_related %}
  {% if p.permalink %}
    {% assign slug = p.permalink | remove: "/sg/" | remove: "/" %}
    {% unless curated_slugs contains slug %}
- [{{ p.title }}]({{ p.permalink }})
      {% assign auto_count = auto_count | plus: 1 %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% if auto_count == 0 %}
- 現在、未掲載分はありません。
{% endif %}
