# FE navigation verification — 2026-10-08

- Base: `55a0ba1` (latest main fetched before editing).
- Scope: FE footer, task/memory/CG classification and learning order, overview/detail links; existing articles only.
- Read: AGENTS, rule map, editorial, AI-search, FE content/template/front matter/tags/audit, editing workflow, Pages compatibility, theme consistency and instruction regression.

## Instruction behavior

Same-session review of the FE-2 navigation constraints, not an independent end-to-end example-writing trial:

- Optional `related_articles` uses existing FE permalinks; it does not authorize `prev` / `next`.
- URLs, original publication dates and all existing prev/next values remain unchanged.
- Specified links stay short and purposeful; automatic matching is used only without valid specified destinations.
- No new articles, forced Subject B sections, duplicate consolidation or unrelated theme changes.

## Local checks

- All 748 FE Markdown files parsed as YAML; changed article destinations resolve to FE pages.
- FE footer rendered for all 748 files with Python Liquid: at most five unique FE links; no self links or category-only matches; specified order preserved.
- Seven fixture cases: topic ordering, duplicate/self/missing/non-FE specified URLs, invalid-list fallback, category-only tags, missing tags, automatic cap and specified-list cap.
- FE index rendered with Python Liquid: task, memory and CG sequences ordered correctly; the five audited additions appear exactly once in their classified lists.
- Agent instruction reference checker and its existing unit tests run separately.

Python Liquid is a functional preview, not the GitHub Pages Ruby/Jekyll stack. Ruby and Bundler are unavailable locally; the main-branch Pages Action and published HTML remain the deployment checks. Their final results are reported in the task response.
