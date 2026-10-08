# Open Questions

Rows are never deleted; status changes instead.

| ID | Question | Impact | Owner | Required by | Status |
|---|---|---|---|---|---|
| **OQ-001** | Project name for the document title. | Document title and header. | Architecture Owner | Phase 10 | resolved (DEC-002) |
| **OQ-002** | What is the organisation, or a description of it (size, sector, structure of HR)? | Frames context, actors and policy variants. | Business Owner | Phase 1 | resolved (DEC-002) |
| **OQ-003** | Who holds the roles Architecture Owner, Business Owner and Risk / Privacy Owner? | Owners on every register row and in the header; sign-off for later phases. | Engagement Sponsor | Phase 1 | open |
| **OQ-004** | Which employee populations does the first release serve (full-time, part-time, contract, new starters, managers)? | Policy variants, eval cases, scope table. | Business Owner | Phase 2 | open |
| **OQ-005** | Which locations or jurisdictions are involved, and which leave rules apply in each? | Rule sets, legal constraints, data residency. | Policy Owner | Phase 2 | resolved (DEC-003) |
| **OQ-006** | Which request types count as PTO and are in the first release (for example planned leave, short-notice leave, other leave types)? | Scope table and automation boundary. | Business Owner | Phase 2 | open |
| **OQ-007** | What makes a PTO request routine rather than an exception? Give the criteria. | Splits the automation boundary; the outcome statement depends on it. | Policy Owner | Phase 2 | open |
| **OQ-008** | Which actions are in the first release (answer a question, submit, change, cancel, check balance)? | Whether any system of record is mutated; automation class per action. | Business Owner | Phase 2 | open |
| **OQ-009** | Which actions must always stay with a human? | Hard limits on autonomy (I-6); review triggers. | Policy Owner | Phase 2 | open |
| **OQ-010** | What is explicitly out of scope for the first release? | Scope table and safe failure for unsupported cases. | Business Owner | Phase 2 | open |
| **OQ-011** | Who holds approval authority for a routine PTO request today, and does policy allow a routine request to be settled by rule without a person approving? | Largest driver of the automation class per action and of the authority matrix. | Policy Owner | Phase 2 | open |
| **OQ-012** | Who holds authority to decide exceptions, and what are the exception categories? | Exception path, review queues, authority matrix. | Policy Owner | Phase 3 | open |
| **OQ-013** | Does any law, agreement or works-council rule require a person to take, or be consulted on, a leave decision or refusal? | Could bar rule-based settlement for some or all requests. | Risk / Privacy Owner | Phase 2 | open |
| **OQ-014** | Which systems hold leave balances, requests, approvals and team calendars, and which is the system of record for each? | Source-of-truth matrix, capability boundary, read-back verification (I-4). | Architecture Owner | Phase 3 | open |
| **OQ-015** | How are employees identified and authenticated when they make a request? | Identity handling (I-1); impersonation threats. | Architecture Owner | Phase 3 | open |
| **OQ-016** | Where does the PTO policy live, who owns it, and is it versioned and effective-dated? | Rule source and degradation when policy is unavailable (I-8). | Policy Owner | Phase 3 | open |
| **OQ-017** | Which channels do employees use to make requests (portal, chat, email, other)? | Experience layer, input threats, view of system context. | Business Owner | Phase 2 | open |
| **OQ-018** | What constraints apply to any model provider (residency, retention, permitted data, approved vendors)? | Model provider boundary and data minimisation (I-9). | Risk / Privacy Owner | Phase 6 | open |
| **OQ-019** | How is a PTO request handled today, step by step, and by whom? | Current-state process and root causes. | Business Owner | Phase 1 | open |
| **OQ-020** | What pain points exist today, and what evidence supports each? | Hypotheses become evidenced or stay labelled. | Business Owner | Phase 1 | open |
| **OQ-021** | What are the baselines: request volumes, handling time, waiting time, share needing HR, rework and error rates? | No target can be set without a baseline (G-4). | Business Owner | Phase 1 | open |
| **OQ-022** | What does waiting mean for the outcome: what time to resolution is acceptable, and what counts as resolved? | Success measures, quality attribute scenarios. | Business Owner | Phase 1 | open |
| **OQ-023** | What counts as HR intervention for measurement purposes? | Primary measure definition and exclusions. | Business Owner | Phase 1 | open |
| **OQ-024** | Which regulatory, legal or contractual constraints apply? | Constraint list and threat model. | Risk / Privacy Owner | Phase 4 | open |
| **OQ-025** | What retention periods apply to PTO records, conversation records and logs? | Retention matrix (G-4: never invented). | Risk / Privacy Owner | Phase 6 | open |
| **OQ-026** | Do PTO requests carry sensitive information (health, family, religious or bereavement reasons)? | Data classification and what the model may receive (I-9). | Risk / Privacy Owner | Phase 6 | open |
| **OQ-027** | Who reviews requests that need a person, and what response time is committed? | Review queues and timeout behaviour (I-6). | Business Owner | Phase 6 | open |
| **OQ-028** | Who may refuse a request, and what appeal or reconsideration route exists? | Adverse-decision taxonomy and appeals. | Policy Owner | Phase 6 | open |
| **OQ-029** | What cost or resource limits apply to the solution (I-11)? | Economic failure scenarios and quality attributes. | Business Owner | Phase 4 | open |
| **OQ-030** | Who approves each autonomy gate, and what evidence must they see? | Autonomy gates and rollback (I-10). | Business Owner | Phase 8 | open |
| **OQ-031** | Are there technology preferences or fixed technology constraints? | Stays negotiable unless promoted to a constraint (G-5). | Architecture Owner | Phase 4 | open |
| **OQ-032** | Is there source material to add under inputs/discovery/ (policy text, interview notes, process exports)? | Replaces hypotheses with evidence. | Business Owner | Phase 1 | open |
| **OQ-033** | Who approves changes to the ADS after it is accepted, and who owns production evidence? | Governance and production feedback loop. | Architecture Owner | Phase 10 | open |
| **OQ-034** | What does each state policy (CA, NY, NJ) say, who owns each, and how do they differ for routine requests? | Rule variants per state; routine versus exception line; eval cases. | Policy Owner | Phase 2 | open |
