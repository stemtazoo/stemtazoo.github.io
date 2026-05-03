# IndexNow Automation

This repository uses GitHub Actions for post-deploy automation related to search indexing.

## Key File

- The IndexNow key file is stored at the repository root as a plain text file and must remain publicly accessible after GitHub Pages deploys.
- The current key file is `f0977966c6644641ae35df01652658c4.txt`.
- The file contents must exactly match the filename stem.
- Do not move the key file into `_includes`, `assets`, `pages`, or any non-root directory.
- Do not add front matter to the key file.

## Workflow Behavior

- IndexNow submission is designed to run after GitHub Pages deployment succeeds, not before.
- Prefer post-deploy submission over push-time submission so the submitted URLs are already live when search engines fetch them.
- If editing `.github/workflows/indexnow.yml`, preserve the post-deploy trigger behavior unless there is a strong reason to change it.
- If editing `scripts/submit_indexnow.py`, prefer standard-library Python and keep the script runnable in GitHub Actions without extra package installs.

## Failure Handling

- A `403` response containing `SiteVerificationNotCompleted` is a retryable verification state, not necessarily a broken configuration.
- Do not treat that specific response as proof that the key file is invalid unless the public key URL has also been checked.
- A successful submission currently returns `IndexNow response: 200` in the workflow logs.

## Maintenance Guidance

- Favor simple, debuggable URL collection logic over aggressive optimization.
- If choosing between full-site submission and a more fragile differential approach, prefer the more reliable option unless rate, scale, or workflow cost becomes a real problem.
- When changing site URL structure, permalink logic, or root verification files, review the IndexNow workflow and submission script together.
