# Rubber Duck Playground

**Hands-on training for every RubberDuck workflow.**

This repository is the official playground for learning how RubberDuck works in real projects. You get runnable labs, a shared demo application, copy-paste MCP prompts, and guided branches for all ten use cases from the [RubberDuck documentation](https://rubberduck.com/#docs).

> **New here?** Start with **[GUIDE.md](GUIDE.md)** — it walks you through setup, your first lab, and how to use RubberDuck MCP end to end.

---

## What this repo is for

| Audience | How to use it |
|----------|----------------|
| **Engineers learning RubberDuck** | Run a lab locally, then repeat the same task with MCP and compare results |
| **Team leads / demos** | Pick one use case, run verify in 30 seconds, paste the prompt live in Cursor |
| **Onboarding** | Assign UC 01 → UC 10 over a sprint; each lab has a verify step and expected outcomes |

You are not reading slides. Each use case ships with **code you can execute**, **scripts that prove the lab works**, and **prompts tuned to this codebase**.

---

## Quick start (under one minute)

```bash
git clone https://github.com/RubberDuck-com/rubberduck-use-case-playground.git
cd rubberduck-use-case-playground
python scripts/run-lab.py --uc 02 --verify
```

Windows:

```powershell
.\scripts\setup.ps1 -Uc 02 -Verify
```

That command creates a virtual environment (first run only), runs the lab smoke test, and prints the RubberDuck **index** command plus the **prompt** to paste in your IDE.

### Try the live security lab (UC 02)

```bash
python scripts/run-lab.py --uc 02 --start-server
```

Open [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs), then run a RubberDuck security audit on the code.

---

## The ten use cases

| # | Name | What you practice |
|---|------|-------------------|
| 01 | Understand Your Code | Trace entry points and map how the app boots |
| 02 | Codebase Audit | Find security sinks in config and the HTTP API |
| 03 | Localize and Fix Bugs | Hunt ORM aggregation bugs with pytest |
| 04 | Code Review | Approve or block a realistic PR diff |
| 05 | Change Impact Analysis | Plan a rename across consumers |
| 06 | Plan a New Feature | Design `--parallel-write` from failing tests |
| 07 | Generate Code That Fits | Implement a GitLab role module to pass tests |
| 08 | Check Code Logic | Review documentation freshness logic |
| 09 | Compare Versions | Diff HTML vs Epub3 builder behavior |
| 10 | Quick Check | Fast assessment of a single function |

Full walkthrough, MCP setup, and branch workflow: **[GUIDE.md](GUIDE.md)**.

---

## Repository layout

| Area | Purpose |
|------|---------|
| `labs/` | One folder per use case with README, verify script, and tasks |
| `demoapp/` | Shared Python codebase (~800 lines): CLI, builders, ORM, HTTP API |
| `scripts/run-lab.py` | One command to install, verify, print prompts, start servers |
| `docs/` | Official prompts aligned with rubberduck.com |
| Git branches `uc-01` … `uc-10` | Focused tutorial on each branch (`TUTORIAL.md`) |

---

## MCP setup

Connect RubberDuck Codebase Intelligence and Semantic Intelligence in Cursor (or Claude Code). Step-by-step: **[SETUP.md](SETUP.md)**.

---

## Run all tests

```bash
pip install -r requirements.txt
pytest tests labs -q
```

Some UC 06 and UC 07 tests **fail on purpose** until you complete the training task.

---

## License

MIT — see [LICENSE](LICENSE).
