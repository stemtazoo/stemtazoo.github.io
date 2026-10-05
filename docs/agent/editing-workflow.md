# Editing And Verification Workflow

Read for site troubleshooting, content-architecture changes, metadata repairs, or repository updates. Section-specific navigation rules control whether prev/next changes are allowed.

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

For description-writing policy, use `docs/agent/metadata-rules.md`; section-specific field requirements remain in each front-matter guide.

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
