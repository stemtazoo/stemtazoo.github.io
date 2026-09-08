# SG Tag Rules

This file is written in English for Codex readability. However, SG article content must be written in Japanese unless the user explicitly requests otherwise.

For SG articles, select roughly 3-5 values for `tags`.

## Basic Rules

- Always include `sg` on every SG page.
- Always include exactly one primary category tag.
- Add 1-3 concrete tags according to the article content.
- Do not over-tag pages.
- If 科目B case judgment is central, prioritize `risk_assessment`, `vendor_management`, `security_training`, or `it_security_operations` as candidates.
- To avoid conflicts with the existing tag design, check existing `pages/sg` articles before deciding tags when needed.
- Primary category tags are the source of truth for SG category-page automatic listings.
- Do not add multiple primary category tags just because an article is related to several categories. Use concrete tags and internal links for secondary relationships.

## Primary Category Tags

```yaml
sg-security-overview
sg-security-management
sg-security-measures
sg-security-law
sg-technology
sg-management
sg-strategy
```

Exactly one of the tags above must be present on each normal SG article.

## Deprecated Broad Tags

The following broad legacy tags may still exist on older SG articles, but do not use them as primary categories in new or updated articles.

```text
security_overview  -> sg-security-overview
security_management -> sg-security-management
security_measures  -> sg-security-measures
security_law       -> sg-security-law
technology         -> sg-technology
management         -> sg-management
strategy           -> sg-strategy
```

When migrating an older article:

1. Read the article role and choose one primary category.
2. Add the corresponding current primary tag.
3. Remove obsolete broad legacy tags when they only duplicate or conflict with the chosen primary category.
4. Keep concrete tags such as `network`, `risk_assessment`, or `privacy_law` when they still describe the article accurately.
5. Do not migrate by blind global replacement because some legacy articles contain more than one old broad tag and require classification judgment.

## Concrete Tag Candidates

```yaml
cia
threat_vulnerability
crypto_auth
asset_management
risk_assessment
isms
incident_management
csirt
malware
unauthorized_access
data_leakage
access_control
security_awareness
privacy_law
network
database
system_architecture
system_audit
service_management
project_management
business_management
system_strategy
system_planning
it_security_operations
vendor_management
security_training
```

## Tag Selection Examples

Cookie article:

```yaml
tags: [sg, sg-technology, web, network, authentication]
```

Law article:

```yaml
tags: [sg, sg-security-law, privacy_law]
```

Risk management article:

```yaml
tags: [sg, sg-security-management, risk_assessment, asset_management]
```

## Audit Before Saving

Run the SG tag audit when creating or refactoring SG articles:

```bash
python scripts/audit_sg_primary_tags.py --strict
```

The audit reports:

- `NO_PRIMARY`: no current primary category tag is present.
- `MULTI_PRIMARY`: more than one current primary category tag is present.
- `LEGACY_TAG`: an old broad tag is still present and should be reviewed.
- `MISSING_TAGS` / `MISSING_SG`: front matter does not meet the SG tag baseline.

A legacy-tag warning does not always mean that a mechanical replacement is safe. Choose the article's single primary role first, then migrate its tags.
