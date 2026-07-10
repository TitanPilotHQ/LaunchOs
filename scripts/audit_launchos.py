#!/usr/bin/env python3
"""Audit the LaunchOS repository for required operating-system artifacts.

The script is intentionally dependency-free and read-only. It exits non-zero
when a required domain, required document, empty markdown file, or obvious
placeholder is found.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_DOMAINS = [
    "01-brand", "02-story", "03-messaging", "04-positioning", "05-pricing",
    "06-website", "07-sales", "08-investors", "09-demo", "10-product",
    "11-roadmap", "12-design-system", "13-videos", "14-social", "15-pr",
    "16-customers", "17-case-studies", "18-legal", "19-finance",
    "20-operations", "21-partnerships", "22-competition",
    "23-market-research", "24-hiring", "25-assets",
]

REQUIRED_ROOT_FILES = ["README.md", "INDEX.md"]
PLACEHOLDER_PATTERNS = [
    re.compile(r"\blorem ipsum\b", re.I),
    re.compile(r"\bcoming soon\b", re.I),
    re.compile(r"\bto be written\b", re.I),
    re.compile(r"\bplaceholder\b", re.I),
    re.compile(r"\bTBD\b"),
]
MIN_MARKDOWN_CHARS = 120


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit LaunchOS completeness")
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    return parser.parse_args()


def audit(root: Path) -> list[str]:
    errors: list[str] = []

    for filename in REQUIRED_ROOT_FILES:
        if not (root / filename).is_file():
            errors.append(f"missing root file: {filename}")

    for domain in REQUIRED_DOMAINS:
        directory = root / domain
        if not directory.is_dir():
            errors.append(f"missing domain directory: {domain}")
            continue
        markdown_files = sorted(directory.rglob("*.md"))
        if not markdown_files:
            errors.append(f"domain has no markdown artifacts: {domain}")

    for path in sorted(root.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"not valid UTF-8: {path.relative_to(root)}")
            continue

        relative = path.relative_to(root)
        if len(text.strip()) < MIN_MARKDOWN_CHARS:
            errors.append(f"too little substantive content: {relative}")
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(text):
                errors.append(f"placeholder language '{pattern.pattern}' in {relative}")

    duplicate_titles: dict[str, list[Path]] = {}
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        title = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), "")
        if title:
            duplicate_titles.setdefault(title.casefold(), []).append(path)

    for title, paths in duplicate_titles.items():
        if len(paths) > 1:
            locations = ", ".join(str(p.relative_to(root)) for p in paths)
            errors.append(f"duplicate H1 title '{title}': {locations}")

    return errors


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    errors = audit(root)
    if errors:
        print("LaunchOS audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    domains = sum(1 for d in REQUIRED_DOMAINS if (root / d).is_dir())
    markdown = sum(1 for _ in root.rglob("*.md"))
    print(f"LaunchOS audit PASSED: {domains} domains, {markdown} markdown artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
