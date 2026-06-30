# Recommended upstream repos (optional)

This playground includes a small `demoapp/` package so you can run every workflow without cloning megarepos. For results closest to [rubberduck.com docs](https://rubberduck.com/#docs), index these public projects instead.

| UC | Title | Suggested repo | Focus path |
|----|-------|----------------|------------|
| UC-01 | Understand Your Code | [sphinx-doc/sphinx](https://github.com/sphinx-doc/sphinx) | `sphinx/cmd/build.py`, `sphinx/application.py` |
| UC-02 | Codebase Audit | sphinx-doc/sphinx | `sphinx/config.py` (exec sink), builders |
| UC-03 | Localize and Fix Bugs | [django/django](https://github.com/django/django) | `django/db/models/sql/query.py` |
| UC-04 | Code Review | django/django | `django/db/models/sql/compiler.py` |
| UC-05 | Change Impact | sphinx-doc/sphinx | `sphinx/config.py` (`config_values`) |
| UC-06 | Plan New Feature | sphinx-doc/sphinx | `sphinx/builders/` |
| UC-07 | Generate Code (codegen) | sphinx-doc/sphinx | `sphinx/ext/` |
| UC-08 | Check Code Logic | sphinx-doc/sphinx | `sphinx/builders/html.py` (`get_outdated_docs`) |
| UC-09 | Compare Versions | sphinx-doc/sphinx | HTML vs Epub3 `prepare_writing` |
| UC-10 | Quick Check | sphinx-doc/sphinx | `render_partial` in HTML builder |

**This repo mapping (faster, self-contained):**

| UC | Path in this repo |
|----|-------------------|
| UC-01 | `demoapp/cmd/build.py`, `demoapp/application.py` |
| UC-02 | `demoapp/config.py` |
| UC-03 | `demoapp/db/query.py` (`get_aggregation`) |
| UC-04 | `demoapp/db/query.py` (`Compiler`) + `fixtures/uc-04-pr-order-by-diff.md` |
| UC-05 | `demoapp/config.py` — try renaming `config_values` → `values` |
| UC-06 | Add `--parallel-write` to `demoapp/builders/html.py` |
| UC-07 | Implement a role in `demoapp/ext/github.py` |
| UC-08 | `demoapp/builders/html.py` — `get_outdated_docs` |
| UC-09 | Compare `StandaloneHTMLBuilder` vs `Epub3Builder.prepare_writing` |
| UC-10 | `demoapp/builders/html.py` — `render_partial` |
