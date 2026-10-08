# **PTO Agent — Architecture Solution Design**

**Document:** ADS.md  
**Status:** Draft  
**Version:** 3.1  
**Architecture Owner:** TBD  
**Business Owner:** TBD  
**Risk / Privacy Owner:** TBD  
**Last Updated:** TBD

---

# **0\. Outcome Statement Test**

No ADS work begins until the business outcome statement has passed this test. It is the first step, ahead of discovery, scope, requirements, and architecture.

## **0.1 The Test**

Given a business outcome statement:

1. Remove any mention of AI, an assistant, automation, or specific technology from the sentence.  
2. Ask whether what remains still describes a coherent goal a reasonable person could pursue by multiple different means, not only the one the author has in mind.

---

## **0.2 Disposition**

**If yes**, the statement passes. The pass is confirmed and the statement is restated cleanly.

**If no**, the statement is a **solution disguised as an outcome**. This SHALL be said explicitly to its author, and the author SHALL be asked what the underlying goal actually is.

The underlying goal SHALL NOT be guessed, and a failing statement SHALL NOT be silently fixed. Only the business owner can supply the goal.

A failed statement is retested from the first step each time it is revised.

---

## **0.3 Outcome Statement Record**

| Field | Value |
| ----- | ----- |
| Statement as given | TBD |
| Statement with technology removed | TBD |
| Result | TBD |
| Restated outcome statement | TBD |
| Confirmed by | TBD |
| Date | TBD |

---

## **0.4 Effect on the Rest of the ADS**

* The restated outcome statement is the root of the traceability chain in Section 25\.  
* Every business outcome in Section 3 SHALL serve the outcome statement and SHALL pass the same test.  
* No section of the ADS may be drafted, and no architecture work may start, while the record in 0.3 is incomplete.  
* A change to the outcome statement is a material change under Section 29 and requires the test to be repeated.

---

# **1\. Executive Summary**

The PTO Agent enables employees to understand and complete supported paid-time-off workflows through natural-language interaction while preserving enterprise policy, organizational authority, privacy, security, auditability, and system-of-record integrity.

The solution is not an LLM with direct access to enterprise APIs.

It is a **controlled decision-and-action system** in which:

* probabilistic models interpret language and perform bounded reasoning;  
* trusted enterprise systems establish identity and authoritative facts;  
* governed knowledge sources establish approved policy content;  
* deterministic controls enforce settled business rules and authorization;  
* durable workflow owns business-process state;  
* authorized humans retain judgment and exception authority;  
* bounded capabilities perform consequential enterprise actions;  
* systems of record remain authoritative for business state;  
* verification establishes what actually happened;  
* evidence preserves reconstructability;  
* evals measure probabilistic and agentic behavior;  
* deterministic tests enforce architectural invariants;  
* autonomy expands only when evidence supports expansion;  
* production telemetry determines whether business outcomes actually occur.

The governing principle is:

> **Probabilistic intelligence may interpret, reason, recommend, and propose. It does not manufacture truth or authority. Consequential business actions require trusted facts, authorized decisions, deterministic controls, bounded capabilities, and verified outcomes.**

---

# **2\. Business Context**

## **2.1 Problem / Opportunity**

Routine PTO workflows can require employees, managers, and HR personnel to navigate policy documents, HR systems, messaging channels, approval workflows, and organizational rules.

Representative friction may include:

* uncertainty about applicable policy;  
* uncertainty about eligibility;  
* inability to determine current balance;  
* repeated HR questions;  
* unclear approval requirements;  
* manual routing;  
* long approval waits;  
* inconsistent interpretation;  
* rework;  
* poor visibility into final request state.

These are hypotheses until supported by discovery evidence.

---

## **2.2 Current-State Process**

Discovery SHALL reconstruct how PTO work actually occurs rather than relying solely on documented procedures.

Representative flow:

Employee needs time off  
        ↓  
Finds policy / asks HR  
        ↓  
HR determines employee context  
        ↓  
HR interprets policy  
        ↓  
Balance checked  
        ↓  
Eligibility determined  
        ↓  
Employee submits request  
        ↓  
Manager approval if required  
        ↓  
HRIS updated  
        ↓  
Employee determines outcome

Discovery must distinguish:

* human processing time;  
* waiting time;  
* system processing time;  
* exception handling;  
* rework.

---

## **2.3 Root Causes**

Candidate root causes include:

* fragmented policy knowledge;  
* policy applicability depends on employee-specific facts;  
* information is distributed across systems;  
* employees cannot distinguish routine from exceptional cases;  
* approval authority is not always obvious;  
* workflows span long periods and multiple actors;  
* consequential actions may have uncertain outcomes;  
* repetitive deterministic decisions are handled manually;  
* insufficient workflow evidence exists for improvement.

---

## **2.4 Baseline**

Before production targets are approved, establish:

* workflow volume;  
* routine vs exceptional request rate;  
* HR intervention rate;  
* HR handling time;  
* manager handling time;  
* elapsed resolution time;  
* approval waiting time;  
* rework rate;  
* policy-error rate;  
* escalation rate;  
* abandonment rate;  
* employee satisfaction;  
* cost per completed workflow.

Targets SHALL NOT be invented without business evidence.

---

# **3\. Business Outcomes**

Each business outcome serves the outcome statement recorded in Section 0 and SHALL pass the same test: with technology removed, it remains a coherent goal that could be pursued by multiple different means.

## **BO-001 — Routine Self-Service**

Employees can resolve supported routine PTO workflows without unnecessary HR intervention.

## **BO-002 — Faster Resolution**

Supported routine workflows complete materially faster than the current process.

## **BO-003 — Policy Correctness**

Consequential decisions use only approved and applicable policy.

## **BO-004 — Preserved Organizational Authority**

Automation does not bypass required employee, manager, HR, security, legal, or organizational authority.

## **BO-005 — Verified Outcomes**

Employees receive successful completion only when authoritative enterprise state confirms the intended result.

## **BO-006 — Economic Improvement**

The cost of resolving supported routine PTO workflows improves without unacceptable degradation of correctness, safety, privacy, or employee experience.

---

# **4\. Success Measures**

## **4.1 Primary Business Measures**

### **SM-001 — HR Intervention Rate**

Percentage of supported routine workflows requiring HR intervention.

### **SM-002 — Verified Self-Service Completion Rate**

Percentage of supported routine workflows reaching verified completion without HR intervention.

### **SM-003 — Resolution Time**

Elapsed time from request initiation to verified final disposition.

### **SM-004 — Cost per Verified Resolution**

Total attributable workflow cost divided by verified completed workflows.

---

## **4.2 Guardrail Measures**

Candidate guardrails include:

* SM-G01 unauthorized consequential action rate;  
* SM-G02 incorrect policy application rate;  
* SM-G03 incorrect automation rate;  
* SM-G04 verification failure rate;  
* SM-G05 duplicate action rate;  
* SM-G06 inappropriate automated denial rate;  
* SM-G07 privacy/security violation rate;  
* SM-G08 successful appeal/reversal rate.

Guardrail targets require appropriate business and risk-owner approval.

---

## **4.3 AI Behavioral Measures**

AI measures are leading indicators, not substitutes for business outcomes.

Examples include:

* intent interpretation;  
* structured extraction;  
* ambiguity recognition;  
* policy applicability;  
* routine/exception classification;  
* human-escalation recognition;  
* groundedness;  
* appropriate tool selection;  
* adversarial robustness.

---

## **4.4 Measurement Definition**

Every production measure SHALL identify:

* ID;  
* definition;  
* formula;  
* population;  
* exclusions;  
* baseline;  
* target;  
* measurement window;  
* authoritative source;  
* owner;  
* associated guardrail.

---

# **5\. Scope and Autonomy Boundary**

Scope must be explicit enough to determine which policies, rules, eval cases, integrations, and authority paths are required.

## **5.1 Supported Leave Types**

TBD by business owner.

Example candidate initial scope:

* vacation / standard PTO.

Explicitly determine whether the following are supported:

* sick leave;  
* bereavement;  
* parental leave;  
* jury duty;  
* FMLA or equivalent protected leave;  
* unpaid leave;  
* floating holidays;  
* other statutory or company-specific leave.

---

## **5.2 Supported Jurisdictions**

TBD.

The ADS SHALL identify:

* supported countries;  
* supported states/provinces;  
* local jurisdictions where relevant;  
* jurisdiction-selection rules.

Unsupported jurisdictions SHALL fail safely rather than receiving a guessed policy.

---

## **5.3 Supported Employee Populations**

TBD.

Examples requiring explicit decisions:

* full-time;  
* part-time;  
* temporary;  
* contractors;  
* union-represented populations;  
* subsidiaries;  
* acquired organizations.

---

## **5.4 Supported Actions**

Each action SHALL have its own authority and risk classification.

| Action | Initial Status |
| ----- | ----- |
| Policy question | TBD |
| Balance inquiry | TBD |
| Create PTO request | TBD |
| Request status | TBD |
| Modify request | TBD |
| Cancel request | TBD |
| Manager approval | TBD |
| Automated denial | TBD |
| Policy exception | Human authority unless explicitly approved otherwise |

---

## **5.5 Workflow Scope**

Explicitly determine support for:

* future requests;  
* retroactive requests;  
* full-day requests;  
* partial-day requests;  
* multi-day requests;  
* overlapping requests;  
* request modification;  
* cancellation;  
* delegated approval.

---

## **5.6 Initial Automation Boundary**

A workflow being “in scope” does not imply autonomous execution.

Every supported scenario SHALL be classified as one of:

INFORMATION\_ONLY  
RECOMMENDATION  
HUMAN\_APPROVAL\_REQUIRED  
LIMITED\_AUTOMATION  
AUTOMATED  
NOT\_SUPPORTED  
---

# **6\. Stakeholders and Actors**

Stakeholders include as applicable:

* Employee  
* Manager  
* HR Specialist  
* HR Policy Owner  
* HR Operations  
* Payroll  
* Legal  
* Privacy  
* Security / Identity  
* Application Operations  
* AI / Architecture Team  
* Business Owner

Each consequential decision SHALL have an accountable authority.

---

# **7\. Business Process and Decision Model**

## **7.1 Process Boundary**

**Start:** Employee expresses a supported PTO need.

**End:** Workflow reaches a known disposition and, where consequential execution occurs, authoritative enterprise state has been verified.

---

## **7.2 Target Process**

Employee Intent  
      ↓  
Interpret Request  
      ↓  
Establish Trusted Identity  
      ↓  
Obtain Required Facts  
      ↓  
Determine Applicable Policy  
      ↓  
Evaluate Eligibility  
      ↓  
Classify Routine / Exception  
      ↓  
Determine Required Authority  
      ↓  
Human Review if Required  
      ↓  
Revalidate Mutable Preconditions  
      ↓  
Authorize  
      ↓  
Execute Through Bounded Capability  
      ↓  
Verify Authoritative State  
      ↓  
Record Evidence  
      ↓  
Communicate Disposition  
---

## **7.3 Decision Inventory**

| ID | Decision | Authority / Source |
| ----- | ----- | ----- |
| D-001 | Who is the employee? | Trusted identity / HR system |
| D-002 | What is being requested? | Employee intent \+ bounded interpretation |
| D-003 | Which policy applies? | Governed policy \+ trusted facts |
| D-004 | Is employee eligible? | Policy/rules |
| D-005 | Is sufficient balance available? | HRIS \+ rules |
| D-006 | Is approval required? | Policy/rules |
| D-007 | Routine or exception? | Rules \+ bounded reasoning |
| D-008 | Who may approve? | Enterprise authority model |
| D-009 | May execution occur now? | Deterministic control |
| D-010 | Did execution succeed? | Authoritative state |
| D-011 | May a denial be automated? | Business/HR/legal authority |

---

# **8\. Authority, Truth, and Temporal Validity**

## **8.1 Core Distinction**

SOURCE OF TRUTH  
What should the system believe?

AUTHORITY  
Who or what is allowed to decide?

TEMPORAL VALIDITY  
Is that fact or authority still valid now?  
---

## **8.2 Authority Matrix**

The architecture SHALL distinguish:

* interpretation authority;  
* business-rule authority;  
* approval authority;  
* exception authority;  
* execution authority;  
* system-of-record authority.

The model SHALL NOT establish:

* employee identity;  
* enterprise roles;  
* organizational authority;  
* human approval;  
* final system-of-record state.

---

## **8.3 Source-of-Truth Matrix**

| Information | Authoritative Source | Model May Establish? |
| ----- | ----- | ----- |
| Employee identity | Enterprise identity | No |
| Employee attributes | HRIS | No |
| PTO balance | HRIS | No |
| Manager | HRIS/directory | No |
| Approved policy | Governed policy repository | No |
| Approval | Approved workflow | No |
| PTO final state | HRIS | No |
| Agent workflow state | Durable workflow store | No |

---

## **8.4 Claims, Facts, Decisions, Evidence**

CLAIM  
Something asserted.

FACT  
Something established from an authoritative source.

DECISION  
A conclusion produced by an authorized mechanism/person.

EVIDENCE  
Information retained to demonstrate a fact,  
decision, authorization, action, or outcome.  
---

## **8.5 Temporal Correctness**

Mutable information may become:

* FRESH;  
* STALE;  
* SUPERSEDED;  
* UNSETTLED;  
* EXPIRED.

Consequential execution SHALL use information sufficiently current for its point of use.

---

## **8.6 Revalidation Boundaries**

Revalidation may be required:

* after material delays;  
* after approval waits;  
* before consequential execution;  
* after relevant state-change events;  
* after uncertain execution;  
* before relying on time-sensitive authority.

Exact freshness policies SHALL be business-defined.

---

# **9\. Business Requirements**

* **BR-001** Natural-language request.  
* **BR-002** Trusted employee context.  
* **BR-003** Applicable approved policy.  
* **BR-004** Eligibility evaluation.  
* **BR-005** Routine workflow automation.  
* **BR-006** Required organizational approval.  
* **BR-007** Human escalation.  
* **BR-008** Verified outcome.  
* **BR-009** Decision/action reconstructability.  
* **BR-010** Workflow economic measurement.  
* **BR-011** Temporal validity of consequential information.  
* **BR-012** Employee-data privacy.  
* **BR-013** Controlled denial and reconsideration handling.  
* **BR-014** Measurable incorrect-automation detection.

---

# **10\. Business Acceptance Criteria**

Business acceptance criteria SHALL describe observable behavior without prescribing implementation.

Example:

### **BAC-008-01 — Verified Completion**

Given an authorized PTO action is executed, the employee shall not receive a successful final disposition until authoritative business state confirms the intended result.

### **BAC-007-01 — Ambiguous Policy**

If applicable policy cannot be established under approved rules, the workflow shall not autonomously execute the consequential action.

### **BAC-013-01 — Denial**

A technical failure, insufficient information, unresolved policy ambiguity, or unavailable dependency SHALL NOT be represented as a business denial.

---

# **11\. Architectural Responsibilities**

Responsibilities include:

### **Interpretation**

AR-INT — interpret intent, extract information, identify ambiguity, obtain clarification.

### **Identity**

AR-ID — establish authenticated identity and trusted employee context.

### **Policy**

AR-POL — discover approved policy, establish applicability, preserve policy evidence.

### **Decision**

AR-DEC — obtain facts, apply settled rules, identify judgment conditions, classify routine/exception.

### **Workflow**

AR-WF — preserve durable state, transitions, waits, retries, recovery.

### **Authority**

AR-AUTH — establish required authority and prevent manufactured authority.

### **Human Review**

AR-HUM — route review, establish reviewer authority, provide evidence, capture decision, resume workflow.

### **Execution**

AR-EXEC — perform authorized actions and prevent duplicate effects.

### **Verification**

AR-VER — establish authoritative resulting state.

### **Evidence**

AR-AUD — preserve business-relevant decision/action evidence.

### **Privacy**

AR-PRIV — minimize disclosure, enforce retention, control access, preserve privacy boundaries.

### **Evaluation**

AR-EVAL — measure probabilistic behavior, incorrect automation, regressions, and autonomy readiness.

### **Cost**

AR-COST — measure and bound resource consumption.

---

# **12\. Architectural Concerns**

Major concerns include:

* hallucination;  
* ambiguity;  
* incorrect policy;  
* stale facts;  
* stale authority;  
* prompt injection;  
* retrieved-content injection;  
* impersonation;  
* privilege escalation;  
* forged approval;  
* inappropriate automation;  
* inappropriate denial;  
* excessive escalation;  
* lost workflow state;  
* duplicate execution;  
* uncertain execution;  
* false success;  
* privacy leakage;  
* excessive data sent to model provider;  
* excessive retention;  
* runaway cost;  
* insufficient evidence.

---

# **13\. Constraints, Assumptions, and Preferences**

## **Constraints**

Candidate constraints:

* enterprise identity remains authoritative;  
* HRIS remains authoritative for PTO state;  
* approved policy sources govern consequential policy decisions;  
* models cannot manufacture authority;  
* mandatory human approval cannot be bypassed;  
* consequential execution cannot rely solely on unverified model output;  
* privacy restrictions apply across model, logging, evaluation, and evidence systems;  
* deterministic economic limits cannot be overridden by models.

## **Assumptions**

Assumptions SHALL be explicitly validated.

## **Preferences**

Technology preferences SHALL remain negotiable unless promoted to constraints with justification.

---

# **14\. Threat and Failure Model**

## **14.1 Threat Categories**

* identity manipulation;  
* privilege escalation;  
* prompt injection;  
* indirect injection;  
* knowledge poisoning;  
* tool manipulation;  
* approval forgery;  
* replay;  
* cross-employee disclosure;  
* sensitive-data disclosure;  
* excessive agency;  
* resource exhaustion.

## **14.2 Failure Categories**

* INPUT;  
* MODEL;  
* KNOWLEDGE;  
* DATA;  
* AUTHORITY;  
* WORKFLOW;  
* DEPENDENCY;  
* EXECUTION;  
* VERIFICATION;  
* PRIVACY;  
* ECONOMIC.

---

## **14.3 Failure Propagation**

Every critical failure scenario SHALL identify:

CAUSE  
  ↓  
LOCAL FAILURE  
  ↓  
BUSINESS CONSEQUENCE  
  ↓  
SAFE RESPONSE  
  ↓  
RECOVERY  
  ↓  
EVIDENCE

Example:

Policy Repository Unavailable  
        ↓  
Applicable Policy Cannot Be Established  
        ↓  
Consequential Decision Cannot Be Trusted  
        ↓  
Automation Stops  
        ↓  
Retry / Human Path

The system SHALL NOT silently substitute model general knowledge for unavailable authoritative policy.

---

# **15\. Quality Attributes**

Priority attributes include:

* correctness;  
* security;  
* privacy;  
* reliability;  
* resilience;  
* recoverability;  
* auditability;  
* traceability;  
* explainability;  
* observability;  
* performance;  
* cost efficiency;  
* maintainability;  
* testability;  
* evaluability;  
* controllability.

Important attributes SHALL have measurable Quality Attribute Scenarios.

---

# **16\. Architecture Drivers**

## **AD-001 Reasoning / Authority Separation**

Probabilistic reasoning must not directly exercise consequential authority.

## **AD-002 Trusted Identity Context**

Consequential identity and authorization facts originate from trusted sources.

## **AD-003 Bounded Policy Applicability**

Only approved and applicable policy may govern consequential automation.

## **AD-004 Durable Workflow**

Long-running workflows preserve state across waits, failures, and restarts.

## **AD-005 Verified Consequential Actions**

Consequential actions are retry-safe and verified against authoritative state.

## **AD-006 Human Authority Preservation**

Judgment, exception, and mandated approval remain with authorized humans.

## **AD-007 Reconstructable Decisions**

Consequential decisions remain reconstructable across changing models, prompts, policies, rules, and software.

## **AD-008 Bounded Agent Economics**

Agent resource consumption is observable, attributable, and bounded.

## **AD-009 Temporal Validity**

Mutable consequential information is sufficiently current at use.

## **AD-010 Evaluation-Gated Autonomy**

Autonomy expands only when evaluation and production evidence supports it.

## **AD-011 Data Minimization and Privacy Boundary**

AI components receive only data required for their approved reasoning purpose.

---

# **17\. Architecture Patterns**

Selected candidate patterns:

* **PAT-001** Reasoning / Authority Separation  
* **PAT-002** Bounded Capability  
* **PAT-003** Idempotent Verified Action  
* **PAT-004** Durable Agent Workflow  
* **PAT-005** Bounded Policy Applicability  
* **PAT-006** Human Authority  
* **PAT-007** Evidence Ledger  
* **PAT-008** Workflow Cost Ledger  
* **PAT-009** Safe Degradation  
* **PAT-010** Evaluation-Gated Autonomy  
* **PAT-011** Minimum Necessary Model Context

Patterns SHALL document drivers, responsibilities, tradeoffs, risks introduced, and validation mechanism.

---

# **18\. Human Authority and Review Model**

Human review is a business workflow, not an error fallback.

## **18.1 Review Triggers**

Candidate triggers include:

* policy ambiguity;  
* conflicting policies;  
* exception request;  
* insufficient deterministic evidence;  
* authority uncertainty;  
* automated denial not permitted;  
* high-consequence case;  
* failed verification requiring reconciliation;  
* employee appeal.

---

## **18.2 Review Queues**

The architecture SHALL identify:

* queue type;  
* eligible reviewers;  
* required authority;  
* prioritization;  
* ownership;  
* escalation path.

Example conceptual queues:

MANAGER\_APPROVAL  
HR\_POLICY\_REVIEW  
HR\_EXCEPTION\_REVIEW  
EXECUTION\_RECONCILIATION  
PRIVACY\_SECURITY\_REVIEW  
APPEAL\_REVIEW  
---

## **18.3 Human Decision Package**

A reviewer should receive sufficient information to make the decision without reconstructing the entire workflow manually.

Candidate package:

* request;  
* authenticated employee context;  
* relevant authoritative facts;  
* applicable policy/evidence;  
* reason for review;  
* previous decisions;  
* model recommendation where appropriate;  
* uncertainty or conflict;  
* requested decision.

Model-generated recommendations SHALL be distinguishable from authoritative facts.

---

## **18.4 Response-Time Commitment**

Each review class SHALL define:

* expected response time;  
* escalation threshold;  
* timeout behavior;  
* employee communication behavior.

The agent SHALL NOT invent approval because a reviewer fails to respond.

---

## **18.5 Denials**

The architecture SHALL distinguish:

TECHNICAL FAILURE  
INSUFFICIENT INFORMATION  
POLICY AMBIGUITY  
NOT ELIGIBLE  
AUTHORIZED BUSINESS DENIAL

Only the last categories explicitly approved for automated determination may produce an automated business denial.

---

## **18.6 Appeals / Reconsideration**

If business policy provides reconsideration or appeal:

* employee must be informed;  
* appeal must create a distinct workflow event;  
* reviewer authority must be established;  
* original decision evidence must be preserved;  
* appeal outcome must not silently overwrite historical evidence.

---

# **19\. Data and Privacy Architecture**

## **19.1 Data Minimization Principle**

> The model receives the minimum information necessary for the approved reasoning task, not all information available to the application.

---

## **19.2 Data Classification**

Relevant data SHALL be classified, including:

* identity data;  
* employment data;  
* organizational data;  
* leave information;  
* policy data;  
* conversation content;  
* model inputs/outputs;  
* approval evidence;  
* execution evidence;  
* audit data;  
* evaluation datasets.

---

## **19.3 Model Provider Boundary**

For every model interaction, the architecture SHALL document:

* purpose;  
* data fields transmitted;  
* why each field is necessary;  
* prohibited fields;  
* retention behavior;  
* logging behavior;  
* applicable enterprise/provider controls.

Example:

| Reasoning Task | Necessary Context | Normally Unnecessary |
| ----- | ----- | ----- |
| Intent interpretation | Employee utterance | Employee ID, salary, full HR record |
| Policy interpretation | Policy text \+ relevant attributes | Name, email, address |
| Explanation | Decision result \+ approved evidence | Unrelated employee data |

---

## **19.4 Retention Matrix**

Every retained dataset SHALL specify:

| Data | Purpose | System | Retention | Model Provider? | Access | Deletion |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Request text | TBD | TBD | TBD | TBD | TBD | TBD |
| Workflow state | TBD | TBD | TBD | No/limited | TBD | TBD |
| Model output | TBD | TBD | TBD | Generated | TBD | TBD |
| Approval evidence | TBD | TBD | TBD | Normally unnecessary | TBD | TBD |
| Execution evidence | TBD | TBD | TBD | Normally unnecessary | TBD | TBD |
| Eval cases | TBD | TBD | TBD | Depends | TBD | TBD |

Retention values require privacy/legal/security approval.

---

## **19.5 Logging Privacy**

Application, model, security, evaluation, and observability logs SHALL follow the same data-minimization principles as production application flows.

Sensitive data SHALL NOT become acceptable merely because it appears in telemetry.

---

# **20\. Logical Architecture**

┌──────────────────────────────────────────────┐  
│                  EXPERIENCE                  │  
├──────────────────────────────────────────────┤  
│                   WORKFLOW                   │  
├──────────────┬──────────────┬────────────────┤  
│  REASONING   │  KNOWLEDGE   │    CONTROL     │  
├──────────────┴──────────────┴────────────────┤  
│                 CAPABILITY                   │  
├──────────────────────────────────────────────┤  
│              SYSTEM OF RECORD                │  
├──────────────────────────────────────────────┤  
│                VERIFICATION                  │  
└──────────────────────────────────────────────┘

Cross-cutting:

IDENTITY / SECURITY  
HUMAN AUTHORITY  
PRIVACY  
AUDIT / EVIDENCE  
OBSERVABILITY  
COST  
EVALUATION  
---

## **20.1 Reasoning Layer Boundary**

Reasoning may:

* interpret;  
* extract;  
* classify;  
* identify ambiguity;  
* interpret policy prose;  
* recommend;  
* explain.

Reasoning may not:

* establish identity;  
* establish authoritative employee facts;  
* create approval;  
* override controls;  
* directly mutate systems of record;  
* claim unverified execution success.

---

## **20.2 Control Layer Boundary**

Control owns deterministic enforcement including:

* authorization;  
* settled rules;  
* approval validation;  
* schema validation;  
* execution preconditions;  
* autonomy eligibility;  
* cost limits;  
* required revalidation.

---

## **20.3 Capability Boundary**

Capabilities SHALL be:

* narrow;  
* typed;  
* authorized;  
* auditable;  
* bounded;  
* retry-aware;  
* unavailable directly to untrusted callers.

---

## **20.4 Verification Boundary**

Execution success does not establish business success.

INTENDED ACTION  
      ↓  
EXECUTION  
      ↓  
AUTHORITATIVE READ-BACK  
      ↓  
COMPARE INTENDED vs ACTUAL  
      ↓  
VERIFIED / VERIFICATION\_FAILED  
---

# **21\. Architecture Views**

Required views include:

* System Context;  
* Logical Architecture;  
* Trust Boundary;  
* Authority Boundary;  
* Data Flow / Privacy;  
* Routine Workflow Sequence;  
* Human Review Sequence;  
* Denial / Appeal Sequence;  
* Uncertain Execution Sequence;  
* Workflow State Model;  
* Failure / Degradation View.

---

# **22\. Evaluation and Autonomy Plan**

Evaluation begins during architecture definition, not after implementation.

## **22.1 Evaluation Intent**

Eval requirements derive from:

Business Outcome  
       ↓  
Business Requirement  
       ↓  
Probabilistic Responsibility  
       ↓  
Threat / Failure Scenario  
       ↓  
Required Behavior  
       ↓  
Eval Scenario  
---

## **22.2 Incorrect Automation Taxonomy**

Incorrect automation includes:

* wrong intent;  
* wrong extracted facts;  
* wrong policy;  
* wrong eligibility;  
* exception classified as routine;  
* required human review bypassed;  
* wrong approver;  
* unauthorized action;  
* stale information used;  
* inappropriate denial;  
* duplicate action;  
* incorrect execution;  
* false successful outcome.

---

## **22.3 Detection**

### **Offline**

* business-authored cases;  
* historical cases;  
* synthetic cases;  
* edge cases;  
* adversarial cases;  
* regression cases.

### **Pre-Production**

* shadow execution;  
* expert comparison;  
* deterministic comparison;  
* failure injection;  
* security/adversarial evaluation.

### **Production**

* authoritative verification;  
* sampled human review;  
* human overrides;  
* reversals;  
* appeals;  
* escalation analysis;  
* anomaly detection;  
* employee/HR reports;  
* production-derived regression cases.

---

## **22.4 Evaluation Dataset Governance**

Datasets SHALL define:

* source;  
* owner;  
* expected result/rubric;  
* PII classification;  
* permitted use;  
* version;  
* coverage;  
* provenance;  
* regression status.

Production-derived cases SHALL be appropriately de-identified or governed according to approved privacy requirements.

---

## **22.5 Tests vs Evals**

DETERMINISTIC CONTRACT  
        ↓  
TEST

PROBABILISTIC / SEMANTIC BEHAVIOR  
        ↓  
EVAL

Examples of tests:

* authorization;  
* business rules;  
* state transitions;  
* idempotency;  
* schema contracts;  
* database constraints;  
* economic limits.

Examples of evals:

* interpretation;  
* ambiguity recognition;  
* policy reasoning;  
* routine/exception classification;  
* escalation behavior;  
* groundedness;  
* adversarial model behavior.

---

## **22.6 Autonomy Gates**

SHADOW  
   ↓ Gate A  
RECOMMENDATION  
   ↓ Gate B  
LIMITED AUTOMATION  
   ↓ Gate C  
EXPANDED AUTOMATION

Each gate SHALL specify:

| Gate | Required Evidence | Threshold | Approver |
| ----- | ----- | ----- | ----- |
| A | Offline behavioral/security evals | TBD | TBD |
| B | Shadow \+ human comparison \+ architecture acceptance | TBD | TBD |
| C | Production KPIs \+ guardrails \+ regression evidence | TBD | TBD |

Some guardrails may require zero tolerance, including unauthorized consequential action.

---

## **22.7 Autonomy Regression**

Autonomy SHALL be reversible.

Material degradation may trigger:

EXPANDED\_AUTOMATION  
        ↓  
LIMITED\_AUTOMATION  
        ↓  
RECOMMENDATION\_ONLY  
        ↓  
HUMAN\_ONLY

Degradation must not require a model to voluntarily reduce its own authority.

---

# **23\. Architecture Acceptance**

Architecture acceptance proves that implementation conforms to architectural intent.

## **AAC-001 Reasoning / Authority Separation**

Reasoning cannot directly invoke consequential system-of-record mutations.

## **AAC-002 Trusted Identity**

Consequential identity and authority cannot originate from user/model-controlled fields.

## **AAC-003 Bounded Policy**

Only approved and applicable policy governs consequential automated decisions.

## **AAC-004 Durable Workflow**

Waiting workflows survive restart without lost state, repeated action, or bypassed authority.

## **AAC-005 Verified Action**

Unknown execution outcome is reconciled before consequential retry.

## **AAC-006 Human Authority**

Required human judgment cannot be bypassed.

## **AAC-007 Evidence**

Consequential workflow decisions/actions can be reconstructed.

## **AAC-008 Economic Guardrails**

Model behavior cannot override deterministic cost/resource limits.

## **AAC-009 Temporal Correctness**

Required mutable information is revalidated at defined boundaries.

## **AAC-010 Safe Degradation**

Loss of required knowledge, authority, or trusted state reduces autonomy.

## **AAC-011 Privacy Boundary**

Model and telemetry flows expose only approved data required for their purpose.

## **AAC-012 Evaluation Gate**

Autonomy mode cannot exceed the level approved by current evaluation and production evidence.

Architecture acceptance evidence may include:

* static dependency checks;  
* unit/integration tests;  
* security tests;  
* architecture tests;  
* failure injection;  
* recovery tests;  
* adversarial evals;  
* behavioral evals;  
* privacy inspection;  
* load/cost tests.

---

# **24\. Architecture Decisions / ADR Register**

Candidate ADRs:

| ADR | Decision |
| ----- | ----- |
| ADR-0001 | Reasoning does not exercise business authority |
| ADR-0002 | Durable workflow state |
| ADR-0003 | Deterministic business controls |
| ADR-0004 | Bounded enterprise capabilities |
| ADR-0005 | Database migration governance |
| ADR-0006 | Governed policy retrieval |
| ADR-0007 | Policy applicability approach |
| ADR-0008 | Idempotent verified side effects |
| ADR-0009 | Trusted identity and authorization context |
| ADR-0010 | Workflow cost accounting |
| ADR-0011 | Temporal revalidation |
| ADR-0012 | Safe degradation |
| ADR-0013 | Evaluation-gated autonomy |
| ADR-0014 | Model data/privacy boundary |

ADRs record consequential architecture choices and alternatives.

---

# **25\. Architecture Traceability Matrix**

The ADS SHALL maintain an actual traceability matrix rather than only describing traceability.

Illustrative partial matrix:

| Outcome | Measure | Requirement | Responsibility | Concern / Failure | Driver | Pattern | Acceptance |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| BO-001 | SM-001/002 | BR-005 | AR-DEC | Incorrect routine classification | AD-010 | PAT-010 | AAC-012 |
| BO-003 | SM-G02 | BR-003/004 | AR-POL | Wrong applicable policy | AD-003 | PAT-005 | AAC-003 |
| BO-004 | SM-G01 | BR-006/007 | AR-AUTH | Authority bypass | AD-001/006 | PAT-001/006 | AAC-001/006 |
| BO-005 | SM-G04 | BR-008 | AR-VER | Unknown execution outcome | AD-005 | PAT-003 | AAC-005 |
| BO-006 | SM-004 | BR-010 | AR-COST | Runaway consumption | AD-008 | PAT-008 | AAC-008 |
| BO-003/004 | SM-G02/G01 | BR-011 | AR-AUTH/DEC | Stale fact/authority | AD-009 | PAT-009 | AAC-009 |
| BO-004 | SM-G07 | BR-012 | AR-PRIV | Excessive model disclosure | AD-011 | PAT-011 | AAC-011 |

The full implementation trace continues:

Outcome Statement  
 ↓  
Outcome  
 ↓  
Measure  
 ↓  
Requirement  
 ↓  
Responsibility  
 ↓  
Threat / Failure  
 ↓  
Driver  
 ↓  
Pattern  
 ↓  
Architecture Acceptance  
 ↓  
ADR  
 ↓  
TSD Component  
 ↓  
Code  
 ↓  
Test / Eval  
 ↓  
Production Signal

Detailed machine-readable traceability SHOULD be maintained separately.

---

# **26\. Decision Log**

Not every project decision requires an ADR.

The decision log captures important business/design decisions.

| ID | Decision | Owner | Date | Basis | Related IDs |
| ----- | ----- | ----- | ----- | ----- | ----- |
| DEC-001 | HRIS is authoritative for final PTO state | TBD | TBD | TBD | BR-008 |
| DEC-002 | Model cannot establish employee identity | TBD | TBD | TBD | AD-002 |
| DEC-003 | Unknown execution requires reconciliation before retry | TBD | TBD | TBD | AD-005 |

---

# **27\. Rejected Alternatives**

Rejected alternatives SHALL remain visible so future teams do not repeatedly reopen resolved questions without new evidence.

| ID | Alternative | Reason Rejected | Related Decision |
| ----- | ----- | ----- | ----- |
| ALT-001 | Model directly calls unrestricted HRIS API | Violates authority/capability boundary | ADR-0001/0004 |
| ALT-002 | Semantic similarity alone determines policy applicability | Relevance does not establish authority/applicability | ADR-0007 |
| ALT-003 | Successful API response establishes verified completion | Transport success does not establish authoritative business state | ADR-0008 |

---

# **28\. Open Questions and Risks**

Unresolved questions SHALL not silently become implementation assumptions.

| ID | Question | Impact | Owner | Required By |
| ----- | ----- | ----- | ----- | ----- |
| OQ-001 | Which leave types are Phase 1? | Scope/policy/evals | Business | Scope approval |
| OQ-002 | Which jurisdictions are supported? | Policy/legal/evals | Business/Legal | Scope approval |
| OQ-003 | Are modification/cancellation supported? | Workflow/integration | Business | Requirements freeze |
| OQ-004 | Which denials may be automated? | Authority/legal | HR/Legal | Workflow approval |
| OQ-005 | What appeal path applies? | Human review | HR/Legal | Pilot |
| OQ-006 | What are review response-time commitments? | UX/workflow/SLO | HR | Pilot |
| OQ-007 | What employee data may reach the model provider? | Privacy/security | Privacy/Security | Implementation |
| OQ-008 | What are retention periods? | Privacy/audit | Legal/Privacy | Implementation |
| OQ-009 | What autonomy thresholds apply? | Rollout/risk | Business/Risk | Pilot |
| OQ-010 | What conditions force autonomy rollback? | Production safety | Business/Risk | Launch |

---

# **29\. Architecture Governance**

The ADS is an architecture-authority artifact.

Material changes to:

* business outcome statement;  
* business scope;  
* automation boundary;  
* authority;  
* source of truth;  
* privacy boundary;  
* architecture drivers;  
* logical-layer responsibilities;  
* dependency rules;  
* patterns;  
* architecture acceptance;  
* autonomy gates;

require appropriate review.

Implementation must not silently redefine architecture.

Implementation discovers design gap  
        ↓  
STOP / ESCALATE  
        ↓  
Determine whether gap is:  
 requirement  
 business decision  
 architecture decision  
 implementation detail  
        ↓  
Update appropriate artifact  
        ↓  
Resume implementation  
---

# **30\. Production Evidence and Learning**

Production completes the architecture feedback loop.

DISCOVERY  
    ↓  
OUTCOME  
    ↓  
ARCHITECTURE  
    ↓  
IMPLEMENTATION  
    ↓  
EVALUATION  
    ↓  
PRODUCTION  
    ↓  
RUNTIME EVIDENCE  
    ↓  
BUSINESS KPI  
    ↓  
FIELD LEARNING  
    └──────────────→ DISCOVERY / ARCHITECTURE

Production evidence should answer:

* Is HR intervention decreasing?  
* Is resolution time improving?  
* Is policy application correct?  
* Are exceptions correctly escalated?  
* Are automated denials appropriate?  
* Are appeals revealing systematic errors?  
* Are unauthorized actions occurring?  
* Are final outcomes verified?  
* Is employee data handled as approved?  
* What does each verified workflow cost?  
* Which failure modes recur?  
* Which production failures were absent from evals?

Meaningful production failures SHOULD become regression cases.

Architecture-significant failures SHOULD trigger architecture review rather than prompt-only remediation.

---

# **31\. Definition of Architecture Success**

CODE COMPLETE  
      ≠  
FEATURE ACCEPTED  
      ≠  
EVAL PASSED  
      ≠  
ARCHITECTURE ACCEPTED  
      ≠  
PRODUCTION READY  
      ≠  
BUSINESS SUCCESS

The solution succeeds only when:

1. the business outcome statement has passed the outcome test;  
2. supported scope is explicit;  
3. business acceptance criteria pass;  
4. architecture acceptance criteria pass;  
5. deterministic tests pass;  
6. AI and adversarial evals meet approved thresholds;  
7. privacy requirements are satisfied;  
8. human-review workflows are operational;  
9. production readiness criteria are satisfied;  
10. autonomy level is supported by current evidence;  
11. runtime evidence demonstrates safe operation;  
12. agreed business success measures demonstrate the intended outcome.

The final question is:

> **Did the system produce the intended business outcome for the approved scope while preserving truth, authority, privacy, correctness, safety, economics, and human accountability?**

