# How to test each use case

This repo is **one project** (`demoapp/`) with **ten exercises**. You do not switch Git branches — stay on `main`.

## The 2-step loop (every UC)

### Step 1 — Terminal (30 seconds)

```bash
python scripts/run-lab.py --uc 01
```

Replace `01` with `02` … `10`. This:

1. Installs dependencies on first run (`.venv`)
2. **Runs real code** so you see the behavior (including planted bugs)
3. Prints the **pre-filled RubberDuck prompt** to paste in Cursor

**UC-02 only — live API (optional):**

```bash
python scripts/run-lab.py --uc 02 --server
```

Open http://127.0.0.1:8080/docs and try the search endpoint.

**Smoke tests (optional, for CI-minded folks):**

```bash
python scripts/run-lab.py --uc 03 --verify
```

### Step 2 — Cursor (RubberDuck MCP)

1. Connect RubberDuck MCP in Cursor — see [SETUP.md](../SETUP.md)
2. Index once: `Index my local project at: <full path to this repo>`
3. Open `docs/uc-XX.md` **or** copy the prompt printed by `run-lab.py`
4. Paste the entire **Playground prompt** block into chat
5. Compare RubberDuck’s answer with what Step 1 showed you

## What to expect

| UC | Terminal shows | RubberDuck should find |
|----|----------------|------------------------|
| 01 | Builds `sampledocs/_build/index.html` | Entry points, call chains, architecture |
| 02 | SQL built from user input | Sinks in `api/server.py`, `config.py` |
| 03 | Wrong aggregation count + mutated mask | Root cause in `db/query.py` |
| 04 | Order-by / group-by compiler output | PR review verdict on order-by change |
| 05 | `config_values` vs `values` dicts | All callers of `Config` |
| 06 | `parallel_write_safe: False` | Tests-first plan for `--parallel-write` |
| 07 | `github_role` works, `gitlab_role` missing | Patch plan for GitLab role module |
| 08 | Staleness logic output | Verdict on `get_outdated_docs` |
| 09 | HTML vs Epub3 `globalcontext` diff | Equivalence report |
| 10 | `render_partial` behavior | Yes/no with file:line evidence |

Details: [EXPECTED_OUTCOMES.md](EXPECTED_OUTCOMES.md)

## Per-use-case docs

| UC | Doc | Website name |
|----|-----|--------------|
| 01 | [uc-01.md](uc-01.md) | Codebase Atlas |
| 02 | [uc-02.md](uc-02.md) | Security Audit |
| 03 | [uc-03.md](uc-03.md) | Bug Localization |
| 04 | [uc-04.md](uc-04.md) | PR Review |
| 05 | [uc-05.md](uc-05.md) | Change Impact |
| 06 | [uc-06.md](uc-06.md) | Feature Planning |
| 07 | [uc-07.md](uc-07.md) | CodeGen |
| 08 | [uc-08.md](uc-08.md) | Business Logic Check |
| 09 | [uc-09.md](uc-09.md) | Compare Versions |
| 10 | [uc-10.md](uc-10.md) | Quick Check |

## Common mistakes

- **Switching to `uc-XX` branches** — those branches are stale. Use `main` only.
- **Editing the compressed prompt text** — only change the input fields (repo, bug, question). The shorthand is intentional.
- **Skipping Step 1** — you won’t know if RubberDuck found the real issue or hallucinated.
- **Using `--verify` as the main flow** — it runs pytest smoke tests; `--run` (default) shows human-readable behavior.

## Record a demo video

See [RECORDING_SCRIPT.md](RECORDING_SCRIPT.md) for a shot-by-shot script.
