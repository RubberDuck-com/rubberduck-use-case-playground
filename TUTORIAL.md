# Tutorial — UC-07: Generate Code That Fits (codegen)

> Branch `uc-07-generate-code` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

You need to write code that fits seamlessly into an existing codebase.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/ext/github.py` — extend with `gitlab.py` + test
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
I need to implement a :gitlab: role for linking to GitLab issues, similar to demoapp/ext/github.py.

Using RubberDuck, generate code that fits this codebase:
1. Find similar patterns (use search_code, analyze_code)
2. Identify the right location (use symbols_overview, find_files)
3. Check dependencies (use call_chain, trace_variable on similar functions)
4. Generate minimal code that reuses existing patterns and naming
5. Generate a matching test

Show me the diff and explain design choices.
```

## Expected RubberDuck tool flow

`search_code → read_source → symbols_overview → call_chain → analyze_code`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-07.md](docs/uc-07.md)
