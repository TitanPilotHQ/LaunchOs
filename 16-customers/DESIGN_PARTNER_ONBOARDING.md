# Design Partner Onboarding Playbook

## Objective

Move a signed design partner from contract to a useful, governed shadow deployment without creating execution liability or open-ended consulting scope.

## Program Boundaries

Included:

- current AI-workflow assessment
- single-tenant shadow deployment
- approved market-data integration
- configured initial symbol set
- Evidence Explorer access
- governance baseline
- monthly review

Excluded unless separately contracted:

- live autonomous execution
- returns guarantees
- custom alpha research
- discretionary trading advice
- unrestricted feature development
- handling customer funds

## Success Definition

A partner is successfully onboarded when:

1. one sanctioned AI decision workflow is live in shadow mode
2. every eligible decision produces an auditable outcome
3. risk/compliance can review a complete record
4. the desk has documented operators and responsibilities
5. no production trading authority has been granted
6. first monthly governance report is accepted

## Phase 0 — Commercial Handoff

Required artifacts:

- signed agreement
- data-processing terms
- named sponsor
- named technical owner
- named risk/compliance reviewer
- scope and symbol set
- deployment boundary
- success criteria
- referenceability terms

No technical onboarding begins without a named executive sponsor.

## Phase 1 — Discovery Workshop

90 minutes.

Agenda:

- current AI usage
- current decision process
- data sources
- review/approval process
- risk controls
- retention requirements
- security constraints
- committee/DDQ obligations
- target workflow

Outputs:

- current-state workflow map
- target-state workflow map
- integration list
- risk register
- owner matrix

## Phase 2 — Security and Data Boundary

Document:

- hosting location
- single-tenant instance owner
- identity method
- tailnet/device access
- data that enters TITAN
- data that never enters TITAN
- model provider and key ownership
- backup destination
- retention period
- deletion/export path
- incident contacts

Required approval from customer security owner before credentials are provisioned.

## Phase 3 — Environment Provisioning

Checklist:

- instance created
- OS hardened
- database local-only
- service identities created
- secrets installed outside chat/git
- offsite backup configured
- alerts configured
- health green
- restore verification passed
- customer operator access tested

No customer market data is connected until restore verification passes.

## Phase 4 — Data Integration

Start read-only.

Verify:

- symbol/timeframe mapping
- clock handling
- market-data freshness
- calendar source
- spread/cost semantics
- source quality
- backfill completeness
- canonical dossier fixture

Customer signs off that the dossier represents their intended market context. Citation validation proves provenance, not economic truth.

## Phase 5 — AI Configuration

Document:

- approved providers
- approved models
- provider key ownership
- prompt versions
- budget caps
- day/month limits
- timeout behavior
- fallback policy
- data-residency implications

Run:

- provider smoke
- contract regression
- budget refusal drill
- malformed-output rejection drill

## Phase 6 — Shadow Enablement

Gate:

- health green
- verify/replay green
- calendar fresh
- account/data source reachable
- AI budget configured
- prompts pinned
- no execution route authorized
- alerts confirmed

Begin with a defined soak window and exit criteria.

## Phase 7 — Operator Training

Training modules:

1. Landing and system state
2. Signal Inbox
3. Evidence Explorer
4. Decision History
5. Replay
6. AI Budget Monitor
7. Health Dashboard
8. Incident escalation

Every operator must demonstrate:

- finding a cited dossier field
- identifying model vs deterministic output
- explaining a skip
- locating an event by correlation id
- exporting a decision record
- recognizing stale or degraded state

## Phase 8 — Governance Baseline

Produce:

- first 7-day decision summary
- validation statistics
- skip reasons
- provider spend
- prompt/model versions
- operational health
- open risks
- customer action items

Risk/compliance reviewer signs acceptance or records exceptions.

## Monthly Governance Review

Agenda:

- usage and coverage
- validation failures
- model/provider changes
- prompt changes
- budget
- refusal/veto trends
- operator review time
- incidents
- drift/replay status
- upcoming changes

No prompt, threshold, or provider change is treated as routine. Each has an owner, rationale, version, and evaluation plan.

## Customer Responsibility Matrix

Customer owns:

- trading strategy and alpha
- market-data rights
- human decisions
- regulatory obligations
- user access approval
- execution systems

Titan Pilot owns:

- evidence pipeline
- validation contracts
- replayability
- budget enforcement
- platform operations within contracted scope
- incident reporting

Shared:

- dossier correctness review
- workflow adoption
- change governance
- success measurement

## Escalation Levels

P0:

- integrity/replay failure
- secret exposure
- unauthorized execution path
- unexplained data divergence

P1:

- sustained service outage
- calendar/data stale beyond threshold
- provider failure without fallback
- backup/restore verification failure

P2:

- UI defect
- report discrepancy without system-of-record impact
- non-critical workflow friction

## Exit or Offboarding

Provide:

- final export
- event/decision archive
- configuration inventory
- credential revocation evidence
- backup-retention agreement
- access removal
- deletion certificate where applicable

## Definition of Done

Onboarding closes only when:

- customer sponsor accepts the baseline
- operators are trained
- shadow coverage meets target
- no P0/P1 issue is open
- evidence exports work
- monthly review is scheduled
- scope for any next stage is separately approved