# Architecture Solution Design — Template

**Template version:** 3.1
**Status:** Locked specification. Project-neutral.

This template fixes the sections of an ADS and what each must contain. It holds no
project content. The project is defined by the outcome statement recorded in
Section 0 and by `inputs/context.md`.

Text in each section below is guidance for the author, written as "Contains:".
The generated ADS replaces the guidance with the content it asks for.

Header block of the generated document: project name, document status, version,
Architecture Owner, Business Owner, Risk / Privacy Owner, last updated.

---

# 0. Outcome Statement Test

No ADS work begins until the business outcome statement has passed this test.

## 0.1 The Test

1. Remove any mention of AI, an assistant, automation, or specific technology from
   the sentence.
2. Ask whether what remains still describes a coherent goal a reasonable person
   could pursue by multiple different means, not only the one the author has in mind.

## 0.2 Disposition

If yes, the statement passes; it is confirmed and restated cleanly. If no, it is a
solution disguised as an outcome: this SHALL be said explicitly to its author, who
SHALL be asked what the underlying goal actually is. The goal SHALL NOT be guessed
and a failing statement SHALL NOT be silently fixed.

## 0.3 Outcome Statement Record

Contains: statement as given; statement with technology removed; result; restated
outcome statement; confirmed by; date.

## 0.4 Effect on the Rest of the ADS

The restated statement is the root of traceability. Every business outcome serves
it and passes the same test. Changing it is a material change under Section 29.

# 1. Executive Summary

Written last. Contains: what the solution enables and for whom; why it is a
controlled decision-and-action system and not a model with direct system access;
the division of responsibility between probabilistic components, trusted systems,
deterministic controls, humans, and systems of record; the governing principle.

# 2. Business Context

## 2.1 Problem / Opportunity
Contains: the friction or opportunity, each item marked hypothesis or evidenced.

## 2.2 Current-State Process
Contains: how the work actually happens today, as a flow, distinguishing human
processing time, waiting time, system time, exception handling and rework.

## 2.3 Root Causes
Contains: candidate root causes, each tied to a problem item.

## 2.4 Baseline
Contains: the measurements needed before targets can be approved. Targets SHALL
NOT be invented without business evidence.

# 3. Business Outcomes

Contains: `BO` items. Each states what observably changes and for whom, how it
serves the Section 0 outcome statement, and that it passes the Section 0 test.

# 4. Success Measures

## 4.1 Primary Business Measures
## 4.2 Guardrail Measures
## 4.3 AI Behavioral Measures
Leading indicators only, never substitutes for business outcomes.
## 4.4 Measurement Definition
Every `SM` and `SM-G` identifies: ID, definition, formula, population, exclusions,
baseline, target, measurement window, authoritative source, owner, associated
guardrail.

# 5. Scope and Autonomy Boundary

Contains: every scope dimension that determines which rules, policies, eval cases,
integrations and authority paths are needed. Typical dimensions: supported request
or case types; jurisdictions; user populations; supported actions, each with its
own authority and risk classification; workflow variants.

## 5.x Initial Automation Boundary
Being in scope does not imply autonomous execution. Every supported scenario is
classified as one of: INFORMATION_ONLY, RECOMMENDATION, HUMAN_APPROVAL_REQUIRED,
LIMITED_AUTOMATION, AUTOMATED, NOT_SUPPORTED. Unsupported cases fail safely.

# 6. Stakeholders and Actors

Contains: each stakeholder and actor, their role, and the consequential decisions
they are accountable for. Every consequential decision has an accountable authority.

# 7. Business Process and Decision Model

## 7.1 Process Boundary
Start and end conditions. The end is a known disposition, verified against
authoritative state where consequential execution occurred.

## 7.2 Target Process
The target flow from expressed need to communicated disposition, including
establishing trusted identity, obtaining facts, determining applicable rules,
classifying routine versus exception, determining authority, human review,
revalidation, authorization, bounded execution, verification and evidence.

## 7.3 Decision Inventory
`D` items: the decision, and the authority or source that settles it.

# 8. Authority, Truth, and Temporal Validity

## 8.1 Core Distinction
Source of truth (what to believe), authority (who may decide), temporal validity
(is it still valid now).

## 8.2 Authority Matrix
Interpretation, business-rule, approval, exception, execution and system-of-record
authority, per action. States what the model SHALL NOT establish.

## 8.3 Source-of-Truth Matrix
Each information item, its authoritative source, and whether a model may establish it.

## 8.4 Claims, Facts, Decisions, Evidence
## 8.5 Temporal Correctness
Freshness states: FRESH, STALE, SUPERSEDED, UNSETTLED, EXPIRED.
## 8.6 Revalidation Boundaries

# 9. Business Requirements

Contains: `BR` items, each with statement, rationale, the `BO` it serves, priority.

# 10. Business Acceptance Criteria

Contains: `BAC` items describing observable behaviour without prescribing
implementation, including what must not happen. At least one per `BR`.

# 11. Architectural Responsibilities

Contains: `AR` items. Typical responsibilities: interpretation, identity, policy
or rules, decision, workflow, authority, human review, execution, verification,
evidence, privacy, evaluation, cost. Each states its scope, the `BR`s served, and
what it does not own.

# 12. Architectural Concerns

Contains: the concerns that shape the architecture (for example hallucination,
stale facts, injection, impersonation, inappropriate automation, duplicate or
uncertain execution, false success, privacy leakage, runaway cost) and the `AR`
that contains each.

# 13. Constraints, Assumptions, and Preferences

## 13.1 Constraints
`CON` items with justification.
## 13.2 Assumptions
Explicitly validated; included from the register.
## 13.3 Preferences
Negotiable unless promoted to a constraint with justification.

# 14. Threat and Failure Model

## 14.1 Threat Categories
`THR` scenarios, at least one per category.
## 14.2 Failure Categories
INPUT, MODEL, KNOWLEDGE, DATA, AUTHORITY, WORKFLOW, DEPENDENCY, EXECUTION,
VERIFICATION, PRIVACY, ECONOMIC.
## 14.3 Failure Propagation
Every critical `FS` identifies: cause, local failure, business consequence, safe
response, recovery, evidence. Model general knowledge is never silently
substituted for unavailable authoritative sources.

# 15. Quality Attributes

Contains: the priority attributes, and a measurable `QAS` for each important one.

# 16. Architecture Drivers

Contains: `AD` items: statement, what forces it, consequences, what it rules out.

# 17. Architecture Patterns

Contains: `PAT` items documenting drivers addressed, responsibilities,
trade-offs, risks introduced, validation mechanism.

# 18. Human Authority and Review Model

Human review is a business workflow, not an error fallback.

## 18.1 Review Triggers
## 18.2 Review Queues
Queue type, eligible reviewers, required authority, prioritisation, ownership,
escalation path.
## 18.3 Human Decision Package
What a reviewer receives. Model recommendations are distinguishable from facts.
## 18.4 Response-Time Commitment
Expected response time, escalation threshold, timeout behaviour, communication.
Approval is never invented because a reviewer did not respond.
## 18.5 Adverse Decisions
Distinguishes technical failure, insufficient information, rule ambiguity, not
eligible, and authorized business refusal. Only explicitly approved categories may
be decided automatically.
## 18.6 Appeals / Reconsideration

# 19. Data and Privacy Architecture

## 19.1 Data Minimization Principle
## 19.2 Data Classification
## 19.3 Model Provider Boundary
Per model interaction: purpose, fields transmitted, why each is necessary,
prohibited fields, retention, logging, applicable controls.
## 19.4 Retention Matrix
Per dataset: purpose, system, retention, model-provider exposure, access, deletion.
## 19.5 Logging Privacy

# 20. Logical Architecture

Contains: the layers (experience, workflow, reasoning, knowledge, control,
capability, system of record, verification) and cross-cutting concerns.

## 20.1 Reasoning Layer Boundary
What reasoning may and may not do.
## 20.2 Control Layer Boundary
## 20.3 Capability Boundary
Narrow, typed, authorized, auditable, bounded, retry-aware.
## 20.4 Verification Boundary
Execution success does not establish business success.

# 21. Architecture Views

Contains, as diagrams with reading guides: system context; logical architecture;
trust boundary; authority boundary; data flow and privacy; routine workflow
sequence; human review sequence; adverse decision and appeal sequence; uncertain
execution sequence; workflow state model; failure and degradation view.

# 22. Evaluation and Autonomy Plan

## 22.1 Evaluation Intent
Outcome to requirement to probabilistic responsibility to threat or failure to
required behaviour to eval scenario.
## 22.2 Incorrect Automation Taxonomy
## 22.3 Detection
Offline, pre-production, production.
## 22.4 Evaluation Dataset Governance
## 22.5 Tests vs Evals
Deterministic contract: test. Probabilistic or semantic behaviour: eval.
## 22.6 Autonomy Gates
Shadow, recommendation, limited automation, expanded automation. Each gate
specifies required evidence, threshold, approver.
## 22.7 Autonomy Regression
Reversible, and not dependent on a model reducing its own authority.

# 23. Architecture Acceptance

Contains: `AAC` items proving the implementation conforms to architectural intent,
each with the `AD` and `PAT` it proves, evidence type, and pass condition.

# 24. Architecture Decisions / ADR Register

Contains: the register of `ADR` records, each recording the choice and alternatives.

# 25. Architecture Traceability Matrix

Contains: the actual matrix. Outcome statement, outcome, measure, requirement,
responsibility, concern or failure, driver, pattern, acceptance; continuing to
ADR, technical design component, code, test or eval, production signal.

# 26. Decision Log

Contains: `DEC` items: decision, owner, date, basis, related IDs.

# 27. Rejected Alternatives

Contains: `ALT` items: alternative, reason rejected, related decision.

# 28. Open Questions and Risks

Contains: `OQ` items: question, impact, owner, required by. Unresolved questions
never silently become implementation assumptions.

# 29. Architecture Governance

Contains: which changes require review (outcome statement, scope, automation
boundary, authority, source of truth, privacy boundary, drivers, layer
responsibilities, patterns, acceptance, autonomy gates) and the stop-and-escalate
path when implementation discovers a design gap.

# 30. Production Evidence and Learning

Contains: the feedback loop from production to discovery and architecture, the
questions production evidence must answer, and how failures become regression cases.

# 31. Definition of Architecture Success

Contains: the conditions for success, beginning with the outcome statement having
passed the test, and ending with business measures demonstrating the outcome.
Code complete, feature accepted, eval passed, architecture accepted, production
ready and business success are distinct.
