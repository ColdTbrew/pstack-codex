---
name: unslop
description: >-
  Polish report prose to remove obvious AI writing patterns. Use only when
  drafting, rewriting, or reviewing a report or report section, including
  technical, evaluation, benchmark, research, incident, and executive reports.
  Do not use for ordinary chat, status updates, code, diagnostics,
  documentation, emails, or other writing.
---

# Unslop

Edit report text to remove AI patterns and add human voice.

Use this skill only when the requested output is a report or part of one. Do
not invoke it for ordinary conversation or non-report work.

## Process

1. Scan for the patterns below.
2. Rewrite. Preserve meaning and match intended tone.

## Patterns to detect and fix

Rule numbers are stable ids that other skills cite. A removed rule leaves a gap.

### Content

3. **Superficial -ing phrases.** "highlighting...", "ensuring...", "reflecting...", "showcasing...", "fostering...". Delete or expand with real sources.
5. **Vague attributions.** "Experts believe", "Industry reports suggest", "Some critics argue". Name the source or delete.

### Language

7. **AI vocabulary.** Additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore, vibrant. Replace with plain words.
8. **Fancy ways to say "is".** "serves as", "stands as", "boasts", "features". Just say "is" or "has".
9. **"Not just X, but Y."** State the point directly instead.
10. **Rule of three.** Forcing ideas into groups of three. Use the natural number.
11. **Synonym cycling.** Protagonist, main character, central figure, hero all in one paragraph. Pick one, repeat it.
12. **False ranges.** "from X to Y" where X and Y aren't on a meaningful scale. List topics directly.

### Style

13. **Em dash overuse.** Avoid em dashes entirely. Use periods or commas only (no parentheses, en dashes, or hyphen-as-dash substitutes). If a thought needs separation, end the sentence or use a comma.
14. **Colon overuse.** Colons are fine before a list or example, not as mid-sentence connectors. Remove comparison framing and let the point stand on its own.
15. **Boldface overuse.** Don't bold every proper noun or acronym.
16. **Inline-header lists.** A bold label and colon that restates the line ("**Performance:** Performance improved...") is a tell. Convert it to prose. A bold lead-in ending in a period, naming the item and adding new detail, is fine.
17. **Title case headings.** Use sentence case.
18. **Decorative emojis.** Remove from headings and bullets.
19. **Curly quotes.** Replace with straight quotes.

### Communication artifacts

20. **Chatbot phrases.** "I hope this helps!", "Let me know if...", "Of course!", "Certainly!", "Found the smoking gun!" Remove.
22. **Sycophantic tone.** "Great question! You're absolutely right!" Respond directly.

### Filler

23. **Filler phrases.** "In order to" becomes "To". "Due to the fact that" becomes "Because". Delete "It is important to note that".
24. **Excessive hedging.** "could potentially possibly be argued that it might" becomes "may".
25. **Generic conclusions.** "The future looks bright." State specific plans or facts.

### Jargon

26. **Abstract metaphor nouns.** Substrate, wedge, vector, locus, vantage, nexus, primitive (as noun), harness (as metaphor), surface (as in "API surface"), bedrock, scaffolding (as metaphor), modality, paradigm, gold-plating, ratchet (as metaphor), evacuate (for moving code), endgame, north star, flywheel. Replace with concrete words: "base", "add", "way" or "method", "more than the job needs", the real mechanism or "a limit that only tightens", "move out", or "the last phase".

### Plain speech

27. **Say what it does, not how it feels.** Name mechanisms or numbers, not impressions. For example, "`.toSQL()` returns the exact string sent to the database" and "a column rename fails the build" are concrete. If a sentence cannot become a concrete instruction, fact, or number, cut it. If it could appear unchanged in another project's docs, it says nothing about this project; cut it.
28. **Shorten or split dense sentences.** Break up sentences that make readers backtrack. Keep one idea per sentence.
29. **Active voice.** Prefer it and name the actor. Passive is fine only when the actor is unknown or genuinely irrelevant.
30. **Cut adverbs or strengthen the verb.** Replace "runs quickly" with "is fast" or a number, and "significantly improves" with the measured delta.
31. **Prefer the plain word.** Use "use", "help", "many", and "if" over "utilize" or "leverage", "facilitate", "numerous", and "in the event that".
32. **Mannered prose.** Replace flourishes, rhetorical fragments, personified code, figurative verbs, and stock framing with literal wording. Rule 26 covers metaphor nouns.
33. **Over-compression.** Restore articles, verbs, and words hidden by symbols or abbreviations. Write "The parser rejects a bad date, exits with code 2, and writes nothing," not "Parser rejects bad date → exit 2, no write."
