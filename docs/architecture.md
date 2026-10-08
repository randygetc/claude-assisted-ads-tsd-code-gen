# Document Architecture

**LOCKED.** Claude Code proposes changes to this file; it never edits it. A change
needs a PR labelled `control-change`, opened by the architecture owner.

This file plays the role `architecture.md` plays in a code repo: it fixes the
structure and the invariants of the thing being built. Here the thing being built
is `ADS.md`, an Architecture Solution Design for a project that is not known in
advance. The outcome statement in section 0 and `inputs/context.md` define it.

## 1. What is fixed

| Fixed | Source of truth |
|---|---|
| The 32 sections (0 to 31), their numbers and titles | `inputs/ADS_template.md`, mirrored in `scripts/ads.py` |
| Which phase writes which section | `docs/plan.md` phase table, mirrored in `scripts/ads.py` |
| What each section must contain | `inputs/ADS_template.md` |
| The ID series and their meaning | Section 5 below |
| The governing principle and invariants | Section 3 below |
| The provenance rules | Section 4 below |

`inputs/ADS_template.md` is project-neutral. It says what each section must
contain and holds no project content. The generated ADS keeps its skeleton and
replaces the guidance with content for this project.

Nothing about the project is fixed here: no outcomes, requirements, scope, actors,
systems or decisions. Every ID series starts empty.

## 2. Repository layout

```
CLAUDE.md                  project instructions (locked)
docs/architecture.md       this file (locked)
docs/conventions.md        writing conventions (Claude may append)
docs/plan.md               phase plan and status (Claude updates)
docs/KICKOFF.md            the human's guide
inputs/ADS_template.md     the section specification (locked)
inputs/example/            sample ADS for an unrelated project (locked, format only)
inputs/context.md          engagement facts, written by the human
inputs/discovery/          raw source material, added by the human
ads/NN-*.md                one file per phase: the reviewable output
ads/adr/ADR-NNNN-*.md      one file per architecture decision
ads/_header.md             title block for the assembled document
registers/*.md             open questions, assumptions, decisions
scripts/ads.py             check / build / status (locked)
ADS.md                     assembled output, generated, never hand-edited
```

## 3. Invariants

These hold for any solution that includes probabilistic components, whatever the
project. The governing principle may not be weakened, qualified or
paraphrased into something softer:

> Probabilistic intelligence may interpret, reason, recommend, and propose. It does
> not manufacture truth or authority. Consequential business actions require trusted
> facts, authorized decisions, deterministic controls, bounded capabilities, and
> verified outcomes.

No section of the ADS may contradict any of these:

| ID | Invariant |
|---|---|
| I-1 | The model never establishes identity, business facts, roles, approval, or system-of-record state. |
| I-2 | Reasoning never directly mutates a system of record; consequential actions go through bounded capabilities. |
| I-3 | Deterministic control, not the model, decides whether execution may occur. |
| I-4 | Success is reported only after authoritative read-back confirms the intended state. |
| I-5 | An unknown execution outcome is reconciled before any consequential retry. |
| I-6 | Required human judgment, exception authority and mandated approval cannot be bypassed, timed out into approval, or simulated. |
| I-7 | Technical failure, missing information and rule ambiguity are never presented as a business refusal. |
| I-8 | When authoritative policy or trusted state is unavailable, autonomy reduces; model general knowledge is never substituted. |
| I-9 | The model receives the minimum data needed for the approved reasoning task; telemetry follows the same rule. |
| I-10 | Autonomy level never exceeds what current evaluation and production evidence supports, and is reversible without the model's cooperation. |
| I-11 | Deterministic cost and resource limits cannot be overridden by model behaviour. |

If inputs or review feedback appear to require breaking an invariant, stop and
escalate (rule G-8). Do not write a compromise.

If the project turns out to have no probabilistic component in some area, the
affected sections stay in place and say "Not applicable" with the reason. Sections
are never deleted.

## 4. Generation rules

**G-1 Template fidelity.** Section numbers and titles are fixed. Every ID series
starts at 001 for this project. New items take the next free number in their
series. IDs are never renumbered or reused, including after deletion.

**G-2 Fulfil, do not restate.** Where the template says a section "Contains"
something, the ADS contains that thing for this project: the
actual matrix, scenario, queue definition or measure definition. Where it cannot be
written yet, the item is marked `TBD` under G-3. A section that only repeats the
template's guidance is not done.

**G-3 Provenance.** Every statement specific to this project (scope, systems,
policies, volumes, owners, timings, thresholds) is exactly one of:

| Kind | Form | Meaning |
|---|---|---|
| Sourced | `[src: inputs/context.md]`, `[src: DEC-004]` | A human supplied or decided it. |
| Assumed | `[ASM-007]` | A working assumption logged in `registers/assumptions.md`, awaiting validation. |
| Unknown | `TBD (OQ-012)` | Not known; logged in `registers/open-questions.md` with an owner role. |

Statements that follow from the invariants or from general architecture reasoning
need no tag.

**G-4 No invented evidence.** Baselines, targets, thresholds, response-time
commitments, retention periods, volumes and costs are never made up. In `CLIENT`
mode they are sourced or `TBD`. In `REFERENCE` mode they may be assumed, with the
assumption text beginning "Illustrative:". The mode is set in `inputs/context.md`.

**G-5 Logical, not technical.** The ADS names responsibilities, boundaries and
patterns. It does not select products, vendors, frameworks, model names or cloud
services unless `inputs/context.md` states one as a constraint. Technology choice
belongs to the downstream technical design.

**G-6 Traceability.** Every new element names what it serves, using full IDs:

```
SM -> BO      BR -> BO      BAC -> BR     AR -> BR
FS / THR -> AR              AD -> concern, FS or THR
PAT -> AD     QAS -> quality attribute + AD
AAC -> AD and PAT           ADR -> AD
```

An element that serves nothing upstream is removed or justified in the reviewer brief.

**G-7 Tests versus evals.** Every acceptance item states whether it is proven by a
deterministic test or measured by an eval, following template section 22.5. Deterministic
contracts are never assigned to evals.

**G-8 Stop and escalate.** When the work needs a business decision, a scope change,
or a change to a locked file, stop. Log the question, state it in the reply, and
wait. Unresolved questions never silently become assumptions. This mirrors template
section 29.

**G-9 One phase, one branch, one PR.** A phase writes only its own file, the
registers, `docs/plan.md` and `docs/conventions.md` (plus ADR files in phase 9 and
`ads/_header.md` and `ADS.md` in phase 10). A merged phase file changes only through
a separate revision PR recorded in the plan's log.

**G-10 Outcomes are goals, not solutions.** Section 0 comes first: no other
section is drafted until its record is complete. The recorded outcome statement is
the root of the document. Every `BO` in section 3 serves it and passes the same test:
with all mention of AI, assistants, automation and specific technology removed, it
still describes a coherent goal that could be pursued by more than one means. A
`BO` that fails is escalated under G-8, not reworded until it passes.

**G-11 The example is not a source.** `inputs/example/` shows how deep a section
goes and how items are formatted, for a different project. No outcome,
requirement, measure, scope item, actor, system, decision, open question, ID or
sentence from it is carried into this ADS. If a section can only be filled by
borrowing from the example, the content is unknown: mark it `TBD` under G-3.

## 5. ID series

| Prefix | Meaning | Defined in section |
|---|---|---|
| (none) | Outcome statement, recorded once | 0 |
| `BO-nnn` | Business outcome | 3 |
| `SM-nnn`, `SM-Gnn` | Success measure, guardrail measure | 4 |
| `D-nnn` | Decision in the decision inventory | 7 |
| `BR-nnn` | Business requirement | 9 |
| `BAC-nnn-nn` | Acceptance criterion for `BR-nnn` | 10 |
| `AR-XXX` | Architectural responsibility | 11 |
| `CON-nnn` | Constraint | 13 |
| `THR-nnn` | Threat scenario | 14 |
| `FS-nnn` | Failure scenario | 14 |
| `QAS-nnn` | Quality attribute scenario | 15 |
| `AD-nnn` | Architecture driver | 16 |
| `PAT-nnn` | Architecture pattern | 17 |
| `AAC-nnn` | Architecture acceptance criterion | 23 |
| `ADR-nnnn` | Architecture decision record | `ads/adr/` |
| `ALT-nnn` | Rejected alternative | 27 |
| `DEC-nnn` | Decision log entry | `registers/decisions.md` |
| `OQ-nnn` | Open question | `registers/open-questions.md` |
| `ASM-nnn` | Assumption | `registers/assumptions.md` |

## 6. Enforcement

| Rule | Enforced by |
|---|---|
| Locked files | `.claude/settings.json` deny rules; CI fails a PR that touches them without the `control-change` label |
| A passed outcome statement exists before any phase file | `/outcome`; `scripts/ads.py check` |
| Section list, titles, phase mapping | `scripts/ads.py check` |
| Every referenced ID is defined once | `scripts/ads.py check` |
| No `TBD` without an open question | `scripts/ads.py check` |
| Every requirement has an acceptance criterion | `scripts/ads.py check` |
| Outcomes, requirements, drivers, patterns and acceptance criteria all appear in the traceability matrix | `scripts/ads.py check` (final) |
| `ADS.md` matches the phase files | `scripts/ads.py check` (final) |
| Invariants, G-2, G-4, G-5, G-7, G-10, G-11 | Human review of each phase file; these are judgment calls no script can make |
| Nothing reaches `main` unchecked | Branch protection requiring the `ads-check` status |
