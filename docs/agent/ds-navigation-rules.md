# DS Navigation Rules

This file is written in English for Codex readability. However, DS article content and reader-facing navigation labels must be written in Japanese unless the user explicitly requests otherwise.

Use this file when adding, removing, or reorganizing `prev` / `next` navigation for articles under `pages/ds`.

## Purpose

DS pages should guide readers through DS検定 topics and practical data-analysis learning paths without forcing every article into one sitewide sequence.

Existing DS articles may use `prev` / `next` for small related groups, while many pages rely on categories, related-article sections, and indexes. Preserve that mixed convention unless the user explicitly asks for a redesign.

## Core Policy

- Do not guess `prev` / `next`.
- Use `prev` / `next` only for clear, small, theme-based learning sequences.
- Prefer category pages, summary pages, and related-article blocks for broader discovery.
- Confirm actual `permalink` values before adding navigation.
- Do not connect unrelated topics only to avoid an empty `next`.
- Do not duplicate `prev` / `next` as visible body text.
- Keep GitHub Pages compatibility; avoid complex Liquid for navigation unless needed.

## Recommended Learning Order Patterns

Use learning value rather than alphabetical order or publish date.

Common patterns:

```text
Basic concept → related concept → comparison → practical example
```

```text
Intuition → formula/definition → interpretation → common mistakes
```

```text
Data source → preprocessing → analysis method → evaluation → communication
```

```text
SQL basics → filtering/joining → aggregation → common traps
```

## Individual Article Navigation Policy

For normal individual articles, `prev` / `next` should connect only articles in the same coherent topic group.

Use both `prev` and `next` when the page has confirmed neighbors on both sides. Use only `prev` or only `next` at a series boundary when that helps the reader.

Do not add navigation only because pages have similar tags. Similar tags can indicate related articles, but `prev` / `next` should imply a reading order.

## Related Articles vs. `prev` / `next`

Use related-article sections when:

- the pages are useful alternatives but not a strict sequence;
- several similar terms should be compared;
- a reader may branch to statistics, Python, SQL, governance, or AI utilization topics;
- adding `prev` / `next` would imply an order that does not really exist.

Use `prev` / `next` when:

- the pages form a small sequence;
- the order helps beginners learn prerequisites first;
- the target pages' permalinks have been confirmed.

## Front Matter Rules For `prev` / `next`

Use absolute site paths that match the target page's `permalink`.

Good:

```yaml
prev: /ds/correlation-and-causation/
next: /ds/spearman-rank-correlation/
```

Avoid:

```yaml
prev: correlation-and-causation.md
next: ./spearman-rank-correlation
```

Formatting rules:

- Put `prev` and `next` near `permalink` or with other navigation fields in front matter.
- Keep one URL per field.
- Do not point to a page that does not exist.
- When updating article body content at the same time, update `last_modified_at` if the page already uses it.
- For navigation-only front matter updates, updating `last_modified_at` is optional; prefer consistency with nearby DS files.

## Consistency Checks

When practical, check that:

- every `prev` and `next` target exists as a `permalink`;
- the links do not jump to unrelated categories;
- no front matter metadata appears in the visible body;
- related-article sections do not duplicate `prev` / `next` as plain text;
- category and tag conventions still match nearby DS pages.

## PR / Final Response Notes

When a change reorganizes DS navigation, explain:

- which topic group was affected;
- which pages gained, lost, or changed `prev` / `next`;
- whether related-article blocks or category pages were also updated;
- what checks were run.
