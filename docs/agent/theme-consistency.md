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
- `pages/fe`

## Current Shared Layout Assets

- `_layouts/page.html`
- `_layouts/post.html`
- `_includes/sidebar.html` (desktop)
- `_includes/mobile_study_nav.html` (up to 1023px)
- `_includes/study_breadcrumb.html` (GK/SG/FE; DS uses its own breadcrumb)
- `assets/css/style.scss` (breakpoints and current-section styles)
- `_includes/gk_article_footer.html`
- `_includes/sg_article_footer.html`
- `_includes/gk_section.html`
- `_includes/gk_section_tree.html`
- `_includes/gk_collect_urls.html`
- `_includes/ds_section.html`

## Shared Navigation And Sidebar

The sidebar is a compact route to a reader's next useful page, not a list of every article. The four study entrances (G検定, DS検定, SG試験, FE試験) and site search must remain easy to reach on both desktop and mobile. The desktop sidebar can add a small number of links for the current study section; put article-specific next steps near the article body/footer rather than repeating them on every page.

- Keep the shared entrance links and destinations aligned in `_includes/sidebar.html` and `_includes/mobile_study_nav.html`. The desktop sidebar is hidden at widths up to 1023px, so a link essential to all readers must have an accessible mobile route too. Do not assume the desktop-only sidebar covers mobile readers.
- Use actual `<a href="...">` links (with `relative_url` for local paths). Do not make the only route to an important page depend on search input, a JavaScript-only click, or an invisible desktop-only control. The study index should link onward to its articles.
- Make link text specific enough to identify the destination on its own. Avoid vague labels such as 「こちら」 or 「学習開始」 and avoid unnaturally long or keyword-stuffed labels.
- Keep the current-section highlight (`aria-current="location"`) and the route back to a section index consistent. `study_breadcrumb.html` covers GK/SG/FE; check DS's existing page breadcrumbs before adding another shared breadcrumb.
- Keep common navigation compact. Choose section-wide links for the sidebar; use the relevant index/category or article footer for related topics. There is no fixed ideal number of links: revise the list based on whether readers can find the next useful page without wading through repeated links.
- These are site navigation and reader-usefulness rules informed by Google's link guidance, not a promise of indexing or ranking. Google's e-commerce site-structure example supports reachable category-to-content links as a general pattern; this blog's exact sidebar design is an editorial choice.

### When editing shared navigation

1. Check the destination and role of each changed link against the corresponding section index and existing pages; keep names consistent (especially DS検定 versus Python/data-analysis routes).
2. Check `_layouts/page.html` and `_layouts/post.html` for where the shared includes render, including pages with `show_sidebar: false`.
3. Check desktop (at least 1024px) and mobile (below 1024px): reach all four sections and search; check current-section styling, section-top route, keyboard focus and link text.
4. Check that relevant articles can be reached by links from their index/category or related articles, without depending on the site search.
5. Build locally when possible, then confirm the GitHub Pages Action after template or CSS changes.

Reference: [Google Search Central: link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable?hl=ja) and [Google Search Central: site structure (e-commerce example)](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure?hl=ja).

## Expectations For Future Edits

- Keep shared page behavior conceptually aligned across themes.
- Navigation should be predictable and not reinvented independently for each theme.
- Footer components should remain readable, robust, and easy to debug.
- If theme-specific logic is necessary, isolate it in includes rather than scattering logic across many pages.
- Prefer data-driven or front-matter-driven organization over repeated hardcoded HTML when it does not reduce compatibility.

## SG Content Consistency

When editing `pages/sg`, keep the article experience aligned with the SG-specific rules in `docs/agent/sg-content-rules.md`.

- Normal SG articles should use the fixed 6-heading structure defined in `docs/agent/sg-article-template.md`.
- Use `_includes/sg_article_footer.html` for related article behavior instead of adding ad hoc related-link sections to article bodies.
- Keep category and summary pages distinct from single-concept articles.
- Do not introduce SG-only navigation or footer patterns that would make later DS/GK alignment harder unless the user explicitly asks for it.

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
