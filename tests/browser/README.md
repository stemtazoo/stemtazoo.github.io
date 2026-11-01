# Interactive lesson pilot

This pilot covers only the three FE pages registered in `pilot.json`.
The canonical teaching and verification policy remains in
[interactive-learning-rules.md](../../docs/agent/interactive-learning-rules.md).

## Shared UI

The three pages opt in with `study-demo`, load `study_demo_assets.html` before
article JavaScript, and use `StudyDemoUI.selectChoice` / `nextAction`.
The synchronous small script is intentional: inline article initialization must
not race a deferred dependency. The helper owns selection presentation and guide
association; each article still owns its algorithm, correct answers and state.

- Use `study-demo__controls` for controls that must fit their parent width.
- Choice buttons have `data-demo-choice`; the selected value sets `aria-pressed`.
- `study-demo__guide` sits directly between prediction and the action buttons.
- New consumers need a representative browser scenario before expanding coverage.

## Run and scope

The independent `Interactive demo browser checks` workflow builds Jekyll once,
serves the actual output locally, and runs Chromium at 320, 390 and 1280px.
It does not add a test step to the publication workflow or run the full rendered
text audit again. Chromium is the initial pilot browser, not a mobile-device lab.
External requests are blocked; local theme assets and article scripts are tested.

A changed registered article selects its own scenario. Shared assets, layouts,
includes, build configuration and test-harness changes select all three.
Other article changes are explicitly listed as unregistered, not counted as passes.
Manual workflow dispatch runs all three. A missing page, dependency, browser or
failed operation is a failed check, not a skipped success.

```sh
python -m pip install -r tests/browser/requirements.txt
python -m playwright install --with-deps chromium
# Build _site with the project's GitHub Pages-compatible Jekyll first.
python scripts/select_interactive_checks.py --all --output artifacts/interactive-demo/selection.json
python scripts/check_interactive_demos.py --selection artifacts/interactive-demo/selection.json
```

The tests assert containment of controls inside the lesson and viewport, actual
computed selected colors, state changes, next-action guides, reset/back, final
boundaries, expected outcomes and JavaScript-disabled static explanations.
They exercise native keyboard activation in the lock example, not every keyboard
path or screen-reader behavior. Intentional table/history scrolling is allowed.

## Review evidence and unfinished work

Actions uploads `interactive-demo-checks`: screenshots, Playwright traces,
`report.json`, selection and `follow-up.md`; the run summary links the outcome to
its commit. Screenshots after a scenario are evidence for that state only.

The PR author/reviewer owns closing each manual follow-up. Record the URL/version,
environment, operation, expected and observed result in the PR. A browser failure
must be fixed or remain explicitly unresolved; a human check marked unverified
must not become a claimed pass. Human review remains necessary for instruction
clarity, prediction/state proximity, actual mobile browsers, screen readers and
post-merge deployment. Existing update audits remain a follow-up safeguard.

Initial scope: the three repaired articles only. Observe this pilot before a
sitewide migration. The existing teaching rules do not make browser automation a
universal prerequisite for adding useful interactive explanations.

Implementation reference checked 2026-11-02:
[Playwright Python CI](https://playwright.dev/python/docs/ci).
