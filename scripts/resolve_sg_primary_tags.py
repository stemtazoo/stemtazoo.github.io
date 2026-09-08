#!/usr/bin/env python3
"""Apply reviewed SG primary-category tag overrides.

This script is intentionally explicit. Each file in OVERRIDES was reviewed by
article role and nearby SG category conventions. It removes all current primary
category tags and deprecated broad category aliases, then inserts exactly one
reviewed primary tag. Other concrete tags are preserved.

Default mode is dry-run. Use --apply to write changes.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PRIMARY_TAGS = {
    "sg-security-overview",
    "sg-security-management",
    "sg-security-measures",
    "sg-security-law",
    "sg-technology",
    "sg-management",
    "sg-strategy",
}

LEGACY_TAGS = {
    "security_overview",
    "security_management",
    "security_measures",
    "security_law",
    "technology",
    "management",
    "strategy",
}

OVERRIDES = {
    # SG / exam overview
    "exam-scope.md": "sg-security-overview",
    "information-security-management-exam.md": "sg-security-overview",
    "sg-exam-outline-study.md": "sg-security-overview",
    "study-method.md": "sg-security-overview",

    # Security-management / governance / operations
    "csirt-material-official.md": "sg-security-management",
    "dependency-vulnerability-management.md": "sg-security-management",
    "error-proofing.md": "sg-security-management",
    "evidence-preservation-guideline-official.md": "sg-security-management",
    "government-unified-security-standard.md": "sg-security-management",
    "isms-users-guide-official.md": "sg-security-management",
    "patch-management.md": "sg-security-management",
    "pdca.md": "sg-security-management",
    "psirt.md": "sg-security-management",
    "sg-risk-level.md": "sg-security-management",
    "sg_information_security_policy.md": "sg-security-management",
    "sg_sme_security_guideline.md": "sg-security-management",
    "unauthorized-access-countermeasure-standard.md": "sg-security-management",
    "vendor-outsourcing-summary.md": "sg-security-management",
    "vulnerability-information-jvn-cve-cvss.md": "sg-security-management",

    # Technical security measures / attacks / secure development
    "bagle-worm.md": "sg-security-measures",
    "cryptrec-list.md": "sg-security-measures",
    "dast.md": "sg-security-measures",
    "devsecops.md": "sg-security-measures",
    "dns-amplification-attack.md": "sg-security-measures",
    "e-government-recommended-crypto-list.md": "sg-security-measures",
    "monitoring-crypto-list.md": "sg-security-measures",
    "ntp-reflection-attack.md": "sg-security-measures",
    "phishing.md": "sg-security-measures",
    "recommended-candidate-crypto-list.md": "sg-security-measures",
    "sast.md": "sg-security-measures",
    "secure-coding.md": "sg-security-measures",
    "security-testing-types.md": "sg-security-measures",
    "shift-left.md": "sg-security-measures",
    "source-code-review.md": "sg-security-measures",
    "static-dynamic-analysis.md": "sg-security-measures",
    "supporting-utilities.md": "sg-security-measures",
    "udp-amplification-attack.md": "sg-security-measures",
    "vulnerability-assessment-penetration-test.md": "sg-security-measures",
    "vulnerability-cheatsheet.md": "sg-security-measures",
    "wanna-cryptor.md": "sg-security-measures",
    "zero-day-attack.md": "sg-security-measures",
    "sg-backdoor.md": "sg-security-measures",

    # Law / privacy / IP / contracts
    "business-model-patent.md": "sg-security-law",
    "denshi-keisanki-sonkai-gyomu-bogai.md": "sg-security-law",
    "intellectual-property-rights.md": "sg-security-law",
    "jis-q-15001.md": "sg-security-law",
    "online-sales-contract.md": "sg-security-law",
    "patent-law.md": "sg-security-law",
    "patent-vs-trade-secret.md": "sg-security-law",
    "personal-information-protection-management-system.md": "sg-security-law",
    "privacy-law-vs-jis-q-15001.md": "sg-security-law",
    "privacy-mark.md": "sg-security-law",
    "product_liability_law_sg.md": "sg-security-law",
    "public-interest-whistleblower-protection-act.md": "sg-security-law",
    "sg_cross_license.md": "sg-security-law",
    "unfair-competition-definition.md": "sg-security-law",

    # Technology / networks / databases / product evaluation
    "data-flow-diagram.md": "sg-technology",
    "data-model.md": "sg-technology",
    "database-normalization.md": "sg-technology",
    "eal.md": "sg-technology",
    "er-diagram-vs-dfd.md": "sg-technology",
    "er-diagram.md": "sg-technology",
    "forward-reverse-proxy.md": "sg-technology",
    "ipsec-ah.md": "sg-technology",
    "ipsec-ike.md": "sg-technology",
    "ipsec-sa.md": "sg-technology",
    "ipsec.md": "sg-technology",
    "jisec.md": "sg-technology",
    "ntp.md": "sg-technology",
    "primary-key-foreign-key.md": "sg-technology",
    "proxy-arp.md": "sg-technology",
    "sg_d_terminal.md": "sg-technology",
    "sg_hdmi.md": "sg-technology",
    "sg_ieee1394.md": "sg-technology",
    "software-inspection.md": "sg-technology",
    "walkthrough.md": "sg-technology",

    # Management / audit / process control
    "assurance-advisory-audit.md": "sg-management",
    "audit-basic.md": "sg-management",
    "audit-working-papers.md": "sg-management",
    "change-management.md": "sg-management",
    "cicd.md": "sg-management",
    "information-security-audit-standard.md": "sg-management",
    "it-control-objectives.md": "sg-management",
    "security-audit-vs-system-audit.md": "sg-management",
    "security-audit.md": "sg-management",
    "sg-control-total.md": "sg-management",
    "sg-edit-validation-check.md": "sg-management",
    "sg-run-to-run-control.md": "sg-management",
    "sg_internal_audit.md": "sg-management",

    # Strategy / business management
    "sg_csf.md": "sg-strategy",
    "sg_mbo.md": "sg-strategy",

    # Corrections after the safe legacy migration: align with nearby articles.
    "encryption-vs-hash.md": "sg-security-overview",
    "hmac.md": "sg-security-overview",
    "mac-message-authentication-code.md": "sg-security-overview",
    "mac-vs-digital-signature.md": "sg-security-overview",
    "message-digest.md": "sg-security-overview",
    "sha-1.md": "sg-security-overview",
    "sha-2.md": "sg-security-overview",
    "tamper-detection.md": "sg-security-overview",
    "nda-trade-secret.md": "sg-security-law",
    "trade-secret.md": "sg-security-law",
    "unfair-competition-prevention-act.md": "sg-security-law",
}

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TAGS_LINE_RE = re.compile(r"^tags:\s*\[(.*?)\]\s*$", re.MULTILINE)


def split_tags(raw: str) -> list[str]:
    return [
        item.strip().strip("'\"")
        for item in raw.split(",")
        if item.strip()
    ]


def format_tags(tags: list[str]) -> str:
    return "tags: [" + ", ".join(tags) + "]"


def normalize(tags: list[str], primary: str) -> list[str]:
    kept = [
        tag
        for tag in tags
        if tag not in PRIMARY_TAGS and tag not in LEGACY_TAGS
    ]

    if "sg" in kept:
        sg_index = kept.index("sg")
        kept.insert(sg_index + 1, primary)
    else:
        kept.insert(0, primary)
        kept.insert(0, "sg")

    # Preserve order while removing accidental duplicates.
    result: list[str] = []
    seen: set[str] = set()
    for tag in kept:
        if tag not in seen:
            result.append(tag)
            seen.add(tag)
    return result


def process(path: Path, primary: str, apply: bool) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    front = FRONT_MATTER_RE.search(text)
    if not front:
        return False, "no front matter"

    match = TAGS_LINE_RE.search(front.group(1))
    if not match:
        return False, "no inline tags list"

    tags = split_tags(match.group(1))
    new_tags = normalize(tags, primary)
    if new_tags == tags:
        return False, "already normalized"

    old_line = match.group(0)
    new_line = format_tags(new_tags)
    new_text = text.replace(old_line, new_line, 1)
    if apply:
        path.write_text(new_text, encoding="utf-8")
    return True, f"{tags} -> {new_tags}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="pages/sg")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    root = Path(args.root)
    changed = 0
    skipped = 0

    for filename, primary in OVERRIDES.items():
        path = root / filename
        if not path.exists():
            print(f"MISSING      {path}")
            skipped += 1
            continue

        did_change, detail = process(path, primary, args.apply)
        if did_change:
            changed += 1
            prefix = "UPDATED" if args.apply else "WOULD_UPDATE"
            print(f"{prefix:12} {path} -> {primary}")
        else:
            skipped += 1
            print(f"SKIP         {path} -> {detail}")

    print(f"\nchanged={changed} skipped={skipped} mode={'apply' if args.apply else 'dry-run'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
