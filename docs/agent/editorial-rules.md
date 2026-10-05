# Sitewide Editorial Rules

Read this file before creating or meaningfully editing study content, reviewing overlap, or changing learning paths. This is the canonical home for new-article decisions, duplicate handling, editorial roles, reader usefulness, and learning paths.

## Sitewide Editorial Governance

This site should be managed as a coherent study site, not just as a set of independent Markdown articles.
Use these as review perspectives within the task, not as a requirement to spawn separate agents:

- Editor-in-Chief: manage the overall direction of the site, decide whether a request belongs as a new article, an update, a comparison article, a summary article, a category/index improvement, or internal-link work, and check whether pages overlap in role, search intent, or learning purpose.
- SEO / AI Search Editor: review `title`, `description`, `permalink`, `tags`, and internal links so search engines and AI search systems can identify the preferred or representative page for each topic.
- Learning Design Editor: maintain clear learning paths for `pages/sg`, `pages/ds`, `pages/gk`, and `pages/fe`, and separate the roles of individual articles, comparison articles, summary articles, category pages, and index pages.
- Article Writer: write with the same structure, granularity, and wording style as existing pages; for SG content, prioritize exam judgment criteria used to eliminate incorrect choices; for DS content, prioritize practical Python and data-analysis explanations for beginners; for GK content, prioritize conceptual understanding, confusion prevention, and exam-focused review; for FE content, prioritize 科目A judgment and 科目B reading/use for beginner learners.
- Copy Editor: check wording consistency, terminology, headings, explanation depth, Japanese readability, front matter consistency, and UTF-8 Japanese text.
- Site Operations Editor: maintain category pages, index pages, related links, and `prev` / `next` navigation when appropriate, while keeping GitHub Pages compatibility as a top priority.
- Site Quality / AdSense Readiness Editor: ensure pages are useful, original, trustworthy, and easy to navigate, and avoid thin content, copied content, or unnecessary duplication.

Before creating or editing content, agents must consider:

- where the page belongs in the site
- how it relates to existing pages
- whether the request should be handled as a new article, an existing article update, a comparison article, a summary article, a category/index improvement, or internal-link improvement
- whether the change improves the learning flow for readers
- whether related category pages, index pages, internal links, or `prev` / `next` navigation should also be updated
- whether the change preserves the existing editorial style for `pages/sg`, `pages/ds`, `pages/gk`, and `pages/fe`

Do not optimize only one page in isolation when the change affects site structure.

## New Article Decision Workflow

Before creating a new article, agents must check for similar existing content under:

- `pages/sg`
- `pages/ds`
- `pages/gk`
- `pages/fe`

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

For study content, prefer **one clear learning purpose per article** over mechanically enforcing one keyword or one term per page. The key audit question is:

> Can the reason for reading each overlapping page be explained in one sentence?

Pages about the same term may remain separate when they teach materially different judgments, comparisons, mechanisms, or learning steps. Conversely, pages with different titles or URLs should be considered for consolidation when their learning purpose is effectively the same.

Agents must also watch for near-duplicate pages where the following are too similar:

- search intent
- article role
- headings
- explanations
- metadata
- target reader
- category placement

When duplicate or near-duplicate content is found, evaluate it in this order:

1. Compare the actual content and overlap.
2. Identify the learning purpose of each page.
3. When available, use search performance and AI citation / grounding data only as supporting evidence, not as an automatic deletion rule.
4. Check whether a page has a distinct role in another exam area or learning path.
5. Consolidate only when the learning purposes are genuinely redundant.

Low traffic alone is not a reason to delete or merge a useful learning page. When consolidation is appropriate, prefer the page with the clearer current learning role and preserve useful material from the other page. If an old URL may already be used or indexed, preserve a safe path to the preferred page using redirect, canonical, sitemap exclusion, and `noindex,follow` handling when compatible with the site.

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

- whether the page follows the shared AI search / grounding-oriented readability rules in `docs/agent/ai-search-content-rules.md`
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
- Can readers reach the answer-choice judgment criteria early enough to use them before reading the full explanation?

For study articles, do not require a dedicated heading such as `先に判断基準` on every page. If the judgment criteria already appear clearly near the beginning, leave the structure as-is. If useful criteria exist only in later sections such as traps, misconceptions, or the final summary, consider surfacing a short version near `まず結論` without duplicating or padding the article.

### Learning Path Guidance

For study articles that act as an entry point, overview, basics page, or summary, check whether readers can tell what to study next and why.

- Prefer a learning path expressed as **reader need or question → next article**, rather than a bare list of related links.
- Make the reason for the next step clear, such as moving from a basic concept to a comparison, mechanism, failure pattern, or deeper method.
- Add a short section such as `次に読むなら` only when the learning path is otherwise unclear.
- Do not add the section mechanically to every article.
- If the page already provides a clear learning map, role-based related links, or an equivalent path in the body, leave it as-is.
- Avoid duplicating the generic related-articles block. The purpose is to explain **why the reader should continue to a specific page**, not merely to increase internal links.

Apply this across SG, FE, DS, and GK while preserving each area’s existing structure and wording style.

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
