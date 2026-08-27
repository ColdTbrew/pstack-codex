---
name: setup-pstack
description: Configure the Codex custom agents used by pstack-codex. Use for setup-pstack, configuring pstack models, or changing pstack's builder, explorer, reviewer, and worker profiles.
---

# Set up pstack for Codex

Configure the `pstack_*`, `poteto_agent`, and `comment_sicko` profiles under
`~/.codex/agents/`. Each profile is a standalone Codex custom-agent TOML file.

## Workflow

1. Inspect the currently available Codex models and the existing files under
   `~/.codex/agents/`. Never invent a model slug.
2. Show the current role mapping and flag unavailable models.
3. Preserve the role intent when changing models:
   - `poteto_agent` and `pstack_builder_sol`: demanding implementation and synthesis.
   - `pstack_builder_terra` and `pstack_explorer`: fast exploration and alternative builds.
   - `pstack_builder_luna` and `pstack_worker`: narrow, repeatable, high-volume work.
   - `pstack_reviewer_*` and `comment_sicko`: read-only review.
4. Update only the requested TOML files. Keep `name`, `description`, and
   `developer_instructions` intact unless the user asks to change behavior.
5. Validate every TOML file by parsing it and tell the user to start a new Codex task
   if the active task does not pick up the changed profiles.

Use `gpt-5.6-sol` for demanding work, `gpt-5.6-terra` for balanced exploration,
and `gpt-5.6-luna` for bounded mechanical work when those models are available.
