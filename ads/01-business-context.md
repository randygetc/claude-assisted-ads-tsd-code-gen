---
phase: 1
status: approved
---

## Reviewer brief

**1. What this phase added**

- Section 2: the problem as four hypotheses, the current-state process as a time-category frame with nothing yet filled, four candidate root causes, and the eight baseline measurements needed before any target.
- Section 3: two business outcomes, `BO-001` and `BO-002`, each serving the recorded outcome statement and each passing the section 0 test.
- Section 4: twelve measures written out in the full section 4.4 format: three primary (`SM-001`, `SM-002`, `SM-003`), five guardrails (`SM-G01` to `SM-G05`) and four leading indicators for probabilistic behaviour (`SM-004` to `SM-007`).
- Four new open questions: `OQ-035` to `OQ-038`.
- `docs/plan.md`: phase 1 marked `in review`.

**2. Additions to the template**

- Each measure is defined where it is listed (4.1, 4.2, 4.3), not in 4.4. Section 4.4 holds the shared measurement rules and a map of measures to outcomes and guardrails. This avoids defining every `SM` twice.
- Section 4.3 is conditional on `OQ-036`: if the solution has no probabilistic component, the four leading indicators are marked not applicable.
- No section is marked not applicable.

**3. Provenance**

- Sourced: 12 tagged statements, from `DEC-001`, `DEC-003` and `inputs/context.md`.
- Assumed: `ASM-002` only, used in 2.1, `SM-001` and 4.4. No new assumption was added. No baseline, target, window, volume, cost or threshold is assumed.
- Unknown: 74 lines carry an unknown. Every baseline, target and measurement window is unknown and tied to an open question. The largest groups are baselines (`OQ-021`), targets and windows (`OQ-035`), and audit method (`OQ-037`).
- Every problem item and root cause is labelled a hypothesis, because `inputs/context.md` and `inputs/discovery/` hold no process evidence.
- Zero targets on `SM-G03`, `SM-G04` and `SM-G05` come from invariants I-6, I-7 and I-4, not from a business choice.
- New open questions:
  - `OQ-035`: targets and measurement windows (Business Owner).
  - `OQ-036`: whether a probabilistic component is part of the solution (Architecture Owner).
  - `OQ-037`: who audits resolutions and how the sample is drawn (Policy Owner).
  - `OQ-038`: how the applicable state policy is determined for an employee (Policy Owner).

**4. Decisions needed from you**

1. Do you want illustrative baselines and targets? The mode is `REFERENCE`, so I may propose figures as "Illustrative:" assumptions. I did not, because that would fill the measures with invented numbers before you have chosen. If you want them, say which measures and I will log each as an `ASM`.
2. Does the solution include a probabilistic component (`OQ-036`)? The answer decides whether section 4.3 stands.
3. Do `BO-001` and `BO-002` cover the outcome? I left out a third candidate, "HR time moves to exceptions", because the outcome statement does not mention HR capacity. Say if you want it.
4. Can you describe how a PTO request is handled today (`OQ-019`) and name the pain points with any evidence (`OQ-020`)? Section 2.2 stays empty without it.
5. What counts as HR intervention (`OQ-023`) and as resolved (`OQ-022`)? `SM-001` and `SM-002` depend on both.

**5. Look hardest at**

- `BO-002`: the inputs do not state correctness as an outcome. I derived it from the outcome statement: a wrong resolution sends the employee back to HR. If you disagree, remove `BO-002`, `SM-003`, and the leading indicators that serve it.
- Measure design choices I made without a source: reporting `SM-002` as median and 90th percentile, excluding employee-initiated changes from `SM-G01`, and pausing nothing in `SM-002` while the employee supplies information.
- The four hypotheses in 2.1. They are plausible from the outcome statement but nothing here shows they are true.

# 2. Business Context

## 2.1 Problem / Opportunity

No process data, pain-point evidence or baseline has been supplied. Every item below is a hypothesis.

| Item | Statement | Status | Evidence |
|---|---|---|---|
| 1 | Staff at US Wide Corp, in CA, NY and NJ, wait on HR to resolve routine PTO requests. The recorded outcome statement presupposes this friction. [src: DEC-001] [src: inputs/context.md] | Hypothesis | TBD (OQ-020) |
| 2 | HR time spent on routine PTO requests is time not available for requests that need judgment. | Hypothesis | TBD (OQ-021) |
| 3 | Each of CA, NY and NJ has its own PTO policy. [src: DEC-003] Applying the right policy to each request, consistently, is harder than under a single policy. | The first sentence is sourced; the second is a hypothesis | TBD (OQ-020) |
| 4 | Routine requests, meaning those the policy settles by rule alone [ASM-002], can be resolved without a person in the path, leaving a person for exceptions. Whether policy permits this is not known. | Opportunity, hypothesis | TBD (OQ-011) |

## 2.2 Current-State Process

The inputs describe no current process. The only step they name is HR intervention in the handling of routine PTO requests. [src: DEC-001] The flow, its steps and its actors are unknown: TBD (OQ-019). A flow diagram is drawn when that question is answered.

| Time category | What the current-state description SHALL capture | Current state |
|---|---|---|
| Human processing time | The work people do on a request, by role. | TBD (OQ-019) |
| Waiting time | Time a request sits unattended, including waiting on HR. | TBD (OQ-019) |
| System time | Time spent by systems retrieving, calculating or recording. | TBD (OQ-019) |
| Exception handling | How requests that need judgment are recognised and handled. | TBD (OQ-019) |
| Rework | Corrections, reversals and repeat contacts after a first disposition. | TBD (OQ-019) |

## 2.3 Root Causes

All candidates are hypotheses. Evidence for each is unknown: TBD (OQ-019).

| Candidate | Root cause | Tied to item |
|---|---|---|
| A | Routine requests go to HR whatever their complexity. | 1, 2 |
| B | Staff and managers cannot apply the policy themselves, because it is not available to them in a form they can act on. | 1, 4 |
| C | The policy differs by state [src: DEC-003], and the right one must be found for each employee (TBD (OQ-038)). | 3 |
| D | The information needed to settle a request, such as the balance and existing approved leave, is held where the requester cannot see it. | 1 |

## 2.4 Baseline

Targets SHALL NOT be set before these measurements exist. None has been supplied: TBD (OQ-021).

| Measurement | Needed for | Authoritative source | Status |
|---|---|---|---|
| Routine PTO requests per period, by state | Population size for all measures | The record of requests: TBD (OQ-014) | TBD (OQ-021) |
| Share of routine requests with at least one HR touch | `SM-001` | The record of requests: TBD (OQ-014) | TBD (OQ-021) |
| Elapsed time from request to disposition communicated, with the share spent waiting on HR | `SM-002` | The record of requests: TBD (OQ-014) | TBD (OQ-021) |
| HR handling time per routine request | Sizing; context for `SM-001` | TBD (OQ-014) | TBD (OQ-021) |
| Share of resolved routine requests that conform to the applicable state policy | `SM-003` | Audit: TBD (OQ-037) | TBD (OQ-021) |
| Share of resolved routine requests later reversed or corrected | `SM-G01` | The record of requests: TBD (OQ-014) | TBD (OQ-021) |
| Elapsed time for exceptions to reach a human decision | `SM-G02` | The record of requests: TBD (OQ-014) | TBD (OQ-021) |
| Exception rate: share of requests that need judgment | Routine and exception split; `SM-G03` | TBD (OQ-007) | TBD (OQ-021) |

# 3. Business Outcomes

The recorded outcome statement is the root of this section:

> Employees resolve routine PTO requests without waiting on HR intervention. [src: DEC-001]

### BO-001 — Routine PTO requests are resolved without waiting on HR

Staff of US Wide Corp in CA, NY and NJ [src: inputs/context.md] who make a routine PTO request receive a disposition, verified against the authoritative record, without the time or the result depending on an HR touch. What observably changes is the path of a routine request: it ends in a known disposition with no HR step in it, and the employee is told.

**Serves the outcome statement:** this is the statement made observable. It names who benefits and what stops happening.

**Section 0 test:** with all mention of AI, assistants, automation and technology removed, the goal still stands, and policy design, delegated approval, rule-based decisions or a staffed service desk could each pursue it. Pass.

### BO-002 — Resolutions conform to the applicable state policy

A routine request is settled the way the policy of the applicable state prescribes [src: DEC-003], so the result of a request does not depend on who handles it or by what route. What observably changes is that employees do not return to HR to have a wrong disposition corrected.

**Serves the outcome statement:** a resolution that is wrong is not a resolution. The employee comes back to HR to fix it, which is the intervention the outcome removes.

**Section 0 test:** with all mention of AI, assistants, automation and technology removed, the goal still stands, and training, checklists, delegated approval or rule-based decisions could each pursue it. Pass.

# 4. Success Measures

Every measure below serves a business outcome from section 3. Every baseline, target and window is unknown until the Business Owner answers `OQ-021` and `OQ-035`; none has been invented.

## 4.1 Primary Business Measures

### SM-001 — Routine requests resolved with no HR intervention

| Field | Value |
|---|---|
| Serves | `BO-001` |
| Definition | The share of routine PTO requests that reach a verified disposition with no HR touch. What counts as a touch: TBD (OQ-023). |
| Formula | Routine requests resolved with zero HR touches ÷ routine requests resolved, in the window. |
| Population | Routine PTO requests made by staff in CA, NY and NJ [src: inputs/context.md], routine as defined by `ASM-002` until `OQ-007` is answered. |
| Exclusions | Requests withdrawn by the employee before a disposition; requests classified as exceptions. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | The record of requests and dispositions: TBD (OQ-014) |
| Owner | Business Owner |
| Associated guardrail | `SM-G01`, `SM-G03` |

### SM-002 — Time to resolution of routine requests

| Field | Value |
|---|---|
| Serves | `BO-001` |
| Definition | The elapsed time from submission of a routine request to the moment a verified disposition has been communicated to the employee. What counts as resolved: TBD (OQ-022). |
| Formula | Median and 90th percentile of (disposition communicated − request submitted), reported by state. |
| Population | As `SM-001`. |
| Exclusions | Requests withdrawn by the employee; requests classified as exceptions. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | The record of requests and dispositions: TBD (OQ-014) |
| Owner | Business Owner |
| Associated guardrail | `SM-G01`, `SM-G02`, `SM-G05` |

### SM-003 — Policy-conformant resolution

| Field | Value |
|---|---|
| Serves | `BO-002` |
| Definition | The share of resolved routine requests whose disposition conforms to the policy of the applicable state [src: DEC-003]. How the applicable state is determined: TBD (OQ-038). |
| Formula | Audited resolved requests judged conformant ÷ audited resolved requests, in the window. |
| Population | As `SM-001`, limited to the audited sample. |
| Exclusions | Requests withdrawn by the employee; requests classified as exceptions. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | Audit against the state policy and the authoritative record: TBD (OQ-037) |
| Owner | Policy Owner |
| Associated guardrail | `SM-G01`, `SM-G04` |

## 4.2 Guardrail Measures

### SM-G01 — Reversal rate

| Field | Value |
|---|---|
| Serves | `BO-001`, `BO-002` |
| Definition | The share of resolved routine requests whose disposition is later reversed or corrected by a person. It shows whether speed and removal of HR from the path are costing correctness. |
| Formula | Resolved routine requests later reversed or corrected ÷ resolved routine requests, in the window. |
| Population | As `SM-001`. |
| Exclusions | Changes the employee initiates for their own reasons. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | The record of requests and dispositions: TBD (OQ-014) |
| Owner | Business Owner |
| Associated guardrail | Guards `SM-001`, `SM-002`, `SM-003` |

### SM-G02 — Time to a human decision on exceptions

| Field | Value |
|---|---|
| Serves | `BO-001` |
| Definition | The elapsed time for a request that needs judgment to reach a decision by a person with authority. It shows whether routine speed is bought at the expense of exceptions. |
| Formula | Median and 90th percentile of (human decision recorded − request classified as exception). |
| Population | Requests classified as exceptions, by state [src: inputs/context.md]. Exception criteria: TBD (OQ-007). |
| Exclusions | Requests withdrawn by the employee. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | The record of requests and dispositions: TBD (OQ-014) |
| Owner | Business Owner |
| Associated guardrail | Guards `SM-002` |

### SM-G03 — Bypass of required human judgment

| Field | Value |
|---|---|
| Serves | `BO-001`, `BO-002` |
| Definition | The share of requests that meet the exception criteria and are resolved without the human judgment, exception authority or approval that policy requires. |
| Formula | Exception-criteria requests resolved without the required person ÷ requests meeting the exception criteria, in the window. |
| Population | All requests, by audit, because a request wrongly classified as routine is not in the routine population. Exception criteria: TBD (OQ-007). |
| Exclusions | None. |
| Baseline | TBD (OQ-021) |
| Target | Zero. Required human judgment cannot be bypassed (invariant I-6). |
| Window | TBD (OQ-035) |
| Authoritative source | Audit: TBD (OQ-037) |
| Owner | Policy Owner |
| Associated guardrail | Guards `SM-001` |

### SM-G04 — Misattributed refusal rate

| Field | Value |
|---|---|
| Serves | `BO-002` |
| Definition | The share of adverse outcomes communicated to an employee as a business refusal when the cause was a technical failure, missing information or an ambiguous rule. |
| Formula | Adverse outcomes communicated as refusals with a non-business cause ÷ adverse outcomes communicated, in the window. |
| Population | Requests whose communicated outcome is adverse to the employee. |
| Exclusions | Authorised business refusals. Which refusals are authorised: TBD (OQ-028). |
| Baseline | TBD (OQ-021) |
| Target | Zero. Technical failure, missing information and rule ambiguity are never presented as a business refusal (invariant I-7). |
| Window | TBD (OQ-035) |
| Authoritative source | Audit: TBD (OQ-037) |
| Owner | Policy Owner |
| Associated guardrail | Guards `SM-003` |

### SM-G05 — False success rate

| Field | Value |
|---|---|
| Serves | `BO-001` |
| Definition | The share of requests reported to the employee as completed where the authoritative record does not show the intended state. |
| Formula | Requests reported complete whose authoritative state differs from the reported disposition ÷ requests reported complete, in the window. |
| Population | Requests reported complete to the employee. |
| Exclusions | None. |
| Baseline | TBD (OQ-021) |
| Target | Zero. Success is reported only after authoritative read-back confirms the intended state (invariant I-4). |
| Window | TBD (OQ-035) |
| Authoritative source | Comparison of the communicated disposition with the system of record: TBD (OQ-014) |
| Owner | Architecture Owner |
| Associated guardrail | Guards `SM-002` |

## 4.3 AI Behavioral Measures

These are leading indicators only. None substitutes for a business outcome. They apply only if the solution includes a probabilistic component: TBD (OQ-036). If it does not, this subsection is marked not applicable.

### SM-004 — Interpretation accuracy

| Field | Value |
|---|---|
| Serves | `BO-002` |
| Definition | The share of sampled requests where the interpreted request type, dates and intent match what the employee meant. Leads `SM-003`. |
| Formula | Sampled requests interpreted correctly ÷ sampled requests. |
| Population | Routine requests handled by the probabilistic component. |
| Exclusions | Requests withdrawn before interpretation. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | Human review of a sample: TBD (OQ-037) |
| Owner | Architecture Owner |
| Associated guardrail | `SM-G01` |

### SM-005 — False-routine rate

| Field | Value |
|---|---|
| Serves | `BO-002` |
| Definition | The share of sampled requests that meet the exception criteria but were classified as routine. Leads `SM-G03`. |
| Formula | Exception-criteria requests classified as routine ÷ sampled requests meeting the exception criteria. |
| Population | Requests meeting the exception criteria: TBD (OQ-007). |
| Exclusions | None. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | Human review of a sample: TBD (OQ-037) |
| Owner | Architecture Owner |
| Associated guardrail | `SM-G03` |

### SM-006 — Needless escalation rate

| Field | Value |
|---|---|
| Serves | `BO-001` |
| Definition | The share of requests passed to a person that the reviewer judges routine. Too high a rate lowers `SM-001`. Leads `SM-001`. |
| Formula | Escalated requests judged routine by the reviewer ÷ escalated requests. |
| Population | Requests passed to a person. |
| Exclusions | Escalations required by policy regardless of the case. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | Reviewer judgment recorded on the request: TBD (OQ-037) |
| Owner | Architecture Owner |
| Associated guardrail | `SM-G03` |

### SM-007 — Ungrounded statement rate

| Field | Value |
|---|---|
| Serves | `BO-002` |
| Definition | The share of sampled statements to employees about policy, balance or request status that no authoritative source supports. Leads `SM-003`, `SM-G04` and `SM-G05`. |
| Formula | Sampled statements without authoritative support ÷ sampled statements. |
| Population | Statements to employees produced by the probabilistic component. |
| Exclusions | None. |
| Baseline | TBD (OQ-021) |
| Target | TBD (OQ-035) |
| Window | TBD (OQ-035) |
| Authoritative source | Human review of a sample: TBD (OQ-037) |
| Owner | Architecture Owner |
| Associated guardrail | `SM-G04`, `SM-G05` |

## 4.4 Measurement Definition

Every `SM` and `SM-G` in this section states: ID, definition, formula, population, exclusions, baseline, target, measurement window, authoritative source, owner and associated guardrail. The definitions sit with the measures in 4.1, 4.2 and 4.3.

Rules that apply to all measures:

- A target SHALL NOT be set before its baseline exists. The Business Owner sets targets and windows (`OQ-035`); the architecture does not.
- Zero targets on `SM-G03`, `SM-G04` and `SM-G05` follow from invariants I-6, I-7 and I-4. They are not a business choice and need no baseline to hold.
- Routine versus exception follows `OQ-007`. Until it is answered, populations use `ASM-002`.
- Measures are reported by state, because the three states have separate policies. [src: DEC-003]
- A leading indicator in 4.3 is never reported in place of the business measure it leads.

| Measure | Kind | Serves | Associated guardrail |
|---|---|---|---|
| SM-001 | Primary | BO-001 | SM-G01, SM-G03 |
| SM-002 | Primary | BO-001 | SM-G01, SM-G02, SM-G05 |
| SM-003 | Primary | BO-002 | SM-G01, SM-G04 |
| SM-G01 | Guardrail | BO-001, BO-002 | Guards SM-001, SM-002, SM-003 |
| SM-G02 | Guardrail | BO-001 | Guards SM-002 |
| SM-G03 | Guardrail | BO-001, BO-002 | Guards SM-001 |
| SM-G04 | Guardrail | BO-002 | Guards SM-003 |
| SM-G05 | Guardrail | BO-001 | Guards SM-002 |
| SM-004 | Leading indicator | BO-002 | SM-G01 |
| SM-005 | Leading indicator | BO-002 | SM-G03 |
| SM-006 | Leading indicator | BO-001 | SM-G03 |
| SM-007 | Leading indicator | BO-002 | SM-G04, SM-G05 |
