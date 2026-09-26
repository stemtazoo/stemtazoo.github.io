# Primary Source And Freshness Audit Rules

This file defines shared rules for selecting, adding, refreshing, and auditing primary / official sources across study content in this repository.

Use it especially for `pages/gk`, `pages/sg`, and `pages/ds`, and also as a shared baseline when another section-specific rule does not define a stricter source policy.

This file does **not** replace article-writing rules. When an audit results in an article edit, the edited page must still comply with its section-specific content, template, front-matter, tag, navigation, and GitHub Pages rules.

## When To Read This File

Read this file before work whose main purpose includes one or more of the following:

- auditing whether articles lack useful primary or official sources;
- adding original research papers to named AI / machine-learning methods or models;
- adding or refreshing IETF / RFC references;
- checking whether a law, standard, guideline, protocol specification, or public rule has been revised or superseded;
- replacing obsolete primary sources with current authoritative sources;
- performing a multi-article source-quality or freshness review;
- deciding whether a source should **not** be added because it would not improve the article.

For a small wording correction that does not affect factual authority, provenance, or freshness, this file does not need to drive the edit.

For new GK / SG / DS articles, apply this file when a natural primary or official source exists for the article topic.

## Rule Precedence

A source audit is a decision process, not permission to weaken an article.

Use this order when rules appear to compete:

1. Build safety and repository-wide requirements in `AGENTS.md`.
2. Current official facts, laws, standards, specifications, and examination scope.
3. Section-specific content and article-template rules.
4. This shared source / freshness audit workflow.
5. Optional source additions.

Therefore:

- Do not add a source merely because one exists.
- Do not make an article longer merely to display references.
- Do not replace beginner-friendly explanation with standards language or paper terminology.
- Do not turn RFC numbers, publication years, or paper titles into memorization targets unless the exam genuinely requires them.
- Do not create a new article merely because a source audit reveals a related concept.
- Do not add a new heading only to satisfy an audit if the existing article structure already provides a natural place.
- Preserve the site's core value: beginner-friendly explanation, answer-choice judgment, confusion prevention, and useful learning flow.

## Match The Source To The Claim

Choose the source according to **what the article is claiming**.

### Current rule, specification, or requirement

Use the latest current authority:

- responsible Japanese ministry, agency, public body, or IPA;
- ISO / IEC / IEEE / ITU where appropriate;
- IETF / RFC Editor for Internet protocols;
- W3C / WHATWG / ECMA for relevant web / language standards;
- the responsible official project or standards organization.

### Historical origin or named research method

Use the original or canonical research source when provenance matters:

- original peer-reviewed paper;
- canonical conference / journal publication;
- original technical report or preprint when that is the recognized source;
- original book when the concept is historically defined there.

### Current software or project behavior

Use maintained official documentation from the responsible project or vendor when the article describes present behavior rather than historical origin.

### Secondary sources

Use secondary explanations for discovery or supporting context only when they materially help the learner.

A secondary explanation should not displace a stronger available primary source for:

- current normative requirements;
- protocol definitions;
- model / method origin claims;
- official examination scope;
- claims about a standard being current or obsolete.

## Original Source And Current Authority Are Different Roles

Do not confuse **where a concept came from** with **what is authoritative now**.

Use:

```text
Historical origin / named model
→ original paper / original book

Current protocol / standard / rule
→ latest official specification

Current examination scope
→ latest official exam guidance
```

An article may need one, both, or neither.

Examples:

- GAN article → Goodfellow et al. original paper is natural.
- TLS article → current TLS RFC is more important than the historically original TLS document.
- Old SG question based on an obsolete rule → article body should still use the current official rule, with a historical note only when needed.

## Source-Addition Decision

Before editing, classify the candidate.

### A. Add or update

Add / refresh the source when it materially improves at least one of:

- factual correctness;
- currentness;
- authority or traceability;
- an exam answer-choice judgment criterion;
- distinction from a commonly confused term;
- clarification of a material misconception;
- provenance of a named model, algorithm, architecture, loss, or training technique.

### B. Existing support is sufficient

Do not edit when:

- an appropriate current primary source is already present;
- the candidate only duplicates the same authority;
- the existing explanation is already correctly and sufficiently supported.

### C. A source exists, but addition is unnecessary

Do not edit when:

- the source is historically interesting but does not improve learning;
- it adds specialist detail beyond the article's exam role;
- it would make a concise article harder to read;
- the article covers a broad / generic concept with no single canonical origin source;
- the source does not improve correctness, judgment criteria, confusion prevention, or traceability.

The default is **not** “find a source, then add it.”

The default is:

> **Add only when the source improves the article.**

## GK-Specific Decision Rules

For `pages/gk`:

### Named model / method rule

When the article is centered on a specifically named research model, architecture, algorithm, loss, or training technique and a recognized original paper exists, prefer adding the original / canonical paper.

Typical examples:

- AlexNet, VGG, ResNet, U-Net, SegNet;
- Transformer, BERT, Word2Vec;
- DQN, PPO, Rainbow, Agent57;
- VAE, GAN, Conditional GAN, VQ-VAE;
- Adam, AdaGrad, AdaDelta;
- Contrastive Loss, CutMix.

### Comparison article rule

For comparison articles, add the original paper for each compared named method only when it helps verify the distinction the article teaches.

Avoid long bibliography dumps.

As a practical default:

- 2 methods → usually 2 core sources;
- 3–5 named methods → one canonical source per method is acceptable when the comparison depends on their original design;
- large summary pages → select only the sources needed to support the main classification or link to already well-sourced individual articles instead.

### Generic-concept rule

Do **not** force an “original paper” onto broad concepts that do not have one clean canonical source for the article's scope.

Examples may include:

- sigmoid or softmax as broad mathematical functions;
- generic pooling;
- generic normalization as a broad preprocessing idea;
- generic regularization;
- linear regression;
- other long-established mathematical / statistical concepts.

For these topics, use a primary / official source only when it directly improves a specific claim.

### Placement

When an original paper is useful and a dedicated source block improves traceability, prefer:

```md
## 参考資料（原論文）

- [Paper title｜publisher / venue](canonical URL)
  - 試験で重要なポイントとの対応を1〜2文で説明。
```

Place it near the end, before:

```liquid
{% include gk_article_footer.html %}
```

Do not require this heading on every GK page.

## SG-Specific Decision Rules

For `pages/sg`:

### Official-source priority

Prefer the source that directly defines the current rule, protocol, security practice, or public guidance.

Common high-value sources include:

- IPA;
- NISC;
- JPCERT/CC;
- CRYPTREC;
- e-Gov and responsible ministries / agencies;
- 個人情報保護委員会;
- IETF / RFC Editor;
- relevant ISO / IEC / JIS authorities.

### IETF / RFC rule

For Internet protocols and protocol-security articles, IETF / RFC Editor is often the defining primary source.

Before adding an RFC:

1. confirm that the RFC actually supports the claim made in the article;
2. check whether it is current, obsolete, updated, or superseded;
3. prefer the current RFC for current behavior;
4. keep an older RFC only when historical context is useful;
5. do not cite an obsolete RFC as the current specification.

Examples of natural RFC-backed SG topics:

- DNS / DNSSEC;
- DHCP;
- HTTP / HTTPS;
- TLS;
- SSH;
- IPsec / IKE;
- SMTP / IMAP;
- SPF / DKIM / DMARC;
- S/MIME;
- certificate status protocols;
- protocol-level reflection / amplification countermeasures.

### Supersession sweep

When a cited standard or RFC is replaced:

1. update the primary target article;
2. search the repository for the old RFC / standard identifier;
3. inspect comparison, summary, and related articles that may repeat the old reference;
4. update only pages where the old source is presented as current;
5. leave historical mentions only when they are clearly labeled as historical.

This prevents source freshness from drifting across related pages.

### Placement

Follow `docs/agent/sg-content-rules.md`.

Normally place official / reference links in:

```md
## 公式情報・参考リンク
```

near the end of the article, before the SG footer.

Do not turn an SG page into a standards bibliography.

## DS-Specific Decision Rules

For `pages/ds`, prioritize **current practical authority** over historical provenance when the article is about tools, systems, data handling, law, security, or implementation.

### DS source-priority rule

Use the source type that best matches the practical role of the article:

1. **DS検定 scope / skill items**
   - Prefer the current official materials from the Data Scientist Society / データサイエンティスト協会.
2. **Law / privacy / governance**
   - Prefer the current responsible authority or legal text, such as 個人情報保護委員会, e-Gov, EU / EUR-Lex, or the responsible U.S. state authority.
3. **Data engineering / software / libraries**
   - Prefer maintained official project documentation, such as Apache Hadoop / Spark, Docker, Jupyter, Python, pandas, scikit-learn, NLTK, database or cloud project documentation.
4. **Internet / security protocols**
   - Prefer the current RFC / IETF, NIST, IPA, or other defining current authority.
5. **Named ML / statistical methods**
   - Use an original / canonical paper when origin or model design materially helps understanding, but prefer official implementation documentation when the article's main value is practical use.
6. **Generic statistics / mathematics / business concepts**
   - Do not force historical papers merely to create a citation. Add a source only when it improves interpretation, currentness, practical implementation, or exam judgment.

### Practical-documentation-over-origin rule

For DS articles, the question is often:

> **What should a learner use or verify today?**

Therefore:

- Spark article → current Apache Spark docs usually matter more than the original Spark paper.
- Docker article → current Docker docs matter more than Docker's historical origin.
- Jupyter / pandas / scikit-learn article → current official docs are normally the primary practical source.
- Random Forest / PCA article → an original paper can be useful, but if the article focuses on implementation or parameter behavior, official library docs may be more valuable.
- t-test / correlation / variance article → do not add an old historical paper unless it directly improves a specific interpretation or misconception.

### DS law and privacy rule

For privacy / law articles:

- check whether the law has been amended or complemented by newer rules;
- keep the article body aligned with the current legal framework;
- avoid simplified comparisons that imply one law is universally “stricter” than another;
- prefer concrete rights, scope, duties, and decision criteria over broad ranking language;
- when a named amendment changes the current framework, mention it when material to the learner.

### DS protocol / security rule

For OAuth, TLS, SSH, API / HTTP, FTP, zero trust, PKI, and similar practical-security topics:

- use current RFC / NIST / official sources;
- distinguish a base specification from a current Best Current Practice when both matter;
- when the current specification changes the simplified teaching model, correct the body rather than merely adding a link;
- do not present a historical implementation shortcut as the current protocol design.

### Placement

When a source block is useful, prefer:

```md
## 公式情報・参考リンク

- [Official source](canonical URL)
  - DS検定・実務で確認したいポイントを1〜2文で説明。
```

Place it before `## 対応スキル項目（...）` when that section exists, or near the end before the DS footer / related-article block.

This heading is optional. Do not add it when the source would not improve the page.

## Freshness And Supersession Check

For any versioned or normative source:

- check whether a newer version exists;
- check whether the current source explicitly obsoletes / supersedes an older one;
- check revision / publication dates when material;
- prefer canonical, current official URLs;
- avoid tracking parameters;
- distinguish an archived page from the current official page;
- when current and historical wording differ, make the current rule primary in the article body.

For IETF sources, inspect RFC status rather than assuming a well-known RFC number is still current.

For laws / public guidance, check the responsible authority rather than relying on a secondary article.

For research papers, publication age alone does not make a source stale when the claim is about the origin of the named method.

## Verification Before Editing

Before adding or replacing a source:

1. read the target article;
2. identify the exact claim the source will support;
3. confirm the source title / organization / authors / method match the claim;
4. use the strongest canonical URL available;
5. check whether the article already contains an equivalent source;
6. check nearby comparison / summary pages when consistency matters;
7. avoid copying long text from the source;
8. write the article's explanation in this site's beginner-friendly voice.

When current web access is available, verify current standards / normative sources on the web rather than relying only on repository text.

## Audit Workflow

For a multi-article audit:

1. Define the target section and source type.
2. Inventory relevant articles.
3. Identify current source coverage.
4. Separate candidates into:
   - missing high-value primary source;
   - stale / superseded source;
   - already sufficient;
   - source exists but addition unnecessary.
5. Prioritize:
   - stale current-authority references;
   - named methods / protocols with direct defining sources;
   - comparison articles where primary sources clarify the distinction;
   - lower-value optional additions last.
6. Edit only high-value candidates.
7. For superseded identifiers, run a repository-wide search for stale references.
8. Update `last_modified_at` for meaningful article changes.
9. Confirm GitHub Pages build status after repository-wide or multi-file edits.

## Source Commentary Style

Keep source annotations short and learner-focused.

Good:

```md
- [RFC 7296 - Internet Key Exchange Protocol Version 2 (IKEv2)](...)
  - IKEv2を、相互認証とSAの確立・維持を行う仕組みとして定義しています。
```

Good:

```md
- [Attention Is All You Need｜NeurIPS](...)
  - Transformerの原論文です。Self-AttentionとMulti-Head Attentionを中核にしています。
```

Avoid:

- long bibliographic descriptions unrelated to exam judgment;
- copying abstracts;
- listing many papers without explaining why they matter;
- adding paper history that the learner does not need.

## Final Quality Check

Before finishing a source-driven edit, confirm:

- the source supports the claim actually made;
- current authority is used where current behavior / rules matter;
- original research is used where method provenance matters;
- no obsolete rule is presented as current;
- no unnecessary source was added;
- article readability did not get worse;
- exam judgment and confusion-prevention remain easy to find;
- source headings follow the section-specific article conventions;
- Markdown / Liquid remains GitHub Pages compatible;
- meaningful edits update `last_modified_at`;
- related pages were checked when a source was superseded;
- the latest Pages build is checked after multi-file updates.

## Final Report For Source Audits

Briefly report:

- audit scope;
- articles updated;
- authoritative / primary sources added or refreshed;
- important candidates intentionally left unchanged and why;
- any superseded source identifiers found;
- latest GitHub Pages build status when relevant.

Do not claim that every page needs a primary source.

A successful audit may legitimately conclude that some articles should remain unchanged.
