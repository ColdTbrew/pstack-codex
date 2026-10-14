# Upstream 0.15.24 synchronization

The Codex port now tracks `cursor/plugins` commit
`1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, pstack 0.15.24.
The previous baseline was 0.15.17 at `11713c683fe4add4fd403ea880580abbc9e0875f`.
The source comparison covered 65 changed files, including the 0.15.20 changes
reported by Issue #3. The earlier check-plan patch is included in this update.

## Result

- 53 explicit-only skills and the existing 10 Astra/Sol/Luna custom-agent profiles.
- New In Your Own Words and Sharpen skills, discovery entries, and help recipes.
- Short, visual, read-only Ketchup catch-ups; audit ticks report changed state.
- Coordinator owns the playbook and task plan; delegates get absolute skill paths.
- Verification launch must become usable from empty data; seed preconditions and
  stand-in setup gaps remain explicit failures or unverified evidence.
- Autopilot verifies initial/major changes with a full independent swarm, minor
  changes with a single independent verifier, and every new head with current CI.
- Merge preparation checks trunk interactions and the actual merge result rather
  than endlessly rebasing for unrelated trunk movement. Branch leases are pinned.
- Autopilot-stack gives topology to the root and landing to the operator. Owners
  never rebase, retarget, close, merge, or arm auto-merge.
- Shipping advances bottom-up, confirms the forge's actual merged result, and
  re-checks patch evidence after child retarget/rebase. Existing authorization
  gates for merges and merge-when-ready remain explicit.
- Orchestrate computes PR frontiers from GitHub/Origin base chains, with no Graphite
  dependency. Review threads paginate and malformed pages fail closed.
- Worktree audit supports an explicit base, origin/HEAD/main/master fallback,
  single-branch fetch refspecs, and Origin/GitHub PR states. Codex active/archived
  session lookup and holds for WIP, open/draft PRs, and recent tasks remain intact.
- The remaining upstream principle/source prompt simplifications are incorporated.

## Codex adaptations

Manual source changes were reconciled semantically. Cursor model aliases and speed
suffixes are not supported Codex APIs, so job-sensitive launch guidance uses the
installed role's model, reasoning effort, and service tier. Explicit user settings
win. All current model/effort/tier values are preserved, including Luna max/fast.

Codex keeps bounded verification waves, report-only Unslop, opt-in creation of new
test files, `.agents/skills`, native task waits, and Codex session JSONL. New generic
`plugin.json` and the upstream `check-plan.test.ts` (Cursor-specific fixture) live in
provenance, not active registration/testing. The Codex checker and its Node tests
remain active. The converter now preserves them and the package test command,
and flags future updates to these boundaries for manual review.

Comment Sicko naming was already normalized; Unslop already had the narrower Codex
scope. No extra runtime changes were needed for those upstream edits. Original
Cursor-only Grok Bot and Benny remain preserved but unregistered, as before.

Independent validation found and resolved these integration issues:

- Duplicate Babysit steps obscured the owner rebase exception. The retained step
  now explicitly preserves Autopilot-full ownership and Autopilot-stack root control.
- Generic Feature/Opening-a-PR instructions now defer to mode-specific ownership.
- The plan template no longer requires an unlanded stack child to target trunk.
- Installed skill paths replace assumptions that application repositories contain
  plugin source. Codex waits replace the nonexistent loop skill. Concurrency comes
  from the active session rather than a fixed four-agent claim.
- Autonomy no longer grants unsolicited messaging permission.

## Verification

- `npm test` in the plugin scripts directory: 12 Node check-plan tests plus
  63 Bun orchestration/watcher tests, all passing. The first cold Bun invocation
  timed out in two CLI tests; warm reruns, including the default test command,
  passed without changing timeout settings or production code.
- Watcher and orchestration TypeScript strict checks passed.
- Five Python integration/preservation tests passed: real local Git worktrees,
  both forge state formats, Codex transcripts, error paths, and future-stage guards.
- All 53 skill frontmatters, explicit-invocation policies, concrete Markdown links,
  repository plugin validation, Bash syntax, and whitespace checks passed.
- All agent model/effort/service-tier values match the pre-sync Codex baseline.
- Isolated Codex CLI marketplace installation and all 10 agent installations passed.
  This was a cloud test installation; it did not update the user's local machine.
- Independent read-only workflow validation and source-coverage audit passed after
  fixes. No live GitHub merges, worktree deletion, scheduled jobs, or production
  deployments were exercised by the tests.
- Offline upstream check against the pinned checkout reports zero changed files.
  This proves source coverage bookkeeping; semantic correctness also relies on
  the validations above, not the lock alone.

Run the checks:

```bash
python -m unittest discover -s scripts/tests -v
cd plugins/pstack-codex/skills/poteto-mode/scripts
npm test
npm run typecheck
npx tsc --noEmit --strict --skipLibCheck --target esnext --module esnext \
  --moduleResolution bundler --allowImportingTsExtensions --types bun-types orch/*.ts
```

See `docs/UPSTREAM_SYNC.md` for future updates. Install the merged repository through
its marketplace, then run `scripts/install-agents.sh` and start a new Codex task.
