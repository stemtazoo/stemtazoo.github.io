---
layout: page
title: UMLクラス図とは？クラスの箱・属性・操作・関係記号の読み方【基本情報技術者試験】
description: UMLクラス図の長方形に書くクラス名、属性・操作の区画と省略表記を図解します。関連・汎化・集約・コンポジション・依存・実現を、記号の形、実線と破線、向きで切り分け、関連名とロール名の位置、多重度の読み方、時間順を表す図との違いをFE科目A向けに整理します。
permalink: /fe/uml-class-diagram/
tags: [fe, fe-technology, system-development, uml]
fe_section: テクノロジ系
fe_subsection: システム開発技術
fe_order: 64
date: 2026-09-27
last_modified_at: 2026-10-03
---

<link rel="stylesheet" href="{{ '/assets/css/fe-uml-class-diagram.css' | relative_url }}">

## まず結論

**UMLのクラス図**は、クラスが持つ**属性・操作**と、クラス同士の**関係**を表す静的な構造図です。

**クラスを表す長方形の中にはクラス名を書きます。** 属性・操作の区画は省略できるため、3段に区切られていない箱でもクラスを表せます。

試験では、**「箱の中に何を書くか」と「線や先端の記号が何を表すか」**を分けて読みます。特に、白抜き三角は汎化、白抜きひし形は集約、と形を見分けましょう。

## 直感的な説明

クラス図は、システムに登場する「もの」の設計図を並べ、その関係を表した図です。

例えば「商品」なら、商品コードや価格は**持っている情報＝属性**、在庫確認や価格変更は**できる処理＝操作**です。

<div class="fe-uml-diagrams">
<div class="fe-uml-diagrams__grid">
<figure>
<figcaption>属性・操作を示す表記</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 230" role="img" aria-labelledby="fe-uml-full"><title id="fe-uml-full">商品クラスの上段にクラス名、中段に商品コードと価格という属性、下段に在庫確認と価格変更という操作を記述する。</title><rect x="10" y="15" width="205" height="200" fill="#fff" stroke="#253e50" stroke-width="2"/><path d="M10 65 H215 M10 145 H215" fill="none" stroke="#253e50" stroke-width="2"/><g font-size="18"><text x="112" y="47" text-anchor="middle">商品</text><text x="24" y="99">商品コード</text><text x="24" y="127">価格</text><text x="24" y="174">在庫確認()</text><text x="24" y="202">価格変更()</text><text x="231" y="47">クラス名</text><text x="231" y="113">属性</text><text x="231" y="188">操作</text></g></svg>
<p>何を持つか、何ができるかを示す。</p>
</figure>
<figure>
<figcaption>クラス名だけの省略表記</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 230" role="img" aria-labelledby="fe-uml-short"><title id="fe-uml-short">区画を省略した長方形にも、商品というクラス名を書く。属性と操作を表示しなくてもクラスを表せる。</title><rect x="60" y="72" width="220" height="75" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="170" y="118" text-anchor="middle" font-size="22">商品</text><text x="170" y="187" text-anchor="middle" font-size="18">区画の省略も可能</text></svg>
<p>属性・操作を表示しなくてもクラスを表す。</p>
</figure>
</div>
</div>

**見るポイント：区画の数が変わっても、箱の中の「商品」はクラス名です。** 省略されているからといって、属性や操作が存在しないとは限りません。

## 定義・仕組み

### クラス名・属性・操作

クラスは、同じ性質や振る舞いを持つオブジェクトの共通定義です。クラスと個々のオブジェクトの違いは、[クラスとインスタンス](/fe/class-instance/)で確認できます。

| 要素 | 表すもの | 商品クラスの例 |
|---|---|---|
| クラス名 | そのクラスが何か | 商品 |
| 属性 | 持っているデータ・性質 | 商品コード、価格 |
| 操作 | 提供する処理・振る舞い | 在庫確認()、価格変更() |

操作は、プログラミングのメソッドに近いものとして理解するとつかみやすくなります。

### クラス間の関係記号

**見るポイント：形 → 実線か破線か → どちら側に付くか、の順に読みます。** ここでは、代表的な記法を比較します。

<div class="fe-uml-diagrams">
<div class="fe-uml-diagrams__grid">
<figure>
<figcaption>関連</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 115" role="img" aria-labelledby="fe-uml-rel-0"><title id="fe-uml-rel-0">関連：顧客と注文。実線。クラス同士のつながりを表す。</title><rect x="10" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="60" y="64" text-anchor="middle" font-size="17">顧客</text><rect x="230" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="280" y="64" text-anchor="middle" font-size="17">注文</text><line x1="110" y1="58" x2="230" y2="58" stroke="#253e50" stroke-width="2"/></svg>
<p>実線。クラス同士のつながりを表す。</p>
</figure>
<figure>
<figcaption>汎化</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 115" role="img" aria-labelledby="fe-uml-rel-1"><title id="fe-uml-rel-1">汎化：会員と顧客。実線＋白抜き三角。会員は顧客の一種で、三角は親側。</title><rect x="10" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="60" y="64" text-anchor="middle" font-size="17">会員</text><rect x="230" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="280" y="64" text-anchor="middle" font-size="17">顧客</text><line x1="110" y1="58" x2="212" y2="58" stroke="#253e50" stroke-width="2"/><polygon points="230,58 212,47 212,69" fill="#fff" stroke="#253e50" stroke-width="2"/></svg>
<p>実線＋白抜き三角。会員は顧客の一種で、三角は親側。</p>
</figure>
<figure>
<figcaption>集約</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 115" role="img" aria-labelledby="fe-uml-rel-2"><title id="fe-uml-rel-2">集約：チームと選手。実線＋白抜きひし形。ひし形は全体側。</title><rect x="10" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="60" y="64" text-anchor="middle" font-size="17">チーム</text><rect x="230" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="280" y="64" text-anchor="middle" font-size="17">選手</text><line x1="142" y1="58" x2="230" y2="58" stroke="#253e50" stroke-width="2"/><polygon points="110,58 126,47 142,58 126,69" fill="#fff" stroke="#253e50" stroke-width="2"/></svg>
<p>実線＋白抜きひし形。ひし形は全体側。</p>
</figure>
<figure>
<figcaption>コンポジション</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 115" role="img" aria-labelledby="fe-uml-rel-3"><title id="fe-uml-rel-3">コンポジション：注文と注文明細。実線＋黒ひし形。全体と部分の強い結び付き。</title><rect x="10" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="60" y="64" text-anchor="middle" font-size="17">注文</text><rect x="230" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="280" y="64" text-anchor="middle" font-size="17">注文明細</text><line x1="142" y1="58" x2="230" y2="58" stroke="#253e50" stroke-width="2"/><polygon points="110,58 126,47 142,58 126,69" fill="#253e50" stroke="#253e50" stroke-width="2"/></svg>
<p>実線＋黒ひし形。全体と部分の強い結び付き。</p>
</figure>
<figure>
<figcaption>依存</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 115" role="img" aria-labelledby="fe-uml-rel-4"><title id="fe-uml-rel-4">依存：帳票作成と印刷機能。破線＋開いた矢印。利用する側から利用される側へ。</title><rect x="10" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="60" y="64" text-anchor="middle" font-size="17">帳票作成</text><rect x="230" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="280" y="64" text-anchor="middle" font-size="17">印刷機能</text><line x1="110" y1="58" x2="230" y2="58" stroke="#253e50" stroke-width="2" stroke-dasharray="7 5"/><path d="M216 48 L230 58 L216 68" fill="none" stroke="#253e50" stroke-width="2"/></svg>
<p>破線＋開いた矢印。利用する側から利用される側へ。</p>
</figure>
<figure>
<figcaption>実現</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 115" role="img" aria-labelledby="fe-uml-rel-5"><title id="fe-uml-rel-5">実現：印刷機と印刷可能。破線＋白抜き三角。三角は仕様側。</title><rect x="10" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="60" y="64" text-anchor="middle" font-size="17">印刷機</text><rect x="230" y="30" width="100" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><text x="280" y="50" text-anchor="middle" font-size="12">«interface»</text><text x="280" y="71" text-anchor="middle" font-size="17">印刷可能</text><line x1="110" y1="58" x2="212" y2="58" stroke="#253e50" stroke-width="2" stroke-dasharray="7 5"/><polygon points="230,58 212,47 212,69" fill="#fff" stroke="#253e50" stroke-width="2"/></svg>
<p>破線＋白抜き三角。三角は仕様側。</p>
</figure>
</div>
</div>

| 関係 | 線・記号 | 読む方向・判断基準 |
|---|---|---|
| 関連 | 実線 | クラス同士に意味のあるつながりがある |
| 汎化 | 実線＋白抜き三角 | 子から親へ。「会員は顧客の一種」 |
| 集約 | 実線＋白抜きひし形 | ひし形は全体側。全体と部分の関係 |
| コンポジション（合成） | 実線＋黒ひし形 | ひし形は全体側。部分は同時に複数の全体に属さず、全体の削除時にはその部分も削除される |
| 依存 | 破線＋開いた矢印 | 利用する側から利用される側へ |
| 実現 | 破線＋白抜き三角 | 実装する側から仕様側へ。図の「印刷可能」はインタフェース |

集約・コンポジションは、全体と部分の関係を表す関連の一種です。白抜きの集約を、黒ひし形のコンポジションと同じ強い関係だと決めつけないようにします。

### 関連名とロール名

**関連名**は関係そのものの名前、**ロール名**は関連の端に付ける役割の名前です。

例えば、会社と社員の関係に「雇用」という関連名を付け、会社側に「雇用主」、社員側に「所属者」というロール名を付けられます。

<div class="fe-uml-diagrams">
<figure>
<figcaption>関連名は線の近く、ロール名は関連端</figcaption>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 165" role="img" aria-labelledby="fe-uml-roles"><title id="fe-uml-roles">会社と社員を実線で結ぶ。線の中央付近に関連名の雇用、会社側の端にロール名の雇用主、社員側の端にロール名の所属者を置く。会社側の多重度は1、社員側は0..*。</title><rect x="10" y="55" width="90" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><rect x="360" y="55" width="90" height="55" fill="#fff" stroke="#253e50" stroke-width="2"/><line x1="100" y1="83" x2="360" y2="83" stroke="#253e50" stroke-width="2"/><g font-size="18"><text x="55" y="90" text-anchor="middle">会社</text><text x="405" y="90" text-anchor="middle">社員</text><text x="230" y="40" text-anchor="middle">雇用（関連名）</text><text x="110" y="70">雇用主</text><text x="350" y="70" text-anchor="end">所属者</text><text x="110" y="106">1</text><text x="350" y="106" text-anchor="end">0..*</text></g><text x="230" y="145" text-anchor="middle" font-size="17">両端の役割名＝ロール名</text></svg>
<p>社員から見た会社の役割は「雇用主」、会社から見た社員の役割は「所属者」。</p>
</figure>
</div>

### 多重度

多重度は、**反対側の1インスタンスから見て、その側が何個対応するか**を表します。

| 表記 | 意味 |
|---|---|
| 1 | 必ず1個 |
| 0..1 | 0個または1個 |
| 0..* | 0個以上 |
| 1..* | 1個以上 |

会社側が「1」、社員側が「0..*」なら、会社1社に社員は0人以上、社員1人に対応する会社は1社です。これは、この図で定めたモデル上の条件です。

詳しくは、[UMLの多重度](/fe/uml-multiplicity/)で整理しています。

図の表記は、[OMG：UML 2.5.1仕様](https://www.omg.org/spec/UML/2.5.1/PDF)の9.2（クラスを含む分類要素）、7.7（依存・実現）、11.5（関連）で確認できます。出題範囲は、[IPA：試験要綱・シラバス](https://www.ipa.go.jp/shiken/syllabus/gaiyou.html)を参照できます。

## 科目Aでどう出る？

### 箱の中と線の近くを分ける

| 問われる場所・記号 | 判断 |
|---|---|
| クラスを表す長方形の中、または区切った上段 | クラス名 |
| クラスの箱の中段・下段 | 典型的には属性・操作 |
| クラス同士を結ぶ線の近く | 関連名 |
| 関連の端の近く | ロール名・多重度 |
| 実線の先端の白抜き三角 | 汎化。親側を向く |
| 実線の端の白抜きひし形 | 集約。全体側に付く |
| ユースケース図の楕円の中 | ユースケース名 |

長方形はほかの図でも使うので、**箱だけで図の種類を断定せず、属性・操作や周囲の関係記号も合わせて見ます。**

### ほかのUML図との違い

| 手掛かり | 考える図 |
|---|---|
| クラス・属性・操作・クラス間の関係 | **クラス図** |
| ライフライン・メッセージの時間順 | シーケンス図 |
| オブジェクト間のリンク・番号付きメッセージ | コミュニケーション図 |
| 状態・イベント・遷移 | 状態遷移図 |
| 利用者（アクター）・楕円の機能 | ユースケース図 |

図全体の使い分けは[UMLの見分け方](/fe/uml/)、時間順とつながりの違いは[シーケンス図とコミュニケーション図](/fe/sequence-communication-diagram/)で確認できます。

## どんな場面で使う？

クラス図は、販売管理なら「顧客・注文・商品」、設備管理なら「設備・点検記録・担当者」のように、システムの構造を整理するときに使います。

クラスごとの情報や処理に加え、どのクラスが関係するか、どれが親クラスか、全体と部分の関係があるかを検討できます。

**処理の時間順を見たいならシーケンス図、状態の変化を見たいなら[状態遷移図](/fe/state-transition-diagram/)**というように、表したい内容に合わせて図を選びます。

## よくある誤解・混同

### 3段に区切られていなければクラスではない

属性・操作の区画は省略できます。クラス名だけを書いた長方形でもクラスを表せます。

### 三角形とひし形は同じ意味

**白抜き三角＋実線は汎化、白抜きひし形＋実線は集約**です。汎化では親側、集約では全体側に記号が付きます。

さらに、白抜き三角でも**破線なら実現**です。記号の形と線の種類をセットで見ます。

### 箱の中の名前は関連名やロール名

クラスを表す箱の名前はクラス名です。関連名は線の近く、ロール名は関連端に置かれます。「集約」は関係の種類であり、クラス名を記述する欄の名称ではありません。

### 属性と操作は同じ

「価格」は属性、「価格変更()」は操作です。**データか処理か**で切り分けます。

### オブジェクトやリンクがあればクラス図

オブジェクト間のリンクとメッセージを表すなら、コミュニケーション図が候補です。具体的なインスタンスの構造を表すオブジェクト図もあるため、単語だけで断定しません。

クラス図は、個々の実行結果や時間順ではなく、クラスの静的な構造を表します。

## まとめ（試験直前用）

- **クラスの箱の中＝クラス名。属性・操作の区画は省略できる**
- 属性は持つデータ、操作はできる処理
- **実線＋白抜き三角＝汎化、実線＋白抜きひし形＝集約**
- 破線＋白抜き三角＝実現。形・線・向きを合わせて読む
- 関連名は線の近く、ロール名・多重度は関連端。多重度は反対側の1個から読む

{% include fe_article_footer.html %}
