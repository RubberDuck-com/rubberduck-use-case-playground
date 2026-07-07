"""Human-readable metadata for each use case (docs + README)."""

PLAYGROUND_GITHUB = "RubberDuck-com/rubberduck-use-case-playground"
PLAYGROUND_URL = f"https://github.com/{PLAYGROUND_GITHUB}"

META = {
    "01": {
        "website_name": "Codebase Atlas",
        "plain": "Map an unfamiliar repo: entry points, call chains, data flows, architecture — pinned to a commit.",
        "gain": "You get an onboarding report so you (or an agent) know where the app starts and how code connects — with file:line proof, not guesses.",
        "edit": "Usually nothing for this playground — the Target below is pre-filled.",
        "expect": "Report names repo + pinned SHA, lists entry points (e.g. `demoapp/cmd/build.py:main`), call chains, and data flows.",
        "demo_note": "Builds a real HTML file at `sampledocs/_build/index.html`.",
    },
    "02": {
        "website_name": "Security Audit",
        "plain": "Find security-sensitive paths with source-to-sink evidence (not pattern-only noise).",
        "gain": "A defensible security report: each finding has entry → data-flow → sink, severity, and file:line citations.",
        "edit": "`target=` is pre-filled. Optional: change `focus=` for a narrower scope.",
        "expect": "`SECURITY_AUDIT.md` with findings table; ends with `RubberDuck initialization: passed` or a clear failure.",
        "demo_note": "Optional live API: `python scripts/run-lab.py --uc 02 --server` then open http://127.0.0.1:8080/docs",
    },
    "03": {
        "website_name": "Bug Localization",
        "plain": "Trace a symptom or failing test to root cause in the code graph.",
        "gain": "Root cause, evidence table, blast radius, minimal fix direction — each step cited at file:line.",
        "edit": "Fill `Bug signal` with the symptom (example provided below).",
        "expect": "`BUG_LOCALIZATION_REPORT.md` pointing at `demoapp/db/query.py` aggregation logic.",
        "demo_note": "Shows the live ORM bug: wrong aggregation count and mutated mask.",
    },
    "04": {
        "website_name": "Full-Repo PR Review",
        "plain": "Review a change against the whole-repo model, not just the diff hunk.",
        "gain": "APPROVE/BLOCK verdict with blast radius, missing tests, and evidence.",
        "edit": "Point `Review diff` at `fixtures/uc-04-pr-order-by-diff.md` or paste the diff.",
        "expect": "Verdict with file:line; diff treated as diff evidence, not applied source.",
        "demo_note": "Runs compiler order-by/group-by logic that the PR touches.",
    },
    "05": {
        "website_name": "Change Impact",
        "plain": "Before you rename or change shared code, see every caller and test you must touch.",
        "gain": "Impact map, safe change order, risk score, and out-of-scope residual.",
        "edit": "Fill `Proposed change` (example: rename `config_values` → `values`).",
        "expect": "`IMPACT_REPORT.md` listing consumers of `demoapp/config.py`.",
        "demo_note": "Shows `config_values` and mirrored `values` dict.",
    },
    "06": {
        "website_name": "Feature Planning",
        "plain": "Tests-first sealed plan before writing production code.",
        "gain": "A plan with files to touch, tests first, acceptance criteria — no code written yet.",
        "edit": "Fill `Feature request` (example: add `--parallel-write` to the HTML builder).",
        "expect": "`FEATURE_PLAN.md`; builder flags show parallel write is not implemented yet.",
        "demo_note": "Shows `parallel_write_safe: False` today.",
    },
    "07": {
        "website_name": "CodeGen",
        "plain": "Generate a patch that fits the repo, validated before you see it.",
        "gain": "Preview `PR_READY.diff` + validation report; reuses existing patterns.",
        "edit": "Fill `Repository or local project` and `Change request` (GitLab role like github).",
        "expect": "`RubberDuck CodeGen: passed` or `blocked` with `BUILD_REPORT.md`.",
        "demo_note": "Shows `github_role` works; `gitlab_role` is missing (the task).",
    },
    "08": {
        "website_name": "Business Logic Check",
        "plain": "Does a stated rule actually hold in the code?",
        "gain": "Yes/no verdict with the enforcing (or missing) guard at file:line.",
        "edit": "Fill `Logic question` about `get_outdated_docs` freshness behavior.",
        "expect": "`LOGIC_CHECK.md` with branch map and verdict.",
        "demo_note": "Runs staleness logic live.",
    },
    "09": {
        "website_name": "Compare Versions",
        "plain": "Compare two implementations or refs with a structured equivalence verdict.",
        "gain": "Side-by-side divergence matrix — what changed, what stayed the same.",
        "edit": "Fill Side A / Side B (HTML vs Epub3 `prepare_writing`).",
        "expect": "`COMPARISON_REPORT.md` with equivalence verdict.",
        "demo_note": "Prints HTML vs Epub3 `globalcontext` diff live.",
    },
    "10": {
        "website_name": "Quick Check",
        "plain": "One narrow yes/no question, still evidence-bound.",
        "gain": "Fast answer with file:line proof; states what was not checked.",
        "edit": "Fill `Question` about `render_partial` in the HTML builder.",
        "expect": "`QUICK_CHECK.md` with yes/no and evidence table.",
        "demo_note": "Runs `render_partial` with and without input.",
    },
}


def fill_playground_prompt(uc_id: str, prompt: str) -> str:
    """Pre-fill library prompt for this playground repo."""
    p = prompt
    if uc_id == "01":
        p = p.replace("Target: <paste repository GitHub link here>", f"Target: {PLAYGROUND_URL}")
    elif uc_id == "02":
        p = p.replace("target=<owner/repo-or-local-path>", f"target={PLAYGROUND_GITHUB}")
    elif uc_id == "03":
        p = p.replace("Repository \t`<owner/repo>`;", f"Repository \t`{PLAYGROUND_GITHUB}`;")
        p = p.replace(
            "Bug signal \t`<EXPLAIN BUG IN PROSE>`",
            "Bug signal \t`get_aggregation in demoapp/db/query.py returns wrong count and mutates inner annotation_select_mask`",
        )
        p = p.replace("Branch/ref \t`<branch-or-ref>`;", "Branch/ref \t`main`;")
        p = p.replace("Commit \t\t`<commit-sha>`;", "Commit \t\t`latest`;")
    elif uc_id == "04":
        p = p.replace("Repository `<owner/repo>`;", f"Repository `{PLAYGROUND_GITHUB}`;")
        p = p.replace(
            "Review diff `<REVIEW_TARGET.diff>`.",
            "Review diff `fixtures/uc-04-pr-order-by-diff.md`.",
        )
        p = p.replace("Branch/ref `<branch-or-ref>`;", "Branch/ref `main`;")
        p = p.replace("Commit `<commit-sha>`;", "Commit `latest`;")
    elif uc_id == "05":
        p = p.replace("Repository `<owner/repo>`;", f"Repository `{PLAYGROUND_GITHUB}`;")
        p = p.replace(
            "Proposed change `<change description>`.",
            "Proposed change `Rename Config.config_values to Config.values in demoapp/config.py`.",
        )
        p = p.replace("Branch/ref `<branch-or-ref>`;", "Branch/ref `main`;")
        p = p.replace("Commit `<commit-sha>`;", "Commit `latest`;")
    elif uc_id == "06":
        p = p.replace("Repository `<owner/repo>`;", f"Repository `{PLAYGROUND_GITHUB}`;")
        p = p.replace(
            "Feature request `<feature goal>`.",
            "Feature request `Add --parallel-write flag to demoapp HTML builder for parallel file writes`.",
        )
        p = p.replace("Branch/ref `<branch-or-ref>`;", "Branch/ref `main`;")
        p = p.replace("Commit `<commit-sha>`;", "Commit `latest`;")
    elif uc_id == "07":
        p = p.replace(
            "Repository or local project: [FILL IN]",
            f"Repository or local project: {PLAYGROUND_GITHUB}",
        )
        p = p.replace(
            "Change request: [FILL IN USING PROSE - JUST DESCRIBE IT WITH YOUR OWN WORDS]",
            "Change request: Implement a gitlab_role in demoapp/ext/ like github_role for GitLab issue links",
        )
    elif uc_id == "08":
        p = p.replace("Repository `<owner/repo>`;", f"Repository `{PLAYGROUND_GITHUB}`;")
        p = p.replace(
            "Logic question `<specific invariant/path>`.",
            "Logic question `Does StandaloneHTMLBuilder.get_outdated_docs correctly detect all stale docs?`",
        )
        p = p.replace("Branch/ref `<branch-or-ref>`;", "Branch/ref `main`;")
        p = p.replace("Commit `<commit-sha>`;", "Commit `latest`;")
    elif uc_id == "09":
        p = p.replace("Repository `<owner/repo>`;", f"Repository `{PLAYGROUND_GITHUB}`;")
        p = p.replace("Side A `<current behavior/ref>`;", "Side A `StandaloneHTMLBuilder.prepare_writing`;")
        p = p.replace("Side B `<diff/ref>`.", "Side B `Epub3Builder.prepare_writing`.")
        p = p.replace("Branch/ref `<branch-or-ref>`;", "Branch/ref `main`;")
        p = p.replace("Commit `<commit-sha>`;", "Commit `latest`;")
    elif uc_id == "10":
        p = p.replace("Repository `<owner/repo>`;", f"Repository `{PLAYGROUND_GITHUB}`;")
        p = p.replace(
            "Question `<narrow yes/no target>`.",
            "Question `What does render_partial do in demoapp/builders/html.py and who calls it?`",
        )
        p = p.replace("Branch/ref `<branch-or-ref>`;", "Branch/ref `main`;")
        p = p.replace("Commit `<commit-sha>`;", "Commit `latest`;")
    return p.strip()
