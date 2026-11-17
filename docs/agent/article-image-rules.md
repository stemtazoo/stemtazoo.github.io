# Article Images and Responsive Eyecatches

This guide owns **website-side use** of images in FE, GK, DS and SG articles. The image-generation instructions, output filenames and visual correctness review are owned by [blog-instagram-prompts](https://github.com/stemtazoo/blog-instagram-prompts/blob/main/docs/workflows/eyecatch.md); do not duplicate its detailed generation policy here.

## When to include an image

- Add an image only if it improves the reader's understanding, comparison, or navigation. An eyecatch is not a mandatory section for every article.
- Prefer text and tables for searchable definitions, precise figures and accessible detail; images should complement rather than redundantly restate long passages. Do not remove necessary explanations just because a graphic repeats them.
- For an image embedded near `## まず結論`, keep the introduction readable and preserve existing teaching aids, examples, interactive controls, and exam-judgment points.

## OGP versus body image

- Treat the Front Matter `image.path` as the **desktop/OGP default**. Keep `image.width`, `image.height`, and `image.alt` accurate for that image. Do not point social metadata to a tall mobile-only asset without an explicit decision and preview check.
- A separate mobile asset is optional, not required globally. If mobile text or chart labels become illegible at article width, consider a portrait/stacked version with the same factual content and verified shading/labels.
- When both assets exist, use a standards-based `<picture>` in the article body and a normal `<img>` fallback; prefer a small, article-local change instead of site-wide CSS/JavaScript. Example:

```html
<picture>
  <source media="(max-width: 640px)" srcset="MOBILE_URL" width="1122" height="1402">
  <img src="DESKTOP_URL" width="1200" height="630"
       alt="記事の内容に沿った具体的な代替説明"
       style="display:block;width:100%;max-width:100%;height:auto;">
</picture>
```

- The dimensions above are **illustrative**, not mandatory. Use the actual dimensions of each verified file. Keep the same meaning for both variants so one shared `alt` accurately describes either; do not put essential new facts only in a picture.
- Use the image generation repository's slug-based `<slug>.<ext>` and `<slug>-mobile.<ext>` names. The article may refer to actual verified storage URLs but must not invent pCloud addresses.

## Review / release evidence

1. Record the canonical article, source ref, desktop/mobile URLs, each asset's measured dimensions, format, and any network-access limitation. A user-provided URL or locally generated file alone does not establish an HTTP 200 response from external hosting.
2. Verify diagram semantics, exact Japanese text, figures and highlighted regions against the current article. Inspect a reduced-size phone view. Report static source checks separately from device/browser checks.
3. Validate Front Matter YAML and readable HTML; confirm `<picture>` selects the mobile asset at or below the chosen breakpoint and desktop fallback above it, **in a browser** when available. Test responsive layout and meaningful `alt`.
4. After GitHub Actions/Pages deployment, inspect the delivered HTML, body image, OGP/Twitter metadata and mobile/desktop screenshots. Check SNS preview separately when possible. Do not treat a commit, successful build, or metadata output as proof that a remote image loaded.
5. Keep a single-article pilot isolated until validated. If the pilot demonstrates measurable benefit, consider wider adoption; never enforce two assets for all articles automatically.
