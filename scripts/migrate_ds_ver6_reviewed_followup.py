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
