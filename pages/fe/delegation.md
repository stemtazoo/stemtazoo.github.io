---
layout: page
title: 委譲（デリゲーション）とは？処理を別のオブジェクトに任せる仕組み【基本情報技術者試験】
description: 委譲を「受け取った処理の一部を別のオブジェクトへ任せる仕組み」として整理し、Pythonのメソッド呼び出しと戻り値で流れを追いながら、継承・合成・伝搬との違いをFE科目A・B向けに解説します。
permalink: /fe/delegation/
tags: [fe, fe-technology, programming, object-oriented]
fe_section: テクノロジ系
fe_subsection: アルゴリズムとプログラミング
fe_order: 66
date: 2026-10-25
last_modified_at: 2026-10-25
---

## まず結論

**委譲（デリゲーション、delegation）**とは、あるオブジェクトが受け取った仕事の一部を、**別のオブジェクトに処理してもらう仕組み**です。

基本情報技術者試験では、説明文の動詞で判断します。

~~~text
処理を別のオブジェクトへ依頼する
→ 委譲

上位クラスの機能を下位クラスが引き継ぐ
→ 継承
~~~

**委譲は「任せる」、継承は「引き継ぐ」**と押さえると、選択肢を切りやすくなります。

このページでは**処理を依頼する流れ**を中心に扱います。クラスの上下関係は[継承](/fe/inheritance/)、オブジェクトを部分として持つ関係は[UMLクラス図](/fe/uml-class-diagram/)で別に説明しています。

## 直感的な説明

例えば、注文を受け付ける担当と、支払いを処理する担当がいる場面を考えます。

~~~text
利用者
  ↓ 注文・支払依頼
注文オブジェクト
  ↓ 支払処理を依頼（委譲）
決済オブジェクト
  ↓ 支払いを処理し、結果を返す
注文オブジェクト
  ↓ 結果を返す
利用者
~~~

注文オブジェクトは「注文を受け付ける」仕事を担当しますが、決済の細かい処理まで自分で実装する必要はありません。

**注文が受け取った仕事のうち、決済だけを決済オブジェクトへ任せる**のが委譲です。

## 定義・仕組み

### Pythonで委譲を確認する

注文処理を担当する`Order`と、決済処理を担当する`PaymentProcessor`という2つのクラスを用意します。

~~~python
class PaymentProcessor:
    def pay(self, amount):
        print(f"決済処理：{amount}円")
        return "支払完了"

class Order:
    def __init__(self, processor):
        self.processor = processor

    def checkout(self, amount):
        print("注文確定")
        result = self.processor.pay(amount)  # 決済を委譲
        print("決済結果を受信")
        return result

processor = PaymentProcessor()
order = Order(processor)
print(order.checkout(1500))
~~~

実行すると、次の順番で表示されます。

~~~text
注文確定
決済処理：1500円
決済結果を受信
支払完了
~~~

重要なのは、`Order`には決済の処理本体を書いていないことです。

~~~python
result = self.processor.pay(amount)
~~~

この1行で`PaymentProcessor`の`pay()`を呼び出し、**支払いを任せてから結果を受け取っています**。これが委譲の中心です。

### 処理の流れを1ステップずつ確認する

<link rel="stylesheet" href="{{ '/assets/css/fe-delegation-demo.css' | relative_url }}">

<div class="fe-delegation-demo" data-fe-delegation-demo>
  <p class="fe-delegation-demo__title">どのオブジェクトが処理している？</p>
  <div class="fe-delegation-demo__objects">
    <div data-delegation-order><strong>Order</strong><span>注文を管理</span></div>
    <span class="fe-delegation-demo__arrow" aria-hidden="true">⇄</span>
    <div data-delegation-payment><strong>PaymentProcessor</strong><span>決済を担当</span></div>
  </div>
  <ol class="fe-delegation-demo__steps">
    <li data-delegation-stage="0">利用者が <code>Order.checkout(1500)</code> を呼ぶ</li>
    <li data-delegation-stage="1"><code>Order</code> が <code>PaymentProcessor.pay(1500)</code> を呼ぶ（委譲）</li>
    <li data-delegation-stage="2"><code>PaymentProcessor</code> が決済処理し「支払完了」を返す</li>
    <li data-delegation-stage="3"><code>Order</code> が戻り値を受け取り、呼出元へ返す</li>
  </ol>
  <p class="fe-delegation-demo__status" data-delegation-status role="status" aria-live="polite">最初はOrder.checkout()が呼ばれます。</p>
  <div class="fe-delegation-demo__controls">
    <button type="button" data-delegation-prev>戻る</button>
    <button type="button" data-delegation-next>次へ</button>
    <button type="button" data-delegation-reset>最初から</button>
    <span data-delegation-progress>1 / 4</span>
  </div>
  <p class="fe-delegation-demo__hint">見るポイント：呼び出す側と、実際に決済を実行する側は別のオブジェクトです。「戻り値」がどこへ戻るかにも注目しましょう。</p>
</div>

<script src="{{ '/assets/js/fe-delegation-demo.js' | relative_url }}" defer></script>

この図では、**依頼する側と、処理を実行する側が交代する**様子を確認できます。ボタンが使えない場合でも、4行を上から読むと同じ処理順序です。

## 科目Aでどう出る？

科目Aでは、オブジェクト指向の用語を**何が起きているか**で見分けます。

| 説明にある働き | 判断する概念 |
|---|---|
| 受け取った操作の処理を他のオブジェクトへ任せる | **委譲** |
| あるオブジェクトへの操作が、関係する他のオブジェクトにも伝わる | 伝搬（プロパゲーション） |
| 下位クラスが上位クラスの属性や処理を引き継ぐ | [継承](/fe/inheritance/) |
| 複数のオブジェクトを部分として組み合わせる | 合成（コンポジション） |

「別のオブジェクト」という言葉だけでは、委譲と合成を区別できません。

**処理を任せる話か、部品として組み合わせる話か**を確かめます。

### 迷ったときの確認問題

ある`Order`オブジェクトが`checkout()`を受け付け、その処理の一部で別の`PaymentProcessor`オブジェクトの`pay()`を呼び出している。この処理の分担を表す用語はどれか。

- ア．継承
- イ．委譲
- ウ．オーバーライド
- エ．カプセル化

<details markdown="1">
<summary>▶ 答えと理由を確認する</summary>

**正解：イ（委譲）**

`Order`が決済の処理を`PaymentProcessor`へ任せています。上位・下位クラスの関係はないので継承ではありません。メソッドの再定義もしていないためオーバーライドでもありません。

</details>

## 科目Bでどう使う？

科目Bでメソッド呼び出しが続く処理を読むときは、**現在実行中のメソッドと、戻り先**を分けて追います。

先ほどのPython例では、次の順です。

| 順序 | 実行している場所 | 注目する処理 |
|---:|---|---|
| 1 | `Order.checkout()` | 「注文確定」を表示 |
| 2 | `Order.checkout()` | `self.processor.pay(amount)`を呼び出す |
| 3 | `PaymentProcessor.pay()` | 「決済処理」を表示して「支払完了」を返す |
| 4 | `Order.checkout()` | 戻り値を`result`に代入し、「決済結果を受信」を表示 |
| 5 | 呼出元 | `Order.checkout()`の戻り値を表示 |

**別オブジェクトのメソッドへ移動しても、呼び出し元の処理が消えるわけではありません。** 呼び出したメソッドが戻ったら、その次の行から再開します。

FE科目Bのトレースでは、この「呼ぶ → 別のメソッドで処理 → 戻る」を意識すると読み間違いを減らせます。

## よくある誤解・混同

### 委譲と継承は同じ？

違います。

~~~text
継承：親クラスの定義を子クラスが引き継ぐ
委譲：別オブジェクトのメソッドに処理を任せる
~~~

Pythonのコードでも、`class Order(PaymentProcessor)`のような親クラス指定はありません。`Order`は別のオブジェクトの`pay()`を呼んでいます。

### 委譲と合成は同じ？

同じではありません。

- **合成**：全体と部分の強い所有関係（UMLではコンポジション）
- **委譲**：あるオブジェクトが別のオブジェクトへ処理を任せること

部品として持っているオブジェクトに処理を委譲する設計は可能です。しかし**参照を持っているだけで、必ずUMLの合成になるわけではありません**。クラス間の構造は[UMLクラス図](/fe/uml-class-diagram/)と区別して考えます。

### 委譲と伝搬は同じ？

違います。

~~~text
委譲：依頼された処理を別オブジェクトに任せる
伝搬：操作や通知が関係するオブジェクトに伝わっていく
~~~

「**任せる**」か「**伝わる**」かを判断の手掛かりにします。

### メソッド呼び出しがあればすべて委譲？

単に別のメソッドを呼んだだけでは、委譲と断定できません。元のオブジェクトが担当する仕事を、別のオブジェクトへ**任せて処理させているか**が重要です。

## まとめ（試験直前用）

- **委譲**は、受け取った仕事の一部を別オブジェクトへ任せる仕組み
- **継承＝引き継ぐ、委譲＝任せる**
- **合成＝部品を組み合わせる、委譲＝処理を依頼する**
- 科目Bでは、呼出先のメソッドから**呼出元へ戻る位置**を追う
- 「別オブジェクトに処理を任せる」という表現を決め手にする

{% include fe_article_footer.html %}
