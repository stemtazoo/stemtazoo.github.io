---
layout: page
title: ファイル転送プロトコルとは？主要プロトコルの違いを整理【DS検定】
description: ファイル転送プロトコルは主要プロトコルの違いを整理するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/file-transfer-protocol/
categories: [business]
tags: [ds, design]
prev: /ds/ffp/
next: /ds/filter/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

ファイル転送プロトコルとは、ネットワーク上でファイルを送受信するための通信ルール（プロトコル）のことです。

DS検定では、「FTP・FTPS・SFTP・SCPなどの違い（暗号化の有無）」を判断できるかがよく問われます。

特に次の切り分けが重要です。

FTP：暗号化なし

FTPS：SSL/TLSで暗号化

SFTP：SSHで暗号化


## 直感的な説明

ファイル転送プロトコルは、**「ネットワーク版の宅配ルール」**のようなものです。

例えば会社のシステムでは次のような場面があります。

サーバーにデータファイルをアップロードする

ログファイルを別サーバーに送る

BIツールにデータを渡す


このとき、

どうやって通信するか

セキュリティはどうするか


を決めるルールが ファイル転送プロトコルです。

イメージとしてはこうです。

PC  ──(ファイル転送プロトコル)──> サーバー

ただし問題は セキュリティです。

昔のプロトコルは通信が暗号化されないため、盗聴されるリスクがあります。

そのため現在は、暗号化されたプロトコルがよく使われます。



## 定義・仕組み

ファイル転送プロトコルとは、ネットワーク上でファイルを送受信するための通信プロトコルです。

代表的なものを整理すると次のようになります。

プロトコル	特徴	暗号化

FTP	もっとも基本的なファイル転送	なし
FTPS	FTP + SSL/TLS	あり
SFTP	SSHを使ったファイル転送	あり
SCP	SSHを使ったコピー	あり
HTTP	Web通信（ファイル転送用途でも使われる）	なし
HTTPS	HTTP + SSL/TLS	あり


ポイントは 暗号化の方法の違いです。

FTP（File Transfer Protocol）

もっとも基本的なファイル転送プロトコルです。

通信は暗号化されない

パスワードも平文で送信される


そのため現在では、セキュリティ上あまり使われないことも多いです。

FTPS（FTP Secure）

FTPを拡張したものです。

SSL/TLSで通信を暗号化

FTPを安全にしたもの


SFTP（SSH File Transfer Protocol）

SSHを使ったファイル転送です。

SSH通信で暗号化

SCPと似ているが、途中再開ができる


SCP（Secure Copy Protocol）

SSHを利用したファイルコピーです。

通信は暗号化される

転送が途中で止まると途中再開できない




## どんな場面で使う？

実務では次のような場面で使われます。

データ連携

例えば、

システムA → システムBへデータ送信

日次バッチでCSVを転送


基幹システム → (SFTP) → データ分析基盤

データ分析基盤

データサイエンスの実務では、

ログデータ

CSV

学習データ


などを SFTPでサーバーに送る といったケースが多いです。

Webサーバー運用

Webサイトでは、

HTML

画像

データ


をサーバーにアップロードするために、FTPやSFTPが使われます。



## よくある誤解・混同

① FTPとHTTPの混同

HTTPは Web通信のためのプロトコルです。

ただし、HTMLや画像、JSONなどの転送に使われるため、ファイル転送と誤解されやすいです。

② FTPは安全だと思ってしまう

FTPは通信が暗号化されません。

選択肢で「FTPは暗号化通信を行う」と書かれていたら 誤りです。

③ FTPSとSFTPの混同

名前は似ていますが、仕組みが違います。

プロトコル	仕組み

FTPS	FTP + SSL/TLS
SFTP	SSH


「どっちがSSH？」を聞かれたら SFTP です。



## まとめ（試験直前用）

ファイル転送プロトコルは、ネットワークでファイルを送る通信ルール。

DS検定では次の判断が重要です。

FTP：暗号化なし

FTPS：SSL/TLSで暗号化

SFTP：SSHで暗号化

SCP：SSHを使うが途中再開できない


選択肢では、

「FTPは暗号化される」

「SFTPはFTPの拡張」


などの誤解を狙った文章に注意します。



## 対応スキル項目（データエンジニアリング力シート）

IT基盤

データ管理基盤

★ データの収集・蓄積・加工・提供に関する基本的なIT技術を理解している

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>

<div style="margin-top: 16px;">
  🏠 <a href="/ds/">DS検定トップに戻る</a>
</div>

<div style="display:flex;justify-content:space-between;margin-top:12px;">

  {% if page.previous.url %}
    <a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url }}">{{ page.next.title }} →</a>
  {% endif %}

</div>
