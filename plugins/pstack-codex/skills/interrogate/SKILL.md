---
name: interrogate
description: "Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Multiple LLM reviewers challenge changes from independent angles."
---

# Interrogate

Spawn the three Codex reviewer profiles to adversarially review code changes. Profile and model diversity creates independent blind spots; agreement is higher-confidence signal, while lone findings still deserve inspection. The deliverable is a synthesized verdict. Do NOT auto-apply changes.

## Review

1. **Scope:** Use the files or diff the user points to; on a feature branch, use `git diff main...HEAD` (or the appropriate base); for references to recent work, gather relevant files. Package the diff or contents with context reviewers need.
2. **Intent:** Before spawning, state intent in one clear paragraph derived from the user message, commit messages, PR description if any, and code. If unsure, ask the user.
3. **Reviewers:** Select the ordinary or high-risk reviewer set from [model routing](../poteto-mode/references/model-routing.md). Launch independent reviewers concurrently within the active session limit, including root and descendants; use waves when needed. If a profile is unavailable, proceed with remaining reviewers and report the dropout. Run `$pstack-codex:setup-pstack` separately to repair or change a profile; do not invent a model slug during review.
4. Read `references/reviewer-prompt.md` and fill one shared template with the intent, diff or file contents, rubric (`references/rubric.md`), and code-quality lens (`references/code-quality-review.md`). Give the same filled template to every reviewer.
5. **Synthesize:** Parse every finding; merge duplicates and name the models raising them. Findings raised independently by 2+ models are highest signal; read lone findings but weight accordingly. Note explicit disagreements as context.
6. **Lead judgment:** You are a pragmatic senior engineer, not a neutral aggregator. Read `references/lead-judgment.md`; categorize every finding, naming model(s) and giving a one-line rationale:
   - **Act on:** Real correctness, security, or maintainability issues given the goals; would block a real PR.
   - **Consider:** Legitimate, but tradeoff against addressing now is uncertain.
   - **Noted:** Valid but not actionable, context-dependent, premature, or low-impact now.
   - **Dismissed:** Wrong, nitpicky, or missing context; briefly explain why.

## Output

### Intent
> [Stated intent paragraph]

### Reviewers
- Reviewer [label]: [model name], [N findings] (one bullet per reviewer)

### Act On
[Each finding, models raising it, and why it matters.]

### Consider
[Each finding, models raising it, and tradeoff.]

### Noted
[Brief list.]

### Dismissed
[Each finding with brief rationale.]

### Agreement Map
[Where models agreed or diverged, and what the pattern tells us.]
