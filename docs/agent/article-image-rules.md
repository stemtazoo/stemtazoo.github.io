# Article Images and Responsive Eyecatches

This guide owns **website-side use** of images in FE, GK, DS and SG articles. The image-generation instructions, output filenames and visual correctness review are owned by [blog-instagram-prompts](https://github.com/stemtazoo/blog-instagram-prompts/blob/main/docs/workflows/eyecatch.md); do not duplicate its detailed generation policy here.

## When to include an image

- Add an image only if it improves the reader's understanding, comparison, or navigation. An eyecatch is not a mandatory section for every article.
- Prefer text and tables for searchable definitions, precise figures and accessible detail; images should complement rather than redundantly restate long passages. Do not remove necessary explanations just because a graphic repeats them.
- Before placement, compare the planned image with nearby figures, tables and interactive examples. Give each a distinct reader task. If a diagram repeats the same example and explanation, simplify it or keep the clearer version. Preserve text needed to reproduce the calculation, searchable values, and the interactive exercise.
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

## Caption content

- Compare the proposed caption with the figure, its alt text, the preceding and following paragraphs, and any nearby example or table. Look for repeated meaning as well as repeated wording.
- Use a visible caption when it helps readers interpret this particular figure. Prefer one short sentence that points to an axis, arrow, comparison, or assumption. Keep figure identification and attribution when readers need them.
- Omit `<figcaption>` when the surrounding explanation already gives readers everything they need to read the image. Preserve the figure and meaningful alt text. Keep definitions, calculation steps, and exam judgment criteria in the article so readers can follow the explanation without the image.
- For example, when the article already explains the parts of a Pareto chart, guide readers to the point where the line reaches 80% and the item directly below it.

## Body image size and caption balance

- For explanatory images embedded in the article body, **use the available article text width as the default**. An `img` with `width:100%` still fills only its parent: check the containing `figure` and any theme or browser margins before deciding that the image itself needs to change. Respect the article container; do not expand beyond it or create horizontal overflow.
- When using `<figure>`, set its horizontal margin intentionally (for example, `margin:16px 0 20px` for a full article-width figure). Verify theme-specific styles do not override the intended width. Retain responsive `width:100%;max-width:100%;height:auto` on the image.
- A caption should be visibly subordinate to normal body text while remaining legible, with appropriate spacing, contrast and line height. As a **starting point, not a fixed global rule**, `font-size:0.88em`, `line-height:1.5` and a muted but readable text color worked in the GK teacher-forcing pilot; adjust to the theme and check on mobile.
- Judge the *whole article view*, not just whether image labels are legible in isolation. Inspect image size relative to nearby paragraphs and headings, arrows and small annotations, caption wrapping, surrounding whitespace and the transition to the next section, especially around a 340px content width.
- If a landscape image initially looks too small on a phone, **first check the container width, figure margins, layout and caption** before requesting a separate mobile asset or regenerating the image. If meaningful diagram details remain unreadable at the available width, follow the [mobile-variant decision workflow](https://github.com/stemtazoo/blog-instagram-prompts/blob/main/docs/workflows/mobile-variant-decision.md) in the image-generation repository.
- Evidence: the [GK teacher-forcing article](/gk/teacher-forcing/) became easier to read on a phone after reducing the figure's horizontal margins and visually subordinating its caption; the image pixels and OGP asset were unchanged. This is an observed pilot, not a guarantee for all illustrations.

## Review / release evidence

1. Record the article ref and use the [production workflow's delivery checks](https://github.com/stemtazoo/blog-instagram-prompts/blob/main/docs/workflows/eyecatch.md#file-and-storage) for the exact asset URL, dimensions, type and replacement-revision evidence.
2. Verify diagram semantics, exact Japanese text, figures and highlighted regions against the current article. Inspect a reduced-size phone view. Report static source checks separately from device/browser checks.
3. Validate Front Matter YAML and readable HTML; confirm `<picture>` selects the mobile asset at or below the chosen breakpoint and desktop fallback above it, **in a browser** when available. For a 640px breakpoint, record the actual `currentSrc` and successful image load at 640px and 641px. At a typical narrow article width, record the article and image widths, verify the main diagram question, caption wrapping and nearby fixed-width content, and check for horizontal overflow. Confirm meaningful `alt` and, if the placement touches an interactive example, run one representative case.
4. After GitHub Actions/Pages deployment, inspect the delivered HTML, body image, OGP/Twitter metadata and mobile/desktop screenshots. Check SNS preview separately when possible. Do not treat a commit, successful build, or metadata output as proof that a remote image loaded.
5. Keep a single-article pilot isolated until validated. If the pilot demonstrates measurable benefit, consider wider adoption; never enforce two assets for all articles automatically.
