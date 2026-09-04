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
