---
layout: page
title: CAPTCHAとは？人間とボットを見分ける仕組み【基本情報技術者試験】
description: CAPTCHAを、人間による操作と自動プログラムによる操作を判別するための仕組みとして整理します。チャレンジレスポンス認証、ワンタイムパスワード、SQLインジェクション対策との違いもFE科目A向けに解説します。
permalink: /fe/captcha/
tags: [fe, fe-technology, security, authentication, captcha]
fe_section: 情報セキュリティ
fe_subsection: 情報セキュリティ問題
fe_order: 146
date: 2026-09-19
last_modified_at: 2026-09-19
---

## まず結論

CAPTCHA（キャプチャ）とは、**Webサイトなどへのアクセスや操作が、人間によるものか自動プログラムによるものかを判別するための仕組み**です。

基本情報技術者試験では、次の表現が出たらCAPTCHAを疑います。

```text
人間かコンピュータかを判別
自動プログラム・botを排除
利用者に問題や操作を求める
```

覚える一文はこれです。

> **人間かボットかを見分ける → CAPTCHA**

## 直感的な説明

Webサイトには、人間だけでなく自動プログラムもアクセスできます。

例えば、会員登録フォームへ自動的に大量の登録を行ったり、投稿フォームへ大量のスパムを送ったりするプログラムがあります。

そこでWebサイト側が、

```text
「この画像の中から信号機を選んでください」
「表示された文字を入力してください」
```

など、人間には比較的答えやすい課題を出します。

```text
Webサイト
   ↓ 問題を出す
利用者
   ↓ 応答する
Webサイト
   ↓
人間による操作かを判定
```

これがCAPTCHAの基本的な考え方です。

ただし、現在のCAPTCHAは必ずしも「画像を選ばせる方式」だけではありません。利用者の操作やアクセス状況を分析し、明示的な問題を表示せずにbotらしさを判定する方式もあります。

## 定義・仕組み

CAPTCHAという名称は、**Completely Automated Public Turing test to tell Computers and Humans Apart** に由来します。

CAPTCHAを体系的に提案したCarnegie Mellon Universityの研究では、CAPTCHAを、人間には解ける一方で当時のコンピュータプログラムには解くことが難しい、自動生成・自動採点されるテストとして説明しています。

- [Carnegie Mellon University：CAPTCHA: Using Hard AI Problems for Security](https://www.cs.cmu.edu/~jcl/papers/captcha_crypt/captcha_crypt.pdf)
- [Carnegie Mellon University KiltHub：CAPTCHA: Using Hard AI Problems for Security](https://kilthub.cmu.edu/articles/journal_contribution/CAPTCHA_Using_Hard_AI_Problems_for_Security/6604025)

これらはCAPTCHAの概念を提案した研究者による原著論文であり、**CAPTCHAそのものの一次情報として非常に有効**です。

### CAPTCHAの基本的な流れ

```text
1. Webサイトが課題を提示する
2. 利用者が回答・操作する
3. Webサイトが応答を評価する
4. 人間による操作かを判断する
```

代表的な方式には、次のようなものがあります。

| 方式 | 例 |
|---|---|
| 文字認識型 | 歪んだ文字列を読み取る |
| 画像選択型 | 指定された対象を含む画像を選ぶ |
| パズル型 | 部品を正しい位置へ移動する |
| 行動分析型 | 操作やアクセス状況からbotらしさを判定する |

### 現在のreCAPTCHA

GoogleのreCAPTCHAでは、利用者へ明示的な課題を出す方式だけでなく、利用者の操作をもとにスコアを返す方式も提供されています。

Googleの公式資料では、reCAPTCHA v3はユーザーに課題を表示するのではなく、操作に対するスコアを返し、サイト側がそのスコアに応じて追加認証などの対応を選べる仕組みとして説明されています。

- [Google for Developers：Choosing the type of reCAPTCHA](https://developers.google.com/recaptcha/docs/versions)
- [Google for Developers：reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3)
- [Google for Developers：Verifying the user's response](https://developers.google.com/recaptcha/docs/verify)

Googleの資料は、**reCAPTCHAというGoogle製品の現在の動作や実装についての一次情報**として有効です。

試験対策では、細かな製品仕様よりも、

> **CAPTCHAは「人間か自動プログラムか」を判別する仕組み**

という本質を押さえることが大切です。

## 科目Aでどう出る？

科目Aでは、CAPTCHAそのものの名称を選ばせるほか、別の認証・セキュリティ技術と混ぜて出題されます。

### 判断の軸

```text
人間かbotかを判定
→ CAPTCHA

一定時間ごとに異なるパスワード
→ ワンタイムパスワード

乱数などに応答して正当な相手か確認
→ チャレンジレスポンス認証

SQL文と入力データを分離
→ プレースホルダ／バインド
```

CAPTCHAとチャレンジレスポンス認証は、どちらも「問題を出して応答を見る」ため混同しやすいですが、目的が違います。

| 技術 | 何を確認する？ |
|---|---|
| CAPTCHA | 人間か自動プログラムか |
| チャレンジレスポンス認証 | 正当な利用者・相手か |
| ワンタイムパスワード | 一度または短時間だけ有効な認証情報 |
| プレースホルダ | SQLの命令と入力値を分離する |

試験中は次のように切ると分かりやすいです。

> **人間性の確認 → CAPTCHA**  
> **本人性・相手の正当性の確認 → 認証**

チャレンジレスポンス認証については、[チャレンジレスポンス認証とは？](/fe/challenge-response-authentication/)で詳しく整理しています。

## どんな場面で使う？

CAPTCHAは、自動プログラムによる大量操作を抑えたい場面で利用されます。

例えば、

- 会員登録フォーム
- ログイン画面
- 問合せフォーム
- コメント・投稿フォーム
- チケットや商品の購入処理
- パスワード再設定

などです。

目的は、単に利用者を本人認証することではなく、**自動化された大量アクセスや不正操作を抑制すること**です。

## よくある誤解・混同

### CAPTCHAは本人確認をする仕組み？

違います。

CAPTCHAで確認したいのは、基本的に**操作している主体が人間か自動プログラムか**です。

```text
CAPTCHAに成功
→ 人間らしい操作である

CAPTCHAに成功
≠
その人が本人である
```

本人確認には、パスワード、多要素認証、生体認証など別の仕組みが使われます。

### CAPTCHAとチャレンジレスポンス認証は同じ？

違います。

どちらも問題と応答を利用しますが、確認対象が異なります。

```text
CAPTCHA
→ 人間 vs bot

チャレンジレスポンス認証
→ 正当な利用者 vs なりすまし
```

### CAPTCHAは文字認証だけ？

違います。

現在では、画像選択、パズル、操作状況の分析など、さまざまな方式があります。

GoogleのreCAPTCHA v3のように、ユーザーへ明示的な問題を出さず、操作に基づくスコアで判断する仕組みもあります。

### プレースホルダもCAPTCHAの一種？

違います。

プレースホルダは、SQLインジェクション対策で使われます。

```text
プレースホルダ
→ SQL文と入力値を分離

CAPTCHA
→ 人間とbotを判別
```

SQLインジェクションについては、[SQLインジェクションとは？](/fe/sql-injection/)で整理しています。

### CAPTCHAを入れればbotを完全に防げる？

そうとは限りません。

CAPTCHAはbot対策の一つですが、攻撃側の技術も進歩しています。そのため、実際のサービスではアクセス制限、リスク分析、多要素認証など複数の対策を組み合わせます。

試験では「CAPTCHA = 完全な防御」と考えるのではなく、**人間と自動プログラムを見分けるための対策**と捉えるのが適切です。

## まとめ（試験直前用）

- CAPTCHAは、人間による操作か自動プログラムによる操作かを判別する仕組み
- 文字認識、画像選択、パズル、行動分析など複数の方式がある
- **人間かbotか → CAPTCHA**
- CAPTCHAは本人確認そのものではない
- **本人性・正当な相手か → 認証**
- チャレンジレスポンス認証とは目的が違う
- プレースホルダはSQLインジェクション対策
- CMUの原著論文はCAPTCHAの概念に関する一次情報
- Google公式資料はreCAPTCHAの現在の仕様・実装に関する一次情報

覚える一文はこれです。

> **人間かボットかを見分ける → CAPTCHA**

{% include fe_article_footer.html %}
