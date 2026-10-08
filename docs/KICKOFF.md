# Kickoff

Your guide to generating an Architecture Solution Design with Claude Code, one
reviewed phase at a time. The kit does not know your project. It learns it from
the outcome statement you give in step 1 and from `inputs/context.md`. Claude Code does not need this file; it works from `CLAUDE.md`,
`docs/architecture.md`, `docs/conventions.md` and `docs/plan.md`.

## How this maps to a code project

| Code project | This repo |
|---|---|
| Source files | `ads/NN-*.md`, one per phase |
| Build output | `ADS.md`, assembled by `scripts/ads.py build` |
| Compiler and tests | `scripts/ads.py check` |
| Spec | `inputs/ADS_template.md` (sections only, no project content) |
| Architecture rules | `docs/architecture.md`: invariants I-1 to I-11, rules G-1 to G-11 |
| Requirements from the customer | `inputs/context.md`, `inputs/discovery/` |
| Issue tracker | `registers/` (open questions, assumptions, decisions) |
| CI | `.github/workflows/ads-check.yml` |

The check script catches structural faults: a missing section, an ID that is
referenced but never defined, a `TBD` nobody owns, a requirement with no acceptance
criterion, a gap in the traceability matrix. It cannot tell whether the content is
right. That is your review.

## 0. Setup (once)

**0.1 Create the repo.**

```bash
cd ads-kit          # rename the folder for your project if you like
git init -b main
python3 scripts/ads.py check          # expect: 0 errors
git add -A && git commit -m "ADS generation kit"
gh repo create <your-repo-name> --private --source=. --push
gh label create control-change --description "Changes locked control files"
```

**0.2 Protect `main`.** In GitHub: Settings, Branches, add a rule for `main`:
require a pull request before merging, require the status check `ads-check`, and
do not allow bypassing. The `ads-check` status only appears in the picker after
it has run once, so add that requirement after the Phase 0 PR.

**0.3 Fill in `inputs/context.md`.** Set the mode first. `CLIENT` means numbers are
never assumed; `REFERENCE` allows illustrative values that are logged as
assumptions. Answer what you know and leave the rest as `unknown`. Drop any policy
documents or interview notes into `inputs/discovery/`. Commit these to `main`
before turning on branch protection, or through a PR afterwards.

The less you supply, the more of the ADS comes back as tracked `TBD`s. That is the
correct result, not a failure: the template says targets shall not be invented.

You can do 0.3 after step 1 if you prefer; the outcome test reads no inputs.

**0.4 Start Claude Code** from the repo root so the deny rules resolve:

```bash
claude
```

## 1. Step 1: test the outcome statement

Before any phase, give Claude Code the business outcome statement:

> /outcome <your statement>

The command carries this prompt:

```
I'm going to give you a business outcome statement. Before doing
anything else, test it:

1. Remove any mention of AI, an assistant, automation, or specific
   technology from the sentence.

2. Does it still describe a coherent goal a reasonable person could
   pursue by multiple different means — not just the one I have in
   mind?

If yes, confirm it passes and restate it cleanly.

If no, tell me explicitly that this is a solution disguised as an
outcome, and ask me what the underlying goal actually is — don't
guess at it or silently fix it yourself.
```

On a fail nothing is written; you answer the question and try again. On a pass you
confirm the restated wording, and it is recorded in `registers/decisions.md` on the
`phase/00-intake` branch. It merges with Phase 0.

This is section 0 of the specification, so it is part of the ADS, not only a
habit of the kit. The statement becomes the root of the document. Phase 0 writes
it up as section 0, every
business outcome in section 3 must serve it and pass the same test (rule G-10),
and `/phase 0` and the check script both refuse to proceed without it.

## 2. The loop

Every phase is the same four moves.

**Generate.**

> /phase 1

Claude Code branches, writes the phase file, updates the registers and the plan,
runs the check until it passes, and stops without committing.

**Examine.** Open `ads/01-business-context.md`. Start with the reviewer brief at the
top, then read the sections. Use the checklist for that phase in section 3.

**Revise.** Give feedback in plain language. Answers to open questions are recorded
as decisions for you.

> In 4.1, SM-003 should start at submission, not at first contact. For OQ-001:
> first release covers the two simplest request types only. Section 2.3 reads like the template; make
> the root causes specific to what the interview notes say.

Claude Code edits the same file, re-runs the check and stops again. Repeat until
you are satisfied.

**Merge.**

> Approved. /phase-done

Claude Code commits, pushes, opens the PR with the reviewer brief as its body,
waits for CI, squash-merges and returns to `main`. You are asked to confirm the
push, the PR and the merge; those prompts are a deliberate second gate.

If you would rather read the rendered Markdown and the diff on GitHub, say
"open the PR but do not merge" instead, review there, then say "merge it".

## 3. Phase by phase

Prompt for every phase is `/phase N`. What changes is what you look for.

**Phase 0 — Outcome statement and intake.** Runs on the branch `/outcome` created.
Section 0 should match what you confirmed, word for word. Above it, a working paper listing what your inputs establish and what
they do not. Check that the top questions are the right ones, and that no
assumption has quietly settled something you should decide. Answering questions
here is cheaper than at any later point.

**Phase 1 — Business context, outcomes, measures.** Does each business outcome
still read as a goal with the technology stripped out? Is every pain point marked as a
hypothesis unless you gave evidence? Does each measure have a real formula,
population and source? Are baselines and targets sourced or `TBD`, never
plausible-looking numbers?

**Phase 2 — Scope, actors, process, decisions.** Does every action have an
automation class? Is "in scope" kept separate from "automated"? For each decision
in the inventory, is the authority a person or system, never the model?

**Phase 3 — Authority, truth, requirements.** Read the two matrices line by line;
they drive everything after. Does every requirement have an acceptance criterion
you could observe from outside? Are there negative criteria (what must not happen)?

**Phase 4 — Responsibilities, concerns, threats, quality.** Does each failure
scenario end in a safe response, not a retry loop? Is a technical failure ever
presented to the user as a refusal? Are quality scenarios measurable?

**Phase 5 — Drivers and patterns.** Does each pattern state the risk it introduces
and how it will be validated? Is anything here a product choice in disguise?

**Phase 6 — Human review and privacy.** Trace every timeout: none may end in
approval. For each model interaction, would you defend every field in the "sent"
column to a privacy officer?

**Phase 7 — Logical architecture and views.** Follow the arrows: can reasoning reach
a system of record without passing control and a capability? In the state model,
is there any route to "completed" that skips verification?

**Phase 8 — Evaluation and acceptance.** Is each item correctly a test or an eval?
Does each gate name its evidence and approver? Could each acceptance criterion be
failed by a real implementation?

**Phase 9 — Decisions.** Do the ADRs record real alternatives and real trade-offs?
Is the decision log an accurate history of what you decided in review?

**Phase 10 — Traceability and close-out.** Pick three requirements at random and
walk each across the matrix. Read the executive summary last and check it claims
nothing the body does not support. `ADS.md` is in this PR.

## 4. Changing something already merged

> Revise phase 3: BR-006 needs to cover delegated approval. Use a revision branch.

Claude Code branches `revise/03-...`, edits the merged file, updates anything
downstream that references the change, and runs the same review and merge loop.
IDs are never renumbered, so later phases keep working.

## 5. Changing the rules

`CLAUDE.md`, `docs/architecture.md`, `inputs/ADS_template.md`, `inputs/example/`,
`scripts/`, `.github/` and
`.claude/` are locked three ways: Claude Code's deny rules, the instructions in
`CLAUDE.md`, and a CI step that fails any PR touching them. To change one, make the
edit yourself on a branch and label the PR `control-change`. If you change the
section list or the phase mapping, change `docs/plan.md` and the two tables at the
top of `scripts/ads.py` together.

Deny rules stop the edit tools, not every possible shell command, so the CI step
is the backstop. Do not make Claude Code an admin on the repo.

## 6. When something goes wrong

| Symptom | What to do |
|---|---|
| Check fails with "referenced but never defined" | An ID was used before being created, or mistyped. Ask Claude Code to fix the document, not the script. |
| Check fails with "TBD without an OQ" | An unknown was not logged. This is the check doing its job. |
| Content resembles the PTO example | Rule G-11 was broken. Reject the phase; the example is never a source. |
| A phase file mostly repeats the template | Rule G-2 was missed. Say "this restates the template; write the actual content or mark it TBD". |
| Confident numbers you never supplied | Rule G-4 was broken. Reject the phase and ask for every figure's source. |
| Product or vendor names appear | Rule G-5. Ask for the logical responsibility instead, unless you set the product as a constraint. |
| Claude Code starts the next phase unasked | Stop it; the loop requires your approval between phases. |
| Context is getting long | Start a fresh session between phases. Everything it needs is in the repo. |

A fresh session per phase is good practice anyway: it proves the repo, not the
chat history, carries the state.

## 7. After phase 10

`ADS.md` on `main` is the reviewable draft. What remains is human work: the open
questions still marked `open`, the assumptions still `unvalidated`, and sign-off by
the three owners named in the header. Each answer comes back in through a revision
PR, which is the governance loop template section 29 asks for.
