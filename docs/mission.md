# Mission: Why This Tool Exists

## The manual labour the system replaces

Everyone who works across fields performs the same task by hand. They read two literatures. They hold two vocabularies in their head. And they decide whether two claims are the same claim wearing different clothes, whether they genuinely conflict, or whether they simply cannot be compared.

A PhD student does it in a related-work section. A researcher does it when comparing two theories across a vocabulary wall. A consciousness scientist does it when asking whether Integrated Information Theory and Global Neuronal Workspace actually disagree or merely describe the same thing differently.

This work takes days to months. It does not scale. Its output is one person's opinion with a bibliography attached, and it cannot be reproduced, audited, or checked by anyone who was not in the room.

## The deeper problem

Large language models made generating such connections free, and simultaneously made trusting them impossible.

A model will produce a fluent, plausible, uncheckable correspondence on demand. Ask it again tomorrow and it produces a different one. Citation hallucination in deployed research systems runs between eleven and fifty-seven percent, and the best attribution classifiers reach roughly eighty percent macro-F1.

So the bottleneck moved. The question is no longer "can we find a connection." It is "can anyone verify the connection we found."

## Why existing tools do not close it

| Tool class | What it does | What it does not do |
|---|---|---|
| Literature search (Semantic Scholar, Elicit, Consensus) | Finds and summarises documents | Does not compare claim structures |
| Knowledge graphs (Causaly) | Encodes entities and relations inside one domain | Does not adjudicate correspondences across domains |
| General assistants (ChatGPT, NotebookLM) | Summarises what you give it | Ungraded, non-reproducible |
| Expert networks | Does the reasoning properly | Three billion dollars of annual spend, one human hour at a time |

Nobody occupies the layer between retrieval and expert judgment.

## The novel goal, stated precisely

**Build the verifier for cross-domain claim comparison.**

Mathematics has proof checkers: AlphaProof works because Lean verifies every step. Code has execution: AlphaEvolve works because candidate programs either run faster or they do not. Autonomous research has structured world models and provenance: Kosmos's credibility rests on a queryable database and a traceability discipline, not on a smarter model.

Comparative theory analysis had nothing. No Lean. No execution. No verifier of any kind. The work was done by experts, in rooms, over years, with no mechanism to check the output.

The Consilience's contribution is to build that verifier: a system that takes claims from different fields, different vocabularies, and different centuries, and determines whether two of them are structurally the same, genuinely different, or not comparable at all. Deterministically, with a grade, with an explicit statement of what the match does not license, and with a link to the exact source sentence behind every assertion.

## Why nobody else is building this

Every AI-for-science tool today is either on the synthesis side (generating hypotheses, summarising literature) or in the experiment lab (running assays, folding proteins). The part in between, where a theoretical scientist needs creative intuition to notice that two fields describe the same structure in different words, that part has no tool.

Nobody is close to building one. It is still a want, not a need, for most of the field. But the cost is real. Temporal difference learning in computer science and dopamine reward prediction error in neuroscience are the same formal structure, discovered independently decades apart because no one read across both fields. Bellman's optimality equations in dynamic programming and Hamilton's equations in classical mechanics describe the same formal structure, developed centuries apart because the vocabularies share nothing.

That kind of lag, between when a structural correspondence exists and when someone notices, is the norm across science, not the exception. The Consilience exists to make that recognition systematic instead of accidental.
