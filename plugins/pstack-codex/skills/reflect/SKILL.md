---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
---

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

## When to invoke

Invoke when the user says "reflect" or "$pstack-codex:reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## Process

### 1. Ground the review in the active task

Build a compact task digest from the current conversation, decision log, changed files, commands, results, and subagent handoffs. Use Codex task/thread tools only when the current task is not fully visible or the user explicitly asks to include related prior tasks. Do not broadly scan unrelated task history.

### 2. Spawn three reviewers in parallel

Launch three read-only reviewers concurrently over the same digest. The parent applies any approved edits.

| Lens | Custom agent | Prompt template |
|---|---|---|
| Judgment | `pstack_reviewer_sol` | `references/judgment-reviewer.md` |
| Tooling | `pstack_reviewer_terra` | `references/tooling-reviewer.md` |
| Divergent | `pstack_reviewer_luna` | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the task digest where marked. Reviewers return findings in their Codex subagent response.

### 3. Synthesize

Spawn `pstack_reviewer_sol` as the synthesizer. Use `references/synthesizer.md` verbatim, with each reviewer's full output inlined where marked. The synthesizer returns a structured Accepted / Rejected / Backlog list.

### 4. Structural enforcement check

Sanity-check the synthesizer's Accepted list. For any item that would be enforced more reliably by a lint rule, script, metadata flag, or runtime check, move it from Accepted to Backlog. See the **encode-lessons-in-structure** principle skill.

### 5. Apply

Before applying any Accepted edit, present the synthesizer's full Accepted/Rejected/Backlog output to the user and wait for explicit approval. The user picks which subset to apply and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

Backlog items file to whatever devex / backlog tracker your team uses automatically. Only the Accepted list waits for approval.

For each approved Accepted item, follow the Routing field exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): parent does directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to Codex's built-in `$skill-creator` skill and run its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): hand to `$skill-creator` and run its description-optimization loop.
- `new skill via $skill-creator: <kebab-name>`: hand creation to `$skill-creator`. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done. Skip this step if it doesn't.

### 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
