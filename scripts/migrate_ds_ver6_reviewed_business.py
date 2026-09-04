#!/usr/bin/env python3
"""Add DS ver.6 metadata to individually reviewed legacy DS articles.

Only exact filenames listed in REVIEWED are changed. Existing categories, tags,
prev/next, dates, and article bodies are preserved.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"

REVIEWED = {
    "five-forces-analysis.md": ("value-creation", "business-design"),
    "customer-journey.md": ("value-creation", "business-design"),
    "design-thinking.md": ("value-creation", "business-design"),
    "agile-development.md": ("value-creation", "project-management"),
    "scrum.md": ("value-creation", "project-management"),
    "critical-path.md": ("value-creation", "project-management"),
    "compliance-risk.md": ("foundation", "action-norms"),
    "internal-control.md": ("value-creation", "governance-risk"),
    "bcp.md": ("value-creation", "governance-risk"),
    "operational-risk.md": ("value-creation", "governance-risk"),
    "reputation-risk.md": ("value-creation", "governance-risk"),
    "risk-management.md": ("value-creation", "governance-risk"),
    "cps.md": ("value-creation", "technology-social-trends"),
    "industry4-0.md": ("value-creation", "technology-social-trends"),
    "society5.md": ("value-creation", "technology-social-trends"),
    "social-data-ai-utilization.md": ("value-creation", "technology-social-trends"),
    "rfm-analysis.md": ("datascience", "modeling"),
    "feature.md": ("datascience", "data-preparation"),
    "estimator-properties.md": ("datascience", "statistics"),
    "power-law.md": ("datascience", "statistics"),
    "inheritance.md": ("dataengineering", "programming"),
    "encapsulation.md": ("dataengineering", "programming"),
    "polymorphism.md": ("dataengineering", "programming"),
    "dunning-kruger-effect.md": ("foundation", "logical-thinking"),
    "cognitive-bias.md": ("foundation", "logical-thinking"),
    "confirmation-bias.md": ("foundation", "logical-thinking"),
    "evidence-based.md": ("foundation", "data-understanding"),
    "primary-data.md": ("foundation", "data-understanding"),
    "primary-secondary-data.md": ("foundation", "data-understanding"),
    "mfa.md": ("foundation", "security"),
    "oauth.md": ("foundation", "security"),
    "pki.md": ("foundation", "security"),
    "rbac.md": ("foundation", "security"),
    "malware.md": ("foundation", "security"),
    "ssl-tls.md": ("foundation", "security"),
    "vpn-ssh.md": ("foundation", "security"),
    "zero-trust.md": ("foundation", "security"),
    "iam-policy.md": ("foundation", "security"),
    "hash-function.md": ("foundation", "security"),
    "publickey-vs-symmetric.md": ("foundation", "security"),
    "digital-signature.md": ("foundation", "security"),
    "digital-signature2.md": ("foundation", "security"),
    "least-privilege.md": ("foundation", "security"),
    "hash-vs-encryption.md": ("foundation", "security"),
    "rainbow-table-attack.md": ("foundation", "security"),
    "key-stretching.md": ("foundation", "security"),
    "access-control-list.md": ("foundation", "security"),
    "authentication-authorization.md": ("foundation", "security"),
    "authentication-vs-authorization.md": ("foundation", "security"),
    "gdpr.md": ("foundation", "action-norms"),
    "ccpa.md": ("foundation", "action-norms"),
    "elsi.md": ("foundation", "action-norms"),
    "opt-out.md": ("foundation", "action-norms"),
    "third-party-provision.md": ("foundation", "action-norms"),
    "anonymized-information.md": ("foundation", "action-norms"),
    "personal-identifier-code.md": ("foundation", "action-norms"),
    "pseudonymized-information.md": ("foundation", "action-norms"),
    "sensitive-personal-information.md": ("foundation", "action-norms"),
}


def migrate(path: Path, area: str, section: str) -> bool:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise RuntimeError(f"{path}: invalid front matter")
    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise RuntimeError(f"{path}: missing front matter end") from exc

    fm = lines[1:end]
    existing_area = [line for line in fm if line.startswith("ds_area:")]
    existing_section = [line for line in fm if line.startswith("ds_section:")]
    if existing_area or existing_section:
        expected_area = f"ds_area: {area}"
        expected_section = f"ds_section: {section}"
        if existing_area == [expected_area] and existing_section == [expected_section]:
            return False
        raise RuntimeError(f"{path}: existing DS metadata differs from reviewed mapping")

    tag_pos = next((i for i, line in enumerate(lines[:end]) if line.startswith("tags:")), None)
    if tag_pos is None:
        raise RuntimeError(f"{path}: tags line not found")

    lines[tag_pos + 1:tag_pos + 1] = [f"ds_area: {area}", f"ds_section: {section}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def main() -> int:
    changed = []
    for filename, (area, section) in REVIEWED.items():
        path = DS_DIR / filename
        if not path.exists():
            raise RuntimeError(f"missing reviewed file: {path}")
        if migrate(path, area, section):
            changed.append(filename)
            print(f"UPDATED {filename}: {area}/{section}")
    print(f"Changed {len(changed)} reviewed article(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
