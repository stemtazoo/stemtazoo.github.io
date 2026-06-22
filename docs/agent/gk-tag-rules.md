# GK Tag Rules

This file is written in English for Codex readability. However, GK article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules for `tags` in articles under `pages/gk`.

## Basic Rules

- Always include `gk` on every GK page.
- Select a small number of concrete tags, usually 2-5 total including `gk`.
- Check nearby GK articles before introducing a new tag spelling.
- Prefer existing tag vocabulary over one-off synonyms.
- Do not over-tag pages with every related keyword.
- Tags should support discovery and grouping, not repeat the whole title.

## Common Tag Families

Existing GK pages use tags such as these. Confirm current usage before applying them:

```yaml
machine_learning
deep_learning
neural_network
cnn
rnn
transformer
attention
nlp
image_recognition
reinforcement_learning
evaluation_metrics
clustering
dimensionality_reduction
generative_ai
xai
ai_ethics
```

## Selection Examples

Transformer / attention article:

```yaml
tags: [gk, deep_learning, transformer, attention]
```

NLP model article:

```yaml
tags: [gk, nlp, transformer, attention]
```

Reinforcement learning article:

```yaml
tags: [gk, reinforcement_learning, machine_learning]
```

Evaluation metric article:

```yaml
tags: [gk, evaluation_metrics, machine_learning]
```

## Cautions

- Do not use SG or DS-only category tags in GK articles.
- Do not change tags across many existing articles only for cosmetic consistency in a content-rule task.
- If a tag appears to be misspelled but is already used by indexes, investigate before changing it.
