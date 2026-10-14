---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
---

# Reflect

Before each spawn, select the reasoning effort and service tier for the job under [model routing](../poteto-mode/references/model-routing.md). Preserve explicit user settings and the installed role profile; never substitute Cursor model slugs.

Mine the current conversation for durable learnings, then route them into skill edits.

## When to invoke

Invoke when the user says "reflect" or "$pstack-codex:reflect". Skip trivial, off-topic, already-covered conversations the parent handled correctly, and one-offs.

## Process

### 1. Ground the review

Build a compact digest from the current conversation, decision log, changed files, commands, results, and subagent handoffs. Use Codex task/thread tools only if the task is not fully visible or the user asks to include related prior tasks; do not scan unrelated history.

### 2. Review in parallel

Launch three read-only reviewers concurrently over the same digest. The parent applies approved edits.

| Lens | Custom agent | Prompt template |
|---|---|---|
| Judgment | `pstack_reviewer_sol` | `references/judgment-reviewer.md` |
| Tooling | `pstack_reviewer_astra` | `references/tooling-reviewer.md` |
| Divergent | `pstack_reviewer_luna` | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the digest where marked; reviewers return findings in their Codex subagent responses.

### 3. Synthesize and check

Spawn `pstack_reviewer_sol` as synthesizer. Use `references/synthesizer.md` verbatim, inlining each reviewer's full output; it returns Accepted / Rejected / Backlog. Check Accepted: move anything a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See **encode-lessons-in-structure**.

### 4. Apply

Present the synthesizer's full Accepted/Rejected/Backlog output and wait for explicit approval. The user selects the subset and may redirect routings. Skill changes affect every future agent; do not auto-apply. File Backlog items automatically to the team's devex/backlog tracker; only Accepted waits for approval.

Follow each approved item's Routing exactly:

- Trivial existing-skill edit (one-line bullet, tightened sentence, stale fact): parent does it directly.
- Substantive existing-skill edit (new section, pattern table, or more than ~10 lines): use Codex's built-in `$skill-creator` draft / test / iterate loop.
- `tune description: <skill path>`: use `$skill-creator`'s description-optimization loop.
- `new skill via $skill-creator: <kebab-name>`: use `$skill-creator`; do not invent the shape ad hoc.

If the environment ships a SKILL.md validator, run it on every touched skill; otherwise skip.

### 5. Summarize

Short list, no preamble:

- Edits applied: `<skill path>` and one-line change.
- New skills created: `<skill path>` and one-line change (rare).
- Backlog filed: `<issue title>` (`<tags>`).
- Dropped: each rejected finding and the synthesizer's reason.
