#!/usr/bin/env python3
"""Create the Titan Pilot LaunchOS directory structure safely.

Run from the repository root:
    python3 scripts/scaffold_launchos.py

The script is idempotent: it creates missing directories and starter README
files without overwriting existing content unless --force is supplied.
"""

from __future__ import annotations

import argparse
from pathlib import Path

SECTIONS: dict[str, str] = {
    "01-brand": "Brand identity, visual rules, typography, voice, and governance.",
    "02-story": "Founder story, company narrative, product origin, and long-form storytelling.",
    "03-messaging": "Canonical messages, taglines, elevator pitches, FAQs, and copy systems.",
    "04-positioning": "Category definition, ideal customer, differentiation, and market position.",
    "05-pricing": "Packaging, pricing hypotheses, enterprise licensing, and monetization strategy.",
    "06-website": "Website architecture, copy, SEO/GEO/AEO, UX, implementation, and deployment.",
    "07-sales": "Sales motion, outreach, discovery, demos, objection handling, and pipeline.",
    "08-investors": "Pitch materials, diligence, fundraising narrative, metrics, and updates.",
    "09-demo": "Product demo scripts, scenarios, walkthroughs, recordings, and proof assets.",
    "10-product": "Product strategy, requirements, UX, roadmap inputs, and decision records.",
    "11-roadmap": "Company, product, engineering, launch, and commercial milestones.",
    "12-design-system": "Design tokens, components, interaction rules, accessibility, and motion.",
    "13-videos": "Launch films, storyboards, Veo prompts, voice-over, music, and editing notes.",
    "14-social": "LinkedIn, X, YouTube, content calendar, publishing, and analytics.",
    "15-pr": "Press kit, media narrative, announcements, founder profile, and outreach.",
    "16-customers": "Ideal customer profiles, interviews, feedback, onboarding, and success.",
    "17-case-studies": "Evidence-led case studies, outcomes, architecture stories, and templates.",
    "18-legal": "Legal checklists, terms, privacy, risk disclosures, and compliance planning.",
    "19-finance": "Budgets, forecasts, unit economics, runway, pricing models, and reporting.",
    "20-operations": "Company operations, review cadences, vendor management, and launch runbooks.",
    "21-partnerships": "Broker, prop-firm, data, cloud, media, and strategic partnership plans.",
    "22-competition": "Competitive research, battlecards, comparisons, and differentiation evidence.",
    "23-market-research": "Market sizing, trends, customer research, reports, and source notes.",
    "24-hiring": "Hiring roadmap, role scorecards, interview loops, onboarding, and culture.",
    "25-assets": "Approved logos, images, diagrams, screenshots, exports, and media inventory.",
}

README_TEMPLATE = """# {title}\n\n## Purpose\n\n{purpose}\n\n## Operating rule\n\nKeep this area evidence-led, current, and specific to Titan Pilot. Do not add invented traction, unsupported claims, or placeholder content.\n\n## Core files to add\n\n- `STATUS.md` — current state, owner, last review, and blockers\n- `TODO.md` — prioritized next actions with acceptance criteria\n- `NOTES.md` — research notes, raw inputs, and unresolved questions\n\n## Review cadence\n\nReview whenever a related company, product, commercial, or launch decision changes.\n"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--force", action="store_true", help="Overwrite generated README files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    created: list[str] = []
    skipped: list[str] = []

    for directory, purpose in SECTIONS.items():
        folder = root / directory
        folder.mkdir(parents=True, exist_ok=True)
        readme = folder / "README.md"
        title = directory.split("-", 1)[1].replace("-", " ").title()
        content = README_TEMPLATE.format(title=title, purpose=purpose)

        if readme.exists() and not args.force:
            skipped.append(str(readme.relative_to(root)))
            continue

        readme.write_text(content, encoding="utf-8")
        created.append(str(readme.relative_to(root)))

    print(f"Created or updated {len(created)} README files.")
    for item in created:
        print(f"  + {item}")
    if skipped:
        print(f"Skipped {len(skipped)} existing README files. Use --force to overwrite.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
