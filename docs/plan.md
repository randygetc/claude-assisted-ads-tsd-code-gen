# Plan

The working plan for generating `ADS.md`. Claude Code updates the Status column and
the Log; the phase table's files and section mapping are fixed (they are mirrored in
`scripts/ads.py`, so changing them needs a `control-change` PR).

## Step 1 — Outcome test

Before any phase: `/outcome`. The business outcome statement must pass the test
(strip the technology; is a goal left that could be pursued by several means?) and
be recorded in `registers/decisions.md`. Status: done (DEC-001, 2026-10-07)

## Phases

| Phase | File | ADS sections | Status |
|---|---|---|---|
| 0 | `ads/00-intake.md` | 0, plus the intake working paper | merged |
| 1 | `ads/01-business-context.md` | 2, 3, 4 | not started |
| 2 | `ads/02-scope-process.md` | 5, 6, 7 | not started |
| 3 | `ads/03-authority-requirements.md` | 8, 9, 10 | not started |
| 4 | `ads/04-responsibilities-risks.md` | 11, 12, 13, 14, 15 | not started |
| 5 | `ads/05-drivers-patterns.md` | 16, 17 | not started |
| 6 | `ads/06-human-review-privacy.md` | 18, 19 | not started |
| 7 | `ads/07-logical-architecture.md` | 20, 21 | not started |
| 8 | `ads/08-evaluation-acceptance.md` | 22, 23 | not started |
| 9 | `ads/09-decisions.md` + `ads/adr/` | 24, 26, 27 | not started |
| 10 | `ads/10-traceability-closeout.md` + `ADS.md` | 1, 25, 28, 29, 30, 31 | not started |

Status values: `not started`, `in review`, `merged`.

The order follows the dependency chain in template section 25: outcomes and measures,
then scope and decisions, then requirements, then responsibilities and failure
modes, then drivers and patterns, then the structures that realise them, then how
they are proven. The executive summary is written last because it summarises
what was actually decided.

## Phase detail

Each phase must satisfy its "Done when" list and pass `scripts/ads.py check`.

### Phase 0 — Outcome statement and intake (section 0)

Two parts. Section 0 goes into the ADS. The intake working paper sits above it,
after the reviewer brief, and stays out of the assembled document.

- Section 0: the test as specified, and the record in 0.3 completed from the
  `Outcome statement:` row in the decision log: statement as given, statement with
  technology removed, result, restated statement, confirmed by, date. Nothing in
  the record is assumed or left `TBD`.
- Inventory every input: what each file in `inputs/` establishes, by topic.
- For each template section, state whether the inputs are sufficient, partial or
  absent.
- Reconcile `registers/open-questions.md` with the inputs: open a question for
  every fact the template requires that the inputs do not supply.
- Propose the assumptions needed to proceed, as `ASM` rows.
- List the ten questions whose answers would most change the architecture.

Done when: the section 0 record is complete and matches the decision log; every
missing fact maps to an `OQ`; nothing comes from the example (G-11); no assumption covers a G-4 item in
`CLIENT` mode; the reviewer can see exactly what they need to supply.

### Phase 1 — Business context, outcomes, measures (sections 2, 3, 4)

- Section 2: problem, current-state process with time categories, root causes,
  baseline list. Hypotheses stay labelled as hypotheses unless sourced.
- Section 3: opens with the recorded outcome statement. As many `BO` items as the outcome
  statement and inputs support, and no more, each with a one-paragraph statement of what observably changes and for whom, how it
  serves the outcome statement, and a one-line result of the G-10 test.
- Section 4: every `SM` and `SM-G` written out in the full definition format of
  section 4.4 (ID, definition, formula, population, exclusions, baseline, target,
  window, source, owner, associated guardrail). AI behavioural measures listed as
  leading indicators with the business measure each one leads.

Done when: every `BO` passes G-10 and serves the outcome statement; every `SM`
names its `BO`; every primary measure has at least one
guardrail; no baseline or target is invented.

### Phase 2 — Scope, actors, process, decisions (sections 5, 6, 7)

- Section 5: each scope dimension as a decided table (supported, not supported,
  `TBD`), the action table with an automation class from section 5.6 per action,
  and safe-failure behaviour for anything out of scope.
- Section 6: each actor with role in the workflow, decisions they are accountable
  for, and what they need from the system.
- Section 7: process boundary, the target process with a sentence per step naming
  the responsible layer, and the decision inventory expanded: inputs, authority,
  whether deterministic or judgment, and what happens when it cannot be made.

Done when: every action has an automation class and an accountable authority;
every decision `D-nnn` names its authority and its cannot-decide behaviour.

### Phase 3 — Authority, truth, requirements (sections 8, 9, 10)

- Section 8: the authority matrix (one row per authority type per action), the
  source-of-truth matrix completed for every information item used in section 7,
  freshness classes, and the revalidation boundaries placed on the target process.
- Section 9: each `BR` as a full statement with rationale, the `BO` it serves and
  priority.
- Section 10: at least one `BAC` per `BR`, including negative cases (what must not
  happen).

Done when: no information item lacks an authoritative source; every `BR` has a
`BAC`; nothing in section 8 lets the model establish authority (I-1).

### Phase 4 — Responsibilities, concerns, constraints, threats, quality (sections 11 to 15)

- Section 11: each `AR` with scope, the `BR`s it serves, and what it explicitly
  does not own.
- Section 12: each concern with why it matters here and which `AR` contains it.
- Section 13: constraints as `CON` items with justification; assumptions by include
  from the register; preferences kept separate and negotiable.
- Section 14: threat scenarios (`THR`) and failure scenarios (`FS`) in the section
  14.3 propagation format, at least one per threat category and failure category.
- Section 15: a `QAS` for each priority attribute that drives a design choice.

Done when: every concern is owned by an `AR`; every category in 14.1 and 14.2 has
a scenario; every `FS` has a safe response consistent with I-7 and I-8.

### Phase 5 — Drivers and patterns (sections 16, 17)

- Section 16: each `AD` with statement, the concerns and scenarios that force it,
  consequences, and what it rules out.
- Section 17: each `PAT` documented as the template requires: drivers addressed,
  responsibilities, trade-offs, risks introduced, validation mechanism.

Done when: every `FS` and `THR` is answered by at least one `AD`; every `AD` is
realised by at least one `PAT`; every `PAT` states how it will be validated.

### Phase 6 — Human authority and privacy (sections 18, 19)

- Section 18: review triggers tied to `D` and `FS` IDs; each queue defined
  (reviewers, authority, prioritisation, ownership, escalation); the decision
  package per queue; response-time and timeout behaviour; the adverse-decision taxonomy
  with which categories may be automated; the appeal flow.
- Section 19: data classification table; a model-boundary table with one row per
  model interaction (purpose, fields sent, why each is needed, prohibited fields,
  retention and logging behaviour); the retention matrix; logging rules.

Done when: no timeout path produces an approval (I-6); every model interaction is
listed with its minimum field set (I-9); every retention value is sourced or `TBD`.

### Phase 7 — Logical architecture and views (sections 20, 21)

- Section 20: each layer with responsibilities, what it may and may not do, its
  allowed dependencies, and the `AR`s and `PAT`s it hosts. Cross-cutting concerns
  with where each attaches.
- Section 21: every view the template lists, as Mermaid diagrams with reading guides,
  including the workflow state model with every state and legal transition.

Done when: every `AR` is placed in a layer; no dependency lets reasoning reach a
system of record (I-2); the state model has no state without an exit and no path
to success that skips verification (I-4).

### Phase 8 — Evaluation, autonomy, architecture acceptance (sections 22, 23)

- Section 22: eval scenarios derived through the chain in 22.1; the incorrect-
  automation taxonomy mapped to detection method; dataset governance; the
  test-versus-eval split applied to concrete items; gates A to C with required
  evidence, threshold and approver; rollback triggers.
- Section 23: each `AAC` with the `AD` and `PAT` it proves, the evidence type, and
  a pass condition a reviewer could check.

Done when: every probabilistic responsibility has an eval; every deterministic
contract has a test (G-7); every gate threshold is sourced or `TBD`; rollback does
not depend on the model (I-10).

### Phase 9 — Decisions (sections 24, 26, 27)

- One file per ADR in `ads/adr/`: context, decision, alternatives considered,
  consequences, drivers served, status. Section 24 is the register linking them.
- Section 26 by include from `registers/decisions.md`.
- Section 27: rejected alternatives with the reason and the ADR that settled each.

Done when: every `AD` is covered by at least one ADR; every ADR lists real
alternatives; ADRs stay logical (G-5).

### Phase 10 — Traceability and close-out (sections 1, 25, 28 to 31)

- Section 25: the complete matrix, one row per requirement at minimum, every cell
  a full ID.
- Section 28 by include from the open-questions register, plus a risk table.
- Sections 29, 30, 31 made specific to the decisions taken in this ADS.
- Section 1: the executive summary, written from the finished document.
- `ads/_header.md`: title, version, status, owners, date.
- Run `python3 scripts/ads.py build` and commit `ADS.md`.

Done when: the final check passes; every `BO`, `BR`, `AD`, `PAT` and `AAC` is in
the matrix; the summary claims nothing the body does not support.

## Log

One line per event: date, phase, what happened. Include deviations from this plan
and any revision PRs.

- 2026-10-07, step 1: outcome statement passed `/outcome` and was recorded as DEC-001.
- 2026-10-07, phase 0: drafted `ads/00-intake.md`, 34 open questions and 6 assumptions logged; in review.
- 2026-10-07, phase 0: context.md updated by the human; DEC-002 and DEC-003 recorded, ASM-003 rejected, OQ-034 added.
- 2026-10-07, phase 0: approved and merged. Changed during review: context.md facts recorded as DEC-002; per-state PTO policies recorded as DEC-003; ASM-003 rejected; OQ-001, OQ-002, OQ-005 resolved; OQ-034 added.
