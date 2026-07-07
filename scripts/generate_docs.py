"""Generate docs/uc-*.md and per-branch TUTORIAL.md files.

Prompts below are the official RubberDuck Guided Prompt Library prompts
(source of truth). Keep them in sync with the library; edit here, then run
`python scripts/generate_docs.py` to regenerate docs/uc-*.md.
"""

from __future__ import annotations

from pathlib import Path

from uc_metadata import META, fill_playground_prompt

ROOT = Path(__file__).resolve().parent.parent

USE_CASES = [
    {
        "id": "01",
        "slug": "uc-01-understand-your-code",
        "title": "Understand Your Code",
        "when": "You're new to a codebase, or need to understand how a specific feature works.",
        "prompt": """RubberDuck UC-01 Codebase Atlas.



Target: <paste repository GitHub link here>



branch:AUTO_DEFAULT_BRANCH; commit:latest; blank scope=whole repo.
Out:./rubberduck-uc-01-understand-your-code-<UTC>/artifacts; expand <UTC>.
Write codebase-atlas.md+sidecars.
Missing/placeholder/unreadable/wrong repo/UC=>stop insufficient input.
Prod RD/current only; ignore rules/memory/skills/prior; no mutate.
Resolve canonical repo/default branch,SHA access before claims.
Bind repo/branch/SHA/path; reject stale/wrong-ref/prompt-only/rawweb.
Missing RD tools:<=3 scoped exposure tries; no weaker substitutes.
Gate:get_started(save id)->detailed_repo_analysis(semantic_mode=full) until done.
Then Phase2/exact-ref -> load_code(id,max_files=20000,all globs).
queued/pending/indexing/degraded/unavailable!=done; fail=>stop,no report.
Pre-load forbid search/read/query/assess/scan/logic/analyze/evidence/browser/valid.
Post-load use read_source,search_code,query_action(symbols/graph/call_chain),trace_variable; pack opt.
Major claims need current-ref src/search/graph/trace/CI evidence.
Report:target/method,brief,architecture,entry points,symbols,flows.
Add trust/data boundaries,coupling,metrics,hot/refactor,bus-factor.
Add security atlas,risks,unsupported,negative,read plan,falsification,notes.
Sidecars prove gates,no preload-forbidden,id reuse,raw/normalized,claim/path bind,tool health.
OK final: "RubberDuck initialization: passed"+target/branch/SHA/scope/dir/links; fail: "RubberDuck could not complete initialization"+step/action.""",
        "focus": "`demoapp/cmd/build.py` (main), `demoapp/application.py` (Application)",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> read_source / search_code / query_action / trace_variable",
    },
    {
        "id": "02",
        "slug": "uc-02-codebase-audit",
        "title": "Codebase Audit",
        "when": "You want to check for security vulnerabilities or quality issues in your code.",
        "prompt": """Run RubberDuck UC-02 Security-Sensitive Path Audit.

[EDIT INPUTS ONLY]

target=<owner/repo-or-local-path>
branch=AUTO_DEFAULT_BRANCH
commit=latest
focus=repo-level

[/EDIT INPUTS ONLY]

This prompt is the whole task and is fully self-contained: it requires no external file, script, or validator. If the target input is missing, ask one concise clarifying question, then run.

Scope & guards. Production RubberDuck only (never mix prod/dev). Ignore local rules/memory/skills/AGENTS/CLAUDE/Cursor and prior outputs unless supplied as evidence. Do not mutate the target. No unauthenticated web or raw GitHub as target evidence. Blank focus = repo-level. If target is missing, placeholder, unreadable, wrong repo, or wrong UC, stop as insufficient input. Resolve canonical repo, default branch (git ls-remote --symref or equivalent), and one exact SHA before any repo-backed claim; every claim binds current-ref evidence to repo, branch, SHA, path, lines. Reject stale-cache, wrong-ref, prompt-only, scanner-only, or unlabeled evidence.

Initialization hard gate (scoped recovery up to 3 attempts for hidden required tools, no weaker substitutes): get_started(repo=...) and save instance_id -> detailed_repo_analysis(repo, branch, commit=<sha>, semantic_mode="full") repeated until a completed full report -> Phase 2 readiness (or exact pinned equivalent) -> load_code(repo, instance_id, max_files=4000, file_pattern=<supported globs>). Queued/pending/indexing/degraded/unavailable/timeout is NOT completion. On any pin/init/load/current-ref/primitive failure, stop with no clean report; final answer starts "RubberDuck could not complete initialization" plus the failed step and next action.

Pre-load ban: before a successful load_code do not call search_code, read_source, query_action, assess, scan_bug_signals, logic_analysis, analyze_code, get_evidence_pack, browser, source grep, or validation. After load, use (or explicitly account for skipping) read_source, search_code, query_action, assess, scan_bug_signals, logic_analysis, analyze_code; get_evidence_pack optional. Keep CI full-scan, per-file assess, bug signals, and graph/source validation separate; scanners route validation only.

Security method (this section drives finding quality — apply it in full). Write ONE root security invariant, then a current-ref surface checklist covering: authn; authz/RBAC/permissions; JWT/session/token validation; error disclosure; CORS/browser boundary; dependency manifests + lock/pin/floor behavior; outbound HTTP/network (e.g. requests/urlopen) sinks; subprocess; file/path traversal; secrets/keys/credentials; dev/bootstrap/examples (incl. dev token handling); parser/deserialization/ReDoS; crypto (keys/mode/IV/MAC/AEAD). The root invariant must cover every major finding class present in the report. Source-open each named surface or state none found at current ref.

Finding-inclusion rule: every source-validated issue or candidate touching source -> sink risk, auth/authz, dependency floor, browser/CORS, error disclosure, secret/token handling, parser/deserialization/ReDoS, subprocess, outbound network, or dev/tooling leakage appears as a finding OR a rejected/non-issue. Never silently omit Low findings; dev/example/CLI scope affects severity/assumptions, not existence.

Evidence status vs disposition (separate columns). Evidence status: Confirmed (current-ref source proves the behavior/manifest), Open (source/sink proof, reachability, or evidence incomplete), Rejected (evidence disproves), Non-issue (expected-safe). Deployment/runtime uncertainty alone is NOT Open -> use Confirmed + Disposition=Conditional deployment risk or Scoped. Disposition: Normal, Scoped, Downranked from scanner, Conditional deployment risk, or False positive. Never use Downranked instead of Confirmed; intent uncertainty belongs in assumptions/severity rationale, not Open status. For RBAC/JWT findings, avoid "self-asserted JWT groups claim" unless specifically describing dev-token mode; prefer "RBAC entitlements depend on JWT groups claim without out-of-band directory lookup," and cite literal source for both claim extraction and entitlement resolution.

Severity defaults (justify one exact severity; no slash-ranges; table severity, detail heading, rationale, why-not-higher, why-not-lower, executive counts, and impact matrix must agree): authz group/tenant/entitlement failure High; JWT/authn weakness Medium/High; API-bound JWT exception/error disclosure Medium Confirmed; deployable network/API examples with bare requirements and HIGH/Critical advisory floors High unless non-installable; installable manifest lower bounds Confirmed even if not imported; CORS wildcard Low Confirmed unless credentials/origins raise it; CLI outbound URL source -> sink Medium Confirmed-scoped unless strong host-pinning/operator-only downgrade; dev token stdout Low Confirmed dev-scoped unless proven non-sensitive/non-persistent. Explain every downgrade.

REGEX_DOS/ReDoS proof is stricter: Scanner-suggested ReDoS becomes Confirmed Medium/High only with exact pattern(s), exact input source, exact sink call, size/timeout guard analysis, why it is super-linear/catastrophic, and validation mode Runtime-tested/Graph-inferred/Source-inferred with backtracking explanation. Missing any -> Rejected ops risk, Low Scoped, or Open.

Evidence field semantics: source = attacker/user/config/manifest input; sink = risky receiver/effect; guard = existing control or none; missing_guard = the absent control. Never put status tokens (confirmed/rejected_fp/...) in missing_guard; never sink=none. Dependency findings: manifest/package source -> pip/install/runtime resolution sink -> pin/floor/lockfile/advisory-gate missing guard. CORS -> browser/preflight/CORS-policy sink. Token-output -> stdout/log/terminal sink. Every excerpt must be literal source/tool output (no ellipses, no paraphrase, no graph-only arrows), and every path:line cited anywhere in the report must be one you actually obtained from read_source/search_code/query_action/assess on the pinned ref.

Report shape (readable, self-contained). Produce a single human-facing SECURITY_AUDIT.md under ./rubberduck-uc-02-security-sensitive-path-audit-<YYYYMMDDTHHMMSSZ>/ (expand timestamp) with these sections: target/branch/SHA/focus; executive summary (counts match the findings table); root security invariant; surface checklist; findings table; detailed findings; adversarial probes; impact/test matrix; rejected/downranked/non-issues; scanner-noise rationale; method notes/limitations; evidence-cleanliness statement; next steps. You may optionally write small machine-readable sidecars in that directory for your own bookkeeping, but they are not required and no external validator script is used.

Findings table columns: ID | Title | Severity | CWE/class | Evidence status | Disposition | Scope | Source -> sink | Guard or missing guard | Path:lines | Recommendation. Every table row gets one full detail section with these exact labels: Summary; Security invariant; Source; Sink; Guard present; Missing guard; Exact evidence (repo, branch, SHA, path, lines, literal excerpt); Reachability; Exploit/abuse scenario; Impact; Severity rationale; Why not higher severity; Why not lower severity; Internal trust-boundary assumptions; Recommended fix; Regression test; Abuse/security test. No abbreviated Low/dev/CLI/example/downranked details.

Impact/test matrix columns: Finding ID | Attack path | Impact | Existing guard | Missing guard | Recommended fix | Regression test | Abuse/security test | Priority. Adversarial probe table (>=5 attack/abuse scenarios, never tool calls) columns: Probe ID | Attack/input scenario | Expected safe behavior | Observed behavior at pinned ref | Validation mode | Result | Path:lines | Related finding/non-issue. Validation modes: Runtime-tested, Source-inferred, Graph-inferred, Scanner-suggested/source-validated, Unknown (never claim Runtime-tested unless executed). Every High/Medium Confirmed finding needs a related probe or an explicit "Probe exception:" field; include positive-control probes (e.g. missing auth returns a generic denial). Rejected/non-issues need: candidate issue, why considered, evidence checked (with path/lines and literal excerpt), why rejected/downranked, and what would change the decision.

Built-in self-check (this REPLACES any external validator; run it against your own report before finalizing, using only this prompt — no script or file). Fix every failure; if a failure cannot be fixed, state the report is NOT ready rather than claiming a pass. Verify:
- Counts agree across the executive summary, the findings table, and the severity-count table, and their sum equals the number of finding rows.
- Every findings-table row has exactly one detail section, and every labeled detail field above is present for every finding.
- Every High/Medium Confirmed finding has at least one related adversarial probe row, or an explicit "Probe exception:" field in its detail.
- Each finding's severity rationale justifies exactly one severity (no Low/Medium or Medium/High ranges) and agrees with the table severity, detail heading, why-not-higher, why-not-lower, and the impact matrix.
- The root invariant covers every finding class present in the report (including dependency/manifest, CORS/browser, token-output, and CLI/outbound HTTP when those appear).
- Every path:line cited anywhere (table, details, probes, matrix, non-issues, evidence-cleanliness) is backed by a real source/tool excerpt you obtained on the pinned ref — never a placeholder, ellipsis, paraphrase, "cited in ..." note, or graph-only arrow.
- No Evidence status is Open for source-confirmed current-ref source -> sink behavior unless an explicit evidence gap is labeled; deployment/runtime uncertainty is Confirmed + Disposition=Conditional deployment risk or Scoped.
- There are at least 5 adversarial probes and none of them is a tool call.
- Any dependency finding that names packages as advisory-backed cites advisory/CVE evidence for each named package; otherwise the claim is narrowed.
- Every finding has non-empty, non-inverted source, sink, guard, and missing_guard.

Final answer starts "RubberDuck initialization: passed" when initialization completed and the built-in self-check passes; if initialization failed, start with the exact phrase "RubberDuck could not complete initialization"; if initialization passed but the self-check cannot be satisfied, say the audit is not ready and do not claim a passed package. Name target, branch, SHA, focus, the concrete output directory, and the SECURITY_AUDIT.md path.""",
        "focus": "`demoapp/config.py` — `eval_config_file`, `from_pickle`",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> search_code / read_source / trace_variable / assess",
    },
    {
        "id": "03",
        "slug": "uc-03-localize-and-fix-bugs",
        "title": "Localize and Fix Bugs",
        "when": "You have a bug report, traceback, or unexpected behavior and need to find the root cause.",
        "prompt": """Run RubberDuck UC-03 bug localization.

Input fields:

Repository \t`<owner/repo>`;
Branch/ref \t`<branch-or-ref>`;
Commit \t\t`<commit-sha>`;

Bug signal \t`<EXPLAIN BUG IN PROSE>`



Do not edit the repo; localize root cause and propose patch/tests only.
Use prod RubberDuck evidence: `get_started`, completed `detailed_repo_analysis(..., semantic_mode="full")`, Phase 2 ready, `load_code(max_files=4000)`.
Stop if a hard RD primitive stays hidden after 3 scoped exposure retries, ref binding fails, or evidence is stale/wrong branch/commit/path.
Inspect relevant route/entrypoint, handler, input parse, source, branch condition, sink, safe sibling/contrast path, and missing guard.
Validate with source reads plus targeted trace/search/graph/security evidence; no web/raw GitHub or generic fallback evidence.
Write `BUG_LOCALIZATION_REPORT.md`: scenario, root-cause hypothesis, evidence table, root cause, blast radius, minimal fix, regression probes, adversarial negative case, method notes.
Security artifact contract: include sections named Security Invariant, Adversarial Probes, Impact/Test Matrix, Evidence-Cleanliness Blockers, Unsupported Clean/Security-Ready Claims.
Final response starts `RubberDuck initialization: passed` or failure with failed step; name target/ref/scope/output dir and do not claim fixed/clean beyond evidence.""",
        "focus": "`demoapp/db/query.py` — `get_aggregation`, `rewrite_cols`",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> trace_variable / call_chain / search_code / read_source",
    },
    {
        "id": "04",
        "slug": "uc-04-code-review",
        "title": "Code Review",
        "when": "You need to review a code change — PR, colleague's code, or your own before merging.",
        "prompt": """Run RubberDuck UC-04 code review.

Input fields: Repository `<owner/repo>`;
Branch/ref `<branch-or-ref>`;
Commit `<commit-sha>`;
Review diff `<REVIEW_TARGET.diff>`.

Review only; do not edit the repo. Required artifact: `CODE_REVIEW.md`.
Use prod RD current-ref evidence: `get_started`, completed `detailed_repo_analysis(..., semantic_mode="full")`, Phase 2 ready, `load_code(max_files=4000)`.
Stop on missing diff, failed ref proof, stale evidence, hidden hard primitive after 3 scoped retries, or any need for unauthorized mutation.
Assess correctness, security delta, compatibility policy, false-safety risk, maintainability, missing tests, and merge readiness.
Check direct changed paths plus adjacent residual paths, compatibility flags/policies, docs/warnings, and tests.
Treat the supplied diff as diff evidence, not applied source, unless the checkout is explicitly pinned to that patch.
Write `CODE_REVIEW.md`: severity-ranked findings, missing tests, merge checklist, rejected non-issues, recommendations, exact file/line evidence, method notes.
Security artifact contract: include sections named Security Invariant, Adversarial Probes, Impact/Test Matrix, Evidence-Cleanliness Blockers, Unsupported Clean/Security-Ready Claims.
Final response starts RD passed/failed, names target/ref/scope/output dir; do not say merge-ready/security-ready unless evidence and tests support it.""",
        "focus": "`fixtures/uc-04-pr-order-by-diff.md` + `demoapp/db/query.py`",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> analyze_code / read_source / search_code / call_chain",
    },
    {
        "id": "05",
        "slug": "uc-05-change-impact-analysis",
        "title": "Change Impact Analysis",
        "when": "Before making a change, you need to know what will break and what tests to run.",
        "prompt": """Run RubberDuck UC-05 change-impact analysis.

Input fields:
Repository `<owner/repo>`;
Branch/ref `<branch-or-ref>`;
Commit `<commit-sha>`;

Proposed change `<change description>`.

Read-only impact analysis; required artifact `IMPACT_REPORT.md`.
Use prod RD current-ref gates: `get_started`, full `detailed_repo_analysis(..., semantic_mode="full")`, Phase 2 ready, `load_code(max_files=4000)`.
Stop if change input, ref binding, or hard RD gates fail; reject stale/wrong-commit evidence and web/raw GitHub fallback.
Map propagation from entrypoints, handlers, source variables, branch conditions, sinks, safe siblings, callers/callees, residual paths, and tests.
Validate API/state/data impacts, compatibility risk, and safe sequencing with source plus targeted graph/trace/search/security evidence.
Write `IMPACT_REPORT.md`: impact summary, propagation map, caller/callee evidence, test matrix, safe change order, limitations, next steps.
Security artifact contract: include sections named Security Invariant, Adversarial Probes, Impact/Test Matrix, Evidence-Cleanliness Blockers, Unsupported Clean/Security-Ready Claims.
Include security invariant and adversarial probes; do not claim clean/release-ready without relevant core, integration, framework, and security tests.""",
        "focus": "`demoapp/config.py` — rename `config_values`",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> call_chain / trace_variable / search_code",
    },
    {
        "id": "06",
        "slug": "uc-06-plan-new-feature",
        "title": "Plan a New Feature",
        "when": "You want to add a new feature, preferably tests-first.",
        "prompt": """Run RubberDuck UC-06 feature planning.


Input fields:
Repository `<owner/repo>`;
Branch/ref `<branch-or-ref>`;
Commit `<commit-sha>`;


Feature request `<feature goal>`.


Plan only; no repo edits. Required artifact: `FEATURE_PLAN.md`.
Use prod RD current-ref gates: `get_started`, completed `detailed_repo_analysis(..., semantic_mode="full")`, Phase 2 ready, `load_code(max_files=4000)`, source/search/graph evidence.
Stop if ref proof or RD hard gates fail, or if the feature would require unsupported mutation during planning.
Constrain scope explicitly: name what is in scope, out of scope, and what must remain unchanged for compatibility.
Plan around relevant entrypoints, handlers, policy checks, serializers/parsers, external surfaces, residual risks, and tests.
Write `FEATURE_PLAN.md`: scenario, fit analysis, tests-first plan, integration points, security acceptance, implementation sequence, export/PR blockers, method notes.
Security artifact contract: include sections named Security Invariant, Adversarial Probes, Impact/Test Matrix, Evidence-Cleanliness Blockers, Unsupported Clean/Security-Ready Claims.
Acceptance must include adversarial rejection, compatibility preservation, explicit opt-in/policy if retained, and no full-safety claim beyond addressed paths.""",
        "focus": "`demoapp/builders/html.py` — `write_doc`, parallel patterns",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> search_code / read_source / call_chain / analyze_code",
    },
    {
        "id": "07",
        "slug": "uc-07-generate-code",
        "title": "Generate Code That Fits (codegen)",
        "when": "You need to write code that fits seamlessly into an existing codebase.",
        "prompt": """You are running RubberDuck UC-07: CodeGen - Autonomous Code Delivery with Proof.

## Fill In Before Running

```text
_________________________________________________________________________________
Repository or local project: [FILL IN]
Change request: [FILL IN USING PROSE - JUST DESCRIBE IT WITH YOUR OWN WORDS]

Optional:
Branch/ref: auto
Commit: latest on selected branch/ref
Scope limits:
Save results to: auto
_________________________________________________________________________________
```

## Task

Use RubberDuck CodeGen to turn the prose change request into a repo-aware, validated, review-ready software change with proof.

Use this prompt as the whole task. If `Repository or local project` or `Change request` is missing, ask one concise clarifying question before running.

Default behavior: preview first. Create a reviewable patch and proof. Do not edit the target repo unless the user explicitly asks to apply the change. If the user asks to apply changes, stay inside any `Scope limits`.

## CodeGen Contract

1. Resolve `Repository or local project`, `Branch/ref`, and `Commit`. If branch/ref is `auto` and a local project is supplied, use the local checkout's current branch/ref and HEAD. If only a GitHub repo is supplied, use the repo's default branch. If commit is `latest`, pin the selected branch/ref head SHA when applicable.
2. Before starting CodeGen, confirm the selected ref has the expected source inventory. If RubberDuck reports zero source files for a ref that should contain source, try the intended active branch once, then report blocked with the exact ref/indexing mismatch.
3. Start a CodeGen session on the pinned repo/ref/commit with the prose change request. Do not require a plan; CodeGen derives repo fit from the baseline and Fit Pack.
4. Get the Fit Pack before editing. Treat suggested locations, avoid locations, existing patterns, dependency constraints, and validation guidance as the implementation contract.
5. If CodeGen tools, baseline, or Fit Pack are unavailable, stale, wrong-repo, wrong-branch, or wrong-commit, stop and report `RubberDuck CodeGen: blocked`. Do not substitute the old semantic initialization path (`get_started`, `detailed_repo_analysis`, `load_code`) for CodeGen.
6. Produce a reviewable `PR_READY.diff` by default. Edit the target repo only when the user explicitly asks for applied changes; if `Scope limits` are supplied, stay inside them.
7. Implement or draft the smallest fitting change. Add or update focused tests when behavior changes.
8. Run the relevant local validation commands: focused tests for touched behavior plus any obvious repo check/build command.
9. Validate the final diff with `validate_generated_diff`. Fix FAIL results. Adjudicate WARN results with a concrete reason or revise.
10. End the CodeGen session with final diff, tests, validation ID, and remaining risk.

## Security Hardening

If the request is security-sensitive, auth/network/parser/browser-facing, benchmark-like, clean-room, or untrusted-input-adjacent, first state the security invariant and run relevant adversarial or negative tests. If the security gate is incomplete, report blocked instead of claiming success.

## Output

Write `BUILD_REPORT.md` under `Save results to` or, if `auto`, under `./rubberduck-uc-07-codegen-delivery-<YYYYMMDDTHHMMSSZ>/artifacts`.

Include:

- Repository or local project, branch/ref, pinned commit when applicable, preview/apply status, and scope limits.
- CodeGen session ID, Fit Pack ID, and `validate_generated_diff` validation ID.
- Changed files and/or `PR_READY.diff`.
- Tests/checks run and pass/fail results.
- Warnings, blockers, remaining risk, and next actions.

Final answer:

- Start with `RubberDuck CodeGen: passed` when CodeGen and validation passed.
- Start with `RubberDuck CodeGen: blocked` when blocked.
- Name `BUILD_REPORT.md` and `PR_READY.diff` when produced.""",
        "focus": "`demoapp/ext/github.py` — extend with `gitlab.py` + test",
        "workflow": "CodeGen session -> Fit Pack -> PR_READY.diff -> validate_generated_diff",
    },
    {
        "id": "08",
        "slug": "uc-08-check-code-logic",
        "title": "Check Code Logic",
        "when": "Verify correctness of complex logic — conditions, gaps, control flow.",
        "prompt": """Run RubberDuck UC-08 logic check.

Input fields:

Repository `<owner/repo>`;
Branch/ref `<branch-or-ref>`;
Commit `<commit-sha>`;

Logic question `<specific invariant/path>`.


Read-only; required artifact `LOGIC_CHECK.md`.
Use prod RD current-ref gates: `get_started`, completed `detailed_repo_analysis(..., semantic_mode="full")`, Phase 2 ready, `load_code(max_files=4000)`, exact file/path evidence.
Stop if the logic target, ref proof, RD hard gates, or hidden hard primitive after 3 scoped retries fail; no web/raw GitHub or stale cache evidence.
Trace setup, entrypoint, input parse, branch conditions, safe path, risky path, guard/reject/verify points, and sink.
Validate branch map, data flow, guards, rejects, verification, and verdict with source reads plus targeted trace/graph/search/security/logic evidence.
Write `LOGIC_CHECK.md`: scenario, verdict, branch map, data-flow proof, guard/reject/verify check, falsification steps, method notes.
Security artifact contract: include sections named Security Invariant, Adversarial Probes, Impact/Test Matrix, Evidence-Cleanliness Blockers, Unsupported Clean/Security-Ready Claims.
State adversarial paths considered and do not claim safe/correct if a source-visible guard is absent or evidence gates are incomplete.""",
        "focus": "`demoapp/builders/html.py` — `get_outdated_docs`",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> read_source / trace_variable / call_chain / logic_analysis",
    },
    {
        "id": "09",
        "slug": "uc-09-compare-versions",
        "title": "Compare Versions",
        "when": "Compare implementations across classes or versions for compatibility risks.",
        "prompt": """Run RubberDuck UC-09 comparison.
Input fields: Repository `<owner/repo>`; Branch/ref `<branch-or-ref>`; Commit `<commit-sha>`; Side A `<current behavior/ref>`; Side B `<diff/ref>`.
Comparison only; do not edit repo. Required artifact: `COMPARISON_REPORT.md`.
Use prod RD to validate applied/current side: `get_started`, completed `detailed_repo_analysis(..., semantic_mode="full")`, Phase 2 ready, `load_code(max_files=4000)`, current-ref source/graph evidence.
Treat any supplied diff side as diff evidence, not applied code, unless the checkout is explicitly pinned to it.
Stop if either side, ref proof, hard RD gate, or hidden hard primitive after 3 scoped retries is missing.
Compare default behavior, compatibility, security invariant, remaining risky paths, exception/config drift, test adequacy, migration risk, and false assurance.
Write `COMPARISON_REPORT.md`: scenario, equivalence verdict, side-by-side table, divergence risks, compatibility tests, falsification steps, method notes.
Security artifact contract: include sections named Security Invariant, Adversarial Probes, Impact/Test Matrix, Evidence-Cleanliness Blockers, Unsupported Clean/Security-Ready Claims.
State whether sides are equivalent, intentionally divergent, or blocked; do not claim full safety beyond compared evidence.""",
        "focus": "`demoapp/builders/html.py` — HTML vs Epub3 `prepare_writing`",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> read_source / search_code / call_chain",
    },
    {
        "id": "10",
        "slug": "uc-10-quick-check",
        "title": "Quick Check",
        "when": "30-second assessment of an unfamiliar method — what it does, who depends on it, risk.",
        "prompt": """Run RubberDuck UC-10 quick check.



Input fields:

Repository `<owner/repo>`;
Branch/ref `<branch-or-ref>`;
Commit `<commit-sha>`;

Question `<narrow yes/no target>`.



Read-only narrow answer; required artifact `QUICK_CHECK.md`.
Use prod RD current-ref gates: `get_started`, completed `detailed_repo_analysis(..., semantic_mode="full")`, Phase 2 ready, `load_code(max_files=4000)`, exact source evidence.
Stop on missing question, ref proof failure, hidden hard primitive after 3 scoped retries, or stale/wrong-commit evidence.
Inspect only the named file/symbol/path and the minimal adjacent source needed to answer the question.
Validate yes/no with exact source lines plus targeted search/trace/security evidence; optional helper failures are method notes only.
Write `QUICK_CHECK.md`: question, yes/no or scoped verdict, evidence table, limitations, method notes, falsification/next steps.
Quick-check contract: include Security Scope covering invariant, probes considered/not run, impact limits, evidence-cleanliness blockers, and why this is not a full audit.
Label it a quick check, not a full audit; do not claim public exploitability or clean status without broader reachability/probe evidence.""",
        "focus": "`demoapp/builders/html.py` — `render_partial`",
        "workflow": "get_started -> detailed_repo_analysis(semantic_mode=full) -> load_code -> read_source / call_chain / search_code",
    },
]


def write_uc_docs() -> None:
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    for uc in USE_CASES:
        uc_id = uc["id"]
        meta = META[uc_id]
        playground_prompt = fill_playground_prompt(uc_id, uc["prompt"].strip())
        path = docs / f"uc-{uc_id}.md"
        path.write_text(
            f"# UC-{uc_id}: {uc['title']} ({meta['website_name']})\n\n"
            f"## What this does\n\n"
            f"{meta['plain']}\n\n"
            f"## What you gain\n\n"
            f"{meta['gain']}\n\n"
            f"## How to test (2 steps)\n\n"
            f"**Step 1 — Terminal** (see the real behavior):\n\n"
            f"```bash\n"
            f"python scripts/run-lab.py --uc {uc_id}\n"
            f"```\n\n"
            f"{meta['demo_note']}\n\n"
            f"**Step 2 — Cursor** (paste the prompt below into chat after RubberDuck MCP is connected):\n\n"
            f"- Index once: `Index my local project at: <path-to-this-repo>`\n"
            f"- **Edit only:** {meta['edit']}\n"
            f"- Copy the entire **Playground prompt** block below\n\n"
            f"## What a good answer looks like\n\n"
            f"{meta['expect']}\n\n"
            f"Must include: repo name, branch/ref, **pinned commit SHA**, and **file:line** evidence.\n\n"
            f"**Focus files in this repo:** {uc['focus']}\n\n"
            f"---\n\n"
            f"## Playground prompt (copy ALL of this into Cursor)\n\n"
            f"````\n{playground_prompt}\n````\n\n"
            f"<details>\n<summary>Official library prompt (reference — unfilled placeholders)</summary>\n\n"
            f"````\n{uc['prompt'].strip()}\n````\n\n"
            f"</details>\n\n"
            f"More: [HOW_TO_TEST.md](HOW_TO_TEST.md) · [rubberduck.com docs](https://rubberduck.com/#docs)\n",
            encoding="utf-8",
        )


def write_branch_tutorial(uc: dict) -> None:
    text = (
        f"# Tutorial — UC-{uc['id']}: {uc['title']}\n\n"
        f"> Branch `{uc['slug']}` — public playground for "
        f"[RubberDuck](https://rubberduck.com) workflows.\n\n"
        f"## When to use\n\n{uc['when']}\n\n"
        f"## Setup\n\n"
        f"1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).\n"
        f"2. **Focus files:** {uc['focus']}\n"
        f"3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)\n\n"
        f"## Prompt\n\n"
        f"````\n{uc['prompt'].strip()}\n````\n\n"
        f"## Expected RubberDuck tool flow\n\n`{uc['workflow']}`\n\n"
        f"## Success criteria\n\n"
        f"- Every claim cites **file:line** from MCP tools\n"
        f"- Coherence / graph-backed evidence (not generic LLM guessing)\n"
        f"- Compare your run with the official doc narrative on rubberduck.com\n\n"
        f"## More detail\n\nSee [docs/uc-{uc['id']}.md](docs/uc-{uc['id']}.md)\n"
    )
    (ROOT / "TUTORIAL.md").write_text(text, encoding="utf-8")


def main() -> None:
    write_uc_docs()
    print(f"Wrote {len(USE_CASES)} files under docs/")


def create_branches() -> None:
    import subprocess

    write_uc_docs()
    subprocess.run(["git", "init"], cwd=ROOT, check=True)
    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    subprocess.run(
        ["git", "commit", "-m", "Initial commit: RubberDuck use-case playground"],
        cwd=ROOT,
        check=True,
    )
    for uc in USE_CASES:
        subprocess.run(["git", "branch", uc["slug"]], cwd=ROOT, check=True)
        subprocess.run(["git", "checkout", uc["slug"]], cwd=ROOT, check=True)
        write_branch_tutorial(uc)
        subprocess.run(["git", "add", "TUTORIAL.md"], cwd=ROOT, check=True)
        subprocess.run(
            ["git", "commit", "-m", f"Add tutorial for UC-{uc['id']}: {uc['title']}"],
            cwd=ROOT,
            check=True,
        )
    default = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT, text=True
    ).strip()
    base = "main" if "main" in subprocess.check_output(
        ["git", "branch", "--list", "main"], cwd=ROOT, text=True
    ) else "master"
    subprocess.run(["git", "checkout", base], cwd=ROOT, check=True)
    # main branch: no per-UC TUTORIAL
    tutorial = ROOT / "TUTORIAL.md"
    if tutorial.exists():
        tutorial.unlink()
    print("Created branches:", ", ".join(u["slug"] for u in USE_CASES))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--branches":
        create_branches()
    else:
        main()
