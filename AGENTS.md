# AGENTS.md

This file is the entry point for AI coding agents and collaborators modifying this repository.
Detailed rules live under `docs/agent/`; read the relevant file before editing related areas.

## Purpose

This repository powers a Jekyll site with multiple content themes under `pages/`, currently including:

- `pages/ds`: Data Science / skill-check style content
- `pages/gk`: G-kentei study content
- `pages/sg`: Security / SG study content

The project goal is not only to publish correct content, but to keep the site buildable on GitHub Pages and visually consistent across themes.

## Core Priorities

When making changes, use this order of priority:

1. Keep GitHub Actions / GitHub Pages builds passing.
2. Preserve or improve content correctness.
3. Maintain layout consistency across themes.
4. Prefer simple, GitHub Pages-compatible Liquid over clever Liquid.
5. Avoid changes that create theme-by-theme drift unless explicitly requested.
6. Maintain coherent sitewide information architecture.
7. Avoid unnecessary duplicate or near-duplicate content.
8. Preserve or improve reader usefulness and original value.
9. Keep navigation clear across themes and category pages.

## Sitewide Editorial Governance

This site should be managed as a coherent study site, not just as a set of independent Markdown articles.
Agents should act like an editorial team for the whole blog operation:

- Editor-in-Chief: manage the overall direction of the site, decide whether a request belongs as a new article, an update, a comparison article, a summary article, a category/index improvement, or internal-link work, and check whether pages overlap in role, search intent, or learning purpose.
- SEO / AI Search Editor: review `title`, `description`, `permalink`, `tags`, and internal links so search engines and AI search systems can identify the preferred or representative page for each topic.
- Learning Design Editor: maintain clear learning paths for `pages/sg`, `pages/ds`, and `pages/gk`, and separate the roles of individual articles, comparison articles, summary articles, category pages, and index pages.
- Article Writer: write with the same structure, granularity, and wording style as existing pages; for SG content, prioritize exam judgment criteria used to eliminate incorrect choices; for DS content, prioritize practical Python and data-analysis explanations for beginners; for GK content, prioritize conceptual understanding, confusion prevention, and exam-focused review.
- Copy Editor: check wording consistency, terminology, headings, explanation depth, Japanese readability, front matter consistency, and UTF-8 Japanese text.
- Site Operations Editor: maintain category pages, index pages, related links, and `prev` / `next` navigation when appropriate, while keeping GitHub Pages compatibility as a top priority.
- Site Quality / AdSense Readiness Editor: ensure pages are useful, original, trustworthy, and easy to navigate, and avoid thin content, copied content, or unnecessary duplication.

Before creating or editing content, agents must consider:

- where the page belongs in the site
- how it relates to existing pages
- whether the request should be handled as a new article, an existing article update, a comparison article, a summary article, a category/index improvement, or internal-link improvement
- whether the change improves the learning flow for readers
- whether related category pages, index pages, internal links, or `prev` / `next` navigation should also be updated
- whether the change preserves the existing editorial style for `pages/sg`, `pages/ds`, and `pages/gk`

Do not optimize only one page in isolation when the change affects site structure.

## New Article Decision Workflow

Before creating a new article, agents must check for similar existing content under:

- `pages/sg`
- `pages/ds`
- `pages/gk`

Use repository search, filenames, front matter, headings, and internal links to identify related pages before creating a new page.

When similar content exists, compare:

- `title`
- `description`
- `permalink`
- `tags`
- headings
- search intent
- article scope
- target reader
- related category pages
- related index pages

Then decide whether the request should be handled as:

1. a new standalone article
2. an update to an existing article
3. a comparison article
4. a summary article
5. a category/index page improvement
6. an internal-link improvement only
7. consolidation or cleanup of old pages

Do not create a new article only because the requested term is slightly different.
Create a new article only when it has a clear role that is different from existing pages.

If a new article is created despite similar existing pages, clearly distinguish its role from related pages and consider adding a section such as:

- `Related articles`
- `Difference from similar terms`
- `How this article differs`
- `Exam trap / confusion point`

For SG content, use Japanese section names consistent with the existing site style.

## Content Portfolio And Duplicate Content Management

Duplicate content does not only mean identical text.
Agents must also watch for near-duplicate pages where the following are too similar:

- search intent
- article role
- headings
- explanations
- metadata
- target reader
- category placement

When duplicate or near-duplicate content is found, agents should consider:

- updating an existing article instead of creating a new one
- clarifying the difference between similar articles
- converting the topic into a comparison article
- converting the topic into a summary article
- improving a category page or index page
- consolidating outdated pages
- adding internal links between related pages
- considering redirect / canonical / noindex-like handling when appropriate for the site structure and compatible with the current Jekyll and GitHub Pages setup

However, this is a study site.
Similar terms are often intentionally separated to help learners compare concepts.
Do not blindly merge pages.
Instead, separate roles clearly:

- Individual articles explain one term or concept deeply.
- Comparison articles help readers distinguish similar terms.
- Summary articles provide quick review points and exam judgment criteria.
- Category pages act as learning paths and indexes.
- Index pages help readers find existing content efficiently.

For summary pages and category pages, avoid copying large parts of individual articles.
Use short explanations, comparison tables, judgment criteria, internal links, and learning paths.

## SEO And AI Search Visibility

Agents should manage the site so that search engines and AI search systems can clearly understand which page is the preferred or representative page for a topic.
Duplicate or near-duplicate pages may not be a penalty by themselves, but they can blur intent signals, dilute clicks, links, impressions, and engagement signals, and cause search engines or AI systems to surface an outdated or unintended URL.

When creating or editing pages, agents should check:

- whether the page has a clear and unique search intent
- whether the `title` and `description` are distinct from similar pages
- whether the `permalink` reflects the page scope
- whether internal links guide readers to the most appropriate page
- whether old or overlapping pages should be updated, consolidated, redirected, or linked
- whether category pages and summary pages act as navigation aids rather than duplicate content
- whether sitemap or IndexNow-related files may be affected by major URL changes
- whether old URLs, archive-like pages, or unintended duplicate URLs may still be discoverable

Do not over-optimize for search engines at the expense of reader usefulness.
The primary goal is a useful, trustworthy, easy-to-navigate study site.

## Site Quality And Reader Usefulness

This site should provide relevant, original, and useful content for readers.

When creating or editing pages, agents should check:

- Does the page provide original value beyond generic explanations?
- Does the page include this site's own study perspective?
- Does the page help readers understand exam judgment criteria?
- Does the page explain common traps and similar-term confusion?
- Is the page easy to navigate from category pages, index pages, related links, and `prev` / `next` links?
- Is the layout readable with clear headings, tables, summaries, and internal links where appropriate?
- Does the page avoid thin content, copied content, or unnecessary duplication?
- If external references are used, are they used as support rather than as the main content?
- Can readers quickly find what they need?

For study articles, original value means:

- beginner-friendly explanations
- exam-focused judgment criteria
- common misunderstanding points
- comparisons with similar terms
- practical examples
- workplace or real-world context where appropriate
- clear review summaries
- useful internal links

Do not optimize only for ads or monetization.
Prioritize reader usefulness, originality, trust, learning flow, and long-term site quality.

## Required References

Read the relevant detailed guide before changing each area:

- GitHub Pages / Liquid compatibility: `docs/agent/github-pages-compat.md`
- IndexNow deployment automation: `docs/agent/indexnow.md`
- Theme and layout consistency: `docs/agent/theme-consistency.md`
- SG article writing policy: `docs/agent/sg-content-rules.md`
- SG article template: `docs/agent/sg-article-template.md`
- SG front matter rules: `docs/agent/sg-frontmatter-rules.md`
- SG tag rules: `docs/agent/sg-tag-rules.md`
- SG example-question and confirmation-question rules: `docs/agent/sg-example-question-rules.md`
- SG series-summary rules: `docs/agent/sg-series-summary-rules.md`
- SG navigation / prev-next rules: `docs/agent/sg-navigation-rules.md`

- SG Markdown rendering safety (must-read before creating or editing SG articles):
  - `docs/agent/sg-article-template.md` (standard article structure and Markdown layout)
  - `docs/agent/sg-content-rules.md` (Markdown spacing, links, tables, rendering checks)
  - `docs/agent/sg-frontmatter-rules.md` (multi-line YAML front matter and metadata leakage prevention)
  - `docs/agent/sg-example-question-rules.md` (choice formatting and explanation quality in confirmation questions)


## SG Article Policy

When creating or editing `pages/sg` articles, write them as study articles for the Information Security Management Examination (SG試験).

### SG記事のAI検索・読者理解向け改善

SG記事を新規作成・改善・横展開する場合は、必要に応じて次のルールを参照すること。

- `project_rules/sg_article_ai_search_improvement.md`

このルールは、AI検索専用の小手先対策ではなく、読者がSG試験で選択肢を切れるようにするための改善ルールである。

特に、通常記事に以下のブロックを追加・調整する場合は、このルールに従うこと。

- このページで切り分けること（先にここだけ）
- SG試験で選択肢を切る判断軸（〇〇編）
- 関連記事との役割分担（混同防止）

ただし、全記事に機械的に追加してはいけない。
対象記事の選定、追加位置、文章量、関連記事リンク、対象外ページの扱いは、上記ルールファイルに従うこと。

- Prioritize the judgment criteria used to eliminate answer choices over deep technical or legal detail.
- Explain concepts in the context of workplace decisions, operations, risk response, education, vendor management, and practical security management.
- For laws and standards, focus on what the rule protects and how it is used, not on memorizing minor clauses.
- Bridge 科目A knowledge and 科目B case-question judgment.
- Match the structure, granularity, and wording style of existing `pages/sg` articles.
- Use GitHub Pages-compatible Markdown and simple Liquid.

## Editing Strategy

When fixing site issues:

1. Reproduce the issue from logs or local build.
2. Identify whether the problem is content, front matter, include logic, layout logic, or GitHub Pages version compatibility.
3. Make the smallest robust fix first.
4. Rebuild locally when possible.
5. Treat GitHub Actions confirmation as final for Pages compatibility.

When fixing or improving content architecture:

1. Identify the affected theme and content area.
2. Search for related or similar existing pages.
3. Decide whether the best fix is a new article, an existing article update, a comparison page, a summary page, a category/index update, or internal-link improvement.
4. Make the smallest robust change that improves both reader usefulness and site structure.
5. Rebuild locally when possible.
6. Treat GitHub Actions confirmation as final for Pages compatibility.

## Front Matter And Encoding

- Preserve readable Japanese text and use UTF-8.
- If terminal output looks garbled, verify file contents before assuming the file itself is broken.
- Be careful when editing `layout`, `title`, `description`, `permalink`, `tags`, theme-specific ordering fields such as `gk_section` / `gk_order`, and navigation fields such as `prev` / `next`.
- Do not rename or remove front matter keys that includes depend on without updating those includes.
- For new or updated articles, keep `title` aligned with the article scope, make `description` specific and distinct from similar pages, keep `permalink` stable and role-appropriate, and choose `tags` that support category and index behavior.
- For article pages where `last_modified_at` is already used for display, update `last_modified_at` in front matter when you modify the article content. Use `YYYY-MM-DD` format (example: `2026-05-06`).
- For newly added articles, always set `last_modified_at` in front matter at creation time to avoid missing update-date metadata.
- Update `prev` / `next` only when it improves the learning flow.
- Layouts may fall back to `page.date` when `last_modified_at` is missing, but this is only a fallback; preferred source is explicit `last_modified_at`.

## Communication Preferences

- Explain build failures using the actual failing file and line when available.
- Mention when a fix is specifically for GitHub Pages compatibility rather than for local Jekyll.
- Prefer concise Japanese explanations unless the user switches language.
- If there is a tradeoff between cleaner code and older GitHub Pages compatibility, call that out explicitly.

## Commit Guidance

Prefer small, focused commits with messages that explain the intent clearly.
When responding to instructions from Visual Studio Code, include a suggested GitHub commit message at the end of the final response.

Examples:

- `Fix GitHub Pages Liquid compatibility in GK footer`
- `Stabilize SG index Liquid conditions for older Jekyll`
- `Unify theme footer navigation behavior`
