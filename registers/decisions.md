# Decision Log

Business and design decisions, including answers given during phase review. Rows
are never deleted; a reversed decision gets a new row that names the old one.

| ID | Decision | Owner | Date | Basis | Related IDs |
|---|---|---|---|---|---|
| **DEC-001** | Outcome statement: "Employees resolve routine PTO requests without waiting on HR intervention." Original wording: "Employees should be able to resolve routine PTO requests without waiting on HR intervention" | Human | 2026-10-07 | Outcome test (KICKOFF step 1) | |
| **DEC-002** | Project facts supplied in `inputs/context.md`: project name is Project Leaves; the organisation is US Wide Corp with offices in CA, NY and NJ; the people served are staff; the jurisdictions are CA, NY and NJ. | Human | 2026-10-07 | `inputs/context.md` | OQ-001, OQ-002 |
| **DEC-003** | Each of the three states (CA, NY, NJ) has its own PTO policy. The first release therefore cannot assume one policy set. | Human | 2026-10-07 | review of phase 0 | OQ-005, ASM-003 |
