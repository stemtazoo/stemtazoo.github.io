# UML多重度：CSS・JavaScript追加の試行（2026-10-30）

## 選定の根拠と役割

- 分析元は `stemtazoo/study-site-analytics`（依頼中のstudy-site-analysisに相当する既存リポジトリ）。固定コミット `3ace2460f61dbab680e01503d919206e6384ad9f`。
- `reports/recent-page-content-review-2026-10-24.md`：/fe/uml-multiplicity/のGSC 3Mは12クリック/193表示、7Dは10クリック/137表示。期間は重なり、前週比や改善効果とは解釈しない。記事は十分なので維持という従来判断を尊重し、本文の主張を改めず操作例を補う。
- 10/29のBingレポートでも継続観測候補。/ds/sql-ddl-dml/は検索意図の確認待ち、/ds/variance-standard-deviation/は既に操作図があり、今回は対象外。CSMA/CDは処理のモデル化が必要になるため、単純な対応件数で確認できるUMLを小さな試行に選んだ。
- サイト基準版 `9ef7e38613cee0953475537ea3c8d8abe22cd76d`。4分野の多重度検索と、FEクラス図・ER多重度、DS/SG ER図の役割を比較。UMLの「反対側を1個に固定して読む」目的を保ち、新記事は作らない。
- 監査main `8ca213bda77160fa8ad11d094d1090a273ab7e75` のFE・横断decisions.jsonにはuml/multiplicityの記録を見つけなかった。台帳なしを根拠に比較を省略していない。
- OMG UML 2.5.1の7.5.3.2（多重度による下限・上限）を照合：https://www.omg.org/spec/UML/2.5.1/PDF 。新しい規範・試験仕様の主張は追加しない。

## 変更とコード確認

注文側の多重度4種、固定する側2種、試す件数0〜3を選ぶと、読む端・説明・許容判定が更新される。顧客側の多重度は1のまま。0〜3は試す例であり、*の上限や全体の総数ではない。リセットは0..*・顧客1人・相手1件へ戻す。

専用のCSS/JSとルート属性に限定した。既存fe-visualizer.js/cssは変更せず、別記事への動作追加もない。操作部はJSが起動するまでhidden、静的な図・読み方は本文に残る。色に加えて「読む」という文字を表示。ラベル付きselect/buttonとrole=statusを使い、44px以上のコントロール、狭い幅での縦配置をCSSに指定した。これらはコード確認であり、実画面のアクセシビリティ認定ではない。

## 実行結果

環境：Node v24.22.1、jsdom 26（ブラウザではないDOM実行環境）、実ファイルのHTML断片とJSを読み込み。`docs/agent/example-checks/uml-multiplicity-demo.cjs`で再現可能。

```bash
npm install --prefix /tmp/uml-dom-check jsdom@26 --no-audit --no-fund
NODE_PATH=/tmp/uml-dom-check/node_modules node docs/agent/example-checks/uml-multiplicity-demo.cjs
node --check assets/js/fe-uml-multiplicity-demo.js
git diff --check
```

| 確認 | 期待・観測 | 結果 |
| --- | --- | --- |
| 多重度4種×方向2種×件数4種 | 32通りすべてで、独立した許容件数一覧と画面に出す判定文が一致 | 合格（DOM実行） |
| 読む端の切替 | 顧客からは注文側、注文からは顧客側に「読む」。強調は常に1箇所 | 合格（DOM実行） |
| 0..1の上限、1..*の下限 | 2件/0件がそれぞれ不許可。逆方向では注文側を変えても顧客側の1を読む | 合格（32通りに含む） |
| リセット・連続リセット | 0..*・customer・1へ復帰、再実行しても同じ | 合格（DOM実行） |
| 同じ部品を2個置いた場合 | 片方を変更してももう片方の初期表示を保持 | 合格（DOM実行） |
| JS未実行の断片 | 操作部hidden、初期の静的説明が存在 | 合格（DOM検査）。実ブラウザのJS無効表示は未確認 |
| JS構文・差分 | node --checkとgit diff --check | 合格 |
| front matter | YAMLを解析し、元date・permalink保持、last_modified_at更新 | 合格 |

## 未確認と公開後の操作

ローカル確認ページへのcloud Chrome接続はERR_CONNECTION_REFUSED。埋込み確認ページのナビゲーションもブラウザのURLポリシーに拒否されたため、回避手段は試していない。したがって**ブラウザ操作・CSS実描画・公開ページ確認は未実施**。jsdomの成功をブラウザ操作済みとは扱わない。

Ruby/BundlerがないためローカルJekyllビルドも未実施。公開後はビルド・配信版を確認し、次を実操作する。

1. 初期0..*で注文0件が許可、1..*へ変更すると不許可、1件へ戻すと許可になる。
2. 0..1で2件が不許可になる。
3. 注文1件から見るへ切り替え、顧客側の1を読むことと、相手0/1/2件の不許可/許可/不許可を確認。
4. リセットで初期説明・図の強調・selectが一致する。
5. デスクトップと375px程度の幅で、読みやすさ、横はみ出し、タップ領域、Tab操作とフォーカスを確認。JS無効で静的説明が残ることも確認。

検索流入・理解度の改善は未測定。選定データは優先度の補助であり、教材の必要性や効果の証明ではない。
