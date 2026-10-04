# Structure-Directed Source Acquisition

The engine discovers its own sources by searching for structural patterns, not topics.

## The problem with manual source selection

In any cross-domain comparison, the researcher selects the sources. This creates a room where everyone already knows each other. The engine only finds correspondences between the theories you uploaded. If the structural match exists in a field you never thought to include, the engine cannot find it.

Manual source selection also carries confirmation bias: you upload sources you expect to match. The engine finds what you put in front of it, which is what you already suspected.

## How the engine searches by structure, not topic

When the engine has exhausted its initial corpus, it analyzes its own gaps:

1. **Identify unmatched claims.** The engine finds every claim that never matched, every claim that appeared only in rejections, and every claim that was quarantined as thematic-only. In the physics workspace demo: 379 unmatched claims, 112 rejection-only, 12 quarantined thematic.

2. **Strip vocabulary and describe the structural pattern.** For each unmatched claim, the engine removes domain-specific vocabulary and describes the structural pattern in domain-neutral language. Instead of "neuronal avalanches follow a power law with exponent minus 3/2," the query becomes "a system exhibiting a power-law branching process with exponent minus 3/2."

3. **Generate search queries in alien vocabularies.** The engine generates queries targeting fields the corpus does not cover. Instead of "find more neuroscience papers," it searches for "a system with a minus 3/2 branching exponent" or "a fixed ordered named multi-stage differentiation cascade." This reaches fields nobody would have thought to include.

4. **Search arXiv and Semantic Scholar.** 240 structural queries. The engine retrieves candidate papers from fields it was never given.

5. **Extract claims from found papers.** Same extraction pipeline, same schema constraints, same quality gates. 24 papers found from statistical physics, developmental biology, RAF chemistry, population ecology, soft matter, dusty plasma, formal grammar, and lambda calculus. 256 new claims extracted, 100% quote-verified.

6. **Match new claims against all existing claims.** Same matching rules. Same quality audit.

7. **Apply the same strict audit.** Same 5-criterion test. Only matches that survive are reported.

## What it found

In the physics workspace demo, engine-directed discovery produced 4 new demo-ready matches and closed 2 specific gaps:

**Gap closure 1:** The engine found mean-field self-organized-branching theory from statistical physics, where the branching exponent tau = 3/2 exactly matches the cortex's minus 1.50. Same universality class, from a field the researcher never uploaded.

**Gap closure 2:** The engine found Drosophila segmentation genetics from developmental biology, supplying the fixed ordered named differentiation cascade that physics lacked, matching an ordered emergence sequence from a philosophical text. A developmental biology paper matching a 2,000-year-old philosophical text on multi-stage emergence, found because the engine searched for "fixed ordered named cascade," not for "Drosophila" or "philosophy."

**Gap narrowed:** The engine found critical-slowing-down early warning signals from complex systems theory, supplying the specific test to distinguish a true phase transition from a smooth crossover.

## The confirmation bias caveat

Engine-directed discovery carries its own bias risk. The engine searches for patterns that match its existing claims. This means it is searching for confirmations, not refutations. A match found by the engine is more likely to be a genuine structural correspondence (because the query was structurally precise) but also more likely to be sought rather than stumbled upon.

Mitigation: every engine-found match goes through the same strict audit as manually-sourced matches. The audit criteria do not change based on how the source was found. In the physics demo, the same 5-criterion test applied. Additionally, engine-found sources carry a visible badge: "found beyond uploaded sources," so a reader knows this source was discovered by the engine, not chosen by the researcher.

## The novelty audit gate (specified, not yet built)

The next stage: every engine-found match that passes the structural audit also passes a novelty check. Is this correspondence already known in the literature? If so, it is a blind recovery (still valuable as validation, but not novel). If not, it is a genuinely new correspondence. The novelty gate uses Semantic Scholar and Google Scholar to check whether the structural correspondence has been previously published by anyone.

In the physics demo, a post-build literature audit found that most engine-discovered correspondences were blind recoveries of correspondences known to specialists in the relevant fields. Two genuinely novel claims survived. This audit was manual. The specified next stage automates it.

## Why this matters

Literature search tools typically find papers by topic keywords. The engine searches for papers by structural pattern. It can find that a developmental biology paper from 2003 structurally matches a 2,000-year-old philosophical text because both describe the same fixed ordered emergence cascade, and it can find this without anyone telling it to look at developmental biology.

The lag between when a structural correspondence exists in the literature and when someone notices it is measured in decades. This capability exists to close that lag.
