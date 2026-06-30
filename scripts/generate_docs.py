"""Generate docs/uc-*.md and per-branch TUTORIAL.md files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

USE_CASES = [
    {
        "id": "01",
        "slug": "uc-01-understand-your-code",
        "title": "Understand Your Code",
        "when": "You're new to a codebase, or need to understand how a specific feature works.",
        "prompt": """Using the RubberDuck semantic intelligence tools, give me a complete overview of this codebase.
Show me:
1. All major classes and functions (use symbols_overview)
2. The main entry points
3. How the request/data flows through the system (use call_chain on the main entry points)

Base your answer ONLY on the analysis tools, not on general knowledge.""",
        "focus": "`demoapp/cmd/build.py` (main), `demoapp/application.py` (Application)",
        "workflow": "list_repos → load_repo → search_code → load_code → symbols_overview → call_chain → trace_variable",
    },
    {
        "id": "02",
        "slug": "uc-02-codebase-audit",
        "title": "Codebase Audit",
        "when": "You want to check for security vulnerabilities or quality issues in your code.",
        "prompt": """Using RubberDuck semantic intelligence tools, perform a security-sensitive path audit on my loaded code:

1. First, find all entry points that accept external input (use search_code to find HTTP handlers, API endpoints, form handlers, user input processing)
2. For each entry point, trace the data flow of the input variable (use trace_variable)
3. Search for dangerous sinks: exec, eval, subprocess, SQL queries, file operations, shell commands (use search_code with regex patterns)
4. For any dangerous sink found, check if user input can reach it (use call_chain to trace the path from entry to sink)

Focus ONLY on the loaded code scope. If no dangerous path is found in the loaded files, say so honestly — do not speculate about code outside the loaded scope.

Report findings as:
- Entry point (file, line)
- Data flow path
- Sink (file, line, type of danger)
- Risk level (high/medium/low)""",
        "focus": "`demoapp/config.py` — `eval_config_file`, `from_pickle`",
        "workflow": "codebase_audit → load_repo → search_code → read_source → trace_variable → call_chain",
    },
    {
        "id": "03",
        "slug": "uc-03-localize-and-fix-bugs",
        "title": "Localize and Fix Bugs",
        "when": "You have a bug report, traceback, or unexpected behavior and need to find the root cause.",
        "prompt": """I have unexpected aggregation behavior in demoapp/db/query.py get_aggregation().

Using RubberDuck semantic tools:
1. load_repo on demoapp/db/query.py
2. trace_variable on annotation_select_mask, inner_query, col_cnt, has_existing_annotations
3. call_chain on rewrite_cols and get_aggregation
4. search_code for annotation_select_mask assignments
5. read_source on rewrite_cols and get_aggregation

Find all interacting bugs and propose a minimal fix with tests. Base conclusions only on tool evidence.""",
        "focus": "`demoapp/db/query.py` — `get_aggregation`, `rewrite_cols`",
        "workflow": "load_repo → trace_variable → call_chain → control_guards → search_code → read_source",
    },
    {
        "id": "04",
        "slug": "uc-04-code-review",
        "title": "Code Review",
        "when": "You need to review a code change — PR, colleague's code, or your own before merging.",
        "prompt": """Review the PR described in fixtures/uc-04-pr-order-by-diff.md against demoapp/db/query.py Compiler.get_order_by.

Using RubberDuck:
1. Prove whether annotation_select is always a subset of annotations
2. Trace is_ref to get_group_by and get_extra_select
3. search_code for annotation_select_mask and set_annotation_mask

Verdict: APPROVE or BLOCK with evidence (file:line).""",
        "focus": "`fixtures/uc-04-pr-order-by-diff.md` + `demoapp/db/query.py`",
        "workflow": "load_repo → analyze_code → read_source → search_code → call_chain",
    },
    {
        "id": "05",
        "slug": "uc-05-change-impact-analysis",
        "title": "Change Impact Analysis",
        "when": "Before making a change, you need to know what will break and what tests to run.",
        "prompt": """I want to rename Config.config_values to Config.values in demoapp/config.py.

Using RubberDuck, analyze the impact:
1. Use plan_change with description of what I want to change
2. Find all callers (use call_chain direction="callers")
3. Find downstream functions (use call_chain direction="callees")
4. Check shared variables (use shared_variables)
5. Trace key variables (use trace_variable)

Report:
- Risk level with reasoning
- Affected functions (file, line, dependency type)
- Recommended change order
- What tests to run""",
        "focus": "`demoapp/config.py` — rename `config_values`",
        "workflow": "plan_change → search_code → call_chain → shared_variables → trace_variable",
    },
    {
        "id": "06",
        "slug": "uc-06-plan-new-feature",
        "title": "Plan a New Feature",
        "when": "You want to add a new feature, preferably tests-first.",
        "prompt": """I want to add a --parallel-write flag for parallel file writing in demoapp builders.

Using RubberDuck, help me plan tests-first:

Step 1 — Understand existing patterns:
1. Search for similar functionality (use search_code, analyze_code)
2. Find test directory and patterns
3. Identify where this feature belongs (use symbols_overview)

Step 2 — Design tests first:
Write test cases BEFORE implementation, following existing conventions.

Step 3 — Implementation plan:
- Which files to modify
- What new code to add
- What NOT to add (keep minimal)

Do NOT generate implementation code yet — only tests and plan.""",
        "focus": "`demoapp/builders/html.py` — `write_doc`, parallel patterns",
        "workflow": "search_code → symbols_overview → read_source → call_chain → analyze_code",
    },
    {
        "id": "07",
        "slug": "uc-07-generate-code",
        "title": "Generate Code That Fits (codegen)",
        "when": "You need to write code that fits seamlessly into an existing codebase.",
        "prompt": """I need to implement a :gitlab: role for linking to GitLab issues, similar to demoapp/ext/github.py.

Using RubberDuck, generate code that fits this codebase:
1. Find similar patterns (use search_code, analyze_code)
2. Identify the right location (use symbols_overview, find_files)
3. Check dependencies (use call_chain, trace_variable on similar functions)
4. Generate minimal code that reuses existing patterns and naming
5. Generate a matching test

Show me the diff and explain design choices.""",
        "focus": "`demoapp/ext/github.py` — extend with `gitlab.py` + test",
        "workflow": "search_code → read_source → symbols_overview → call_chain → analyze_code",
    },
    {
        "id": "08",
        "slug": "uc-08-check-code-logic",
        "title": "Check Code Logic",
        "when": "Verify correctness of complex logic — conditions, gaps, control flow.",
        "prompt": """Verify demoapp/builders/html.py StandaloneHTMLBuilder.get_outdated_docs():

1. read_source on get_outdated_docs
2. trace_variable on template_mtime, build_info, buildinfo
3. call_chain on get_outdated_docs
4. control_guards on each branch condition line
5. search_code for other builders' get_outdated_docs implementations

Report all branches, gaps (static/theme/css/extension changes), with formal evidence.""",
        "focus": "`demoapp/builders/html.py` — `get_outdated_docs`",
        "workflow": "load_repo → read_source → trace_variable → call_chain → control_guards → search_code",
    },
    {
        "id": "09",
        "slug": "uc-09-compare-versions",
        "title": "Compare Versions",
        "when": "Compare implementations across classes or versions for compatibility risks.",
        "prompt": """Compare prepare_writing between StandaloneHTMLBuilder and Epub3Builder in demoapp/builders/html.py.

Using RubberDuck:
1. read_source both methods
2. compare_snapshots or analyze_code for structural diff
3. search_code for all prepare_writing implementations
4. shared_variables and call_chain on both

Report what Epub3 adds, shared state, and compatibility risks.""",
        "focus": "`demoapp/builders/html.py` — HTML vs Epub3 `prepare_writing`",
        "workflow": "load_repo → read_source → compare_snapshots → search_code → call_chain",
    },
    {
        "id": "10",
        "slug": "uc-10-quick-check",
        "title": "Quick Check",
        "when": "30-second assessment of an unfamiliar method — what it does, who depends on it, risk.",
        "prompt": """Never seen this code before. Give a 30-second assessment of render_partial in demoapp/builders/html.py:

1. read_source(function_name="render_partial")
2. call_chain(method="render_partial") — callers and callees
3. search_code(pattern="render_partial")

Report: what it does, who depends on it, risk level, with file:line evidence.""",
        "focus": "`demoapp/builders/html.py` — `render_partial`",
        "workflow": "load_repo → read_source → call_chain → search_code",
    },
]


def write_uc_docs() -> None:
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    for uc in USE_CASES:
        path = docs / f"uc-{uc['id']}.md"
        path.write_text(
            f"# UC-{uc['id']}: {uc['title']}\n\n"
            f"**When to use:** {uc['when']}\n\n"
            f"**Focus in this repo:** {uc['focus']}\n\n"
            f"**Typical MCP workflow:** {uc['workflow']}\n\n"
            f"## Prompt (copy into Cursor / Claude Code)\n\n"
            f"```\n{uc['prompt'].strip()}\n```\n\n"
            f"Full narrative and with/without MCP comparison: "
            f"[rubberduck.com documentation](https://rubberduck.com/#docs)\n",
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
        f"```\n{uc['prompt'].strip()}\n```\n\n"
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
    subprocess.run(["git", "checkout", "main"], cwd=ROOT, check=True)
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
