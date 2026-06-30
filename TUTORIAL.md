# Tutorial — UC-08: Check Code Logic

> Branch `uc-08-check-code-logic` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

Verify correctness of complex logic — conditions, gaps, control flow.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/builders/html.py` — `get_outdated_docs`
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
Verify demoapp/builders/html.py StandaloneHTMLBuilder.get_outdated_docs():

1. read_source on get_outdated_docs
2. trace_variable on template_mtime, build_info, buildinfo
3. call_chain on get_outdated_docs
4. control_guards on each branch condition line
5. search_code for other builders' get_outdated_docs implementations

Report all branches, gaps (static/theme/css/extension changes), with formal evidence.
```

## Expected RubberDuck tool flow

`load_repo → read_source → trace_variable → call_chain → control_guards → search_code`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-08.md](docs/uc-08.md)
