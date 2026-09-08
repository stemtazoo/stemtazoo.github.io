#!/usr/bin/env python3
"""Migrate reviewed legacy AI-utilization security pages to ver.6 supplemental blocks.

ver.6 Foundation ★1 has a direct security item for malware risk, but does not
have direct ★1 items for these authentication/access-control/crypto concepts.
Keep the articles as useful Foundation/security supplemental learning instead of
forcing them onto an unrelated official item.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"

FILES = {
    "mfa.md": "認証の補助学習",
    "oauth.md": "認可・アクセス委任の補助学習",
    "ssl-tls.md": "通信暗号化の補助学習",
    "iam-policy.md": "アクセス制御の補助学習",
    "digital-signature2.md": "電子署名・公開鍵暗号の補助学習",
    "least-privilege.md": "アクセス制御原則の補助学習",
    "zero-trust.md": "セキュリティ設計の補助学習",
}

HEADING_RE = re.compile(r"^## 対応スキル項目（AI利活用スキルシート）\s*$", re.MULTILINE)


def front_matter(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return data
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def bounds(text: str, match: re.Match[str]) -> tuple[int, int]:
    after = match.end()
    nxt = re.search(r"^##\s+", text[after:], re.MULTILINE)
    end = after + nxt.start() if nxt else len(text)
    return match.start(), end


def block(position: str) -> str:
    return "\n".join([
        "## 対応スキル項目（ver.6 基盤）",
        "",
        f"- **位置づけ**：{position}",
        "- **関連領域**：ITセキュリティ",
        "- **★1直接対応**：なし",
        "- ver.6 基盤の★1ではマルウェア等による深刻なリスク理解が直接項目ですが、この用語自体は★1の直接項目ではありません。セキュリティ判断を補う関連テーマとして整理します。",
        "- [ver.6 ★1スキルチェックで確認する](/ds/foundation-skillcheck/)",
        "",
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    changed: list[str] = []
    already: list[str] = []
    for filename, position in FILES.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)
        if meta.get("ds_area") != "foundation" or meta.get("ds_section") != "security":
            raise SystemExit(
                f"{filename}: metadata mismatch {meta.get('ds_area')}/{meta.get('ds_section')}"
            )

        match = HEADING_RE.search(text)
        if not match:
            if "## 対応スキル項目（ver.6 基盤）" in text and "**★1直接対応**：なし" in text:
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: expected legacy AI-utilization block not found")

        start, end = bounds(text, match)
        new_text = text[:start] + block(position) + text[end:]
        changed.append(filename)
        if args.write:
            path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: changed={len(changed)}, already={len(already)}")
    for filename in changed:
        print(f"CHANGE {filename}")
    for filename in already:
        print(f"ALREADY {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
