---
name: figure-it-out
description: "Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions via show-me-your-work. Use for $pstack-codex:figure-it-out, 'figure it out', a large migration, or when no narrower playbook applies."
---

# Figure it out

Before each spawn, select the reasoning effort and service tier for the job under [model routing](../poteto-mode/references/model-routing.md). Preserve explicit user settings and the installed role profile; never substitute Cursor model slugs.

When no playbook fits, design one before writing code: a workflow whose phases scale rigor to the task, apply the scientific method, and leave an auditable decision trail.

## Start

Create or update a Codex plan. First read the Principles section of **poteto-mode**, then add the phases below as todos.

## Phase A: Frame

Ground the work before committing. State:

- A falsifiable definition of done, using the **prove-it-works** principle.
- Quantified scope: rough units, effort, and grounding blockers.
- A rigor level biased high: give one-way doors and high blast radius more gates and artifacts; give reversible, low-stakes work less.

Present the framing and tradeoffs before a long run. Let reversible work proceed under **never-block-on-the-human**, but add one checkpoint for a multi-hour run.

## Phase B: Design the workflow

Decompose work into atomic, independently landable units and sequence the riskiest unknown first. Put scaffolding and verification before features, following **foundational-thinking**.

- Build the verification harness first and capture the pre-change baseline for comparison.
- For one-way-door design decisions, run **architect** (which runs **arena**) with diverse, isolated candidate profiles and an independent read-only judge. Skip mechanical work with a concrete shape. Do not run arena again once the design is settled, following **laziness-protocol**.
- Fan out only across genuine seams. Give each worker its own worktree or branch, following **separate-before-serializing-shared-state**. Do not over-fan.
- Write down the phases for human review.

Then execute the workflow. Add its steps as concrete Codex plan items after Phase C and before Phase D. Run each under Phase C discipline and log a row in Phase D as each step lands.

## Phase C: Run the loop

Treat each unit as an experiment: state a hypothesis, make the smallest change, measure the real artifact against the predicate, and keep or revert based on the result. Follow **sequence-verifiable-units** and verify each unit before starting the next.

- Inspect artifacts rather than trusting self-reports. If something passes too easily, question the observation method.
- Pair delegated work with a judge. If a worker games the gate, reset and strengthen the contract. If the gate is wrong, fix it separately instead of routing around it.
- Report VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass; do not hide a negative result.

## Phase D: Keep the audit trail

Log the run with **show-me-your-work**. Commit the trail when it is useful to the PR reviewer; the trail and diff let them audit the work after stepping away.

## Phase E: Verify and hand back

Check the real product against the Phase A predicate, not just the harness. Encode recurring corrections as gates, lint rules, checks, or scripts, following **encode-lessons-in-structure**.

**Reply:** Give the designed playbook, rigor level and rationale, decision-trail path, predicate verification, and open items.
