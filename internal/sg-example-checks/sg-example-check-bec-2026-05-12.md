# SG例題対応チェック（BEC）

対象例題: 「BEC (Business E-mail Compromise) に該当するものはどれか」

## 論点メモ
- BECの定義（取引先・経営者等へのなりすまし、送金・情報詐取）
- 誤答候補の切り分け
  - 送信先不達を悪用したブラックリスト登録（Backscatter/NDR悪用系）
  - 第三者中継（Open Relay）
  - 誹謗中傷メール（レピュテーション毀損）
- 近縁語との比較
  - フィッシング
  - 標的型攻撃メール
  - メールアカウント乗っ取り（BECの実行手段になり得る）

## 既存記事カバレッジ確認

### 十分
- `pages/sg/business-email-compromise.md`
  - BEC定義、手口、対策、フィッシング/標的型攻撃との違いが整理済み。
  - SG試験での誤答選択肢の切り方（確認省略、差出人盲信など）まで言及あり。

- `pages/sg/third-party-mail-relay.md`
  - 例題誤答候補の「第三者中継」を切るための説明が十分。

- `pages/sg/email-account-compromise.md`
  - 「差出人が本物でも安全とは限らない」点を説明。BECとの関係を補完。

- `pages/sg/targeted-attack-email.md`
  - BECとの混同に対する比較表あり。

### 追記余地（軽微）
- `pages/sg/business-email-compromise.md`
  - 例題で出やすい誤答「第三者中継」「スパム大量送信」「誹謗中傷メール」との一行比較を足すと、選択肢を切る速度が上がる。

## 判定
- 第一判定: 既存記事で十分
- 改善提案: 既存記事に軽微な追記推奨（任意）

