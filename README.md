# Rubber Duck Playground

Hands-on training for [RubberDuck](https://rubberduck.com): launch a real demo app, copy UC-01…UC-10 prompts, and run them in Cursor / Claude with RubberDuck MCP.

<a href="https://trendshift.io/repositories/98700?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-98700" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/98700/daily?language=CSS" alt="RubberDuck-com%2Frubberduck-use-case-playground | Trendshift" width="250" height="55"/></a>

<a href="https://trendshift.io/repositories/98700?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-98700" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/98700/weekly?language=CSS" alt="RubberDuck-com%2Frubberduck-use-case-playground | Trendshift" width="250" height="55"/></a>

<a href="https://trendshift.io/repositories/98700?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-98700" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/98700/monthly?language=CSS" alt="RubberDuck-com%2Frubberduck-use-case-playground | Trendshift" width="250" height="55"/></a>

## 60-second start

1. **Git clone**
   ```bash
   git clone https://github.com/RubberDuck-com/rubberduck-use-case-playground.git
   cd rubberduck-use-case-playground/demo-projects
   ```

2. **Open the hub** — `start-hub.bat` (Windows) or `./start-hub.sh` (Linux/macOS) → http://127.0.0.1:5055/

3. **Welcome** — pick Rubber Duck Pizzeria

4. **Launch** — live console + health diagram (venv → deps → DB → API → UI)

5. **Connect RubberDuck MCP** — **Connect MCP** tab in the hub

6. **Generate prompts** — UC-01…UC-10, **What to expect**, **Copy prompt**

Full walkthrough: [GUIDE.md](GUIDE.md)

---

## What this is

| Piece | What it is |
|-------|------------|
| `demo-projects/` | Hub dashboard (`start-hub.bat` / `start-hub.sh`) |
| `demo-projects/rubberduck_pizzeria-demoapp/` | Restaurant admin UI + kitchen API with intentional lab sinks |
| Hub **Generate prompts** | Project-specific UC-01…UC-10 prompts + expected-outcome bullets |

The older `demoapp/` / `labs/` / `run-lab.py` stack was removed so the repo has **one** clear path: the demo-projects hub.

---

## The ten use cases

| # | Name | What RubberDuck should surface on the pizzeria demo |
|---|------|------------------------------------------------------|
| 01 | Understand Your Code | Atlas: `main.py` → `create_app`, routes, `/api`, `init_db` |
| 02 | Security Audit | SQLi, XSS, pickle/exec, IDOR, CMDi, SSTI, BAC, … |
| 03 | Localize and Fix Bugs | Discount / `get_aggregation` mask bug |
| 04 | Code Review | Hostile review of order_by → raw SQL near search |
| 05 | Change Impact | Rename `config_values` blast radius |
| 06 | Plan a New Feature | Plan parameterized `safe_search_customers` |
| 07 | Generate Code That Fits | Implement safe search + tests |
| 08 | Check Code Logic | Does `include_discount=True` apply? |
| 09 | Compare Versions | Raw SQL search vs parameterized search |
| 10 | Quick Check | What `get_aggregation` returns (short + evidence) |

Details live in the hub under **What to expect** for each UC.

---

## MCP setup

[SETUP.md](SETUP.md) — connect Codebase Intelligence + Semantic Intelligence in Cursor.

Index the pizzeria demo once per session, then paste the prompt copied from the hub.

---

## License

MIT — see [LICENSE](LICENSE).
