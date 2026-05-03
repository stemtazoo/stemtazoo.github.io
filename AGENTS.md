# AGENTS.md

This file is the entry point for AI coding agents and collaborators modifying this repository.
Detailed rules live under `docs/agent/`; read the relevant file before editing related areas.

## Purpose

This repository powers a Jekyll site with multiple content themes under `pages/`, currently including:

- `pages/ds`: Data Science / skill-check style content
- `pages/gk`: G-kentei study content
- `pages/sg`: Security / SG study content

The project goal is not only to publish correct content, but to keep the site buildable on GitHub Pages and visually consistent across themes.

## Core Priorities

When making changes, use this order of priority:

1. Keep GitHub Actions / GitHub Pages builds passing.
2. Preserve or improve content correctness.
3. Maintain layout consistency across themes.
4. Prefer simple, GitHub Pages-compatible Liquid over clever Liquid.
5. Avoid changes that create theme-by-theme drift unless explicitly requested.

## Required References

Read the relevant detailed guide before changing each area:

- GitHub Pages / Liquid compatibility: `docs/agent/github-pages-compat.md`
- IndexNow deployment automation: `docs/agent/indexnow.md`
- Theme and layout consistency: `docs/agent/theme-consistency.md`
- SG content, confirmation-question, and series-summary rules: `docs/agent/sg-content-rules.md`

## Editing Strategy

When fixing site issues:

1. Reproduce the issue from logs or local build.
2. Identify whether the problem is content, front matter, include logic, layout logic, or GitHub Pages version compatibility.
3. Make the smallest robust fix first.
4. Rebuild locally when possible.
5. Treat GitHub Actions confirmation as final for Pages compatibility.

## Front Matter And Encoding

- Preserve readable Japanese text and use UTF-8.
- If terminal output looks garbled, verify file contents before assuming the file itself is broken.
- Be careful when editing `layout`, `title`, `description`, `permalink`, `tags`, theme-specific ordering fields such as `gk_section` / `gk_order`, and navigation fields such as `prev` / `next`.
- Do not rename or remove front matter keys that includes depend on without updating those includes.

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
