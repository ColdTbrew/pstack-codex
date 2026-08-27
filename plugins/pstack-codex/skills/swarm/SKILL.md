---
name: swarm
description: "Fan out N parallel workers, drain them, and return one report. Use for $pstack-codex:swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
---

# Swarm

Fan out N Codex workers. They may cover separate slices, race the same brief, or mix both. The parent drains them, aggregates, and returns one report.

## Start

Create or update a Codex plan with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. Run larger swarms in waves that fit the active Codex concurrency limit.
4. Use `pstack_worker` for coverage slices. For a model race, name the `pstack_builder_sol`, `pstack_builder_terra`, or `pstack_builder_luna` profile assigned to each arm.
5. Give each worker its own writable output when it writes. Use a worktree, branch, or `/tmp/swarm-<slug>/worker-<n>/`.

## Phase B: Fan out

Spawn every wave concurrently with the `pstack_worker` profile unless this is a declared model race. All local Codex agents share the workspace and permission boundary, so every writing brief must state exclusive files, branch, or worktree ownership.

When a worker must start from a non-default branch, name that base branch explicitly.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Keep a compact result table, one-line evidenced issues, and explicit gaps or dropouts.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.
