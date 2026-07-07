# Expected outcomes (what “good” looks like)

Use this when reviewing RubberDuck output or recording demos. Every answer should cite **repo + branch + pinned SHA + file:line**.

## UC-01 — Understand Your Code (Codebase Atlas)

- **Artifact:** `codebase-atlas.md` (or equivalent report)
- **Must mention:** `demoapp/cmd/build.py` as CLI entry, `Application.build`, builder pipeline
- **Evidence:** call chains from `main` → `Application` → builders
- **Pass phrase:** `RubberDuck initialization: passed`

## UC-02 — Security Audit

- **Artifact:** `SECURITY_AUDIT.md`
- **Must find:** SQL injection path in `demoapp/api/server.py` (`search` builds SQL from input)
- **Should find:** `exec()` in `demoapp/config.py` `eval_config_file`, pickle in `from_pickle`
- **Format:** entry → data-flow → sink table with severity

## UC-03 — Bug Localization

- **Artifact:** `BUG_LOCALIZATION_REPORT.md`
- **Root cause:** `demoapp/db/query.py` — `get_aggregation` mutates inner query mask / wrong count
- **Evidence:** failing behavior matches terminal demo (`count=1`, mask mutated)

## UC-04 — PR Code Review

- **Artifact:** review report with APPROVE or BLOCK
- **Context:** `fixtures/uc-04-pr-order-by-diff.md` — order-by / group-by compiler change
- **Must assess:** blast radius, test gaps, semantic risk of `is_ref` in `get_group_by`

## UC-05 — Change Impact

- **Artifact:** `IMPACT_REPORT.md`
- **Change:** rename `config_values` → `values` in `demoapp/config.py`
- **Must list:** every module that reads `Config` attributes

## UC-06 — Feature Planning

- **Artifact:** `FEATURE_PLAN.md` (plan only — no code)
- **Feature:** `--parallel-write` for HTML builder
- **Must include:** tests first, files to touch, acceptance criteria

## UC-07 — CodeGen

- **Artifact:** `PR_READY.diff`, `BUILD_REPORT.md`
- **Task:** implement `gitlab_role` like `github_role` in `demoapp/ext/`
- **Pass:** `RubberDuck CodeGen: passed` after validation

## UC-08 — Business Logic Check

- **Artifact:** `LOGIC_CHECK.md`
- **Question:** does `get_outdated_docs` catch all stale docs?
- **Verdict:** yes/no with branch map and file:line guards

## UC-09 — Compare Versions

- **Artifact:** `COMPARISON_REPORT.md`
- **Compare:** `StandaloneHTMLBuilder.prepare_writing` vs `Epub3Builder.prepare_writing`
- **Verdict:** equivalent / divergent with divergence matrix

## UC-10 — Quick Check

- **Artifact:** `QUICK_CHECK.md`
- **Question:** what does `render_partial` do in `demoapp/builders/html.py`?
- **Format:** narrow yes/no + evidence table + explicit “not checked” scope
