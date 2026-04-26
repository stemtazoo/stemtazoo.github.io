---
layout: page
title: 情報セキュリティ対策まとめ
description: 認証、アクセス制御、マルウェア対策、ネットワーク対策、物理的対策などを整理するSG試験向けまとめページです。
permalink: /sg/category/security-measures/
---

[SGトップへ戻る](/sg/)

## SG試験での見方

- 用語の定義だけでなく、役割で判断する
- 似た用語との違いを押さえる
- 実務上の目的とセットで理解する

## 関連記事一覧

## まず読むまとめ記事

- [認証・アクセス制御まとめ](/sg/auth-access-summary/)
- [技術的セキュリティ対策まとめ](/sg/security-measures-overview/)
- [物理的セキュリティ対策まとめ](/sg/physical-security-summary/)
- [セキュリティ対策の違いまとめ](/sg/security-measures-comparison/)
- [脆弱性対策まとめ](/sg/vulnerability-cheatsheet/)

## 認証・アクセス制御

試験では、「本人確認」なのか「操作権限の制御」なのかで切り分けます。

- [認証方式とは？3要素と多要素認証を整理](/sg/authentication-methods/)
- [アクセス制御（認可）とは？認証との違いを整理](/sg/authorization/)
- [アクセス管理とは？特権IDとneed-to-knowで権限を適切に制御](/sg/access-control/)
- [多要素認証（MFA）とは？認証強化の仕組みと判断ポイント](/sg/multi-factor-authentication/)
- [多要素認証と多段階認証の違いとは？混同しやすい認証方式を整理](/sg/mfa-vs-step-auth/)
- [シングルサインオン（SSO）とは？利便性とリスクを整理](/sg/sso/)
- [IdP（認証サーバ）とは？SSOの中核とリスクを整理](/sg/idp/)
- [リスクベース認証とは？状況に応じて強化する認証の仕組み](/sg/risk-based-authentication/)
- [チャレンジレスポンス認証とは？パスワードを送らない認証の仕組み](/sg/challenge-response-authentication/)
- [特権ID管理とは？管理者権限のリスクと対策を整理](/sg/privileged-id/)
- [最小権限の原則とは？権限管理の基本を理解](/sg/least-privilege/)
- [ゼロトラストとは？境界防御との違いを整理](/sg/zero-trust/)
- [境界防御とは？ゼロトラストとの違いを整理](/sg/perimeter-security/)

## パスワード・ログイン攻撃

試験では、「1つのIDを狙う攻撃」か「多くのIDに同じパスワードを試す攻撃」かで切り分けます。

- [ブルートフォース攻撃とは？総当たり攻撃の仕組みと対策](/sg/brute-force-attack/)
- [リバースブルートフォース攻撃とは？逆総当たりの仕組みと対策](/sg/reverse-brute-force-attack/)
- [辞書攻撃とは？効率的なパスワード破解の仕組み](/sg/dictionary-attack/)
- [パスワードリスト攻撃とは？使い回しを狙う不正ログイン](/sg/password-list-attack/)
- [パスワード管理とは？強度とロックアウトの考え方を整理](/sg/password-management/)
- [レインボーテーブルとは？パスワード解析の仕組みを理解](/sg/rainbow-table/)
- [ソルトとは？パスワードハッシュ強化の仕組み](/sg/salt/)
- [CAPTCHAとは？ボット対策の仕組みをやさしく理解](/sg/captcha/)

## ネットワーク対策

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
- [HTTPとHTTPSの違いとは？安全な通信の判断ポイント](/sg/http-https/)
- [ポート番号とは？通信先サービスの識別を理解する](/sg/port-number/)
- [SMTPのポート番号とは？パケットフィルタリングでの見方を整理](/sg/smtp-port-packet-filtering/)

## DNS・メール対策

試験では、「名前解決の悪用」か「送信元のなりすまし対策」かで切り分けます。

- [DNSとは？名前解決の仕組みとセキュリティのポイント](/sg/dns/)
- [DNSキャッシュポイズニングとは？偽サイトへ誘導する攻撃](/sg/dns-cache-poisoning/)
- [DNSリフレクター攻撃とは？仕組みと対策の考え方](/sg/dns-reflector-attack/)
- [ドメイン名ハイジャックとは？DNSを悪用したなりすましの仕組み](/sg/domain-hijacking/)
- [SPFとは？送信元IPでなりすましを防ぐ仕組み](/sg/spf/)
- [SPF・DKIMとは？なりすましメール対策の仕組み](/sg/spf-dkim/)
- [SMTP-AUTHとは？メール送信時の認証方式](/sg/smtp-auth/)
- [S/MIMEとは？メールの暗号化と電子署名の仕組み](/sg/smime/)
- [メールヘッダーインジェクションとは？改行を悪用する攻撃](/sg/mail-header-injection/)

## Webアプリ攻撃対策

試験では、「入力値を悪用する攻撃」か「利用者の操作を悪用する攻撃」かで切り分けます。

- [SQLインジェクションとは？仕組みと対策をやさしく理解](/sg/sql-injection/)
- [クロスサイトスクリプティングとは？スクリプト実行の仕組み](/sg/xss/)
- [クロスサイトリクエストフォージェリとは？なりすまし操作の仕組み](/sg/csrf/)
- [クリックジャッキングとは？見えない操作誘導の仕組み](/sg/clickjacking/)
- [ディレクトリトラバーサルとは？不正ファイルアクセスの仕組みと対策](/sg/directory-traversal/)
- [セッションハイジャックとは？ログイン乗っ取りの仕組みと対策](/sg/session-hijacking/)
- [中間者攻撃とは？通信を盗み見る仕組みと対策](/sg/man-in-the-middle-attack/)
- [Man-in-the-Browserとは？ブラウザ内改ざん攻撃の仕組み](/sg/man-in-the-browser/)

## マルウェア対策

試験では、「感染後に何をするか」と「どの情報を盗むか」で切り分けます。

- [マルウェアとは？種類と見分け方を整理](/sg/malware/)
- [ランサムウェアとは？身代金要求型攻撃の仕組み](/sg/ransomware/)
- [スパイウェアとは？情報を盗むマルウェアの特徴](/sg/spyware/)
- [キーロガーとは？入力情報を盗む仕組みを理解する](/sg/keylogger/)
- [ルートキットとは？管理者権限で隠蔽する仕組み](/sg/rootkit/)
- [マクロウイルスとは？Officeファイル経由の感染を理解する](/sg/macro-virus/)
- [ボットとは？遠隔操作される仕組みを理解する](/sg/bot/)
- [ボットネットとは？踏み台化とDDoSの関係を理解する](/sg/botnet/)
- [C&Cサーバとは？ボットネットを操る指令の仕組み](/sg/command-and-control/)
- [クリプトジャッキングとは？不正マイニングの仕組みを理解する](/sg/cryptojacking/)
- [サンドボックスとは？安全にプログラムを実行する仕組み](/sg/sandbox/)
- [マルウェア解析とは？静的解析と動的解析の違い](/sg/malware-analysis/)

## 無線LAN対策

試験では、「暗号化方式」か「接続する端末の制御」かで切り分けます。

- [Wi-Fiのセキュリティ方式を比較！WEP・WPA・WPA2・WPA3の違い](/sg/wifi-security-protocols/)
- [WPA2・WPA3・802.1Xとは？無線LAN認証の違いを整理](/sg/wifi-auth-wpa2-wpa3-8021x/)
- [事前共有鍵（PSK）とは？無線LANの接続制御の基本](/sg/psk-wireless-auth/)
- [プライバシーセパレータとは？無線LANで端末同士を隔離する仕組み](/sg/privacy-separator/)
- [MACアドレスとは？機器を識別する番号の役割](/sg/mac-address/)

## 物理的セキュリティ対策

試験では、「人の入退室」か「機器・画面・紙の保護」かで切り分けます。

- [入退室管理とは？物理アクセス制御の基本](/sg/access-control-physical/)
- [アンチパスバックとは？不正な入退室を防ぐ仕組み](/sg/anti-passback/)
- [セキュリティワイヤとは？機器盗難を防ぐ基本対策](/sg/security-wire/)
- [監視カメラとは？抑止と証跡の役割を整理](/sg/surveillance-camera/)
- [クリアデスク・クリアスクリーンとは？情報漏えい防止の基本ルール](/sg/clear-desk-screen/)
- [物理的セキュリティ対策まとめ｜出題パターンと切り分け一覧](/sg/physical-security-summary/)

## バックアップ・可用性対策

試験では、「データを戻す対策」か「サービスを止めない対策」かで切り分けます。

- [遠隔バックアップとは？災害時のデータ保護の基本](/sg/remote-backup/)
- [RAIDとは？冗長化による信頼性向上の仕組み](/sg/raid/)
- [UPSとは？停電時の業務継続を支える仕組み](/sg/ups/)
- [稼働率とは？可用性の考え方とSLAでの判断基準](/sg/availability/)

## 検知・分析・脆弱性対策

試験では、「弱点を見つける」か「攻撃後の証拠を調べる」かで切り分けます。

- [脆弱性対策まとめ｜JVN・CVSS・検査・ペンテスト・ファジングの違い](/sg/vulnerability-cheatsheet/)
- [脆弱性検査とペネトレーションテストの違いとは？判断基準を整理](/sg/vulnerability-scan/)
- [ファジングとは？脆弱性を見つけるテスト手法を整理](/sg/fuzzing/)
- [CVSSとは？脆弱性の深刻度を共通スコアで判断する](/sg/cvss/)
- [JVNとは？脆弱性情報の見方とJVN iPediaとの違い](/sg/jvn/)
- [ポートスキャンとは？攻撃と対策の両面から理解する](/sg/port-scan/)
- [ハニーポットとは？攻撃者をおびき寄せる仕組み](/sg/honeypot/)
- [デジタルフォレンジックとは？証拠としてのデータ活用](/sg/digital-forensics/)
- [ログ管理とは？証跡と異常検知の役割を整理](/sg/log-management/)
- [監査ログとは？不正検知と追跡の基本](/sg/audit-log/)
