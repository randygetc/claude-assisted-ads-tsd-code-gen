---
description: After explicit approval, open the PR for the current phase and merge it
---

The reviewer has approved the current phase. If their latest message is not an
explicit approval or this command, stop and ask.

1. Confirm you are on a `phase/` or `revise/` branch, not `main`.
2. Set `status: approved` in the phase file. In `docs/plan.md`, set the phase
   status to `merged` and add a Log line with today's date and a summary of what
   changed during review.
3. If this is phase 10, run `python3 scripts/ads.py build`.
4. Run `python3 scripts/ads.py check`. If it fails, fix the document and stop for
   re-review; do not continue.
5. Commit everything as `Phase N: <title>` and push the branch.
6. Open the PR with `gh pr create`. Title as the commit. Body: the reviewer brief,
   a "Changed during review" list, and the check summary line.
7. Wait for CI with `gh pr checks --watch`. If a check fails, report it and stop.
8. Merge with `gh pr merge --squash --delete-branch`.
9. `git checkout main && git pull`.
10. Reply with the PR link, the output of `python3 scripts/ads.py status`, and the
    name of the next phase. Do not start it.
