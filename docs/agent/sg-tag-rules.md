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
