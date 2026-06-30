# Tutorial — UC-03: Localize and Fix Bugs

> Branch `uc-03-localize-and-fix-bugs` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

You have a bug report, traceback, or unexpected behavior and need to find the root cause.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/db/query.py` — `get_aggregation`, `rewrite_cols`
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
I have unexpected aggregation behavior in demoapp/db/query.py get_aggregation().

Using RubberDuck semantic tools:
1. load_repo on demoapp/db/query.py
2. trace_variable on annotation_select_mask, inner_query, col_cnt, has_existing_annotations
3. call_chain on rewrite_cols and get_aggregation
4. search_code for annotation_select_mask assignments
5. read_source on rewrite_cols and get_aggregation

Find all interacting bugs and propose a minimal fix with tests. Base conclusions only on tool evidence.
```

## Expected RubberDuck tool flow

`load_repo → trace_variable → call_chain → control_guards → search_code → read_source`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-03.md](docs/uc-03.md)
