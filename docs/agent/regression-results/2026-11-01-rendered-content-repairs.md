# Rendered-content audit follow-up repairs

Base: `02bb4acee48af4e9da8468c241b0f85022aa6b70` (PR #573 merged).

## Evidence and changes

The first Actions report scanned 2,231 HTML pages and found 20 candidates:
14 body-less Jekyll redirects, four TeX command-prefix matches, and two article
defects. The public HTML confirmed the GUI article's escaped closing tags and
unparsed later Markdown, and WAF's literal newline escapes.

- `pages/fe/gui-controls.md`: explicitly close each datalist option. The deployed
  HTML escaped `</datalist>` after the unclosed options and swallowed the remaining
  Markdown. Preserve native form controls and their learning purpose.
- `pages/fe/waf.md`: replace six literal newline escape sequences with real line
  breaks, restoring paragraphs, comparison-table rows and summary list items.
- Detector: use escape-token boundaries to exclude TeX command prefixes; recognize
  body-less redirects only when canonical and refresh targets agree. Real text
  findings in pages that also carry redirect metadata still remain detectable.
- Update both repaired articles' modification dates to 2026-11-01.

## Executed verification

- Nine detector test methods pass, including new TeX and redirect regression cases.
- Downloaded all 20 previously flagged public pages (HTTP 200) and reran the updated
  CLI: 20 pages, two candidates, precisely GUI and WAF. The 18 false positives were
  removed without hiding either known defect in the still-unmodified public HTML.
- Instruction references and whitespace checks pass.
- Same-session four-theme verification remains covered by the existing detector
  fixtures. This narrow detector/documentation change does not alter editorial,
  source-selection, metadata or navigation policies.

## Build and browser limits

The PR preview workflow runs Jekyll, the full HTML audit, and two targeted
post-build tests. Those tests require GUI's later headings/table and all three
datalist options to survive rendering, and WAF's rows/list items to be separate
HTML elements. They also require zero text-audit candidates for both pages.
These are build-output checks, not browser visual or operation tests.

Local Ruby is unavailable, so the local run does not certify the repaired rendered
output. Refer to the PR Actions result for the Jekyll checks. Smartphone layout,
keyboard interaction, and deployed repaired pages have not been verified here.
