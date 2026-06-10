# SG Navigation Rules

This file is written in English for Codex readability. However, SG article content and reader-facing navigation labels must be written in Japanese unless the user explicitly requests otherwise.

Use this file when adding, removing, or reorganizing `prev` / `next` navigation for articles under `pages/sg`.

## Purpose

SG pages should guide readers through study paths without forcing every article into one huge linear sequence.

The existing SG footer already displays `page.prev` and `page.next` as attractive previous / next links. Preserve that display style unless the user explicitly asks for a design change. The main editorial task is to decide the learning order.

## Core Policy

- Manage `prev` / `next` by small theme-based series, not by one sitewide order.
- Use summary pages as learning hubs and maps.
- Use normal individual articles as the main linear reading path inside a series.
- Keep category pages and the SG top page responsible for broader sitewide discovery.
- Prefer explicit, stable `permalink` values over filename guesses.
- Do not add navigation only because two pages were created near each other in time.
- Keep GitHub Pages compatibility; do not introduce complex Liquid for navigation unless needed.

## Recommended Site Structure

Use this hierarchy when deciding navigation:

```text
SG top page
  ↓
category page
  ↓
theme summary page
  ↓
individual article 1 → individual article 2 → comparison article → practice/review article
```

Roles:

- SG top page: entry point for the whole SG study area.
- Category page: broad map for a field such as security management, security measures, law, technology, or management.
- Theme summary page: explains the learning path, differences between related terms, and article list for one theme.
- Individual article: explains one term or concept.
- Comparison article: helps readers distinguish confusing terms.
- Practice/review article: reinforces SG exam decision criteria after the reader learns the terms.

## How To Choose A Series Order

Choose order by learning value, not by alphabetical order, filename order, or publish date.

Use this priority order:

1. Overall concept before details.
2. Prerequisite term before dependent term.
3. Workplace or operational flow when the topic is process-oriented.
4. Basic individual terms before comparison articles.
5. Comparison, traps, and practice pages near the end of the series.
6. Summary or review page at the end only when its primary role is final review.

Common patterns:

```text
Overview → basic terms → mechanism → controls/operations → confusing comparisons → practice/review
```

```text
Identify → evaluate → respond → monitor/review
```

```text
Definition → similar terms → exam trap → case-question judgment
```

## Summary Page Navigation Policy

As a rule, do not add `prev` / `next` to newly created theme summary pages.

Instead, summary pages must provide reader guidance inside the body, especially through these sections:

- `## おすすめの学習順序`
- `## 記事一覧`
- a short sentence that tells readers which article to read first

This keeps summary pages as hubs rather than treating them as ordinary articles in the middle of a chain.

Allowed exceptions:

- If the user explicitly wants the current previous / next footer style on a summary page, adding `next` only is acceptable.
- Use this exception sparingly and only when the summary page clearly acts as the start of a series.
- Avoid adding both `prev` and `next` to a summary page unless the page is intentionally a review page at the end of a series.
- When using an exception, document the reason in the PR body or final response.

Preferred exception pattern:

```yaml
next: /sg/first-individual-article/
```

Avoid this for normal hub summaries:

```yaml
prev: /sg/some-previous-topic/
next: /sg/first-individual-article/
```

## Individual Article Navigation Policy

For normal individual articles, `prev` / `next` should connect only articles in the same theme-based series.

Use both `prev` and `next` when the article has neighbors on both sides.
Use only `prev` for the last article in a series.
Use only `next` for the first article only when the first article is not linked from a summary page and the navigation still helps readers.

Do not connect unrelated themes just to avoid an empty `next`.
It is better for a series to end cleanly than to send readers to a weakly related article.

## Series Ending Policy

At the end of a series, choose one of these endings:

1. End with the last individual article and only `prev`.
2. End with a comparison page that consolidates confusing terms.
3. End with a practice or review page.
4. Add a short body link back to the theme summary page or category page when it helps the reader choose the next theme.

Do not force `next` from the last article to a different theme unless the next theme is a deliberate learning-path continuation.

## Maintenance Workflow

Before changing navigation, do this:

1. Search for related SG articles by filename, title, tags, headings, and existing internal links.
2. Confirm each target page's actual `permalink` in front matter.
3. Identify whether each page is a summary, individual article, comparison article, or practice/review article.
4. Decide the primary series for each page.
5. Check whether an existing summary page or category page already describes the learning order.
6. Update the smallest necessary set of `prev` / `next` fields.
7. If the order changes materially, update the theme summary page's `## おすすめの学習順序` or `## 記事一覧`.
8. If a new summary page is created, update the related category page according to `sg-series-summary-rules.md`.
9. Run a build or at least a navigation consistency check when possible.

## Front Matter Rules For `prev` / `next`

Use absolute site paths that match the target page's `permalink`.

Good:

```yaml
prev: /sg/risk-management/
next: /sg/risk-assessment/
```

Avoid:

```yaml
prev: risk-management.md
next: ./risk-assessment
```

Formatting rules:

- Put `prev` and `next` near `permalink` in front matter.
- Do not add trailing spaces after URL values.
- Keep one URL per field.
- Do not point `prev` or `next` to a page that does not exist.
- When updating article body content at the same time, update `last_modified_at` if the page already uses it.
- For navigation-only front matter updates, updating `last_modified_at` is optional; prefer consistency with nearby SG files.

## Consistency Checks

When practical, run a script that checks:

- every `prev` and `next` target exists as a `permalink` or page URL
- reciprocal links are correct inside a series when expected
- no summary page received `prev` / `next` by accident
- no unrelated category jump was introduced
- no target URL contains trailing spaces

A non-reciprocal link can be acceptable at a series boundary or when a summary page uses the `next`-only exception, but it should be intentional.

## Decision Examples

### Good: summary as hub, individual articles as sequence

```text
/sg/vulnerability-management-summary/  (no prev/next; body has recommended order)
/sg/vulnerability-overview/ → /sg/jvn/ → /sg/cvss/ → /sg/vulnerability-scan/
```

### Good: summary starts a series with `next` only

```text
/sg/auth-access-control-summary/ → /sg/identification/ → /sg/authentication/ → /sg/authorization/
```

Use only when the user wants the footer-style start link or when the summary clearly functions as the first stop.

### Good: comparison near the end

```text
/sg/symmetric-key-cryptography/ → /sg/public-key-cryptography/ → /sg/hybrid-cryptography/
```

### Avoid: weak cross-theme jump

```text
/sg/dnssec/ → /sg/copyright-transfer/
```

Do not connect pages only because both need some `next` value.

## PR / Final Response Notes

When a change reorganizes SG navigation, explain:

- which series was affected
- whether summary pages remain hubs or use the `next`-only exception
- which pages gained, lost, or changed `prev` / `next`
- which summary/category pages were updated for learning flow
- what checks were run
