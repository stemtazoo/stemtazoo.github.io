# GitHub Pages / Liquid Compatibility

Local builds and GitHub Actions do not run on the same stack. Always treat GitHub Pages compatibility as the final source of truth.

## Known GitHub Pages Stack

From a real failed GitHub Actions run on April 12, 2026, the Pages build stack included:

- `github-pages v232`
- `jekyll v3.10.0`
- `liquid 4.0.4`
- Theme base: `jekyll-theme-primer-0.6.0`
- Remote theme in site config: `pages-themes/cayman@v0.2.0`
- Action used: `actions/jekyll-build-pages@v1`

This version gap matters. Newer Liquid or Jekyll syntax may work locally and still fail on GitHub Pages.

## Compatibility Rules

Prefer the following when editing Liquid templates, includes, and layouts:

- Favor basic `{% if %}`, `{% for %}`, `{% assign %}`, `{% capture %}`, `where`, `sort`, and simple `contains`.
- Be conservative with `where_exp`.
- Do not assume complex boolean expressions are safe in older Liquid parsers.
- Avoid parenthesized expressions in Liquid conditions.
- Avoid depending on newer parser behavior unless verified in GitHub Actions.
- When choosing between concise and compatible Liquid, choose compatible Liquid.

## Known Failure Case

The include `_includes/gk_article_footer.html` previously failed in GitHub Actions with:

`Liquid syntax error (_includes/gk_article_footer.html line 41): Expected end_of_string but found id`

The failing code used:

```liquid
{% assign section_pages = site.pages | where_exp: "p", "p.tags contains 'gk' and p.gk_section == page.gk_section and p.gk_order" | sort: "gk_order" %}
```

This was accepted locally, but failed on GitHub Pages under `jekyll 3.10.0 / liquid 4.0.4`.

## Preferred Workaround Pattern

If filtered expressions become fragile, replace them with explicit iteration and simple comparisons.

For example:

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

## Warnings Vs Errors

These are important but not necessarily build failures:

- Sass `@import` deprecation warnings
- remote theme deprecation noise

These should be treated as actual blockers:

- `Liquid Exception`
- `Liquid syntax error`
- page rendering failures
- include or layout parsing failures
