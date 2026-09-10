# pstack-codex port notes

This package derives from `cursor/plugins/pstack` 0.15.0 under the MIT license.

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

## Upstream 0.15.0 reconciliation

The current update pins `cursor/plugins` at
`df3fb154fb982fb83f649de8646d4af6a0cb16b3`.

- Add Attack the Premise and Test Behavior, Not Implementation principles.
- Remove how critique mode and its two reference files. Preserve Codex
  explorer and explainer profiles in the shorter explanation workflow.
- Simplify why while retaining evidence coverage, citation confidence,
  connector discovery, read-only instructions, and bounded agent waves.
- Adopt upstream prose cleanup and concise PR briefing guidance.
- Preserve Codex-owned orchestration, model settings, report-only unslop,
  and explicit invocation for all 46 skills.

## Upstream 0.14.8 reconciliation

The update pins `cursor/plugins` at
`93b00b89ef425a9c1bac0d0b317dfc49c930ac99`.

- PR workflows use GitHub CLI by default and Origin when available, without
  requiring Graphite. Stacks land bottom-up, with base-to-head patch receipts
  and current-head CI checks after rebases.
- Autopilot-full and multi-phase plans compare the load-bearing scenario on
  trunk and head. Missing trunk features require explicit absolute budgets,
  not ratios between unlike scenarios.
- Upstream Fable model changes in architect, arena, how, interrogate,
  poteto-mode, bug-fix, perf-issue, hillclimb, reflect, setup-pstack, and why
  retain the configured Codex Astra/Sol/Terra/Luna roles and reasoning levels.
- The new explicit-invocation flags for how, why, unslop, and TypeScript
  guidance map to `agents/openai.yaml`. TypeScript file scope remains in
  the skill description; Cursor's `paths` frontmatter is not emitted.
- The report-only scope of unslop, Codex waits, session handoffs, and
  concurrency limits remain intact.
- The relocated make-bot-ui skill remains under
  `upstream-cursor-only/grokbot/make-bot-ui` because it depends on Cursor
  webhook routines and secret-request APIs. Its new source location does
  not register it as a Codex skill. The upstream logo is exposed through
  the Codex plugin interface.

## Invocation policy

All 46 registered skills use `allow_implicit_invocation: false`. Invoke them
explicitly with `$pstack-codex:<skill-name>`. The upstream converter applies
this policy to every skill, including skills added by future updates.
