# AI-for-Science Systems Census

Roughly seventy systems were surveyed in July 2026. These are the ones that changed a decision.

## Systems that shaped the architecture

### AlphaProof: the anchor

Language model proposes proof steps. Lean, deterministic code, verifies every one. DeepMind's own framing credits the verifier. Solved three of five non-geometry problems at the 2024 International Mathematical Olympiad, reaching silver medal level.

**Adopted as the anchoring pattern.** Also recorded honestly as the "perfect verifier case that does NOT transfer to physics." Mathematics has a total verifier and the empirical sciences do not, so the pattern is an inspiration rather than a template.

### AlphaEvolve: the same lesson in a second domain

Model mutates candidate programs, execution scores them. Rediscovered cutting-edge solutions for 75% of over fifty open problems in analysis, geometry, combinatorics, and number theory. No result counts because a model believed it. It counts because execution verified it.

**Adopted as corroboration:** wherever a verifier exists, coupling generation to it produces the breakthrough.

### Kosmos (FutureHouse): the world model

Twelve-hour campaigns, roughly fifteen hundred papers per run, seventy-nine percent statement accuracy. Its credibility mechanism is not a smarter model. It is a structured world model: a queryable database of entities, relations, results, and open questions, updated by code after every step, plus a traceability discipline where every claim links to a code cell or source passage.

**Adopted directly.** The world model was implemented as a table in the schema. Their agents write beliefs into it. Our code writes proofs-of-match into it.

### Google AI Co-Scientist: the admission

A seven-agent Elo-tournament hypothesis system that independently re-derived a decade-long biology finding. Its own paper states that self-evaluation is unreliable.

**Used as evidence, not adopted as architecture.** The team that built the largest LLM-judging-LLM system published its failure mode. That citation is load-bearing in every defence of the deterministic judge.

### SciAgents: the closest architecture

Ghafarollahi and Buehler, MIT. A large-scale ontological knowledge graph (33,000 nodes, 49,000 edges) with a multi-agent team: an Ontologist, a Scientist, a second Scientist, and a Critic. Reasoning over sampled paths between two concepts through the graph.

**The single closest architecture to ours.**

What was adopted: the Ontologist role, mapped onto the fixed-ontology semantic contract. The two-concept path query, mapped onto "near structure, far vocabulary."

What was not adopted: in SciAgents the agents reason over the path and produce the hypothesis, the model has the last word. And SciAgents operates inside one domain (bioinspired materials) where everyone shares a vocabulary. They did not need vocabulary stripping. Consilience cannot work without it.

## Systems explicitly NOT adopted

**End-to-end paper-writing systems** (Sakana AI's The AI Scientist, AI-Researcher, Agent Laboratory, AgentRxiv): wrong shape entirely. They automate the whole loop including writing, which multiplies unverified output rather than checking it.

**Autonomous lab systems** (Lila Sciences, Periodic Labs, Chai Discovery, A-Lab, Coscientist): wrong domain, wrong grounding. Their verifier is a wet lab, which is a verifier Consilience will never have.

**The literature-based discovery lineage** (Swanson linking, SciMON, Hope et al. on analogy mining, Sourati and Evans): retained conceptually as ancestry. Undiscovered public knowledge as the thing being hunted, and analogy retrieval as a structural rather than surface problem.

## The pattern

Strip the marketing from every landmark AI-for-science result of the last two years and one pattern repeats: the model generates; something that is not a model verifies. Wherever a domain has a verifier, breakthroughs come from coupling generation to it. Wherever a domain lacks one, systems inherit the generator's failure mode: fluent, confident, unreproducible output.

Comparative theory analysis had no verifier. So this project built one.
