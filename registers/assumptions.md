# Assumptions

Working assumptions awaiting validation. Rows are never deleted.

| ID | Assumption | Why it is needed | Used in | Validate with | Status |
|---|---|---|---|---|---|
| **ASM-001** | Illustrative: A written PTO policy, owned by HR, governs what employees may take and how requests are settled. | The outcome statement names PTO and HR but no policy; the design needs a rule source. | Phases 1, 2, 3 | Policy Owner | unvalidated |
| **ASM-002** | Illustrative: A routine request is one that the written policy settles by rule alone, with no judgment about the individual case; every other request is an exception that needs a person. | The outcome statement says routine without defining it; scope and authority need a working line. | Phases 2, 3 | Policy Owner | unvalidated |
| **ASM-003** | Illustrative: The first release covers one jurisdiction and one policy set. | Bounds the rule variants and eval cases for a reference design. | Phases 2, 3 | Policy Owner | rejected (DEC-003) |
| **ASM-004** | Illustrative: Employees request leave for themselves only; requests made on behalf of others are out of the first release. | Avoids delegation and proxy-authority cases until scope is decided. | Phases 2, 3 | Business Owner | unvalidated |
| **ASM-005** | Illustrative: A system of record exists for leave balances and approved leave, and the solution can read it and verify changes against it. Stated logically, no product. | Source-of-truth and read-back verification (I-4) need an authoritative store. | Phases 3, 7 | Architecture Owner | unvalidated |
| **ASM-006** | Illustrative: A trusted source of employee identity exists and the solution relies on it; the model never establishes identity (I-1). | Every request must be tied to an identified employee. | Phases 3, 4 | Architecture Owner | unvalidated |
