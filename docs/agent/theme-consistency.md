# Theme And Layout Consistency

The repository contains multiple study themes under `pages/`. Changes should be made with cross-theme consistency in mind.

## General Policy

- Do not let one section evolve into a completely different information architecture unless requested.
- Reuse shared layout patterns where practical.
- Similar concepts across themes should use similar page structure, footer logic, and navigation behavior.
- When introducing a new include for one theme, consider whether DS, GK, and SG should eventually follow the same pattern.

## Current Theme Directories

- `pages/ds`
- `pages/gk`
- `pages/sg`

## Current Shared Layout Assets

- `_layouts/page.html`
- `_layouts/post.html`
- `_includes/gk_article_footer.html`
- `_includes/sg_article_footer.html`
- `_includes/gk_section.html`
- `_includes/gk_section_tree.html`
- `_includes/gk_collect_urls.html`
- `_includes/ds_section.html`

## Expectations For Future Edits

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

## Front Matter Rules

- Keep ordering fields numeric when used for comparisons.
- Keep tags consistent and lowercase unless an existing convention requires otherwise.
- Do not rename or remove front matter keys that includes depend on without updating those includes.
- When adding a new content series, define ordering and grouping conventions early.
