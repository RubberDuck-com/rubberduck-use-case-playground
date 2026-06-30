# RubberDuck MCP setup (5 minutes)

## 1. Get a token

Sign up at [rubberduck.com](https://rubberduck.com) and copy your API token from the dashboard.

## 2. Connect Cursor (or Claude Code / Codex)

Add to `~/.cursor/mcp.json` (or project `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "rubberduck-codebase-intelligence": {
      "url": "https://codebase.rubberduck.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" }
    },
    "rubberduck-semantic-intelligence": {
      "url": "https://semantic.rubberduck.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" }
    }
  }
}
```

Restart the IDE session.

## 3. Health check

Paste in chat:

```
Verify that both MCP servers are properly configured and reachable.
Respond only with "healthy" or "unhealthy."
```

## 4. Index this repo

**GitHub (recommended for team demos):**

```
Index my GitHub repo: https://github.com/RubberDuck-com/rubberduck-use-case-playground
```

**Local project:**

```
Index my local project at: /path/to/rubberduck-use-case-playground
```

## 5. Pick a use-case branch

```bash
git checkout uc-07-generate-code   # example
```

Open `TUTORIAL.md` on that branch and paste the prompt into your AI assistant.

## Optional: upstream repos from official docs

Some tutorials reference larger public codebases (Sphinx, Django). See [docs/recommended-repos.md](docs/recommended-repos.md).
