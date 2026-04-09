# GitHub Actions: failed run を再実行する前の確認手順

失敗した run を再実行する前に、次を確認してください。

1. **失敗した run を開く**
2. **`head_sha`（対象コミット）を確認する**
3. `head_sha` が **最新コミットでない** 場合は、`main` に最新を push してから **Re-run jobs** を実行する
4. run 一覧が **dynamic（自動更新）** で古い run を表示している場合は、**最新 run を選び直す**

> ポイント: 古いコミットの run を再実行しても、最新の変更を検証できません。

---

## 画面に出る Node.js 20 警告について

`actions/checkout@v4` の Node.js 20 廃止警告は、2026年4月時点では **warning** であり、
この警告だけで pages build が失敗するわけではありません。

- 失敗の原因は、同じ run の `build` ログ末尾にある **error 行（Liquid Exception など）** を優先して確認する
- 警告対策を先に進める場合は `actions/checkout@v5` など Node.js 24 対応版へ更新する

