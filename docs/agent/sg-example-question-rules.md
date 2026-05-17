# SG Example Question Rules

This file is written in English for Codex readability. However, SG article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules when creating SG articles from past questions, example questions, or screenshots, and when adding confirmation questions inside articles.

## When Turning Past Questions Or Examples Into Articles

- Do not directly quote attached questions or explanations.
- Do not create an article whose main purpose is to explain the answer to that specific question.
- Generalize the material into a teaching article for understanding the term or concept.
- Use the reason the user made a mistake to strengthen common misunderstanding and confusion-prevention sections.
- Always include judgment criteria for eliminating answer choices in the body.

## Pages Where Confirmation Questions May Be Added

Only add confirmation questions to pages that meet all of these conditions:

- The front matter `tags` includes `sg`.
- The page is a normal article that explains one term or one concept.
- The body contains all of these headings:
  - `## まず結論`
  - `## 直感的な説明`
  - `## 定義・仕組み`
  - `## どんな場面で使う？`
  - `## よくある誤解・混同`
  - `## まとめ（試験直前用）`

## Pages Where Confirmation Questions Must Not Be Added

- Index pages, summary pages, comparison pages, list pages, and roadmaps.
- Category top pages, link collections, and pages that cover multiple terms across a theme.
- Pages whose title includes `まとめ`, `一覧`, `比較`, `ロードマップ`, `Index`, `index`, `overview`, `summary`, or `comparison`.
- Pages whose `permalink` includes `overview`, `summary`, `comparison`, or `index`.
- Any page where the classification is uncertain. Prefer maintainability and do not add the question.

## Duplicate Prevention

Do not add a confirmation question if `## 確認問題（SG試験対策）` already exists.

## Placement

Always add the confirmation question immediately before `## まとめ（試験直前用）`.

## Standard Format

```md
## 確認問題（SG試験対策）

次のうち、最も適切なものはどれか。

ア.  
イ.  
ウ.  
エ.  

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：X**

### 解説
- ア：
- イ：
- ウ：
- エ：

👉 判断ポイント  
（1行で、本質的な切り分け基準を書く）

</details>
```

## Question Quality Rules

- Match the SG exam level.
- Do not make the question a simple memorization check; make it require separating answer choices.
- There must be exactly one correct answer.
- Wrong choices should be close but still wrong.
- Avoid obviously disposable choices.
- Use `<details markdown="1">` for collapsible answers.
- Make the `summary` text clearly indicate that it can be clicked.
- Preserve the existing body style, which is beginner-friendly Japanese.

Include at least one of these axes:

- Difference in role.
- Procedure or order.
- Separation of similar terms.
- Sender / receiver.
- Before intrusion / after intrusion.
- Preventive measure / post-incident response.
- Management control / technical control.
