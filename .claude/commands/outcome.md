---
description: Step 1. Test the business outcome statement before any ADS work
argument-hint: [outcome statement]
---

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

Statement: $ARGUMENTS

## Procedure

This is section 0 of `inputs/ADS_template.md`. The statement defines the project;
nothing else is known about it yet. The record it produces becomes section 0
of the ADS in phase 0.

- If no statement follows "Statement:", ask for it and wait. Read no files and
  start no other work first.
- Judge the statement as written. Do not consult `inputs/` to rescue it.
- On a fail: write nothing to the repo. Say what was left after step 1 and why it
  is not a goal on its own, ask the question, and stop. Test the next statement
  the same way, from the top.
- On a pass: show the restatement and ask the human to confirm the wording. Only
  after they confirm:
  1. `git checkout main && git pull`, then create the branch `phase/00-intake`.
  2. Append a row to `registers/decisions.md`. The Decision cell reads exactly:
     `Outcome statement: "<restated>" Original wording: "<as given>"`.
     Owner: the human. Date: today. Basis: `Outcome test (KICKOFF step 1)`.
  3. Do not commit. Reply that step 1 is done and the next step is `/phase 0`.
- If a passed outcome statement is already recorded, say so and ask whether this
  one replaces it. A replacement is a new row that names the old `DEC`.
