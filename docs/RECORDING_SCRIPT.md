# Recording script — Rubber Duck Playground walkthrough

Use this on camera for Piermatteo's ask: *how to trigger each use case, what to do, and what we expect.*

**Repo:** https://github.com/RubberDuck-com/rubberduck-use-case-playground  
**Prompts:** copy from `docs/uc-01.md` … `docs/uc-10.md` (official Guided Prompt Library text). Edit only the input fields (repo, branch/ref, commit, bug/question/diff).

---

## Before recording (checklist)

- [ ] Repo cloned and open in Cursor (`Workspace/rubberduck-use-case-playground`)
- [ ] `python scripts/run-lab.py --uc 01 --setup-only` (venv + deps)
- [ ] RubberDuck MCP connected (Codebase + Semantic Intelligence)
- [ ] GitHub App installed (needed for UC-04 with a real PR)
- [ ] Notifications off, terminal font large, browser zoom readable on video

**Say once on camera:** website names vs repo branch names are the same 10 use cases with different labels.

| # | Website / PDF | Repo name | Branch |
|---|---------------|-----------|--------|
| 01 | Codebase Atlas | Understand Your Code | `uc-01-understand-your-code` |
| 02 | Security Audit | Codebase Audit | `uc-02-codebase-audit` |
| 03 | Bug Localization | Localize and Fix Bugs | `uc-03-localize-and-fix-bugs` |
| 04 | Full-Repo PR Review | Code Review | `uc-04-code-review` |
| 05 | Change Impact | Change Impact Analysis | `uc-05-change-impact-analysis` |
| 06 | Feature Planning | Plan a New Feature | `uc-06-plan-new-feature` |
| 07 | CodeGen | Generate Code That Fits | `uc-07-generate-code` |
| 08 | Business Logic Check | Check Code Logic | `uc-08-check-code-logic` |
| 09 | Compare Versions | Compare Versions | `uc-09-compare-versions` |
| 10 | Quick Check | Quick Check | `uc-10-quick-check` |

**Good answer rule:** every RubberDuck result must name repo, branch/ref, **pinned SHA**, `file:line` evidence. Missing that = incomplete, rerun.

---

## 1. Intro (~45 sec)

**SAY:** This is the Rubber Duck Playground — ten runnable labs and one demo app. I'll show how to trigger each use case and what a correct, evidence-bound answer looks like.

**DO:** Show README → scroll the ten use cases table → briefly show `labs/` and `demoapp/`.

---

## 2. One-time setup on camera (~60 sec)

**SAY:** Each lab runs locally first so you see real behavior before AI.

**DO:**
```bash
python scripts/run-lab.py --uc 02 --verify
```

**EXPECT:** Venv installs (first run), verify passes, launcher prints index hint + prompt.

**SAY:** Now I index the repo once in RubberDuck.

**DO (Cursor chat):**
```
Index my local project at: <absolute path to rubberduck-use-case-playground>
```

**EXPECT:** Loaded repo, one pinned SHA, source files found.

---

## 3. Ten use cases

For each UC: (1) open lab / branch, (2) run verify, (3) copy prompt from `docs/uc-XX.md` and fill inputs, (4) point at evidence-bound output.

### UC-01 — Codebase Atlas

**DO:** `python scripts/run-lab.py --uc 01 --verify` · focus `demoapp/cmd/build.py`, `demoapp/application.py` · paste `docs/uc-01.md` (set target repo + branch + commit).

**EXPECT:** Architecture map, entry points, call/data flows, exact SHA.

### UC-02 — Security Audit

**DO:** `python scripts/run-lab.py --uc 02 --start-server` · open http://127.0.0.1:8080/docs · paste `docs/uc-02.md` (set `target=` to this repo path).

**EXPECT:** `SECURITY_AUDIT.md` style output — entry → sink chains, `file:line`, severity; no "clean" without probes.

### UC-03 — Bug Localization

**DO:** `pytest labs/uc03_buggy_orm/tests -q` (show fail) · paste `docs/uc-03.md` · bug signal = ORM aggregation / GROUP BY symptom.

**EXPECT:** `BUG_LOCALIZATION_REPORT.md` — root cause, evidence table, blast radius, minimal fix; proved vs inferred labeled.

### UC-04 — Code Review

**DO:** Show `fixtures/uc-04-pr-order-by-diff.md` · `python scripts/run-lab.py --uc 04 --verify` · paste `docs/uc-04.md` with review diff.

**EXPECT:** `CODE_REVIEW.md` — verdict, blockers, diff treated as diff evidence not applied source.

### UC-05 — Change Impact

**DO:** `python scripts/run-lab.py --uc 05 --verify` · paste `docs/uc-05.md` · proposed change = rename `config_values` → `values`.

**EXPECT:** `IMPACT_REPORT.md` — callers/callees, test matrix, safe change order, out-of-scope residual.

### UC-06 — Feature Planning

**DO:** Open `labs/uc06_feature/TASK.md` · `pytest labs/uc06_feature/tests -q` · paste `docs/uc-06.md` with feature goal.

**EXPECT:** `FEATURE_PLAN.md` — tests-first plan, no production code written.

### UC-07 — CodeGen

**DO:** Open `labs/uc07_codegen/TASK.md` · paste `docs/uc-07.md` · preview only, not auto-apply.

**EXPECT:** `PR_READY.diff` + `BUILD_REPORT.md` · `RubberDuck CodeGen: passed` or `blocked`.

### UC-08 — Business Logic Check

**DO:** `python scripts/run-lab.py --uc 08 --verify` · paste `docs/uc-08.md` with logic question on `get_outdated_docs`.

**EXPECT:** `LOGIC_CHECK.md` — yes/no verdict, guard at `file:line` or proof guard is missing.

### UC-09 — Compare Versions

**DO:** `python scripts/run-lab.py --uc 09 --verify` · paste `docs/uc-09.md` · Side A vs Side B (HTML vs Epub3 builders).

**EXPECT:** `COMPARISON_REPORT.md` — equivalence verdict + divergence matrix.

### UC-10 — Quick Check

**DO:** `python scripts/run-lab.py --uc 10 --verify` · paste `docs/uc-10.md` · one narrow question on `render_partial`.

**EXPECT:** `QUICK_CHECK.md` — concise yes/no + evidence; states what was not checked (not a full audit).

---

## 4. Optional ending — chained workflow (~2 min)

**SAY:** Real workflows chain prompts: UC-03 → UC-05 → UC-07 → UC-04.

**DO:** Run UC-03 (bug) → feed minimal fix into UC-05 → UC-07 preview patch → UC-04 review.

---

## 5. Outro (~20 sec)

**SAY:** Every use case is evidence-bound to a pinned commit. Prompts live in `docs/`. Full setup: `GUIDE.md` and `SETUP.md`.

**DO:** Show `docs/uc-01.md` prompt block briefly so viewers know where to copy from.

---

## Recording tips

- **Length:** full 10-UC walkthrough is long; Piermatteo may accept a **pilot** (UC-01 + UC-02 + UC-03) first, then part 2.
- **Red X on GitHub commits:** `Rubber Duck / CodeAnalyzer` is a backend app check — does not block labs or MCP demos.
- **Save:** export MP4; share link with Piermatteo / marketing when done.
