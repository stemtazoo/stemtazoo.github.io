# FE Content Rules

This file is written in English for Codex readability. However, FE article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules when creating or editing 基本情報技術者試験 (FE) articles under `pages/fe`.

Always check the related rule files as needed:

- AI search / grounding-oriented readability: `docs/agent/ai-search-content-rules.md`
- Normal article structure: `docs/agent/fe-article-template.md`
- Front matter: `docs/agent/fe-frontmatter-rules.md`
- Tags: `docs/agent/fe-tag-rules.md`
- GitHub Pages / Liquid compatibility: `docs/agent/github-pages-compat.md`
- Theme and layout consistency: `docs/agent/theme-consistency.md`

## FE Article Scope

- FE articles are placed under `pages/fe/`.
- FE articles must be written in Japanese unless the user explicitly requests otherwise.
- Normal FE articles should focus on one term or one concept per page.
- Explain concepts for beginner learners preparing for the 基本情報技術者試験.
- Prioritize `how to judge in 科目A` and `how to read/use it in 科目B` over broad textbook-style explanations.
- Match the structure, granularity, and wording style of existing `pages/fe` articles.
- Use GitHub Pages-compatible Markdown and simple Liquid.

## Explanation Policy

FE articles should help readers solve exam questions, not merely memorize definitions.

- Start with the practical conclusion a beginner should remember.
- Explain intuition before strict definitions or edge cases.
- For algorithms, data structures, programming, and pseudocode topics, connect the concept to 科目A answer-choice judgment and 科目B trace/reading tasks.
- For law, management, strategy, audit, and service-management topics, explain where the concept appears in workplace or exam scenarios.
- Avoid deep specialist explanations that do not help FE exam judgment.
- Use article-facing Japanese phrases naturally when they fit, such as `科目Aでは〜`, `科目Bでは〜`, `選択肢では〜に注意`, and `〜と〜を混同しない`.

## Official Links

Do not write raw URLs in article bodies.

Bad:

```md
https://www.ipa.go.jp/shiken/kubun/fe.html
```

Good:

```md
[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)
```

For official references:

- Prefer official IPA sources.
- Use the IPA FE exam page as the stable official entry point.
- When possible, explain how the article topic connects to the FE syllabus or official exam scope.
- Do not simply paste the same generic official-link sentence into every article.
- Avoid awkward repeated wording such as `確認できるシラバスで確認できます`.
- Keep official-reference paragraphs short and relevant to the article topic.

Preferred wording examples:

```md
公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。
```

```md
このテーマは、基本情報技術者試験の「アルゴリズムとプログラミング」や「データ構造」と関係が深い内容です。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。
```

For algorithm and data-structure articles:

- Mention the connection to `アルゴリズムとプログラミング`.
- Mention `データ構造` when relevant.
- Keep the official-link paragraph short.

## FE Index Listing

The FE index page `/fe/` uses `fe_section`, `fe_subsection`, and `fe_order` to list pages.

When adding new FE articles:

- Make sure the article appears under the intended section on `/fe/`.
- Use `fe_order` spacing such as `10`, `20`, `30`, etc.
- Keep related topics close together.
- Do not omit `fe_section`, `fe_subsection`, or `fe_order` on normal FE articles.

Suggested examples:

| File | `fe_section` | `fe_subsection` | `fe_order` |
|---|---|---|---:|
| `array.md` | `科目B対策` | `データ構造` | `10` |
| `stack.md` | `科目B対策` | `データ構造` | `20` |
| `queue.md` | `科目B対策` | `データ構造` | `30` |
| `linear-search.md` | `科目B対策` | `アルゴリズム` | `40` |
| `binary-search.md` | `科目B対策` | `アルゴリズム` | `50` |

## FE Article Footer

Normal FE articles should end with:

```liquid
{% include fe_article_footer.html %}
```

Rules for `_includes/fe_article_footer.html`:

- Related articles must be limited to pages whose `tags` contain `fe`.
- Do not show DS, SG, or GK articles in FE related articles.
- When matching related articles, ignore the base tag `fe` itself and match using concrete tags such as `algorithm` or `data-structure`.
- Keep the `基本情報技術者トップに戻る` link.
- Do not break the Jekyll build if there are no related articles.
- The related-article filter should include an FE guard such as `{% raw %}{% if p.tags contains "fe" %}{% endraw %}`.

## Markdown Rendering Rules

When creating or editing FE articles under `pages/fe`, keep Markdown safe for GitHub Pages.

- Insert blank lines before and after headings, lists, tables, code fences, and horizontal rules.
- Markdown tables must include a header separator row.
- Official links and internal links must be clickable Markdown links, not raw plain-text URLs.
- Do not duplicate `prev` / `next` as visible body text.
- Do not allow front matter keys such as `description`, `tags`, `fe_section`, `fe_subsection`, or `fe_order` to leak into the article body.

## Build And Display Checks

After creating or editing FE articles or FE includes:

- Run the Jekyll build if possible.
- Confirm that the build passes.
- Confirm that `/fe/` lists the new articles.
- Confirm that FE article related links do not include DS / SG / GK pages.
- Confirm that official links render as clickable Markdown links.

## Final Self-Check Before Saving

Before saving an FE article, check that:

- the body is Japanese unless the user explicitly requested another language;
- the article has a clear role compared with similar FE and cross-theme pages;
- the article focuses on one term or one concept;
- 科目A judgment and 科目B reading/use are addressed when relevant;
- official links are Markdown links and are not generic copy-paste boilerplate;
- `fe_section`, `fe_subsection`, and `fe_order` are present for normal FE articles;
- the footer include is present on normal FE articles;
- front matter is valid YAML and metadata is not visible in the body.
