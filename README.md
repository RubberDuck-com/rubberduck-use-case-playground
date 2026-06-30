# RubberDuck Use Case Playground

Public tutorial repo for all **10 RubberDuck product use cases** plus **codegen** (UC-07), matching the official docs at [rubberduck.com/#docs](https://rubberduck.com/#docs).

One repository. **One branch per use case.** Copy-paste prompts. Small sample codebase included so you do not need to pick a random GitHub project.

## Quick start

1. [Set up RubberDuck MCP](SETUP.md) (token + Cursor config).
2. Index this repo (GitHub or local path).
3. Check out a use-case branch and open **`TUTORIAL.md`**.
4. Paste the prompt into your AI assistant with RubberDuck connected.

```bash
git clone https://github.com/RubberDuck-com/rubberduck-use-case-playground.git
cd rubberduck-use-case-playground
git checkout uc-01-understand-your-code
```

## Branches (10 use cases + codegen)

| Branch | UC | Title |
|--------|-----|--------|
| `uc-01-understand-your-code` | UC-01 | Understand Your Code |
| `uc-02-codebase-audit` | UC-02 | Codebase Audit |
| `uc-03-localize-and-fix-bugs` | UC-03 | Localize and Fix Bugs |
| `uc-04-code-review` | UC-04 | Code Review |
| `uc-05-change-impact-analysis` | UC-05 | Change Impact Analysis |
| `uc-06-plan-new-feature` | UC-06 | Plan a New Feature |
| `uc-07-generate-code` | UC-07 | **Generate Code That Fits (codegen)** |
| `uc-08-check-code-logic` | UC-08 | Check Code Logic |
| `uc-09-compare-versions` | UC-09 | Compare Versions |
| `uc-10-quick-check` | UC-10 | Quick Check |

`main` holds the full index (this file) and shared sample code.

## What's in the repo

| Path | Purpose |
|------|---------|
| `demoapp/` | Small Python sample (builder + config + ORM-style bugs) |
| `docs/uc-01.md` … `uc-10.md` | Per-UC prompts and workflow hints |
| `docs/recommended-repos.md` | Optional Sphinx/Django targets from official docs |
| `fixtures/` | PR snippets and exercise inputs |
| `tests/` | Baseline tests for UC-06 / UC-07 |
| `TUTORIAL.md` | **On each UC branch** — start here |

## Sample code map

| UC | Start here in `demoapp/` |
|----|--------------------------|
| UC-01 | `cmd/build.py`, `application.py` |
| UC-02 | `config.py` |
| UC-03 | `db/query.py` |
| UC-04 | `db/query.py` + `fixtures/uc-04-pr-order-by-diff.md` |
| UC-05 | `config.py` (`config_values`) |
| UC-06 | `builders/html.py` |
| UC-07 | `ext/github.py` (add `gitlab.py`) |
| UC-08 | `builders/html.py` (`get_outdated_docs`) |
| UC-09 | `builders/html.py` (HTML vs Epub3) |
| UC-10 | `builders/html.py` (`render_partial`) |

## Run tests

```bash
python -m pip install pytest
python -m pytest tests/ -q
```

## Official documentation

Prompts and with/without MCP comparisons are maintained on [rubberduck.com](https://rubberduck.com/#docs). This repo is the **hands-on lab** PiGrieco asked for in the 29 Jun 2026 standup.

## License

MIT — see [LICENSE](LICENSE).
