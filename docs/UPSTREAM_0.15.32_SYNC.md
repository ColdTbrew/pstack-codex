# Upstream 0.15.32 sync

Source: cursor/plugins `9580c23696ac8d7abed0c166f2f9918800afb819`,
following the reviewed Codex 0.15.27 port at `cac37b8`.

## Reconciliation

- Add Statechart, Ketchup Video, and Maintain Formal Verification Skill. Both
  Codex READMEs and Poteto Help now describe all 57 explicit-only skills.
- Sharpen now returns a rewritten prompt without executing the task. Update
  discovery text and retain the upstream guide changes as provenance.
- Formal verification records covered files/functions and a sync commit, routes
  TLA+ results through Statechart, and offers the maintenance workflow.
- Preserve the opt-in policy for new tests, fixtures, and test-only helpers in
  all three formal verification workflows. Mark these skill entrypoints as
  Codex-owned so future staging cannot silently remove that policy.
- Reflect shows the approved project/user skill destination, copies the skill
  there, and edits the copy rather than an installed plugin cache. It does not
  create a PR or push as part of reflection.
- Preserve Codex wave sizing, model routing, and all 10 custom-agent profiles.
  Adopt Swarm's result-table clarification; its numbering already includes the
  Codex wave-sizing step.
- Plan checking handles matching multi-backtick code spans without hiding
  punctuation outside them. Port the upstream cases into the existing Node
  regression file while keeping Codex plan and concurrency requirements.
- Orchestration prefers a sole open PR over closed/merged branch history and
  continues to reject multiple active PRs. Preserve the Codex integration-base
  behavior and its existing regression cases.
- PR watching uses fork identity in stack discovery and caps polling/backoff
  sleeps at the remaining timeout, including queued stacks and query retries.
- Worktree auditing selects GNU/BSD timestamp flags once, while preserving
  active and archived Codex transcript lookup and forge/base handling.
- Raw Cursor manifests, guide changes, and the Cursor plan-checking fixture
  remain under `upstream-cursor-only/`.

## Test-file boundary

The upstream Statechart test suite and four Mermaid fixtures were fetched into
ignored `.sync/` staging for validation. They are not added to the port because
the session did not opt in to new test files. Existing tracked regression files
were updated. The 21 shipped Statechart modules match upstream byte for byte.

## Validation

- Existing Python sync and worktree-audit tests: 5 passed.
- Existing Codex Node plan-checker tests, including the upstream additions:
  14 passed.
- Existing Bun orchestration and PR-watcher tests, including the upstream
  additions: 77 passed.
- Strict PR-watcher and orchestration CLI typechecks passed.
- Upstream Statechart suite: 149 cases passed across the full run and a
  targeted rerun; one real-mise integration case was skipped because validation
  supplied TLC directly. The full run initially passed 146 cases and failed
  three installation-mock cases: their mock expects a file named `tla2tools.jar`
  beside the supplied JAR. Providing the same verified JAR under that name made
  all three pass without changing source or tests. Actual mise download and
  installation were not exercised.
- Plugin validation, all 57 skill validations and explicit-only policies, and
  all 10 unchanged TOML profiles passed.
- All 21 Statechart modules passed Node syntax checks. Restaging the pinned
  upstream reproduces the reviewed port, apart from the deliberately omitted
  new test files.
- A direct chart-to-spec-to-TLC-to-PNG run found the expected offline/synced
  counterexample, reproduced the input chart, and produced both overview and
  bug-path images. The overview was visually inspected. This checks the tool
  workflow on the upstream example, not a property of a product codebase.

Validation used the existing Java 21 runtime and cached TLC 1.7.4, whose SHA-256
matches upstream's pin. The renderer uses upstream's pinned Pele 1.8.0 and
resvg 2.6.2. The standalone plugin-creator validator referenced by the older
runbook is not installed; the repository's plugin validator was used instead.

Start a fresh Codex task after installation to load the updated skills.
