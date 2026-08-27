# pstack-codex port notes

This package derives from `cursor/plugins/pstack` 0.14.4 under the MIT license.

The Codex port packages the reusable skills as a Codex plugin and provides
standalone custom-agent TOML files under `codex-agents/`. Cursor-only Grok Bot
webhook and Benny automation sources are retained under `upstream-cursor-only/`
for provenance but are not registered with Codex.

Runtime mappings:

- Cursor `Task` calls -> Codex subagent workflows.
- Cursor model rules -> Codex custom-agent TOML profiles.
- `.cursor/skills` -> `.agents/skills`.
- Cursor `/loop` -> Codex wait, monitoring, long-running goal, or automation tools.
- Cursor control skills -> Codex browser automation and terminal tooling.
- Plugin skill mentions -> `$pstack-codex:<skill-name>` in Codex prompts.
- Cursor transcript lookup -> Codex session JSONL under `~/.codex/sessions`
  and `~/.codex/archived_sessions`.

The exact upstream commit and update procedure are tracked by the containing
repository's `upstream-lock.json` and `docs/UPSTREAM_SYNC.md`.
