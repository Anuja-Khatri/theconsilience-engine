# V1: The Embedding System That Failed

## What V1 was

A knowledge graph over ingested sources with a three-level embedding pipeline:

- **Surface level.** The raw text, embedded conventionally.
- **Conceptual level.** An intermediate abstraction.
- **Essence level.** Claude Haiku rewrote each passage into a tradition-neutral "shared vocabulary," and that rewritten text was embedded. The intent: strip the clothes, embed the body.

On top of this sat cosine clustering at a 0.78 threshold as the connection signal, a Haiku reranker scoring candidates zero to ten, recognition clusters auto-populated by similarity, a per-user "lens" implemented as a prompt variable, a confirmation dialogue producing confidence labels, and seven generation modes.

By the end it had produced 6,341 mappings and nine recognition clusters over the corpus.

## What V1 got right

It genuinely solved cross-vocabulary retrieval. Lexically dissimilar passages that point at the same recognition did retrieve together. Terms from physics and terms from Vedantic philosophy landed in the same neighbourhood in essence-space, which standard vector embeddings cannot do because they cluster by surface vocabulary.

Every competitor lives at the surface layer. The architecture review called this "a real and defensible advantage" and explicitly warned against ripping it out.

## How V1 failed

It called similarity a connection.

The failure was not tuning. It was categorical: **similarity and structural correspondence are different relations.** Two texts can share vocabulary and no structure, which is how numerology works. And two texts can share deep structure under alien vocabulary and score near zero, like temporal-difference learning in computer science and dopamine reward-prediction error in the midbrain.

The result was a false-positive machine: fluent, confident, and wrong at scale.

Specifically: "X causes Y" and "Y causes X" embed close together. The system could not tell that two theories were making opposite directional claims. They looked similar in essence-space. They are saying opposite things.

V1 was killed as an epistemic design in July 2026.

## What the 6,341 mappings became

The mappings were retained as something more valuable than they had been as output: the best hard-negative training set for this domain that exists anywhere. Every false positive is a precisely characterised example of what the new system must not accept.
