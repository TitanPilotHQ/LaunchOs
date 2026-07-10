# Enterprise Demo Playbook

## Goal

Move a qualified Head of Trading from curiosity to a paid AI Desk Audit by proving one thing: Titan Pilot can reconstruct and govern an AI-assisted trading decision better than the desk can today.

## Audience

Primary:

- Head of Trading

Expected attendees:

- risk officer
- compliance reviewer
- CTO/engineering lead
- discretionary trader or desk lead

## Demo Principles

- use a real, sanitized certified decision
- no slides after minute two
- show refusal before execution
- show the AI being caught
- show the deterministic score
- run one replay proof live
- never discuss expected returns
- never improvise public claims

## Required Environment

- protected read-only demo instance
- known-good certified fixtures
- Evidence Explorer
- Decision History
- Replay Explorer
- AI Budget Monitor
- Health Dashboard
- backup screen recording
- offline PDF evidence pack

Pre-demo checklist:

- health green
- fixture links tested
- no sensitive identifiers visible
- browser notifications disabled
- local clock set to UTC display
- zoom and resolution tested
- backup path ready
- attendee roles known

## 30-Minute Demo

### 0:00–2:00 — The Category

One slide only:

> Your desk already uses AI. Can you prove what it told your traders?

Say:

“Titan Pilot is not a signal product. It is the system of record for AI trading decisions.”

Ask one question:

“How would you reconstruct an AI-influenced decision from three months ago today?”

### 2:00–9:00 — Evidence Explorer

Open one real decision.

Show in order:

1. as-of timestamp
2. stored dossier
3. cited analyst thesis
4. machine validation
5. Devil’s Advocate objections
6. deterministic score waterfall
7. final skip/veto/proposal outcome
8. provenance hashes and versions

Narrative:

“The model is allowed to make an argument. It is not allowed to invent its evidence or calculate the final authority.”

### 9:00–14:00 — Show AI Being Caught

Open a historical rejected output.

Show:

- claimed field/value
- actual stored dossier value
- validator rejection
- closed reason code
- no downstream score or signal

Narrative:

“We do not hide model failures. The failure record is part of the product.”

### 14:00–18:00 — Adversarial Review and Refusal

Open a decision with a serious or fatal objection.

Show:

- analyst direction
- objections
- objection severity
- deterministic penalty or forced veto
- final no-trade result

Narrative:

“The default action is nothing. Refusal is a first-class outcome.”

### 18:00–22:00 — Budget and Operator Governance

Show:

- day/month caps
- call-level cost
- pre-token refusal behavior
- exact ledger reconciliation
- approval provenance design

Do not imply current autonomous customer execution.

### 22:00–26:00 — Replay Proof

Run or show a recent replay verification.

Explain:

- events are the source of truth
- projections are rebuilt from the same production fold
- live and rebuilt state are compared
- a mismatch is a safety incident

Narrative:

“This is not a dashboard claiming the system is correct. This is the system running the proof.”

### 26:00–30:00 — Commercial Ask

Ask:

“Would it be useful to map your current AI workflows against this evidence standard?”

Offer:

- two-week AI Desk Audit
- fixed scope
- fixed fee
- no execution access required
- committee-ready gap report

Do not end with “thoughts?” End with a concrete scheduling question.

## 45-Minute Version

Add:

- architecture/security overview
- data residency model
- failure-mode catalogue
- audit export
- current-vs-target workflow mapping
- 10-minute discovery section

## 90-Minute Technical Due-Diligence Version

Add:

- event taxonomy
- source-of-truth map
- replay mechanics
- security controls
- provider failover
- backup/PITR evidence
- prompt/version governance
- known limitations and debt
- live CLI or API proof where safe

## Role-Specific Branches

### Risk Officer

Spend more time on:

- vetoes
- kill switch
- operator audit
- complete skip history
- policy enforcement

### Compliance Reviewer

Spend more time on:

- immutable records
- prompt versions
- data retention
- exportability
- human approval provenance

### CTO

Spend more time on:

- architecture boundaries
- single-tenant deployment
- APIs
- identity and tailnet access
- provider abstraction

### Head of Trading

Spend more time on:

- trader workflow
- evidence review speed
- shadow deployment
- approval friction
- desk-level adoption

## Objection Handling

### “This doesn’t prove the AI is profitable.”

Correct. Titan Pilot proves what the AI said, what evidence it used, what challenged it, and what the desk decided. Alpha remains the desk’s responsibility.

### “We can store prompts in Slack.”

A transcript does not provide deterministic scoring, source validation, approval provenance, risk authority, or replayable system state.

### “Our traders will bypass it.”

The audit identifies unsanctioned workflows first. Adoption succeeds when the governed path is faster and more defensible than the private path.

### “We need live execution.”

Start with shadow evidence. Execution authority should expand only after governance and evaluation are proven.

## Failure Plan

If live demo API fails:

1. state the failure plainly
2. show timestamped last-known state
3. use the certified offline fixture
4. show Health Dashboard failure semantics
5. do not pretend the live system is healthy

A calm, honest failure can strengthen the product story.

## Post-Demo Follow-Up Pack

Send only relevant artifacts:

- one-page category brief
- sanitized decision record
- security summary
- AI Desk Audit scope
- meeting-specific unanswered questions

## Success Criteria

A successful demo ends with:

- confirmed current AI usage
- named governance pain
- named executive sponsor
- agreed audit scope
- date for commercial follow-up

Applause is not a success criterion.