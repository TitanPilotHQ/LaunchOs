# Investor Data Room Index

## Purpose

Define the minimum evidence package required before Titan Pilot accepts institutional diligence or raises capital.

The data room must prove three things:

1. the system exists and is technically disciplined
2. the company understands its commercial risks
3. management does not hide uncertainty behind marketing

## Access Levels

### Level 1 — Introductory

Available after a qualified first meeting:

- company overview
- category thesis
- product demo
- public architecture summary
- public certification summary
- commercial strategy summary
- founder biography

### Level 2 — Diligence

Available after mutual fit and NDA:

- detailed technical architecture
- Phase C and C.5 certification
- security audit
- disaster-recovery report
- roadmap
- financial model
- customer pipeline summary
- detailed competition analysis
- legal structure and IP schedule

### Level 3 — Confirmatory

Available during an active financing process:

- code-access protocol
- full cap table
- contracts
- bank statements
- detailed customer references
- vulnerability and incident register
- source-of-funds/use-of-funds
- insurance and counsel correspondence

Never grant unrestricted repository or production access as an introductory artifact.

## Folder Structure

```text
investor-data-room/
├── 00-index/
├── 01-corporate/
├── 02-team/
├── 03-product/
├── 04-technology/
├── 05-security-risk/
├── 06-market-competition/
├── 07-commercial/
├── 08-customers/
├── 09-financials/
├── 10-legal-ip/
├── 11-roadmap/
└── 12-fundraise/
```

## 00 — Index and Document Control

Required:

- master index
- document owner
- latest revision date
- confidentiality level
- source of truth
- unresolved gaps

Every document must have a date. “Current” is not a date.

## 01 — Corporate

- certificate of incorporation
- constitutional documents
- registered address
- share register
- cap table
- option pool
- board resolutions
- beneficial ownership
- subsidiaries, if any

## 02 — Team

- founder biography
- current responsibilities
- hiring plan
- advisor agreements
- contractor agreements
- key-person and succession plan
- knowledge-transfer evidence

Explicitly disclose solo-founder risk and mitigation.

## 03 — Product

- product overview
- target customer
- problem statement
- Phase D product design
- screenshots and demo recording
- roadmap
- current scope vs future scope
- known product limitations

## 04 — Technology

- TITAN v1 Technical Architecture
- ADR index
- repository map
- deployment architecture
- testing strategy
- CI evidence
- replay and determinism evidence
- performance benchmarks
- dependency and license inventory
- engineering debt register

## 05 — Security and Risk

- security audit
- incident register
- secret-management posture
- backup and PITR design
- DR drill results
- RPO/RTO evidence
- provider-failure matrix
- operator-access model
- data-retention policy
- privacy impact analysis
- penetration-test status

Do not claim third-party certification that has not occurred.

## 06 — Market and Competition

- category thesis: Supervised AI Trading
- bottom-up market sizing
- ideal customer profile
- competitor matrix
- substitutes, including naked ChatGPT/Claude use
- differentiation
- moat analysis
- regulatory/timing risk

## 07 — Commercial

- pricing model
- AI Desk Audit offer
- Design Partner offer
- sales playbook
- pipeline stages
- conversion assumptions
- channel strategy
- sales-cycle assumptions
- service/revenue mix target

## 08 — Customers

Before revenue:

- interview log
- design-partner target list
- letters of intent, if any
- discovery evidence
- repeated objections

After revenue:

- signed agreements
- ARR/MRR schedule
- retention
- usage
- references
- case studies
- customer concentration
- implementation status

Never manufacture logos, testimonials, or pipeline certainty.

## 09 — Financials

- historical P&L
- cash position
- monthly burn
- runway
- revenue forecast
- assumptions sheet
- COGS model
- model/API cost evidence
- single-tenant infrastructure cost
- headcount plan
- scenario analysis
- taxes and liabilities

Base, downside, and upside cases must use distinct assumptions.

## 10 — Legal and IP

- trademark search/status
- domain ownership
- repository ownership
- contributor IP assignments
- software license inventory
- privacy policy
- terms of use
- customer contract templates
- data-processing terms
- regulatory counsel memo
- E&O/cyber insurance status

## 11 — Roadmap

- Ring 0–4 commercial roadmap
- U0–U10 product roadmap
- milestone gates
- staffing dependencies
- regulatory dependencies
- decisions explicitly deferred

## 12 — Fundraise

- amount sought
- valuation expectations, if approved
- use of funds
- 18–24 month milestones
- hiring tied to milestones
- risks capital cannot solve
- investor profile sought
- excluded investor behaviors

## Core Investor Metrics

Before first raise, track:

- paying desks
- ARR
- paid audits completed
- audit-to-subscription conversion
- gross margin
- monthly burn
- runway
- customer concentration
- deployment time
- weekly active decision reviewers
- records generated
- validation failure rate
- uptime/health
- renewal intent

## Red-Flag Register

Disclose plainly:

- demo-account dependence
- no proven alpha
- solo-founder risk
- no external pen test
- no formal regulatory opinion until counsel completes it
- single-region/single-instance limits
- current customer count
- category timing risk

An investor should discover no material negative fact that is absent from management’s own register.

## Readiness Gate

Do not start a formal fundraising process until:

- corporate/IP ownership is clean
- at least one paid customer or design partner exists
- public positioning is consistent
- live demo is stable
- claims register is complete
- financial model is reviewed
- legal risks are clearly framed
- data room index is at least 90% complete

## Definition of Done

The data room is ready when a serious investor can answer, without founder narration:

- What exactly is the company selling?
- Who buys it and why now?
- What has been technically proven?
- What remains commercially unproven?
- What could kill the company?
- What does capital accelerate?
- Why is the founder positioned to execute?