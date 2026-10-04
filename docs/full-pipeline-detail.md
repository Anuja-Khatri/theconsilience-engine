# Full 14-Step Pipeline

Every step: what goes in, what comes out, what can fail.

## Step 1: Ingest

**In:** PDF, audio file, video file, or plain text. Metadata: corpus class, tier, tradition tags, license.
**Tool:** Docling (IBM Research, open source) for PDF with page references. WhisperX (Oxford) for audio and video with diarised turns and speaker labels.
**Out:** Clean structured text with source locations (page number or timestamp).
**Fail mode:** Ingestion refused if metadata is incomplete. No silent defaults.

## Step 2: Chunk

**In:** Structured text from Step 1.
**Out:** Semantic chunks of 250 to 400 tokens with parent section retained. Speaker turns are never split.
**Why this size:** Large enough to preserve a complete scientific commitment. Small enough for accurate extraction. Empirically calibrated.

## Step 3: Claim extraction

**In:** Text chunks.
**Tool:** Claude Haiku with JSON-schema-constrained output validated by Pydantic. Sonnet escalates for hard cases. All runs through Anthropic's Batch API at 50% cost.
**Out:** Typed claim cards. Each card contains: claim kind (location, timing, architecture, mechanism, computability, substrate), commitment direction (asserts or denies), causal direction, physical scale, what would measure it, and the exact source sentence.
**Fail mode:** Malformed output rejected and retried twice, then flagged for human review. Never silently passed.

## Step 4: Cross-model agreement

**In:** Claim cards from Step 3.
**Tool:** A second model of different training lineage independently re-extracts the same passage.
**Out:** Agreement or disagreement on structural fields. Agreed claims proceed. Disagreements flagged for review.
**Why:** Models from the same training lineage share blind spots. Cross-lineage agreement converts residual extraction bias from an unknown into a measured, gated quantity.
**Fail mode:** Disagreements are never silently resolved. They are flagged.

## Step 5: Schema validation

**In:** Claim cards that passed cross-model agreement.
**Tool:** Pydantic schema enforcement.
**Out:** Validated typed claim cards with all required fields present and correctly typed.
**Fail mode:** Cards missing required fields or with wrong types are rejected.

## Step 6: Adversarial calibration

**In:** Validated claim cards.
**Tool:** The calibration set: deliberately convincing fakes designed to fool the system.
**Out:** Detection rate on known fakes. Measured and reported.
**Why:** If the system accepts convincing fakes, it cannot be trusted on real data.

## Step 7: Embedding and candidate pairing

**In:** Validated claim cards.
**Method:** Embed the canonical signature text (signature space, not raw text). Hybrid retrieval: dense plus BM25, reciprocal rank fusion, cross-encoder rerank. Tradition-tag filters prefer cross-tradition pairs.
**Out:** Shortlisted candidate pairs for structural matching.
**Why signature space:** Embedding raw text clusters by vocabulary. Embedding the typed signature clusters by structure. This is the difference between finding "they use the same word" and "they describe the same structure."

## Step 8: Graph construction

**In:** Shortlisted claim card pairs.
**Tool:** NetworkX. Directed typed graphs with attribute-rich nodes and edges.
**Out:** One small directed graph per theory (5 to 15 nodes). Each claim is a node. Each relationship is a typed edge (causes, is_substrate_of, measurable_by, etc.).
**Why small:** Subgraph isomorphism is NP-complete in general but tractable for small graphs. The system is designed to stay within tractable bounds.

## Step 9: VF2 and maximum common subgraph

**In:** Two typed directed graphs (one per theory).
**Tool:** VF2 subgraph isomorphism (Cordella et al., 2004) with node and edge type constraints. Maximum common subgraph (MCS) for partial matches.
**Out:** Exact match (VF2 succeeds: one graph's structure lives inside the other) or partial match (MCS: the largest shared substructure, with unmatched nodes identified as the specific points of disagreement).
**Deterministic:** Same input, same output, same content hash. No temperature, no sampling, no drift.

## Step 10: Newman guard and defect edge veto

**In:** Match results from Step 9.
**Rule:** Every edge in the match must have matching types. One mismatched edge type vetoes the entire correspondence. Matches resting on over-general relations are rejected. "Invokes the same mathematical object" is a typed flag, not a rung, so numerical coincidence without transported causal machinery caps at the lowest rung.
**Out:** Matches that survive typed edge constraints, or rejections with the specific defect edge named.

## Step 11: Equivocation removal test

**In:** Surviving matches from Step 10.
**Rule:** For any correspondence resting on a shared term, strip the term and re-derive cross-side edges from the typed graphs alone. If at least one honest edge survives, the load is latent and the rung caps at generative analogy pending resolution. If none survives, the load is load-bearing, the Newman guard vetoes, and the item grades as fake.
**Out:** Matches with vocabulary-dependency assessed. Fakes identified and rejected.

## Step 12: Circular provenance detection

**In:** Surviving matches.
**Rule:** Evidence chains traversed for source independence. Support resolving substantially to the same author's own uploads or a closed citation loop is flagged self-referential and capped at generative analogy, with the cap displayed in the audit view.
**Out:** Matches with provenance independence verified.

## Step 13: Decidability check

**In:** Genuine disagreements from the matching process.
**Tool:** Versioned instrument capability map. Structured data recording which instrument class reaches which physical scale measuring which observable.
**Out:** Three possible verdicts: testable now (instrument named), testable under a stated assumption (assumption named), or not testable with current technology (structural reason named).
**Version pinning:** When instruments improve, the map updates. Old verdicts stay valid under their original version. New verdicts coexist.

## Step 14: Evidence join

**In:** Decidable disagreements.
**Tool:** ConTraSt database (761 consciousness studies from Tel Aviv University), joined through a human-reviewed mapping.
**Out:** Which divergences have published experiments bearing on them, cited on screen.
**No model, no judgment.** A lookup.

## Step 15: Oracle review and provenance manifest

**In:** All graded matches, rejections, and decidability verdicts.
**Process:** Human reviews every claim before it counts publicly. Approvals stamp the record. Only approved items serve publicly.
**Manifest:** Every verdict resolves to source sentences. Content hashes over inputs, model versions, ontology version, judge version. Same inputs, same output, regenerated in about seven seconds.
**Published rejections:** Every considered-and-rejected match, with the specific structural reason it failed.
