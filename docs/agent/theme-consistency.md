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

## Responsive article comparison tables

Apply across FE, GK, DS and SG when a prose comparison is difficult to read on a narrow phone; do not convert all tables automatically.

- Two concepts compared across several criteria: use the opt-in `study-comparison study-comparison--pair` classes on one semantic HTML table. At 640px and below, each criterion becomes a card with two equal-width cells; at 641px and above retain the normal table.
- Use one source of truth for the explanations, not separate desktop/mobile copies. Preserve row and column headers, explicit roles when CSS changes table display, unique header IDs and matching `headers` references. Each cell contains a real `<span class="study-comparison__label" aria-hidden="true">…</span>` matching its column header; it is visible on mobile and hidden on desktop. Color must not be the only distinction.
- Keep normal font size, allow wrapping, use blue and teal for the two columns where compatible with the article image, and leave at least 16px after the mobile comparison. Do not shrink text to force it to fit.
- For Japanese prose in mobile cards, use strict line breaking and normal word breaking, with emergency wrapping for long tokens. Verify punctuation does not stand alone at the beginning of a line; check long English labels and SQL tokens at the same widths. Use dark inline-code text on a light background, targeting at least 4.5:1 contrast. These rules are scoped to opt-in mobile comparison cards.
- For a term and its explanation, consider a stacked label/value card. For three or more concepts, consider stacked labeled values after checking readability; the pair class is only for exactly one row header plus two data cells. For numerical matrices, timing charts, calculation tables or data whose row/column alignment matters, retain table structure and intentional scrolling as needed. The pair class does not implement these other patterns.
- Use shared CSS in `assets/css/style.scss`; avoid per-article copies for the supported pair pattern. Do not change unrelated tables, interactive controls or OGP assets. Remove adjacent summaries only when their meaning is fully retained elsewhere.
- Check 320–390px viewport widths (including about 340px article width when possible), 640/641px boundary, desktop, CSS-disabled readability, header associations and screen-reader behavior; verify no page or card overflow, wrapping and following-block spacing. Record source checks separately from browser, assistive-technology and Pages build results.
- Pilot evidence: [RISC/CISC](/fe/risc-cisc/) (PR #883, user Android screenshots on 2026-11-24) showed all five comparisons side by side with readable wrapping and no visible clipping; image colors were consistent. The shared-class migration and desktop/accessibility checks are separate from that evidence. The 2026-11-25 Android screenshots for CSMA/CD vs CSMA/CA, Contrastive Loss vs Cross Entropy Loss, DDL vs DML, and encryption vs hash showed readable side-by-side cards and no visible clipping. The GK screenshot showed a standalone comma and DS code appeared faint. These are pre-polish observations, not evidence of the subsequent CSS fix. See the [audit record](https://github.com/stemtazoo/study-site-audit/blob/main/projects/stemtazoo/ui-comparison-2026-11-25/README.md) after its PR is merged. On 2026-11-25 the user reported good post-polish mobile results; a second wave (PR #897) added four articles without CSS changes. User Android screenshots showed all comparison rows in stack/queue, regression/classification, symmetric/public-key cryptography, and authoritative/cache DNS with no visible clipping. On 2026-11-26, user Android screenshots for the eight additional articles in PRs #899 and #900 showed good card readability in the captured portions without further CSS changes. Seventeen articles now have mobile observations across all four themes (the initial five include pre-polish screenshots and the user's post-polish report; the first crashing/fast-tracking row was outside the supplied screenshots). See audit PR #85 and the audit record above for detailed evidence. This is not a desktop, screen-reader, or multi-width certification. Adopt the pair pattern as the standard opt-in mobile presentation for suitable two-concept prose comparisons in new and revised articles. Preserve numerical and trace tables. Before another broad rollout, prioritize desktop, 640/641px boundary, narrow-width, CSS-disabled, and assistive-technology checks; record actual results separately from static HTML checks.

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

## SEO Rendering Checks

When editing layouts, includes, page metadata, or shared templates:

- Check the final rendered HTML, not only the Markdown/front matter source.
- Keep one `<h1>` per normal page. Remember that the remote theme or parent layout may already render the page title as `<h1>`.
- When setting `title`, consider the final HTML `<title>` including any site-name suffix added by `jekyll-seo-tag` or the theme. Avoid relying on the front matter title length alone.
- After layout or metadata changes, verify representative rendered pages before assuming the source-level markup is sufficient.

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
