# Conventions

How the ADS is written. Claude Code may append to the "Learned" section at the end
during a phase; changes to the sections above it are proposed in the reviewer brief.

## Phase file shape

```markdown
---
phase: 3
status: draft
---

## Reviewer brief

(see below)

# 8. Authority, Truth, and Temporal Validity

## 8.1 Core Distinction
...

# 9. Business Requirements
```

- `status` is `draft` until `/phase-done` sets it to `approved`.
- H1 is used only for numbered ADS sections, written `# 8. Title` with the exact
  title from the template. No bold in headings, no escaped periods.
- Subsections are `## 8.1 Title`, then `###` as needed. Keep the template's subsection
  numbers; add new ones after the last existing number.
- Everything above the first H1 is for the reviewer and is left out of `ADS.md`.

## Reviewer brief

Short, factual, written for someone deciding whether to merge. In this order:

1. **What this phase added**: three to six lines.
2. **Additions to the template**: new subsections, and any section marked not
   applicable, with the reason.
3. **Provenance**: counts of sourced, assumed and TBD statements; list the new
   `ASM` and `OQ` IDs with one line each.
4. **Decisions needed from you**: the questions whose answers would change this
   file most, most important first.
5. **Look hardest at**: the two or three places most likely to be wrong.

## IDs

- An ID is **defined** once: as the start of a heading (`### BR-015 — Title`), or
  in bold at the start of a table row or list item (`| **D-012** | ... |`).
- Everywhere else it is a **reference**, written plain: `BR-015`.
- Never abbreviate lists of IDs. Write `BR-003, BR-004`, not `BR-003/004`.
- Titles follow the ID after an em dash with spaces.
- Check the series' highest existing number before adding one.

## Provenance tags

- Sourced: `[src: inputs/context.md]`, `[src: inputs/discovery/interview-notes.md]`,
  `[src: DEC-004]`. Put the tag at the end of the sentence or in the table cell.
- Assumed: `[ASM-007]`.
- Unknown: `TBD (OQ-012)`. The words must be on the same line.
- One open question per distinct unknown. Reuse the existing `OQ` when the same
  unknown appears again.

## Registers

`registers/open-questions.md`, `assumptions.md` and `decisions.md` are append-only
tables. Rows are never deleted; status changes instead.

- Open question status: `open`, or `resolved (DEC-nnn)`.
- Assumption status: `unvalidated`, `validated (DEC-nnn)`, or `rejected (DEC-nnn)`.
- Owners are roles (Business Owner, Policy Owner, Privacy) unless
  `inputs/context.md` names a person.

Sections 13, 26 and 28 pull the registers in with an include line rather than
copying them:

```markdown
<!-- include: registers/open-questions.md -->
```

## Language

- Normative keywords in capitals, with their usual meaning: SHALL (required),
  SHOULD (expected unless justified), MAY (permitted). Use them for requirements,
  not for emphasis.
- Present tense, active voice, one requirement per sentence.
- Name the actor. "The control layer rejects the request", not "the request is
  rejected".
- Use the template's vocabulary exactly: claim, fact, decision, evidence; routine and
  exception; disposition; system of record; bounded capability. Do not introduce
  synonyms.
- No marketing language and no hedging stacks. If something is uncertain, tag it.

## Tables, lists, diagrams

- Tables for anything with more than two attributes per item (matrices, registers,
  scenarios). Lists for simple enumerations. Prose for reasoning.
- Diagrams are Mermaid in fenced blocks so they render on GitHub. Plain-text
  flows are fine for simple linear sequences.
- Every architecture view in section 21 has a diagram, a one-paragraph reading
  guide, and the IDs it illustrates.

## Scenario formats

- Quality attribute scenario: source, stimulus, environment, artifact, response,
  response measure. The measure is sourced, assumed or TBD like any other number.
- Failure scenario: cause, local failure, business consequence, safe response,
  recovery, evidence, as in template section 14.3.
- Acceptance criterion: Given / When / Then in one or two sentences, observable
  from outside the implementation.

## Git

- Branch: `phase/NN-slug`, matching the phase file name.
- One commit per phase, squash-merged. Message: `Phase N: <title>`.
- PR title the same. PR body is the reviewer brief plus the check summary line.
- Revisions to a merged phase: branch `revise/NN-short-reason`, PR title
  `Revise phase N: <reason>`, and a line in the plan's log.

## Learned

Conventions discovered while writing. Add a dated line; do not rewrite the above.
