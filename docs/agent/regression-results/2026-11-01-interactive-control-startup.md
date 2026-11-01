# Interactive control startup: 2026-11-01

Base: `ac8fd67ba528265dcb894861cb45815a9b009abc` (PR #576 merged).

## Problem and change

The FIFO/LRU, recursion (two blocks), DS causal/layer and GK activation/Softmax
demonstrations exposed enabled HTML controls before their JavaScript initialized.
If JavaScript was disabled or the executable asset was unavailable, controls could
appear usable while outputs stayed unchanged or empty.

- Set the five articles' demonstration buttons, sliders and selector to disabled
  in HTML. Enable controls after initial rendering and listener registration;
  previous/next controls retain the existing first/last-step rules.
- Reuse recursion's existing static trace tables and guidance. Add short noscript
  guidance to the other four articles, referring to existing article content.
- Scope DS/GK disabled styles to the affected demonstration roots.
- Version the affected external JS references with `?v=20261101-startup` so new
  disabled markup does not rely on a previously cached pre-change script that
  cannot enable every control. LRU's script is inline.
- Update article modification dates. Preserve the LRU completion fix from #576.

This addresses the priority-2 startup/fallback concern from the display audit.
DS result announcements (priority 3) are unchanged. The audit repository and its
judgment ledger are unchanged.

## Executed checks

Node v24.22.1 and jsdom were used for 50 grouped checks, all passing. Fixtures
parsed the HTML blocks directly from the local article Markdown and executed the
modified inline/external scripts. This is DOM execution, not a Jekyll build or a
browser operation test. jsdom was installed only in a temporary verification
directory; the site has no new runtime or package dependency.

| Scope | Expected and observed result |
| --- | --- |
| Five changed articles plus two shared consumers, scripts omitted | All target controls remain disabled; noscript guidance or existing recursion trace guidance remains in the source DOM. Omitting execution models unavailable scripts; no real browser network-failure or JS-off setting was tested. |
| FIFO/LRU | Initial next/reset enabled and previous disabled; ten steps reach FIFO 3 / LRU 6 and the corrected completion text; back enables next; reset restores the initial boundary. |
| Recursion | Selector/reset/next enabled; f(3)=6 and f(4)=24; back enables next; reset restores the boundary while selector/reset remain enabled. |
| Three stacks | Initial previous disabled and next/reset enabled; final B=[1,2,3,1,2,3]; back and reset restore correct next/previous states. |
| DS causal/layer | All mode buttons enabled; three mode transitions including return to the original mode update results and retain exactly one pressed button. |
| GK activation/Softmax | All controls enabled; ReLU(-6), Sigmoid(0), tanh(6) agree with formulas; tied, extreme and original Softmax scores give expected rounded values and total 1.00. |
| Shared DS evaluation-metrics-comparison | Initialization and 0.80/0.30/0.50 threshold presets still work. |
| Shared GK gradient-descent | Initialization, one update to w=1.5, divergence stop and reset still work. |

Also passed: syntax checks for four external JS files and LRU's inline script,
metadata comparison for five articles (publication date, URLs, titles, grouping,
tags and navigation preserved), and `git diff --check`.

Repository search across pages, includes and layouts found three DS consumers
(causal, layer, evaluation metrics), two GK consumers (activation, gradient
descent), and one consumer of each recursion JS file. The other two articles'
source was not edited. No shared navigation or layout was changed.

## Verification limits and follow-up

The cloud browser connected, but navigating to the local source-block preview
failed with `net::ERR_CONNECTION_REFUSED`. No changed page was operated in a
browser. Desktop/mobile layout, disabled appearance, keyboard operation,
screen-reader behavior and actual JavaScript-disabled fallback remain unverified.
Ruby/Jekyll is unavailable locally; GitHub Pages build and deployed output remain
unverified until Actions/deployment runs. No deployment success is claimed.

After deployment, use desktop and 375px widths to check the initial enabled state,
representative operation and reset on all five pages; check the LRU/recursion final
step. With JS disabled, verify controls stay disabled and existing explanations
and tables remain readable. Separately block the JS request with JS enabled to
check disabled controls: noscript intentionally does not display in that case.
Recheck the DS threshold and GK gradient consumers after shared-asset delivery.
