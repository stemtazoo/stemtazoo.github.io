---
layout: page
title: スクラムの役割とは？プロダクトオーナー・スクラムマスター・開発者の違い【基本情報技術者試験】
description: ScrumのProduct Owner・Scrum Master・Developersの役割を、価値・プロダクトバックログ・開発・支援という判断軸で整理し、FE科目Aでの見分け方を解説します。
permalink: /fe/scrum-roles/
tags: [fe, fe-technology, software-development, agile, scrum]
fe_section: テクノロジ系
fe_subsection: ソフトウェア開発管理技術
fe_order: 43
date: 2026-09-23
last_modified_at: 2026-09-23
---

## まず結論

Scrumでは、Scrum Teamを**Product Owner（プロダクトオーナー）・Scrum Master（スクラムマスター）・Developers（開発者）**で構成します。

基本情報技術者試験では、役割名を丸暗記するより、**「何に責任を持つか」**で切り分けるのがポイントです。

~~~text
プロダクトの価値
＋ Product Backlog
→ Product Owner

開発
＋ 利用可能なIncrement
→ Developers

Scrumの確立
＋ 支援・コーチ
→ Scrum Master
~~~

特に、**「プロダクトの価値を最大化」「プロダクトバックログ」**が出てきたら、Product Ownerを考えます。

## 直感的な説明

3つの役割は、次のようにイメージすると分かりやすいです。

~~~text
Product Owner
「何を優先すれば価値が高まる？」

Developers
「どう作って完成させる？」

Scrum Master
「Scrumがうまく機能するように支援する」
~~~

Product Ownerは、開発者に細かな作業指示を出す「上司」として覚えるのではありません。

**プロダクトの価値とProduct Backlogに責任を持つ人**と捉えるのが重要です。

## 定義・仕組み

### Product Owner

Product Ownerは、Scrum Teamの作業から生まれる**プロダクトの価値を最大化することに責任を持ちます**。

また、Product Backlogを効果的に管理する責任があります。

具体的には、Product Goalを策定・明示し、Product Backlog Itemを作成・明確化して並べ、Product Backlogを透明で見える状態にします。

試験では、**「価値を最大化」「Product Backlog」「優先順位・並び順」**が強い判断ワードです。

### Developers

Developersは、各Sprintで**利用可能なIncrementを作ることにコミットする人たち**です。

Scrum Guideでは、Sprint Backlogという計画を作る、Definition of Doneに従って品質を作り込む、Sprint Goalに向けて日々計画を調整する、といった責任があります。

したがって、**「Sprint Backlog」「Increment」「Definition of Done」「実際に開発する」**ならDevelopersを考えます。

### Scrum Master

Scrum Masterは、Scrum Guideで定義されたScrumを**確立することに責任を持ちます**。

Scrum Teamや組織にScrumの理論と実践を理解してもらえるよう支援し、Scrum Teamの有効性を高めます。

**「Scrumの確立」「支援」「コーチ」**といった表現が判断材料になります。

Scrum Masterを、メンバーへ一方的に命令する従来型の「チームリーダー」と考えないことも重要です。

## 科目Aでどう出る？

科目Aでは、具体的な活動から誰の役割かを選ばせる問題に注意します。

| 問題文の表現 | 判断 |
|---|---|
| プロダクトの価値を最大化する | **Product Owner** |
| Product Backlogを効果的に管理する | **Product Owner** |
| Product Backlog Itemを並べる | **Product Owner** |
| Sprint Backlogという計画を作る | **Developers** |
| Definition of Doneを守って品質を作り込む | **Developers** |
| 利用可能なIncrementを作る | **Developers** |
| Scrumの理論と実践を理解できるよう支援する | **Scrum Master** |
| チームをコーチする | **Scrum Master** |

試験中は、まず名詞を見ると判断しやすくなります。

~~~text
Product Backlog
→ Product Owner

Sprint Backlog・Increment
→ Developers

Scrumそのもの・支援・コーチ
→ Scrum Master
~~~

## どんな場面で使う？

Product Ownerは、限られた時間の中で、何を先に作ればプロダクトの価値を高められるかを考えます。

Developersは、Sprint Goalに向けて、どのように開発を進めるかを計画し、利用可能なIncrementを作ります。

Scrum Masterは、Scrum Teamが自己管理できるようにコーチしたり、進行を妨げる問題への対応を支援したりします。

## よくある誤解・混同

### Product OwnerがSprintの作業計画を全部決める？

違います。

Product OwnerはProduct Backlogの管理に責任を持ちますが、**Sprint Backlogという作業計画を作るのはDevelopers**です。

~~~text
Product Backlog
→ Product Owner

Sprint Backlog
→ Developers
~~~

### Scrum Masterはチームの上司？

そう覚えない方が安全です。

Scrum Masterは、Scrumを確立し、チームや組織がScrumを理解・実践できるように支援する役割です。

### Product OwnerとScrum Masterを混同する

迷ったら、**「価値」か「Scrumの支援」か**を見ます。

~~~text
価値・Product Backlog
→ Product Owner

Scrumの確立・支援・コーチ
→ Scrum Master
~~~

### 「開発チーム」という表現は現在も正式な役割名？

古い教材や過去問題では「開発チーム（Development Team）」という表現を見ることがあります。

現在の2020年版Scrum Guideでは、Scrum Team内を**Product Owner・Scrum Master・Developers**と表現しています。

試験問題の年代によって表現が違っても、役割の内容から判断できるようにしておくと安全です。

## 原典で確認する

Scrumの役割は、共同考案者のKen SchwaberとJeff Sutherlandが公開している**The Scrum Guide**で確認できます。

- [The Scrum Guide（公式）](https://scrumguides.org/scrum-guide.html)
- [Scrum Guide ダウンロードページ](https://scrumguides.org/download.html)

2020年版では、Scrum TeamをProduct Owner・Scrum Master・Developersで構成するとし、それぞれの責任を定義しています。

FE対策では原文を丸暗記する必要はありません。次の3本を判断基準にすると十分です。

~~~text
価値・Product Backlog
→ Product Owner

開発・Increment
→ Developers

Scrumの確立・支援
→ Scrum Master
~~~

関連するイベントについては、次の記事で整理しています。

- [スクラムのイベントとは？プランニング・デイリースクラム・レビュー・レトロスペクティブを整理](/fe/scrum-events/)

## まとめ（試験直前用）

- **価値を最大化・Product Backlog** → Product Owner
- **Sprint Backlog・Increment・Definition of Done** → Developers
- **Scrumの確立・支援・コーチ** → Scrum Master
- Product Ownerは「チームの上司」として覚えない
- Product BacklogとSprint Backlogを混同しない
- 古い「開発チーム」という表現は、現在のScrum GuideではDevelopersに整理されている

~~~text
価値
→ Product Owner

作る
→ Developers

支える
→ Scrum Master
~~~

{% include fe_article_footer.html %}
