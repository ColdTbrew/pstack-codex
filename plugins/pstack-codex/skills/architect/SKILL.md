---
name: architect
description: "Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for $pstack-codex:architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape."
---

# Architect

Sketch types, function signatures, class shapes, and module boundaries with `not implemented` bodies and pseudocode. Synthesize multiple model perspectives, then implement against the chosen sketch. If implementation proves it wrong, redesign.

## Start

Create or update a Codex plan with one entry per phase:

1. Ground
2. Sketch
3. Agree
4. Implement
5. Scrap

## Phase A: Ground the problem

Build a mental model of every system the code touches. Run the **how** skill on relevant subsystems and produce its architectural explanation; naming files is not grounding. If the design changes ownership or layering, also run **why** so existing rationale constrains the design.

Skip this phase only for genuinely greenfield work with no surrounding system.

## Phase B: Sketch

Run **arena** with the design-sketch task and Phase A artifacts. Pass `references/runner-prompt.md` to each runner. Use the `$pstack-codex:arena` candidate set for task difficulty from [model routing](../poteto-mode/references/model-routing.md).

Require at least two structurally distinct designs before synthesis, even when the first looks sufficient. Compare whole shapes, not point fixes. This makes the **exhaust-the-design-space** principle concrete.

Screen each candidate against [`references/design-red-flags.md`](references/design-red-flags.md). Assume the next contributor sees only opened files, copies the nearest example, and takes the shortest compiling path. Prefer a design where a locally plausible change is right for the whole repo.

Compare viable designs on interface depth. Prefer the smaller, simpler public surface that hides more complexity and concentrates capability.

Arena returns one synthesized design package; record its decision in the rationale's "Synthesis decision" section.

## Phase C: Agree (opt-in)

By default, proceed to implementation without a human checkpoint. Pause for sign-off only when the invoker explicitly asks, such as "$pstack-codex:architect with checkpoint" or "stop and show me before implementing."

The synthesis may ship as its own commit, following the **foundational-thinking** principle's "scaffold first" mode. Planned, scoped breakage during implementation is fine under **outcome-oriented-execution**. For adversarial review, run **interrogate** on the sketch.

Treat human pushback as Phase A evidence. Re-ground and rerun Phase B before more code.

## Phase D: Implement against the sketch

Replace `not implemented` bodies and pseudocode with implementation. The sketch is the contract. Surface deviations: ask whether the sketch, requirement, or implementation is wrong.

## Phase E: Scrap when the architecture is wrong

If implementation repeatedly produces friction the sketch cannot absorb, redesign rather than patching a wrong shape, following **redesign-from-first-principles** and **fix-root-causes**.

Look for patterns, not isolated cases:

- The same workaround across unrelated code.
- Unrelated edge cases that need special branches.
- Types needing escape hatches (`any`, casts, or optional fields always set) to compile.
- A reflex to add a lock when the sketch says state is not shared.
- Callers needing to know internal abstraction rules.
- Two or more independent Phase D deviations of the same shape.

Use judgment: a few edge cases do not condemn a design, and data complexity is not design complexity.

When scrapping:

1. Rerun **how** on what was built.
2. Redesign with new constraints as day-one assumptions, following **redesign-from-first-principles**.
3. Subtract before adding, following **subtract-before-you-add**. Make the new sketch smaller before it grows.
4. Return to Phase B and rerun arena.

## Outputs

Write caller usage first, then derive the type sketch. Use one file of new types and signatures for small changes; use a module map and type definitions for larger work. Ship the rationale alongside, following `references/rationale-template.md` and including usage and synthesis decisions.
