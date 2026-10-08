---
description: Generate one ADS phase file and stop for review
argument-hint: <phase number 0-10>
---

Generate phase $ARGUMENTS of the ADS.

1. Read `docs/plan.md`. Confirm every earlier phase is `merged`. If not, stop and
   say which phase is outstanding.
2. `git checkout main && git pull`, then create the branch `phase/NN-slug` matching
   the phase file name in the plan. Phase 0 is the exception: it continues on the
   `phase/00-intake` branch that `/outcome` created. If `registers/decisions.md`
   has no `Outcome statement:` row, stop and tell the human to run `/outcome`.
3. Read, in full: the sections for this phase in `inputs/ADS_template.md`,
   `inputs/context.md`, everything in `inputs/discovery/`, every merged file in
   `ads/`, and all three registers.
4. Write the phase file named in the plan. Follow the phase's detail and "Done
   when" list in `docs/plan.md`, the rules in `docs/architecture.md`, and
   `docs/conventions.md`. Front matter `status: draft`. Begin with the reviewer
   brief.
5. Update the registers for every new `OQ`, `ASM` and `DEC`.
6. Set the phase status to `in review` in `docs/plan.md`.
7. Run `python3 scripts/ads.py check`. Fix the document until it passes. Do not
   touch the script.
8. Re-read your file once against the invariants I-1 to I-11 and the "Done when"
   list. Fix what you find and re-run the check.
9. Stop. Do not commit. Reply with: the file path, the reviewer brief, the check
   summary line, and the decisions you need from the reviewer.
