---
layout: page
title: LEFT JOINとWHEREの関係とは？（SQLのひっかけ問題）【DS検定】
permalink: /ds/left-join-where/
categories: [data-engineering]
tags: [ds, data-processing, sql]
prev: /ds/sql-where/
next: /ds/self-join/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

LEFT JOINのあとにWHEREで右テーブル条件を書くと、LEFT JOINが実質INNER JOINのような動きになることがある。

DS検定では
「LEFT JOINなのに全件出ないのはなぜか？」
という判断をさせる問題がよく出ます。


## 直感的な説明

「LEFT JOIN」は本来、

> 左の表は全部残す

という操作です。

しかし、そのあとで

> “条件に合わない行を消す”

というWHEREが実行されます。

たとえば：

従業員は全員出す（LEFT JOIN）

でも「アクティブなプロジェクトだけ」に絞る（WHERE）

とすると、

👉 プロジェクトが無い人はNULLになる  
👉 NULLは条件に合わないので消える

結果として、

**「アクティブな案件に参加している人だけ」**が残ります。

つまり、LEFT JOINなのに全員は出ません。


## 定義・仕組み

SQLの処理順は次のように考えます。

1. FROM
2. JOIN（ONで結合）
3. WHERE（結合後の絞り込み）
4. SELECT（表示）

例：

SELECT E.name, P.project_name
FROM Employees E
LEFT JOIN Projects P
  ON E.id = P.employee_id
WHERE P.status = 'active';

処理の流れ

① まずLEFT JOINが実行される  
→ 全従業員が残る  
→ プロジェクトがない人はP側がNULLになる

② そのあとWHEREがかかる

P.status = 'active'

- active → 残る
- inactive → 消える
- NULL → 消える（ここが重要）

つまり、

WHEREは「結合後の表」にかかる

ため、NULL行が消えてしまいます。


## ではどう書けばよいか？

もし

> 全従業員を表示しつつ、activeだけ結合したい

なら、条件はONに書きます。

LEFT JOIN Projects P
  ON E.id = P.employee_id
 AND P.status = 'active'

これなら、

- 従業員は全員残る
- activeのみ結合
- それ以外はNULL

になります。


## どんな場面で使う？

### ✔ 実務での例

- 社員一覧を出す
- 進行中プロジェクトだけを横に表示したい

このとき、WHEREに書いてしまうと

「プロジェクト未所属社員が消える」

というバグになります。


### ✔ DS検定で問われるポイント

DS検定では

- LEFT JOINとINNER JOINの違い
- WHEREとONの違い
- NULLの扱い

を理解しているかを問われます。

計算問題ではなく、

「このSQLはどんな結果になるか？」

という判断問題が多いです。


## よくある誤解・混同

❌ 「LEFT JOINなら必ず左は全部出る」

→ WHEREの書き方次第で消える


❌ 「WHEREもJOIN条件の一部」

→ 違う  
ONは「結合の条件」  
WHEREは「結合後のフィルタ」


❌ 「NULLは条件に合うこともある」

→ 比較演算では基本的にNULLは成立しない  
DS検定ではここがひっかけになります。


## DS検定での典型問題

> 次のSQLはどのような結果になるか？

選択肢では：

- 「すべての従業員が表示される」
- 「アクティブ案件の人だけ表示される」

のどちらかで迷わせてきます。

判断基準は：

👉 WHEREが右テーブル条件ならLEFTは崩れる


## まとめ（試験直前用）

- WHEREはJOIN後にかかる
- NULLはWHERE条件を通らない
- 右テーブル条件をWHEREに書くとLEFTがINNER化する
- 「LEFTなのに全件出ない」＝WHEREが原因

DS検定では
「JOINの種類」より
「どこに条件が書いてあるか」を見抜くことが重要。


## 対応スキル項目（データエンジニアリング力シート）

- データ基盤
- データベース
- ★ SQLを用いてデータの抽出・結合・集計ができる
- ★ データベースの基本構造と操作（SELECT、JOINなど）を理解している

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
