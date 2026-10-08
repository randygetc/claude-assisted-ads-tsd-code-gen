---
phase: 0
status: approved
---

## Reviewer brief

**1. What this phase added**

- Section 0 of the ADS: the outcome test, its disposition, and the completed record, matching `DEC-001`.
- An intake working paper (below, not part of `ADS.md`): input inventory, sufficiency of the inputs for each of the 32 sections, and the ten questions that would most change the architecture.
- 34 open questions (`OQ-001` to `OQ-034`) in `registers/open-questions.md`, one per missing fact. Three are already resolved: `OQ-001`, `OQ-002`, `OQ-005`.
- 6 proposed assumptions (`ASM-001` to `ASM-006`) in `registers/assumptions.md`, all marked "Illustrative:" because the mode is `REFERENCE`.
- `docs/plan.md`: step 1 marked done, phase 0 marked `in review`, log lines.
- Revised after your update to `inputs/context.md` and your answer on state policies: `DEC-002`, `DEC-003`, `ASM-003` rejected, `OQ-034` added.

**2. Additions to the template**

- None to section 0. The four template subsections (0.1 to 0.4) are all present.
- The intake working paper is an addition required by `docs/plan.md`. It sits above the first H1 and is left out of `ADS.md`.
- No section is marked not applicable.

**3. Provenance**

- Section 0: 9 statements tagged `[src: DEC-001]`, 0 assumed, 0 unknown. The record has no gaps, as the plan requires.
- Working paper: it describes the inputs and the gaps; it makes no project claim beyond `DEC-001`, `DEC-002`, `DEC-003` and `inputs/context.md`, each tagged where used.
- New open questions: 34, of which 31 are `open` and 3 resolved (`OQ-001`, `OQ-002` by `DEC-002`; `OQ-005` by `DEC-003`), each with an owner role and the phase that needs the answer. Groups: identity and owners (`OQ-003`, `OQ-033`); scope and population (`OQ-004`, `OQ-006` to `OQ-010`, `OQ-017`, `OQ-034`); authority and rules (`OQ-011`, `OQ-012`, `OQ-013`, `OQ-016`, `OQ-028`); systems and identity (`OQ-014`, `OQ-015`, `OQ-031`); process and baseline (`OQ-019` to `OQ-023`, `OQ-032`); privacy and data (`OQ-018`, `OQ-024`, `OQ-025`, `OQ-026`); human review, cost and autonomy (`OQ-027`, `OQ-029`, `OQ-030`).
- New assumptions: 6. Five are `unvalidated`; `ASM-003` is `rejected (DEC-003)`.
  - `ASM-001`: a written PTO policy owned by HR exists.
  - `ASM-002`: a working definition of a routine request.
  - `ASM-003`: one jurisdiction and one policy set in the first release. Rejected: each of CA, NY and NJ has its own PTO policy (`DEC-003`).
  - `ASM-004`: employees request only for themselves.
  - `ASM-005`: a system of record for balances and approved leave exists.
  - `ASM-006`: a trusted identity source exists.
- No assumption covers a number, timing, volume, cost or threshold. Illustrative figures are deliberately left for phase 1, after you have said whether you can supply real ones.

**4. Decisions needed from you**

1. Who holds approval authority for a routine request, and may policy settle it by rule with no person approving (`OQ-011`, `OQ-013`)? This is the largest single driver of the automation boundary. I did not assume it, because an authority rule is a business decision (G-8).
2. What makes a request routine rather than an exception (`OQ-007`)? `ASM-002` is a placeholder definition.
3. Which actions are in the first release: answer only, or also submit, change and cancel (`OQ-008`, `OQ-009`)?
4. `inputs/context.md` now gives the project name, organisation, people served and jurisdictions. Can you fill in the rest, or add material under `inputs/discovery/`? Every remaining `unknown` stays an open question.
5. `DEC-001` names its owner as "Human". Do you want it to carry a named person or a role (`OQ-003`)?

**5. Look hardest at**

- Section 0.4, third paragraph: I read "resolve" as "reach a known disposition, verified against authoritative state" (template 7.1, invariant I-4). The recorded statement does not say this. If you meant "answer", say so now; it changes the later outcomes and measures.
- `ASM-002`: it bounds the first release without any source. If it is wrong, phases 2 and 3 change. `ASM-003` was rejected after review; the single-policy-set scoping it carried is gone and `OQ-034` replaces it.
- The sufficiency ratings in the table below. I rate a section "partial" only when `DEC-001` or `inputs/context.md` supplies something for it. I rated sections 20 and 21 "absent" although their structure follows from the invariants, because they carry no project facts yet.

## Intake working paper

This part stays out of `ADS.md`. It records what the inputs contain at the start of the engagement and what is missing.

### Input inventory

| Input | What it establishes | Trust and use |
|---|---|---|
| `registers/decisions.md`, `DEC-001` | The business outcome statement, in original and restated wording, with date. | Recorded by the human through `/outcome`. The root of the document. |
| `inputs/context.md` | Mode is `REFERENCE`; document version is "1.0 draft". Project name is Project Leaves; the organisation is US Wide Corp with offices in CA, NY and NJ; staff are served; jurisdictions are CA, NY and NJ (`DEC-002`). Every other field reads `unknown`: owners, scope decisions, systems, process facts, volumes, constraints, preferences, source material. | Supplied by the human. Trusted as far as it goes. The file changed after the first draft of this phase. |
| `inputs/discovery/` | Nothing: the directory is empty. | No process exports, policies or interview notes exist yet. |
| `inputs/ADS_template.md` | What each section must contain. No project content. | The specification, not a source of facts. |
| `inputs/example/` | Not consulted in this phase. | Format reference only; never a source (G-11). |
| `registers/open-questions.md`, `registers/assumptions.md` | Empty at the start of the phase. | Populated by this phase. |

What the outcome statement itself establishes, by topic:

| Topic | Established by `DEC-001` | Not established |
|---|---|---|
| Who benefits | Employees; `inputs/context.md` adds that staff are served, at US Wide Corp offices in CA, NY and NJ [src: inputs/context.md]. | Which staff populations (`OQ-004`); who else is affected (`OQ-003`, `OQ-011`). |
| Domain | Requests for PTO. | What counts as PTO and which request types exist (`OQ-006`). |
| Scope qualifier | Routine requests only. | What makes a request routine (`OQ-007`). |
| The friction | Waiting on HR intervention. | How long, how often, with what evidence (`OQ-019`, `OQ-020`, `OQ-021`, `OQ-023`). |
| What success looks like | Employees reach a resolution without HR in the path. | Acceptable time to resolution; what counts as resolved (`OQ-022`). |
| Everything else | Nothing: actions, systems, rules, authority, data, volumes, constraints. | See the table below. |

### Sufficiency of the inputs, by template section

- **Sufficient**: the inputs supply what the section needs.
- **Partial**: the inputs supply something, but key facts are missing.
- **Absent**: the inputs supply nothing. Where the section is derived from earlier phases, the open questions of those phases apply and the row says so.

| Section | Title | Rating | What is missing | Open questions |
|---|---|---|---|---|
| 0 | Outcome Statement Test | Sufficient | Nothing. | none |
| 1 | Executive Summary | Absent | Written last, from the finished document. | none |
| 2 | Business Context | Partial | The organisation is known (`DEC-002`). Only the hypothesis that waiting on HR is the friction. No process, causes or baseline. | `OQ-019`, `OQ-020`, `OQ-021`, `OQ-032` |
| 3 | Business Outcomes | Partial | The statement supports outcome-level items; stakeholders and evidence are missing. | `OQ-004`, `OQ-022` |
| 4 | Success Measures | Absent | Definitions of waiting, resolved and HR intervention; baselines; targets; sources. | `OQ-021`, `OQ-022`, `OQ-023` |
| 5 | Scope and Autonomy Boundary | Partial | Routine PTO requests are in scope; the jurisdictions are CA, NY and NJ, each with its own PTO policy (`DEC-002`, `DEC-003`). Populations, request types, actions, exclusions, channels and the content of each state policy are missing. | `OQ-004`, `OQ-006`, `OQ-008`, `OQ-009`, `OQ-010`, `OQ-017`, `OQ-034` |
| 6 | Stakeholders and Actors | Partial | Employees and HR are named. Approvers, managers and accountable authorities are not. | `OQ-003`, `OQ-011`, `OQ-012` |
| 7 | Business Process and Decision Model | Partial | Only the boundary hint "routine". No process, decisions or authorities. | `OQ-007`, `OQ-011`, `OQ-019`, `OQ-034` |
| 8 | Authority, Truth, and Temporal Validity | Absent | Authority holders, systems of record, policy sources, identity, effective dating. | `OQ-011`, `OQ-012`, `OQ-014`, `OQ-015`, `OQ-016`, `OQ-034` |
| 9 | Business Requirements | Absent | Derived from sections 3 to 8. | none new |
| 10 | Business Acceptance Criteria | Absent | Derived from section 9. | none new |
| 11 | Architectural Responsibilities | Absent | Derived from sections 7 to 10. | none new |
| 12 | Architectural Concerns | Absent | Derived from sections 7 to 10. | none new |
| 13 | Constraints, Assumptions, and Preferences | Partial | Mode is known. Constraints and preferences are not. | `OQ-024`, `OQ-031` |
| 14 | Threat and Failure Model | Absent | Needs systems, data and channels. | `OQ-014`, `OQ-017`, `OQ-024` |
| 15 | Quality Attributes | Absent | Response, accuracy and availability needs; cost limits. | `OQ-022`, `OQ-029` |
| 16 | Architecture Drivers | Absent | Derived from sections 12, 14. | none new |
| 17 | Architecture Patterns | Absent | Derived from section 16. | none new |
| 18 | Human Authority and Review Model | Absent | Reviewers, response time, adverse decisions, appeals. | `OQ-009`, `OQ-013`, `OQ-027`, `OQ-028` |
| 19 | Data and Privacy Architecture | Absent | Data classes, sensitivity, provider limits, retention. | `OQ-018`, `OQ-025`, `OQ-026` |
| 20 | Logical Architecture | Absent | Derived from sections 11 to 19. | `OQ-014` |
| 21 | Architecture Views | Absent | Derived from section 20. | none new |
| 22 | Evaluation and Autonomy Plan | Absent | Baselines, gate evidence and approvers. | `OQ-021`, `OQ-030` |
| 23 | Architecture Acceptance | Absent | Derived from sections 16, 17. | none new |
| 24 | Architecture Decisions / ADR Register | Absent | Derived from sections 16, 17. | none new |
| 25 | Architecture Traceability Matrix | Absent | Derived from the whole document. | none new |
| 26 | Decision Log | Partial | One decision exists (`DEC-001`). | none new |
| 27 | Rejected Alternatives | Absent | Derived from the ADRs. | none new |
| 28 | Open Questions and Risks | Partial | The register now holds 34 questions; risks come later. | none new |
| 29 | Architecture Governance | Absent | Who approves changes to the ADS. | `OQ-033` |
| 30 | Production Evidence and Learning | Absent | Which production signals exist and who owns them. | `OQ-021`, `OQ-033` |
| 31 | Definition of Architecture Success | Absent | Derived from sections 4 and 23. | none new |

### Proposed assumptions

All are marked "Illustrative:" under G-4 for `REFERENCE` mode. None covers a number, timing, volume or cost.

- `ASM-001`: a written PTO policy, owned by HR, governs what employees may take.
- `ASM-002`: a working definition of a routine request, so scope can be drawn before `OQ-007` is answered.
- `ASM-003`: one jurisdiction and one policy set in the first release. Rejected by `DEC-003`: each of CA, NY and NJ has its own PTO policy.
- `ASM-004`: employees request leave for themselves only; no requests on behalf of others.
- `ASM-005`: a system of record exists for leave balances and approved leave (stated logically, no product).
- `ASM-006`: a trusted source of employee identity exists.

Not assumed on purpose: who approves, whether a rule alone may settle a request, and what must always stay with a human. Those are authority decisions, logged as `OQ-009`, `OQ-011`, `OQ-012` and `OQ-013`.

### The ten questions that would most change the architecture

1. **Approval authority and rule-based settlement** (`OQ-011`, `OQ-013`). Decides whether any request class can reach AUTOMATED or LIMITED_AUTOMATION, or stops at RECOMMENDATION or HUMAN_APPROVAL_REQUIRED. Reshapes sections 5, 8, 18, 22.
2. **Routine versus exception** (`OQ-007`, `OQ-012`). Sets the line the outcome statement depends on, and the exception path required by I-6.
3. **Actions in the first release** (`OQ-008`, `OQ-009`). Answering only is read-only; submitting, changing or cancelling mutates a system of record and brings I-2, I-4 and I-5 into play.
4. **Systems of record** (`OQ-014`). Decides what authoritative read-back is possible (I-4) and what an unknown outcome looks like (I-5).
5. **Policy source** (`OQ-016`). Written or machine-readable, owned, versioned, effective-dated. Decides how I-8 degradation works when policy is unavailable.
6. **Identity** (`OQ-015`). Decides how I-1 is met for every request.
7. **Sensitive data and model-provider limits** (`OQ-026`, `OQ-018`). Requests may carry reasons such as health or family matters; this sets the data boundary of section 19 (I-9).
8. **State policies and legal obligations** (`OQ-034`, `OQ-024`). The three states each have a PTO policy (`DEC-003`); their content, and any legal duty to involve a person, decide which requests are routine.
9. **What the measures mean** (`OQ-021`, `OQ-022`, `OQ-023`). Waiting, resolved and HR intervention need definitions and a baseline before any target exists (G-4).
10. **Populations and channels** (`OQ-004`, `OQ-017`). Decide which staff and which interaction paths the first release carries; the state policy variants are already three (`DEC-003`).

# 0. Outcome Statement Test

No ADS work begins until the business outcome statement has passed this test.

## 0.1 The Test

1. Remove any mention of AI, an assistant, automation, or specific technology from
   the sentence.
2. Ask whether what remains still describes a coherent goal a reasonable person
   could pursue by multiple different means, not only the one the author has in mind.

## 0.2 Disposition

The statement passes. The recorded wording names no AI, assistant, automation or
technology, so step 1 removes nothing. [src: DEC-001]

What remains is a coherent goal: employees reach a resolution of their routine PTO
requests without a wait that depends on HR. A reasonable person could pursue it by
several means, for example clearer published policy that employees apply themselves,
delegated approval to line managers, rule-based decisions inside a request tool, a
staffed service desk with a committed response time, or any combination. The
statement prefers none of them.

The statement is therefore confirmed and restated cleanly in 0.3. Nothing was guessed
or silently fixed.

## 0.3 Outcome Statement Record

| Field | Value |
|---|---|
| Statement as given | "Employees should be able to resolve routine PTO requests without waiting on HR intervention" [src: DEC-001] |
| Statement with technology removed | "Employees should be able to resolve routine PTO requests without waiting on HR intervention". It is unchanged, because it names no technology. [src: DEC-001] |
| Result | Pass [src: DEC-001] |
| Restated outcome statement | "Employees resolve routine PTO requests without waiting on HR intervention." [src: DEC-001] |
| Confirmed by | The human who ran `/outcome`, recorded as owner of `DEC-001` [src: DEC-001] |
| Date | 2026-10-07 [src: DEC-001] |

## 0.4 Effect on the Rest of the ADS

The restated statement is the root of traceability. Every business outcome in
section 3 serves it and passes the same test. Changing it is a material change under
section 29. [src: DEC-001]

Three words in the statement carry later work, and the inputs do not yet define any
of them:

- **Routine.** The statement limits the outcome to routine requests. Where the line
  between routine and exception falls is not supplied (`OQ-007`). Exceptions stay
  in the ADS as a path to a person with the authority to decide.
- **HR intervention.** What counts as an HR touch, and so what the outcome removes
  from the path, is not supplied (`OQ-023`).
- **Resolve.** This ADS reads a request as resolved when it reaches a known
  disposition that has been verified against authoritative state, and the employee
  has been told (invariant I-4; template section 7.1). A reply that only answers a
  question is not a resolution. If "resolve" was meant more loosely, the outcomes
  and measures in phase 1 change.

The outcome removes waiting on HR. It does not remove human judgment where policy
requires it: required human judgment, exception authority and mandated approval
cannot be bypassed, timed out into approval, or simulated (invariant I-6).
