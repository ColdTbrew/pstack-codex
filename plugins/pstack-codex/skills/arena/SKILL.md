---
name: arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for $pstack-codex:arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
---

# Arena

Before each spawn, select the reasoning effort and service tier for the job under [model routing](../poteto-mode/references/model-routing.md). Preserve explicit user settings and the installed role profile; never substitute Cursor model slugs.

Fan out N parallel attempts at the same task; read every candidate end to end, pick the strongest base, graft in the best ideas from the others, and verify the synthesis.

## Start

Create or update a Codex plan with one entry per phase: Frame, Fan out, Cross-judge, Pick, Graft, Verify.

### A. Frame

The shared prompt is the contract. State the artifact; derive 3-6 concrete, gradeable success criteria for this task (the picker's rubric; candidates only see the task); assign each candidate an exclusive output path/worktree (otherwise `/tmp/arena-<slug>/candidate-<n>/`), per **separate-before-serializing-shared-state**.

Choose up to three runners to keep root plus candidates within Codex's normal four-thread limit. Use the ordinary or difficult set from [model routing](../poteto-mode/references/model-routing.md); use fewer when there are fewer meaningful design directions.

### B. Fan out

Spawn candidates concurrently with the same task and grounding, their custom-agent profile, and exclusive output paths. Require the artifact and a short rationale naming alternatives considered and rejected. If a candidate produces no output, proceed with N-1 and record the dropout.

### C. Cross-judge

After candidates finish writing, spawn the read-only judge selected by [model routing](../poteto-mode/references/model-routing.md) for task difficulty. It sees the rubric and candidates under neutral path labels, scores each criterion, and recommends a base with rationale. The parent reads candidates in parallel with the judge; never start judging while candidates are writing.

### D. Pick a base

Read every candidate end to end; score criterion by criterion, not on holistic feel, and compare with the cross-judge. Agreement confirms the base; disagreement may signal bias or an ambiguous rubric, so read both rationales before deciding. Pick the base a future maintainer can extend without breaking invariants; when tied, prefer the cleaner boundary or smaller API per the Laziness Protocol.

### E. Graft

Revisit every loser for what is worth porting (usually one or two things). Fold grafts in by hand per **redesign-from-first-principles**, not mechanically, keeping one coherent mental model. Convergence on one shape is strong agreement: record and ship the consensus without grafting. Wild divergence means Phase A was under-specified; reframe and rerun, do not average it.

### F. Verify

Verify the synthesis per **prove-it-works**. If verification finds a missed problem, reframe and rerun if Phase A was wrong, or return to grafting if a candidate caught it. Do not paper over.

## Outputs

Deliver one synthesized artifact and a short note alongside it, recording: base and why; cross-judge verdict; each graft and its source; rejected ideas and why; convergence or dropouts; verification result.
