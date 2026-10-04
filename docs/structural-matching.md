# Structural Matching Across Vocabularies (Product Side 2)

## The problem

Two fields can describe the same structure in completely different words. Temporal difference learning in computer science and dopamine reward prediction error in neuroscience are the same formal structure. Bellman's optimality equations in dynamic programming and Hamilton's equations in classical mechanics describe the same formal structure. In each case, the correspondence took decades to formalise because the vocabularies share nothing.

No existing tool can find these correspondences with structural receipts.

## Why embeddings fail

Cosine similarity and structural correspondence are different mathematical relations.

Two texts can share vocabulary and no structure. This is how numerology works: surface pattern matching without structural support.

Two texts can share deep structure under alien vocabulary and score near zero in embedding space. No embedding system would pair temporal-difference learning papers with dopamine-reward papers because the words share nothing.

Worse: "X causes Y" and "Y causes X" embed close together because they contain the same concepts. An embedding system calls them a match. They are saying opposite things. This is the specific failure that killed V1.

## How typed subgraph isomorphism works

Each theory is represented as a small directed graph (5 to 15 nodes). Each node is a typed claim. Each edge is a typed relationship (causes, is_substrate_of, measurable_by, etc.).

**VF2 subgraph isomorphism** (Cordella et al., 2004) asks: can all of Theory A's nodes be placed onto nodes of Theory B such that every edge in A maps to an edge in B of the same type? If yes, A's structure lives entirely inside B. That is a structural correspondence.

**Maximum common subgraph (MCS)** asks: what is the largest piece of A that fits inside B? If 6 of A's 8 nodes map perfectly, the ratio (6/8) tells you how much structure corresponds. The 2 unmatched nodes are precisely where the theories diverge. Those become the disagreements.

Both algorithms are deterministic. Same input, same output, same content hash. No temperature, no sampling, no drift.

Both are off-the-shelf algorithms shipped in NetworkX. VF2 was published in 2004. The algorithms are not novel. The typed schema they operate on is.

## The Newman guard

Named for the 1928 objection that any two systems share some structure once relations are untyped, which makes structural claims trivially satisfiable.

The guard: every edge in the match must have matching types. One mismatched edge type vetoes the entire correspondence. A failed match is not a vague "low similarity score." It is a specific structural reason: "this edge requires 'causes' but the candidate has 'is_substrate_of' — type mismatch."

This is the same principle chemists have used for decades in molecular substructure search without calling it Newman's guard.

## The connection to cheminformatics

Chemists match molecular substructures with typed graph matching where atom types and bond types must match exactly. A carbon-carbon double bond is not the same as a carbon-oxygen single bond, even if both are "bonds." The Consilience applies the same principle to scientific claims: a causal mechanism is not the same as a substrate relationship, even if both connect the same concepts.

The algorithm family is identical. The domain is different.
