# Expected outcomes (what “good” looks like)

Use when reviewing RubberDuck output or recording demos.

**Every answer must include:** repo name, branch/ref, **pinned commit SHA**, and **file:line** evidence.

**Every answer must NOT:** guess without evidence, use stale/wrong commit, skip initialization gates, or claim “fixed/clean” beyond what evidence supports.

---

## UC-01 — Understand Your Code (Codebase Atlas)

| Field | Value |
|-------|-------|
| **Local verify** | `python labs/uc01_understand/verify.py` |
| **Terminal demo** | `python scripts/run-lab.py --uc 01` |
| **Prompt** | `docs/uc-01.md` → Playground prompt block |
| **Expected tools** | `get_started` → `detailed_repo_analysis(semantic_mode=full)` → `load_code` → `read_source` / `search_code` / `query_action` |
| **Artifact** | `codebase-atlas.md` |
| **Must mention** | `demoapp/cmd/build.py:main`, `Application.build`, builder pipeline |
| **Must NOT** | Run search/read before `load_code` completes; report without pinned SHA |
| **Pass phrase** | `RubberDuck initialization: passed` |

---

## UC-02 — Security Audit

| Field | Value |
|-------|-------|
| **Local verify** | `python labs/uc02_security_lab/verify.py` |
| **Terminal demo** | `python scripts/run-lab.py --uc 02` (optional: `--server` for live API) |
| **Prompt** | `docs/uc-02.md` |
| **Expected tools** | `get_started` → `detailed_repo_analysis` → `load_code` → security trace / `search_code` |
| **Artifact** | `SECURITY_AUDIT.md` |
| **Must find** | SQL injection in `demoapp/api/server.py:search`; `exec()` in `config.py:eval_config_file`; pickle in `from_pickle` |
| **Must NOT** | Pattern-only findings without source→sink path; omit Low findings silently |
| **Format** | entry → data-flow → sink table with severity |

---

## UC-03 — Bug Localization

| Field | Value |
|-------|-------|
| **Local verify** | `pytest labs/uc03_buggy_orm/tests -q` |
| **Terminal demo** | `python scripts/run-lab.py --uc 03` |
| **Prompt** | `docs/uc-03.md` |
| **Expected tools** | `get_started` → `detailed_repo_analysis` → `load_code` → `trace_variable` / `query_action` |
| **Artifact** | `BUG_LOCALIZATION_REPORT.md` |
| **Root cause** | `demoapp/db/query.py` — `get_aggregation` mutates inner mask, wrong count |
| **Terminal evidence** | `count=1`, `inner mask (mutated) : {'total'}` |
| **Must NOT** | Mutate the repo; claim fixed without evidence |

---

## UC-04 — PR Code Review

| Field | Value |
|-------|-------|
| **Local verify** | `python labs/uc04_pr_review/verify.py` |
| **Terminal demo** | `python scripts/run-lab.py --uc 04` |
| **Prompt** | `docs/uc-04.md` |
| **Review target** | `fixtures/uc-04-pr-order-by-diff.md` |
| **Artifact** | Review report with **APPROVE** or **BLOCK** |
| **Must assess** | Blast radius, test gaps, `is_ref` risk in `get_group_by` |
| **Must NOT** | Treat diff as applied source; say merge-ready without evidence |

---

## UC-05 — Change Impact

| Field | Value |
|-------|-------|
| **Local verify** | `python labs/uc05_impact/verify.py` |
| **Terminal demo** | `python scripts/run-lab.py --uc 05` |
| **Prompt** | `docs/uc-05.md` |
| **Proposed change** | Rename `config_values` → `values` in `demoapp/config.py` |
| **Artifact** | `IMPACT_REPORT.md` |
| **Must list** | All consumers (verify counts ~18 references) |
| **Must NOT** | Miss callers in `demoapp/`, `labs/uc05_impact/consumers/` |

---

## UC-06 — Feature Planning

| Field | Value |
|-------|-------|
| **Local verify** | `pytest labs/uc06_feature/tests -q` → **1 xfailed** (exercise) |
| **Terminal demo** | `python scripts/run-lab.py --uc 06` |
| **Prompt** | `docs/uc-06.md` |
| **Feature** | `--parallel-write` for HTML builder |
| **Artifact** | `FEATURE_PLAN.md` (plan only — no code) |
| **Must include** | Tests first, files to touch, acceptance criteria |
| **Must NOT** | Write production code during planning step |

---

## UC-07 — CodeGen

| Field | Value |
|-------|-------|
| **Local verify** | `pytest labs/uc07_codegen/tests -q` → **1 xfailed** (exercise) |
| **Terminal demo** | `python scripts/run-lab.py --uc 07` |
| **Prompt** | `docs/uc-07.md` |
| **Task** | Implement `gitlab_role` like `github_role` in `demoapp/ext/` |
| **Artifact** | `PR_READY.diff`, `BUILD_REPORT.md` |
| **Pass phrase** | `RubberDuck CodeGen: passed` |
| **Must NOT** | Show unvalidated patch; skip build/test proof |

---

## UC-08 — Business Logic Check

| Field | Value |
|-------|-------|
| **Local verify** | `python labs/uc08_logic/verify.py` |
| **Terminal demo** | `python scripts/run-lab.py --uc 08` |
| **Prompt** | `docs/uc-08.md` |
| **Question** | Does `get_outdated_docs` catch all stale docs? |
| **Artifact** | `LOGIC_CHECK.md` |
| **Must include** | Branch map, yes/no verdict, file:line guards |
| **Must NOT** | Verdict without tracing branch conditions |

---

## UC-09 — Compare Versions

| Field | Value |
|-------|-------|
| **Local verify** | `python labs/uc09_compare/verify.py` |
| **Terminal demo** | `python scripts/run-lab.py --uc 09` |
| **Prompt** | `docs/uc-09.md` |
| **Compare** | `StandaloneHTMLBuilder.prepare_writing` vs `Epub3Builder.prepare_writing` |
| **Artifact** | `COMPARISON_REPORT.md` |
| **Terminal evidence** | Epub3 adds `theme_writing_mode`, `html_tag`, `use_meta_charset`, `skip_ua_compatible` |
| **Must NOT** | Equivalence claim without side-by-side divergence matrix |

---

## UC-10 — Quick Check

| Field | Value |
|-------|-------|
| **Local verify** | `python labs/uc10_quick/verify.py` |
| **Terminal demo** | `python scripts/run-lab.py --uc 10` |
| **Prompt** | `docs/uc-10.md` |
| **Question** | What does `render_partial` do in `demoapp/builders/html.py`? |
| **Artifact** | `QUICK_CHECK.md` |
| **Must include** | Narrow yes/no, evidence table, explicit “not checked” scope |
| **Must NOT** | Broad repo scan when question is single-function |

---

## Full suite

```bash
python -m pytest tests labs -q
```

**Expected:** `3 passed, 2 xfailed` (exit 0). UC-06 and UC-07 are training exercises.

**Session log with prompts + RubberDuck outputs:** `docs/FULL_SESSION_LOG.md`
