# GK Navigation Rules

This file is written in English for Codex readability. However, GK article content and reader-facing navigation labels must be written in Japanese unless the user explicitly requests otherwise.

Use this file when adding, removing, or reorganizing `prev` / `next` navigation or GK learning order metadata for articles under `pages/gk`.

## Purpose

GK pages should guide readers through G検定 topics by concept order: foundations, machine learning methods, deep learning architectures, applications, evaluation, and social/legal topics.

The current GK theme relies heavily on `gk_section`, `gk_order`, category/index pages, and the GK footer include. Preserve that convention unless the user explicitly asks for a redesign.

## Core Policy

- Do not guess `prev` / `next`.
- Prefer existing `gk_section` and `gk_order` for GK ordering when they are already used.
- Connect pages only when the learning relationship is clear.
- Do not connect unrelated themes only to fill empty navigation.
- Confirm actual `permalink` values before adding any navigation link.
- Keep GitHub Pages compatibility; avoid complex Liquid for navigation unless needed.

## Recommended Learning Order Patterns

Use learning value rather than alphabetical order.

Common patterns:

```text
Basic concept → model family → specific architecture → comparison/traps → review
```

```text
Metric definition → related metrics → metric comparison → exam traps
```

```text
Reinforcement learning basics → value-based methods → policy-based methods → comparison
```

## `gk_section` / `gk_order` Maintenance

Before changing `gk_section` or `gk_order`:

1. Search existing GK articles in the same area.
2. Confirm the current section names and order numbers.
3. Identify whether the page is an individual article, comparison article, summary page, or cheatsheet.
4. Make the smallest metadata change that improves learning flow.
5. Avoid broad renumbering unless the user requested a navigation reorganization.

## `prev` / `next` Policy

If a GK page already uses `prev` / `next`, preserve valid links unless they are wrong.

When adding new `prev` / `next`:

- Use absolute site paths matching actual `permalink` values.
- Add links only within a small coherent theme-based series.
- Put `prev` and `next` in front matter near `permalink`.
- Do not point to a page that does not exist.
- Do not use filenames as navigation values.

Good:

```yaml
prev: /gk/cnn/
next: /gk/resnet/
```

Avoid:

```yaml
prev: cnn.md
next: ./resnet
```

## Footer Convention

Normal GK articles commonly end with:

```liquid
{% include gk_article_footer.html %}
```

Preserve this convention for normal GK articles. Do not replace it with manual navigation blocks unless the user explicitly asks or nearby articles of the same type already do so.

## PR / Final Response Notes

When a change reorganizes GK navigation, explain:

- which section or series was affected;
- which metadata fields changed;
- whether `gk_section` / `gk_order` or `prev` / `next` was used;
- what checks were run.
