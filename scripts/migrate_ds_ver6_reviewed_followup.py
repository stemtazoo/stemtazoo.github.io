#!/usr/bin/env python3
"""Apply additional individually reviewed DS ver.6 mappings.

This follow-up batch reuses the guarded migration/correction helpers from the
main reviewed migration script so existing metadata is never overwritten
without an explicit expected source mapping.
"""

try:
    from scripts.migrate_ds_ver6_reviewed_business import DS_DIR, migrate, correct
except ModuleNotFoundError:
    from migrate_ds_ver6_reviewed_business import DS_DIR, migrate, correct

REVIEWED = {
    "data-literacy.md": ("foundation", "data-understanding"),
    "paper-structure.md": ("foundation", "logical-thinking"),
    "personally-related-information.md": ("foundation", "action-norms"),
    "ab-test.md": ("datascience", "statistics"),
    "anchoring-effect.md": ("foundation", "logical-thinking"),
    "availability-heuristic.md": ("foundation", "logical-thinking"),
    "average-methods-comparison.md": ("datascience", "modeling"),
    "bi-tool-functions.md": ("datascience", "data-understanding"),
    "business-logic-and-data-importance.md": ("foundation", "logical-thinking"),
    "cap-theorem.md": ("dataengineering", "data-storage"),
    "constructor.md": ("dataengineering", "programming"),
    "cps-iot-digitaltwin-cheatsheet.md": ("value-creation", "technology-social-trends"),
    "data-cube.md": ("datascience", "data-understanding"),
    "data-driven.md": ("foundation", "data-understanding"),
    "data-driven-management.md": ("value-creation", "business-design"),
    "data-transformation.md": ("datascience", "data-preparation"),
    "digital-twin.md": ("value-creation", "technology-social-trends"),
    "jupyter-r-usage.md": ("dataengineering", "environment-setup"),
    "k-anonymity.md": ("foundation", "action-norms"),
    "paired-vs-independent-data.md": ("datascience", "statistics"),
    "regular-expression-summary.md": ("datascience", "unstructured-data"),
    "stemming-vs-lemmatization.md": ("datascience", "unstructured-data"),
    "type1-type2-error.md": ("datascience", "statistics"),
}

CORRECTIONS = {
    "data-literacy-practice.md": (
        ("datascience", "statistics"),
        ("foundation", "data-understanding"),
    ),
}

EXPECTED = {**REVIEWED, **{name: target for name, (_, target) in CORRECTIONS.items()}}


def main() -> int:
    changed = []

    for filename, (area, section) in REVIEWED.items():
        path = DS_DIR / filename
        if not path.exists():
            raise RuntimeError(f"missing reviewed file: {path}")
        if migrate(path, area, section):
            changed.append(filename)
            print(f"UPDATED {filename}: {area}/{section}")

    for filename, (source, target) in CORRECTIONS.items():
        path = DS_DIR / filename
        if not path.exists():
            raise RuntimeError(f"missing correction file: {path}")
        if correct(path, source, target):
            changed.append(filename)
            print(
                f"CORRECTED {filename}: "
                f"{source[0]}/{source[1]} -> {target[0]}/{target[1]}"
            )

    print(f"Changed {len(changed)} follow-up reviewed article(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
