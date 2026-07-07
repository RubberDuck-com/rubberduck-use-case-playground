# Rubber Duck Playground

Hands-on training for [RubberDuck](https://rubberduck.com): **one codebase**, **ten workflows**, **real output** — not slides.

## 60-second start

```bash
git clone https://github.com/RubberDuck-com/rubberduck-use-case-playground.git
cd rubberduck-use-case-playground
python scripts/run-lab.py --uc 02
```

That single command:

1. Installs deps (first run only)
2. **Runs real demo code** (e.g. shows SQL built from user input for UC-02)
3. Prints the **pre-filled RubberDuck prompt** to paste in Cursor

Connect RubberDuck MCP first — see [SETUP.md](SETUP.md).

**Full walkthrough:** [docs/HOW_TO_TEST.md](docs/HOW_TO_TEST.md)

---

## What this is

| Piece | What it is |
|-------|------------|
| `demoapp/` | Shared Python app (~800 lines) with deliberate bugs, security sinks, and extension tasks |
| `labs/uc-01` … `uc-10` | One folder per exercise (verify scripts, focus paths) |
| `docs/uc-01.md` … `uc-10.md` | Plain-English explanation + **playground-ready prompt** (repo pre-filled) |
| `scripts/run-lab.py` | One command: demo + prompt |
| `scripts/demo.py` | Low-level demo runner (used by `run-lab.py`) |

**Stay on `main`.** The `uc-XX-*` Git branches are legacy and missing current labs — do not use them.

---

## The ten use cases

| # | Name | Terminal demo | RubberDuck finds |
|---|------|---------------|------------------|
| 01 | Understand Your Code | Builds HTML docs | Entry points, architecture |
| 02 | Security Audit | SQL injection payload | Sinks in API + config |
| 03 | Localize and Fix Bugs | ORM aggregation bug | Root cause in `query.py` |
| 04 | Code Review | Compiler order-by logic | PR verdict + blast radius |
| 05 | Change Impact | Config dict rename scope | All callers |
| 06 | Plan a New Feature | Missing parallel-write flag | Tests-first plan |
| 07 | Generate Code That Fits | GitHub role works, GitLab missing | Validated patch |
| 08 | Check Code Logic | Staleness check output | Logic verdict |
| 09 | Compare Versions | HTML vs Epub3 diff | Equivalence report |
| 10 | Quick Check | `render_partial` behavior | Fast yes/no + evidence |

Expected RubberDuck output: [docs/EXPECTED_OUTCOMES.md](docs/EXPECTED_OUTCOMES.md)

---

## Commands

```bash
# Default: live demo + prompt (recommended)
python scripts/run-lab.py --uc 03

# UC-02: start the API server
python scripts/run-lab.py --uc 02 --server

# Optional: pytest smoke test only
python scripts/run-lab.py --uc 03 --verify

# Prompt only (skip demo)
python scripts/run-lab.py --uc 01 --no-run
```

Windows shortcut:

```powershell
.\scripts\setup.ps1 -Uc 02
```

---

## MCP setup

[SETUP.md](SETUP.md) — connect Codebase Intelligence + Semantic Intelligence in Cursor.

Index once per session:

```
Index my local project at: <full path to this repo>
```

Then paste the prompt from `docs/uc-XX.md` or from `run-lab.py` output.

---

## Run all tests

```bash
pip install -r requirements.txt
pytest tests labs -q
```

UC-06 and UC-07 tests **fail on purpose** until you complete the training task.

---

## License

MIT — see [LICENSE](LICENSE).
