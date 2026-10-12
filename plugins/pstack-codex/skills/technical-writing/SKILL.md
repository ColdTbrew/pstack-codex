---
name: technical-writing
description: "Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, Global English syntax. Use for $pstack-codex:technical-writing or when writing or reviewing docs, RFCs, readmes, PR descriptions, or commit messages."
---

# Technical writing

Write so a tired engineer understands on the first read. Apply all four layers: document mode, reader address, sentence load, and ambiguity.

Three rules sit above the layers:

- **Cut every word that does no work.** If the sentence survives without it, remove it. "In order to" becomes "to"; "It is important to note that" disappears.
- **Use the short, everyday word.** Use "use", "help", and "do" over "utilize", "facilitate", and "perform" unless a longer word is more precise.
- **If a rule makes a sentence worse, fix it another way or leave it.** Rules serve the reader, not mechanical compliance.

Use the codebase's real symbol, file, flag, and command names. Don't invent jargon. Use words developers say aloud, and define a named pattern on first use. If you find a new abstract metaphor, propose its replacement as an addition to `unslop` in your reply; do not edit that skill.

## Vary the rhythm

A document can follow every layer and still sound machine-written. Mix short points with longer sentences carrying one fact and its condition or consequence. Split sentences with two thoughts, not sentences that carry one thought at length. Give explanations a view on tradeoffs; keep references dry. Prefer specific facts, such as "a column rename fails the build," over generalities.

## Pick the mode first (Diátaxis)

Choose one mode by asking whether the content supports action or understanding, and learning or work:

- Action + learning: **tutorial**.
- Action + work: **how-to**.
- Understanding + work: **reference**.
- Understanding + learning: **explanation**.

Use the distinction for a whole document or a sentence.

**Tutorial: learning by doing.** Say what the learner will build. Make each step produce a visible result and say what to expect. Keep explanation to one clause and a link. Write as "we" in commands.

**How-to: steps to a goal.** Solve the reader's problem. Assume competence and give actions, not teaching or background. Link extra context. Allow choices and name the guide for its task, such as "How to calibrate the radar array."

**Reference: facts for lookup.** Describe only. State facts, options, limits, and errors without hedging. Mirror the structure of the thing described and generate from code where possible.

**Explanation: understanding and why.** Cover one bounded topic, anchor it in a real why question, and give context such as decisions, history, constraints, and alternatives. Opinion belongs here, not in other modes.

Do not mix modes. Split and link instead.

## Write sentences to the reader (Google developer style)

- Address "you" in present tense; use "will" only for genuine future events.
- Name the actor. Use passive voice only when the actor is unknown or irrelevant.
- Write instructions as commands and facts plainly. Put a condition before its instruction and the common case before exceptions.
- Sound like a knowledgeable friend. Avoid buzzwords, figurative language, "please" in instructions, and "simply", "easy", or "quickly" in procedures.
- Do not pre-announce or start consecutive sentences with the same phrase.
- Link with descriptive words, never "click here". Prefer useful context on the page.
- Make headings state the point in sentence case. Use task verb phrases and concept noun phrases. Keep one h1 and do not skip heading levels.
- Use numbered lists for sequences and bullets otherwise. Introduce lists with a complete sentence and keep items parallel.
- Use code font for code, bold for UI, serial commas, and state when a list is partial instead of writing "etc.".

## Make statements load one at a time (STE rules)

Use one instruction per sentence and one thought per other sentence. Split instructions over about 20 words and other sentences over about 25. Put warnings before guarded steps. Keep articles. Give each word one meaning and job, and use one verb per action. Write procedures as direct commands, not narration or passive voice. Avoid "-ing" words when a plain verb works.

## Leave no sentence open to two readings (Global English)

- Keep "only" and "not" next to the words they change. Break up long noun strings.
- Give every "it", "they", and "this" one clear referent. Never use "this" or "which" for a whole clause.
- Keep verbs and structural words such as "that". Repeat articles when needed to distinguish items.
- Clarify what "and" or "or" joins; use "both...and", "either...or", or "if...then" when useful.
- Prefer periods to semicolons and replace em dashes with sentences. Parenthetical text must be grammatical; never form plurals with "(s)".
- Avoid slashes. Name each thing consistently; do not churn unchanged sentences.
- Skip idioms, colloquialisms, Latin abbreviations, and metaphors.

## Voice and repo specifics

- Apply **unslop** to every document this skill touches; it owns the catalog of AI vocabulary, filler, hedging, and formatting tells.
- Apply every layer except Diátaxis to PR descriptions and commit messages. A PR body briefs a reviewer in under a minute; link swarm logs, SHA lists, and metric tables instead of pasting them.
- Product UI strings follow product copy guidelines, not documentation rules.
- Indent code snippets with tabs. Use real paths and symbols. Keep count and tree claims true at the landing commit and include the regeneration command.

## Worked example

Before:

> Configuration of the proto import ratchet budget script parameters is performed via budget.json. Note that it's important to remember that running with --write, which updates the committed budget to reflect the current count, should only be done when lowering it. If exceeded, CI fails.

After:

> `budget.mjs` reads the committed budget from `budget.json` and counts the files that import protos. If the count exceeds the budget, CI fails. Run `budget.mjs --write` only to lower the budget.
