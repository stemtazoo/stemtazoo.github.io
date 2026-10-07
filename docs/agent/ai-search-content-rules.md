# AI Search Content Rules

Use this shared guide when creating or meaningfully editing study articles under `pages/sg`, `pages/ds`, `pages/gk`, and `pages/fe`.

These rules are based on the general direction of AI search and grounding systems: content may be retrieved as small passages, summarized, cited, or compared outside the original page layout. The goal is not to chase a specific vendor or product, but to make each article clearer for readers and easier for AI systems to quote, ground, and distinguish accurately.

## Grounding-Oriented Readability

- Start each article with a short, direct definition or conclusion that answers `What is this?` before giving details.
- Keep one normal article focused on one concept, one term, one method, or one exam judgment point.
- Write paragraphs so that each paragraph is understandable even if it is extracted independently from the page.
- Use explicit, searchable headings that name the concept and learning purpose, rather than vague headings that depend on surrounding context.
- Do not change the required fixed heading structure for each theme. When fixed headings are used, make the paragraphs under each heading self-contained and searchable.
- Avoid vague references such as `this`, `that`, `it`, `the above`, `これ`, `それ`, `上記`, and `前述` when the sentence may be read out of context. Repeat the noun or concept name when clarity matters.
- Compare confusing terms clearly with short explanations, tables, or judgment criteria so readers and AI systems can distinguish the pages.
- Include official or primary source links when useful for grounding, especially for laws, standards, syllabi, public organizations, and vendor-defined technologies.
- Do not keyword-stuff or repeat unnatural phrases. Preserve the existing beginner-friendly Japanese tone and write for human learners first.
- For exam-prep articles, prioritize judgment criteria for eliminating wrong choices over broad textbook-style coverage.

## Performance Interpretation

AI citation / grounding metrics are supporting evidence, not a standalone article-quality score.

- Do not revise, merge, or devalue an article only because AI citations, citation share, or Share of Authority are low or zero.
- Evaluate ordinary search performance and AI citation performance as separate dimensions. An article may be useful as a search-entry page, an AI grounding source, both, or neither yet.
- When AI citation data is available, compare the observed grounding query with the article's intended learning purpose and direct answer before proposing a content change.
- Treat query demand and whether an AI system chooses to ground a topic as partly external to the article. A strong direct answer improves extractability but does not guarantee citations.
- Preserve a strong human-facing or search-performing article when the only negative signal is weak AI citation performance.

## Practical Writing Checks

Before saving an article, check whether a short excerpt from the page would still make sense if shown in an AI answer, search snippet, or related-article card.

- Does the first paragraph directly define the topic or state the practical conclusion?
- Do freely worded headings contain meaningful words that identify the topic or comparison? For required fixed headings, preserve the theme's wording and check that the text immediately below explicitly identifies the topic or comparison.
- Does each important paragraph name the concept instead of relying on vague pronouns?
- Are similar terms separated by criteria such as purpose, timing, target, mechanism, or exam-choice wording?
- Are official links supportive and relevant, rather than a generic link collection?
- Does the article remain natural Japanese for beginners, not an SEO keyword list?
