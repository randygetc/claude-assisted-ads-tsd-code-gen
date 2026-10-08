# ADS Kit

Generates an Architecture Solution Design with Claude Code. The project is not
fixed in advance: it starts from a business outcome statement that must pass a
test, then proceeds in eleven reviewed phases, each merged to `main` by pull request.

Start with **docs/KICKOFF.md**.

| Path | What it is | Claude Code edits? |
|---|---|---|
| `CLAUDE.md` | Project instructions and the review loop | No |
| `docs/architecture.md` | Fixed structure, invariants, generation rules | No |
| `docs/conventions.md` | How the document is written | Appends only |
| `docs/plan.md` | Phases, done-when criteria, status, log | Yes |
| `docs/KICKOFF.md` | Your guide | No need |
| `inputs/ADS_template.md` | The section specification, project-neutral | No |
| `inputs/example/` | A sample ADS for an unrelated project; format only, never a source | No |
| `inputs/context.md`, `inputs/discovery/` | Your facts and source material | No |
| `ads/` | One file per phase; ADRs in `ads/adr/` | Yes |
| `registers/` | Open questions, assumptions, decisions (start empty) | Yes |
| `scripts/ads.py` | `check`, `build`, `status` | No |
| `.claude/` | Permissions and the `/outcome`, `/phase`, `/phase-done` commands | No |
| `.github/workflows/ads-check.yml` | Required CI check | No |
| `ADS.md` | Assembled output (appears in phase 10) | Via build only |
