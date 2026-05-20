# SG Content Rules

This file is written in English for Codex readability. However, SG article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules when creating or editing Information Security Management Examination (SG試験) articles under `pages/sg`.

Always check the related rule files as needed:

- Normal article structure: `docs/agent/sg-article-template.md`
- Front matter: `docs/agent/sg-frontmatter-rules.md`
- Tags: `docs/agent/sg-tag-rules.md`
- Past questions, examples, and confirmation questions: `docs/agent/sg-example-question-rules.md`
- Series summary pages: `docs/agent/sg-series-summary-rules.md`

## Basic Stance

- Write in beginner-friendly Japanese.
- Avoid formulas unless they are truly necessary.
- Explain concepts so that judgment criteria remain, not so that readers only memorize terms.
- Explain why an answer choice is wrong when relevant.
- Keep one normal article focused on one term or one concept.
- Make each article understandable as a standalone page.
- Write the title, `description`, and body with future links from index pages and category pages in mind.
- Match the structure, granularity, and wording style of existing `pages/sg` articles.

## SG Exam Explanation Policy

SG articles should prioritize exam decision criteria for eliminating choices over exhaustive explanations of technologies or systems.

- Write as study content for the Information Security Management Examination (SG試験).
- Make the judgment axes tested in the exam clear, rather than deeply covering every technical or legal detail.
- Explain concepts in the context of workplace decisions, operations, risk response, education, vendor management, and practical security management.
- For laws and standards, focus on what the rule protects and how it is used, not on memorizing minor clauses.
- Bridge basic SG knowledge from 科目A and case-question judgment from 科目B.

Use article-facing Japanese phrases like these naturally when they fit:

- `SG試験では〜と問われることが多い`
- `選択肢では〜と書かれていたら注意`
- `〜と〜を混同させてくる`
- `判断するときは、〜を見る`

Do not force unnatural SEO phrases or repeated boilerplate into the body.

## Confusion Prevention

Normal articles must include at least one of the following in the body:

- Differences from similar terms.
- Common misunderstandings.
- Typical SG exam traps.
- Criteria for eliminating answer choices.
- Points that may look correct in practice but are easy to treat as wrong in the exam context.

In particular, `## よくある誤解・混同` should help readers judge that a specific expression is wrong.

## Official And Reference Links

For SG articles, add at least one official link when reliable official information exists for the term.

Preferred source examples:

- IPA
- NISC
- JPCERT/CC
- CRYPTREC
- 個人情報保護委員会
- e-Gov法令検索
- Official information related to JIS / ISO / IEC

Link placement rules:

- Place official links naturally in `## 定義・仕組み` or `## どんな場面で使う？`.
- In SG articles, place official/reference links in a dedicated `## 公式情報・参考リンク` section near the end of the article, just before the footer include, unless an inline citation is clearly more natural.
- Do not turn the article into a link collection.
- Keep the main role of the article as SG exam study explanation.
- If no reliable official source can be confirmed, do not force a link.
- Use normal Markdown syntax for external links.
- When you add official links, verify that each destination URL actually exists if the current environment allows it (for example, by opening it or checking HTTP response status).
- If verification fails because of an environment/network error such as `CONNECT tunnel failed, response 403`, do not treat it as a broken link. Report it as "not verifiable in the Codex environment" and keep the link only when it is clearly an official, theme-direct URL.
- Prefer a theme-direct official page over a broad top page whenever possible (for example, an incident-response page rather than an organization home page).
- If a link is not clearly official or theme-direct and cannot be verified, do not add it to the article body; report it as an unverified candidate instead.

Example:

```md
公式な出題範囲は、IPAの[情報セキュリティマネジメント試験の試験内容](https://www.ipa.go.jp/shiken/kubun/sg/outline.html)でも確認できます。
```


## SG Markdown Rendering Rules

When creating or editing SG articles under `pages/sg`, always ensure that Markdown renders correctly on GitHub Pages.

### Markdown spacing

Always insert blank lines:

- before and after headings
- before and after tables
- before and after lists
- before and after horizontal rules (`---` or `* * *`)
- before and after collapsible question blocks such as `<details markdown="1">`

Do not place headings, lists, tables, or horizontal rules immediately after normal text without a blank line.

### Internal links

- Do not leave internal URLs as code text, such as `` `/sg/authorization/` ``.
- When referencing another SG article, always use a clickable Markdown link.
- Use the target article title as link text when possible.
- If the exact title is unknown, use a clear natural Japanese label.

### Tables

- Markdown tables must include a header separator row (for example `|---|---|`).
- Keep blank lines before and after every table.
- Avoid pseudo-table plain text that relies only on spaces.

### Final self-check before saving

Before saving any SG article, check the following:

- front matter is valid multi-line YAML (`---` start and end)
- `description` and `tags` are not visible in the article body
- internal SG links are clickable Markdown links
- tables have separator rows
- confirmation-question choices are one per line
- each explanation includes a short reason
- headings, lists, tables, and horizontal rules have blank lines around them

### Optional quick checks

Use simple checks only as hints, and always review context manually:

```bash
rg -n "`/sg/" pages/sg
rg -n "ア\..*イ\..*ウ\..*エ\." pages/sg
```

Do not fix articles by blind global replacement.

## Procedure For Creating A New SG Article

1. Identify the term or concept to turn into an article from the user's request.
2. Check whether the same article, a closely related article, or a summary article already exists under `pages/sg`.
3. If an existing article is more appropriate, update or improve that article instead of creating a new one.
4. If creating a new article, choose an English slug that matches the `permalink`.
5. Create `pages/sg/英語スラッグ.md`.
6. Write front matter in the standard format.
7. Write the body with the fixed six-heading structure.
8. For terms that need official links, confirm and add reliable official information.
9. Add `{% include sg_article_footer.html %}` at the end.
10. Confirm that the Markdown is not broken.
11. Confirm that `tags` has roughly 3-5 values and includes both `sg` and one primary category tag.
12. Confirm that `last_modified_at` is present.
13. Confirm that the article does not feel inconsistent with existing articles in granularity or wording.

## Procedure For Editing An Existing SG Article

1. Read the target article.
2. Check articles on nearby themes.
3. Preserve the existing article role while aligning it with the SG standard six-heading structure where appropriate.
4. If there is an attached question or a likely user misunderstanding, strengthen `## よくある誤解・混同`.
5. Add an official link in a natural place when a reliable source is available.
6. Check front matter `description`, `tags`, and `last_modified_at`.
7. Update `last_modified_at` when the article body was meaningfully changed.
8. Briefly explain the changes in the final response.

## Cautions

- Do not put work notes or Codex-facing comments into article content.
- Do not add unnecessary related-article sections to article bodies.
- Do not guess `prev` / `next`.
- Do not convert `tags` into a string.
- Do not add a blank line before front matter.
- Do not invent URLs when an official link cannot be found.
- Do not create articles that directly quote past exam images.
- Do not casually create a new article that duplicates an existing article.

## Final Report

When editing SG articles or SG rules, briefly report:

- Files created or updated.
- Main rules reflected.
- Points checked.
- Whether front matter, `tags`, `description`, six-heading structure, footer, and official links were checked.
