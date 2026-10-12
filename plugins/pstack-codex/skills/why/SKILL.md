---
name: why
description: "Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Discovers available MCPs and queries each evidence category (source control, issue tracker, long-form docs, real-time chat, infrastructure observability, error tracking, product analytics warehouse) in parallel, then returns a cited read on decisions and tradeoffs. Use how for runtime behavior."
---

# Why

Investigate the motivation and intent behind code.

Companion to the `how` skill. `how` answers what the code does and how it works. `why` answers what forces led to its shape.

Use the Codex custom-agent profiles in [model routing](../poteto-mode/references/model-routing.md).

## Operating Posture

Operate as a **careful, cautious, and precise investigator**. Be honest about what you know vs what you're inferring. Read `references/epistemics.md` for the full confidence framework and phrasing guide. The synthesizer must follow it.

## Step 1. Understand the Target and the Question

The **target** is usually a chunk of code, a pattern, a feature, or a named design decision. The **question** is usually a design rationale, a tradeoff, a motivating edge case, an external constraint, dead code, or a broad history sweep.

If the target is vague ("why do we do it this way?" with no clear referent), make your best guess from conversation context. State your interpretation briefly so the user can redirect, then proceed.

## Step 2. Establish the Code Anchor

Before spawning investigators, build seed context inline: relevant file paths and line ranges, key symbols, recent commits touching the target, PR numbers from merge commits (`(#1234)` in the subject), and linked ticket IDs. Use `git blame -L <start>,<end> <file>` for last-touch commits, `git log --follow -p -- <file>` for history through renames, `git log --oneline -20 -- <file>` for recent commits, and `git log -1 --format=%B <commit>` to extract PR numbers. Pull substantive PR bodies and discussion with `gh pr view <number> --json title,body,author,createdAt,mergedAt,labels,closingIssuesReferences,comments,reviews`. Pass this anchor to investigators.

## Step 3. Spawn Parallel Investigators (default posture)

**Default to the full parallel investigation.** Discover available connectors and MCP tools in this Codex task using the available-tools map and tool search when exposed; do not assume a local `mcps/` directory exists.

Map each available MCP to its primary evidence category, recording ambiguity:

1. Source control history
2. Issue / ticket tracker
3. Long-form documents
4. Real-time team chat
5. Infrastructure observability
6. Error / exception tracking
7. Product analytics warehouse

Source control is always available through git and `gh`. Classify other MCPs using their name, server instructions, tool names, and resource descriptors. Aim for a complete coverage map; document null results rather than skipping searches.

Run one read-only `pstack_explorer` per available evidence category, one source per investigator, in waves within the active Codex concurrency limit. Verify MCP tool access before assigning an MCP-backed category; investigators must not write to external systems.

Each investigator gets:
1. `references/investigator-prompt.md`
2. The category playbook `references/sources/<source>.md`, adapted from `references/source-playbook.md`
3. `references/sources/incident-postmortem.md` when the target looks defensive (null checks, retries, timeouts, rate limits, feature flags, egress guards, OOM handlers)
4. The code anchor and the user's question

### Investigator roster

Spawn one for each available matching category. Use the roster to anticipate findings and name gaps when a category returns empty:

1. **Source control** (git, `gh`, comments, tests). Always spawn; the only guaranteed source, best for implementation-time rationale from review.
2. **Issue / ticket tracker** (e.g. Linear, Jira, GitHub Issues, Plane, Shortcut). Best for the product or business forcing function.
3. **Long-form documents** (e.g. Notion, Confluence, Google Docs, Coda). Best for rationale written before implementation.
4. **Real-time team chat** (e.g. Slack, Discord, Teams, Mattermost). Best for deliberation absent from docs, especially when the paper trail is thin.
5. **Infrastructure observability** (e.g. Datadog, New Relic, Honeycomb, Grafana, Splunk). Best for runtime signals that motivated infra-related code.
6. **Error / exception tracking** (e.g. Sentry, Rollbar, Bugsnag, Airbrake). Best for error trajectories behind defensive code.
7. **Product analytics warehouse** (e.g. Databricks, Snowflake, BigQuery, ClickHouse, dbt, Redshift). Best for product/data reality, experiments, migrations, and metric origins.

### When to skip an investigator

Skip only with an explicit written justification in the final Sources Consulted:

- No MCP is available for that category: report the missing source as a gap, not a choice.
- The source is provably irrelevant, not merely probably irrelevant.

An inline answer is exceptionally rare: only for a trivial single-commit target whose PR description fully answers the question, and only after confirming all seven category searches would be redundant. Say so explicitly.

## Step 4. Synthesize

Spawn one read-only `pstack_reviewer_sol` to synthesize the findings and verify citations. Provide:
1. Findings, including null results and justified skips
2. The code anchor and user's original question
3. `references/epistemics.md`
4. `references/synthesizer-prompt.md`

## Step 5. Present

Present the synthesizer's output. Lightly edit for clarity or conversation context, but **do not rewrite the confidence language**.

## Output Format

Use the structure in `references/synthesizer-prompt.md`: The Question, The Code in Question, What We Found, What We Can Reasonably Infer, Competing Hypotheses, What We Don't Know, Sources Consulted, Confidence Summary. Keep confidence separation intact and list every investigator in Sources Consulted, including empty results and justified skips.

After Sources Consulted, if the question precedes a code change, turn lineage findings into Preserve / Change / Avoid / Risk constraints for planning.

## Common Failure Modes to Avoid

- **Recency bias**. The current shape may reflect many earlier decisions; trace beyond the latest commit.
