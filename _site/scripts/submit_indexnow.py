#!/usr/bin/env python3
"""Submit changed GitHub Pages URLs to IndexNow."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable
from urllib import error, request


GLOBAL_TRIGGER_PATHS = (
    "_config.yml",
    "_includes/",
    "_layouts/",
    "assets/",
)

GLOBAL_FALLBACK_URLS = ("/", "/ds/", "/gk/", "/sg/")
ROOT_TEXT_KEY_RE = re.compile(r"^[A-Za-z0-9_-]{8,}$")
POST_NAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Submit changed URLs from this repository to IndexNow."
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root. Defaults to the current directory.",
    )
    parser.add_argument(
        "--config",
        default="_config.yml",
        help="Path to _config.yml relative to repo root.",
    )
    parser.add_argument(
        "--key-file",
        help="IndexNow key file relative to repo root. Auto-detected when omitted.",
    )
    parser.add_argument(
        "--from-git-diff",
        nargs=2,
        metavar=("BEFORE", "AFTER"),
        help="Collect changed files from git diff BEFORE..AFTER.",
    )
    parser.add_argument(
        "--all-known",
        action="store_true",
        help="Submit all known public URLs derived from tracked files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the payload without sending it.",
    )
    return parser.parse_args()


def read_simple_config(path: Path) -> dict[str, str]:
    config: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key not in {"url", "baseurl"}:
            continue
        value = value.strip().strip("'").strip('"')
        config[key] = value
    return config


def parse_front_matter(path: Path) -> dict[str, object]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8-sig")

    if not text.startswith("---"):
        return {}

    lines = text.splitlines()
    data: dict[str, object] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            continue
        if value.startswith("[") and value.endswith("]"):
            items = [item.strip().strip("'").strip('"') for item in value[1:-1].split(",")]
            data[key] = [item for item in items if item]
        else:
            data[key] = value.strip("'").strip('"')
    return data


def normalize_url_path(raw_path: str) -> str:
    if not raw_path:
        return "/"
    path = raw_path if raw_path.startswith("/") else "/" + raw_path
    return path if path == "/" or path.endswith("/") else path + "/"


def join_site_url(site_root: str, url_path: str) -> str:
    return site_root.rstrip("/") + url_path


def detect_key_file(repo_root: Path) -> Path:
    matches: list[Path] = []
    for candidate in repo_root.glob("*.txt"):
        stem = candidate.stem.strip()
        body = candidate.read_text(encoding="utf-8").strip()
        if stem == body and ROOT_TEXT_KEY_RE.match(stem):
            matches.append(candidate)
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise FileNotFoundError("No IndexNow key file was found at the repository root.")
    raise RuntimeError(
        "Multiple possible IndexNow key files were found. Pass --key-file explicitly."
    )


def infer_post_url(front_matter: dict[str, object], stem: str) -> str:
    permalink = front_matter.get("permalink")
    if isinstance(permalink, str) and permalink.strip():
        return normalize_url_path(permalink.strip())

    match = POST_NAME_RE.match(stem)
    slug = match.group(1) if match else stem
    categories = front_matter.get("categories")
    if isinstance(categories, list):
        category_path = "/".join(str(item).strip("/") for item in categories if str(item).strip("/"))
    elif isinstance(categories, str) and categories.strip():
        category_path = categories.strip().strip("/")
    else:
        category_path = ""

    if category_path:
        return normalize_url_path(f"/{category_path}/{slug}/")
    return normalize_url_path(f"/{slug}/")


def map_file_to_url(repo_root: Path, rel_path: str, site_root: str) -> str | None:
    rel = rel_path.replace("\\", "/").lstrip("./")
    path = Path(rel)

    if not rel or rel.startswith(".github/") or rel.startswith("_site/"):
        return None
    if rel in {"README.md", "AGENTS.md", "ACTIONS_TROUBLESHOOTING.md"}:
        return None
    if path.suffix.lower() not in {".md", ".html", ".txt", ".xml"}:
        return None

    full_path = repo_root / path
    front_matter = parse_front_matter(full_path) if full_path.exists() and path.suffix.lower() == ".md" else {}

    if rel == "index.md" or rel == "index.html":
        return join_site_url(site_root, "/")

    if len(path.parts) == 1 and path.suffix.lower() in {".html", ".txt", ".xml"}:
        return join_site_url(site_root, f"/{path.name}")

    if path.parts and path.parts[0] == "pages":
        permalink = front_matter.get("permalink")
        if isinstance(permalink, str) and permalink.strip():
            return join_site_url(site_root, normalize_url_path(permalink.strip()))

        public_parts = list(path.parts[1:-1])
        if path.stem != "index":
            public_parts.append(path.stem)
        url_path = "/" + "/".join(public_parts)
        return join_site_url(site_root, normalize_url_path(url_path))

    if path.parts and path.parts[0] in {"_posts", "posts"} and path.suffix.lower() == ".md":
        return join_site_url(site_root, infer_post_url(front_matter, path.stem))

    return None


def list_tracked_files(repo_root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def list_changed_files(repo_root: Path, before: str, after: str) -> list[str]:
    if before and set(before) == {"0"}:
        return list_tracked_files(repo_root)

    result = subprocess.run(
        ["git", "diff", "--name-only", before, after],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def collect_urls(repo_root: Path, changed_files: Iterable[str], site_root: str) -> list[str]:
    urls: set[str] = set()
    changed = [path.replace("\\", "/") for path in changed_files]

    for rel_path in changed:
        url = map_file_to_url(repo_root, rel_path, site_root)
        if url:
            urls.add(url)

    if any(rel == "_config.yml" or rel.startswith(GLOBAL_TRIGGER_PATHS[1:]) for rel in changed):
        for url_path in GLOBAL_FALLBACK_URLS:
            urls.add(join_site_url(site_root, url_path))

    return sorted(urls)


def submit_to_indexnow(site_root: str, key: str, key_location: str, urls: list[str], dry_run: bool) -> int:
    payload = {
        "host": site_root.replace("https://", "").replace("http://", "").strip("/"),
        "key": key,
        "keyLocation": key_location,
        "urlList": urls,
    }

    print(json.dumps(payload, ensure_ascii=False, indent=2))

    if dry_run:
        return 0

    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        "https://api.indexnow.org/indexnow",
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=30) as response:
            print(f"IndexNow response: {response.status}")
            return 0 if 200 <= response.status < 300 else 1
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(f"IndexNow HTTP error: {exc.code} {exc.reason}", file=sys.stderr)
        if detail:
            print(detail, file=sys.stderr)
            if exc.code == 403 and "SiteVerificationNotCompleted" in detail:
                print(
                    "IndexNow site verification is still pending. Treating this run as a non-fatal retryable state."
                )
                return 0
        return 1
    except error.URLError as exc:
        print(f"IndexNow request failed: {exc}", file=sys.stderr)
        return 1


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    config = read_simple_config((repo_root / args.config).resolve())

    site_url = config.get("url", "").rstrip("/")
    baseurl = config.get("baseurl", "").strip("/")
    if not site_url:
        print("The site url was not found in _config.yml.", file=sys.stderr)
        return 1

    site_root = site_url if not baseurl else f"{site_url}/{baseurl}"

    key_file = (repo_root / args.key_file).resolve() if args.key_file else detect_key_file(repo_root)
    key = key_file.read_text(encoding="utf-8").strip()
    key_location = join_site_url(site_root, f"/{key_file.name}")

    if args.all_known:
        candidate_files = list_tracked_files(repo_root)
    elif args.from_git_diff:
        before, after = args.from_git_diff
        candidate_files = list_changed_files(repo_root, before, after)
    else:
        print("Choose either --all-known or --from-git-diff.", file=sys.stderr)
        return 1

    urls = collect_urls(repo_root, candidate_files, site_root)
    if not urls:
        print("No public URLs matched the selected files.")
        return 0

    print(f"Submitting {len(urls)} URL(s) to IndexNow.")
    return submit_to_indexnow(site_root, key, key_location, urls, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
