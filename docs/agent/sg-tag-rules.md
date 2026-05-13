# SG Tag Rules

SG記事の `tags` は、3〜5個を目安に厳選します。

## 基本ルール

- 全ページに必ず `sg` を入れる。
- 必ず「主分類タグ」を1つ入れる。
- 内容に応じて具体タグを1〜3個入れる。
- タグを付けすぎない。
- 科目Bのケース判断が中心なら、`risk_assessment` / `vendor_management` / `security_training` / `it_security_operations` を優先候補にする。
- 既存記事のタグ設計と矛盾しないように、必要なら既存 `pages/sg` の記事を確認してから決める。

## 主分類タグ

```yaml
sg-security-overview
sg-security-management
sg-security-measures
sg-security-law
sg-technology
sg-management
sg-strategy
```

## 具体タグ候補

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

## タグ選定例

Cookieの記事:

```yaml
tags: [sg, sg-technology, web, network, authentication]
```

法令記事:

```yaml
tags: [sg, sg-security-law, privacy_law]
```

リスク管理系の記事:

```yaml
tags: [sg, sg-security-management, risk_assessment, asset_management]
```
