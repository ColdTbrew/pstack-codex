# Model routing

Use this policy when selecting pstack agents. Explicit user choices take precedence. The companion `codex-agents/*.toml` files define the shipped model and reasoning settings; setup-pstack manages installed overrides.

## Roles

| Role | Profile or launch choice | Model | Reasoning |
| --- | --- | --- | --- |
| Root coordinator | Current chat, start with Astra | `gpt-6-astra` | `medium` |
| Default end-to-end delegated owner | `poteto_agent` | `gpt-6.1-sol` | `medium` |
| Track sub-coordinator | General agent with an explicit track brief | `gpt-6.1-sol` | `medium` |
| Difficult implementation | `pstack_builder_astra` | `gpt-6-astra` | `medium` |
| Scoped feature or bug fix | `pstack_builder_sol` | `gpt-6.1-sol` | `medium` |
| Codebase exploration | `pstack_explorer` | `gpt-6.1-sol` | `high` |
| Alternative implementation | `pstack_builder_sol` / `pstack_builder_astra` by difficulty | `gpt-6.1-sol` / `gpt-6-astra` | `medium` |
| Mechanical implementation / coverage | `pstack_builder_luna` / `pstack_worker` | `gpt-6-luna` | `max` |
| General independent review | `pstack_reviewer_sol` | `gpt-6.1-sol` | `high` |
| Broad bounded review | `pstack_reviewer_luna` | `gpt-6-luna` | `max` |
| High-risk review / disputed findings | `pstack_reviewer_astra` | `gpt-6-astra` | `high` |
| Comment review | `comment_sicko` | `gpt-6.1-sol` | `high` |

The three Luna profiles set `service_tier = "fast"` and retain `model_reasoning_effort = "max"`. Service tier and reasoning effort are separate settings. Other profiles inherit the session's service tier.

The root runs on the current chat model. A skill or custom-agent TOML does not switch it. Recommend Astra medium when starting an orchestration session; continue on an explicitly selected model. Only create track coordinators when the orchestrate playbook needs them. Use the available general agent with explicit Sol/medium settings and a self-contained track brief; when model overrides require a limited or empty history fork, supply the necessary context in that brief. Do not repurpose an implementation-only or read-only profile as a coordinator.

## Selection and escalation

Use `poteto_agent` on Sol/medium for ordinary end-to-end implementation helpers. Select `pstack_builder_astra` on Astra/medium for unresolved design choices, changes to contracts across modules, or a scoped Sol attempt that cannot establish correctness; supply the task brief and matched poteto-mode playbook so the helper follows the same wrapper. Use Astra review for concurrency, possible data loss, major architectural changes, or consequential disagreement between reviewers. Ordinary scoped work remains on Sol; mechanical work remains on Luna. Route codebase exploration to the Sol explorer.

Keep implementation and verification in separate agents. A reviewer must not have written the artifact, including when builder and reviewer use the same model. Resolve findings with evidence rather than vote count alone.

## Mode composition

| Mode | Ordinary work | Difficult or high-risk work |
| --- | --- | --- |
| Arena candidates | Sol + Luna builders; add Astra for a third meaningful alternative | Astra + Sol + Luna builders |
| Arena judge | Sol reviewer | Astra reviewer |
| Interrogate reviewers | Sol + Luna reviewers; add Astra when a third independent review is warranted | Astra + Sol + Luna reviewers |
| Swarm slices | Luna worker | Sol builder for scoped implementation; Astra builder for difficult implementation |

Use fewer candidates when there are fewer meaningful alternatives. Fit every launch within the active session limit, counting the root and all descendants; the current four-agent limit leaves three child slots. Arena judges start after candidates finish.

If a profile is unavailable, report the missing role. Arena and interrogate may proceed with fewer independent participants and an explicit coverage gap; do not present a missing Astra review as completed. For individual implementation or review, use an available Sol profile as the disclosed fallback and retain the same acceptance criteria. If a Sol track coordinator cannot be launched, the root drains that track directly. Never silently change a model slug or count repeated instances of one model as model diversity.
