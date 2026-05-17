# SG例題対応チェック（HTTP Cookie）

対象例題: 「HTTPのcookieに関する記述のうち，適切なものはどれか」

## 論点メモ
- Cookieの基本動作
  - サーバが `Set-Cookie` で値を発行
  - ブラウザがCookieを保存
  - 以後のリクエストで `Cookie` ヘッダとして送信
- 誤答候補の切り分け
  - 「Webサーバだけに保存」は誤り（ブラウザ側保存が本質）
  - 「ブラウザが全て暗号化して送信」は誤り（暗号化はHTTPS/TLSの役割）
  - 「有効期限をクライアントが設定」は誤り（通常はサーバが属性で指定）
- 近縁語との比較
  - セッションID
  - Webビーコン
  - HTTPS
  - CSRF/XSS（Cookie悪用の文脈）

## 既存記事カバレッジ確認

### 十分
- `pages/sg/web-beacon.md`
  - Cookieが「ブラウザ側に保存される仕組み」であることをWebビーコンとの比較で明示。
- `pages/sg/http-https.md`
  - 「暗号化はHTTPSで行う」軸が整理されており、「ブラウザがCookieだけを特別に暗号化する」という誤答を切れる。
- `pages/sg/session-hijacking.md`
  - Cookie（セッションID）を悪用する攻撃文脈を扱っており、試験での関連知識として有効。

### 不足（今回の例題に対して）
- Cookieを主題にした単独記事（定義、`Set-Cookie`/`Cookie` ヘッダ、属性、誤解整理）がない。
- 「サーバ側設定とブラウザ側保存」の役割分担を一問で切る解説が分散している。

## 判定
- 第一判定: 新規記事作成推奨
- 第二候補: 既存記事（`web-beacon.md`）へ軽微追記

## 推奨対応
- 新規記事案
  - タイトル: `Cookieとは？HTTPヘッダで扱う状態管理の基本【SG試験】`
  - permalink: `/sg/cookie/`
  - tags: `[sg, sg-technology, web, network, authentication]`
  - 追加すべき要点
    - `Set-Cookie`（サーバ→ブラウザ）と`Cookie`（ブラウザ→サーバ）の方向
    - 有効期限、Secure属性、HttpOnly属性、SameSite属性の最小説明
    - 「暗号化はCookie機能ではなくHTTPS」の明確化
    - SG試験の誤答選択肢を切る確認問題（保存場所、暗号化主体、有効期限設定者）

