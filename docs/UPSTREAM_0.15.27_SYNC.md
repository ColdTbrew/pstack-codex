# Upstream 0.15.27 sync

Source: cursor/plugins `6b78e9f4e46c75d1697d837e51f07c2692e60b24`,
following the reviewed Codex 0.15.24 port at `11eca70`.

## Reconciliation

- `.cursor-plugin/plugin.json` and `plugin.json`: retain raw manifests as provenance;
  advance the Codex manifest and lock together.
- `README.md`: retain raw source, add formal verification discovery to both Codex
  READMEs, and advance the inventory to 54 skills.
- `correct`: adopt observable behavioral test criteria.
- `ketchup`: include all pending decisions, with per-item evidence and risk;
  embed existing media and preserve Codex rendering capability discovery.
- `poteto-help`: route formal verification questions and update setup and Ketchup.
- `poteto-mode`: reconcile premise, root-cause, and behavioral-test summaries;
  the upstream name normalization already matches the Codex name.
- `setup-pstack`: offer missing app and formal verification skills once each;
  generation requires acceptance and respects test-file creation policy.
- `swarm`: adopt upstream prose removal but retain Codex bounded-wave sizing.
- New formal verification skill: retain verification scope, counterexamples,
  mutation checks, report-only findings, and explicit invocation. Add the existing
  Codex opt-in policy for new tests, fixtures, and test-only helpers.
- Other automatic changes update principles, TypeScript guidance, Sharpen,
  Interrogate references, and the formal verification recipe.
- Claude Code adapter, Cursor guides, manifests, and bot UI stay under
  `upstream-cursor-only/`; they are not executable Codex instructions.
- All 10 agent profiles are unchanged from the reviewed 0.15.24 port.

## Validation

- Existing Python sync and worktree-audit tests: 5 passed.
- Existing Node plan checker tests: 12 passed.
- Existing Bun orchestration and PR-watcher tests: 65 passed.
- PR-watcher strict typecheck passed. Orchestration CLI strict typecheck passed
  with `--allowImportingTsExtensions` for Bun's `.ts` imports.
- The package declares `bun-types` but its config requests `bun`; local validation
  installed `@types/bun` without saving a package or lock change. The missing type
  dependency is pre-existing; this documentation update does not change tooling.
- Built-in sync plugin validator and all 54 skill validators passed.
- All 54 invocation policies remain explicit-only; all 10 TOML profiles parse.
- `git diff --check` passed. No new test files were authored in this update.

A fresh Codex task is required to check skill loading in a new session.
