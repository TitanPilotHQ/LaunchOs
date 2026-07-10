# Public Claims Governance

## Rule

TitanPilot publishes evidence, not adjectives. No measurable claim may appear on the website, deck, demo, social media, research report, proposal, or sales email without a traceable source.

## Claim Record

Every claim must record:

- claim ID
- exact wording
- claim type: measured / architectural / certification / forecast / opinion
- source repository
- source file or event/report identifier
- evidence date
- scope and limitations
- public-safe wording
- owner
- reviewer
- expiry or next-review date
- allowed channels
- status: draft / approved / retired / corrected

## Allowed Claim Classes

### Measured

Examples: latency, replay duration, test count, soak duration, validation rate. Must include the measurement window and environment.

### Architectural

Examples: read surface holds a SELECT-only database role; AI modules cannot import execution. Must be backed by code, tests, grants, or an ADR.

### Certification

Examples: Phase C passed a 48-hour production shadow soak. Must link to the certification report and state exactly what was certified.

### Forecast

Examples: revenue plan, customer target, roadmap timing. Must be labeled as a target or hypothesis, never fact.

### Opinion

Examples: category thesis or strategic belief. Must not be formatted as measured proof.

## Forbidden Claims

Never publish:

- guaranteed returns
- profitability claims without independently reviewable forward evidence
- market-beating claims
- fabricated customer logos, testimonials, ratings, or adoption counts
- regulatory approval or compliance certification not actually held
- institutional-grade as an unsupported adjective
- autonomous trading as current functionality when the certified mode is shadow or supervised
- fake live prices, scores, users, revenue, or event counts

## Approval Workflow

1. Draft claim in the register.
2. Locate primary evidence in Titan or Research.
3. Record scope and limitations.
4. Produce public-safe wording.
5. Review for technical accuracy.
6. Review for legal/regulatory risk when needed.
7. Approve specific channels.
8. Publish.
9. Revalidate on expiry or when source behavior changes.

## Correction Policy

If a published claim becomes inaccurate:

1. remove or correct it immediately
2. preserve the previous wording in the claim history
3. record cause, date, and affected channels
4. correct derivative assets
5. publish a correction when the original claim was material

## Initial Claims Register

| ID | Claim | Type | Status | Evidence needed |
|---|---|---|---|---|
| CLM-001 | Phase C completed a 48-hour production shadow soak | Certification | Approved in principle | Phase C certification report |
| CLM-002 | 0 validation failures occurred in the certified soak window | Measured | Approved in principle | event/call census and report |
| CLM-003 | replay verification passed throughout the certified window | Measured | Approved in principle | scheduled and final verify results |
| CLM-004 | operator read surface uses a SELECT-only database role | Architectural | Approved in principle | role grants and certification |
| CLM-005 | U0-U4 contain no approval or write surface | Architectural | Approved in principle | API capability flags and tests |
| CLM-006 | TITAN does not promise returns | Policy | Approved | commercial strategy |

`Approved in principle` means the claim is directionally accepted but the Portfolio repository must still cite the exact source and evidence date before publication.