# AGENTS.md

This file documents working conventions for AI coding agents and collaborators modifying this repository.

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

## Build And Runtime Constraints

Local builds and GitHub Actions do not run on the same stack. Always treat GitHub Pages compatibility as the final source of truth.

### Local environment

Local validation may run against a newer Jekyll toolchain and can succeed even when GitHub Pages later fails.

### GitHub Actions / GitHub Pages environment

From a real failed GitHub Actions run on April 12, 2026, the Pages build stack included:

- `github-pages v232`
- `jekyll v3.10.0`
- `liquid 4.0.4`
- Theme base: `jekyll-theme-primer-0.6.0`
- Remote theme in site config: `pages-themes/cayman@v0.2.0`
- Action used: `actions/jekyll-build-pages@v1`

This version gap matters. Newer Liquid or Jekyll syntax may work locally and still fail on GitHub Pages.

## GitHub Actions Compatibility Rules

Prefer the following when editing Liquid templates, includes, and layouts:

- Favor basic `{% if %}`, `{% for %}`, `{% assign %}`, `{% capture %}`, `where`, `sort`, and simple `contains`.
- Be conservative with `where_exp`.
- Do not assume complex boolean expressions are safe in older Liquid parsers.
- Avoid parenthesized expressions in Liquid conditions.
- Avoid depending on newer parser behavior unless verified in GitHub Actions.
- When choosing between concise and compatible Liquid, choose compatible Liquid.

### Known failure case

The include `_includes/gk_article_footer.html` previously failed in GitHub Actions with:

`Liquid syntax error (_includes/gk_article_footer.html line 41): Expected end_of_string but found id`

The failing code used:

```liquid
{% assign section_pages = site.pages | where_exp: "p", "p.tags contains 'gk' and p.gk_section == page.gk_section and p.gk_order" | sort: "gk_order" %}
```

This was accepted locally, but failed on GitHub Pages under `jekyll 3.10.0 / liquid 4.0.4`.

### Preferred workaround pattern

If filtered expressions become fragile, replace them with explicit iteration and simple comparisons. For example:

- loop through `site.pages`
- guard with `if section_page.tags`
- compare `section_page.gk_section == page.gk_section`
- cast numeric front matter with `| plus: 0` when comparing orders
- track best previous / next candidates with assigned variables

This is less elegant, but much more stable on GitHub Pages.

## Validation Workflow

After changing layouts, includes, front matter structure, navigation logic, or page indexes:

1. Run a local Jekyll build if possible.
2. If local build and GitHub Pages behavior may differ, explicitly assume GitHub Actions is the real check.
3. Review Actions logs for:
   - `Liquid Exception`
   - `Liquid syntax error`
   - `in _includes/...`
   - `in _layouts/...`
   - `in pages/...`
4. Distinguish build-breaking errors from non-blocking warnings.

### Warnings vs errors

These are important but not necessarily build failures:

- Sass `@import` deprecation warnings
- remote theme deprecation noise

These should be treated as actual blockers:

- `Liquid Exception`
- `Liquid syntax error`
- page rendering failures
- include or layout parsing failures

## Deployment Automation

This repository also uses GitHub Actions for post-deploy automation related to search indexing.

### IndexNow

- The IndexNow key file is stored at the repository root as a plain text file and must remain publicly accessible after GitHub Pages deploys.
- The current key file is `f0977966c6644641ae35df01652658c4.txt`.
- The file contents must exactly match the filename stem.
- Do not move the key file into `_includes`, `assets`, `pages`, or any non-root directory.
- Do not add front matter to the key file.

### IndexNow workflow behavior

- IndexNow submission is designed to run after GitHub Pages deployment succeeds, not before.
- Prefer post-deploy submission over push-time submission so the submitted URLs are already live when search engines fetch them.
- If editing `.github/workflows/indexnow.yml`, preserve the post-deploy trigger behavior unless there is a strong reason to change it.
- If editing `scripts/submit_indexnow.py`, prefer standard-library Python and keep the script runnable in GitHub Actions without extra package installs.

### IndexNow failure handling

- A `403` response containing `SiteVerificationNotCompleted` is a retryable verification state, not necessarily a broken configuration.
- Do not treat that specific response as proof that the key file is invalid unless the public key URL has also been checked.
- A successful submission currently returns `IndexNow response: 200` in the workflow logs.

### IndexNow maintenance guidance

- Favor simple, debuggable URL collection logic over aggressive optimization.
- If choosing between full-site submission and a more fragile differential approach, prefer the more reliable option unless rate, scale, or workflow cost becomes a real problem.
- When changing site URL structure, permalink logic, or root verification files, review the IndexNow workflow and submission script together.

## Layout And Theme Consistency

The repository contains multiple study themes under `pages/`. Changes should be made with cross-theme consistency in mind.

### General policy

- Do not let one section evolve into a completely different information architecture unless requested.
- Reuse shared layout patterns where practical.
- Similar concepts across themes should use similar page structure, footer logic, and navigation behavior.
- When introducing a new include for one theme, consider whether DS, GK, and SG should eventually follow the same pattern.

### Current theme directories

- `pages/ds`
- `pages/gk`
- `pages/sg`

### Current shared layout assets

- `_layouts/page.html`
- `_layouts/post.html`
- `_includes/gk_article_footer.html`
- `_includes/sg_article_footer.html`
- `_includes/gk_section.html`
- `_includes/gk_section_tree.html`
- `_includes/gk_collect_urls.html`
- `_includes/ds_section.html`

### Expectations for future edits

- Keep shared page behavior conceptually aligned across themes.
- Navigation should be predictable and not reinvented independently for each theme.
- Footer components should remain readable, robust, and easy to debug.
- If theme-specific logic is necessary, isolate it in includes rather than scattering logic across many pages.
- Prefer data-driven or front-matter-driven organization over repeated hardcoded HTML when it does not reduce compatibility.

## Front Matter Conventions

Many pages depend on front matter for navigation and grouping. Be careful when editing:

- `layout`
- `title`
- `description`
- `permalink`
- `tags`
- theme-specific ordering fields such as `gk_section` and `gk_order`
- navigation fields such as `prev` and `next`

### Rules

- Keep ordering fields numeric when used for comparisons.
- Keep tags consistent and lowercase unless an existing convention requires otherwise.
- Do not rename or remove front matter keys that includes depend on without updating those includes.
- When adding a new content series, define ordering and grouping conventions early.

## Encoding And Text Handling

This repository contains Japanese content. Preserve readable Japanese text.

- Prefer UTF-8 when editing files.
- Avoid introducing mojibake.
- If terminal output looks garbled, verify the file contents before assuming the file itself is broken.
- Be especially careful when editing includes and layouts that contain Japanese labels.

## Editing Strategy

When fixing site issues:

1. Reproduce the issue from logs or local build.
2. Identify whether the problem is content, front matter, include logic, layout logic, or GitHub Pages version compatibility.
3. Make the smallest robust fix first.
4. Rebuild locally when possible.
5. Treat GitHub Actions confirmation as final for Pages compatibility.

## Commit Guidance

Prefer small, focused commits with messages that explain the intent clearly.

Examples:

- `Fix GitHub Pages Liquid compatibility in GK footer`
- `Stabilize SG index Liquid conditions for older Jekyll`
- `Unify theme footer navigation behavior`

## Communication Preferences For Future AI Edits

When assisting with this repository:

- Explain build failures using the actual failing file and line when available.
- Mention when a fix is specifically for GitHub Pages compatibility rather than for local Jekyll.
- Prefer concise Japanese explanations unless the user switches language.
- If there is a tradeoff between cleaner code and older GitHub Pages compatibility, call that out explicitly.

## Recommended Ongoing Maintenance

This file is intended to evolve. Good future additions include:

- a short map of how each theme is organized
- a list of safe Liquid patterns
- a list of known unsafe patterns on GitHub Pages
- content style rules per theme
- release / deploy checklist items
