# Architecture Overview

The Consilience is a neurosymbolic system in the strict sense: neural reading, symbolic judgment. Language models handle extraction (perception). Deterministic code handles all judgment (reasoning). They never share a feedback loop.

## The governing pattern: LLM Modulo

The architecture follows Kambhampati et al.'s LLM Modulo framework (ICML 2024 Spotlight). The model proposes (extracts typed claims from text). An external verifier, which is not a model, checks every output. No claim reaches the user without passing through deterministic code.

Kambhampati's data showed autonomous LLM plans are correct roughly 12% of the time. Our V1 embedding system, where the model also did the judging, produced 6,341 false positives. Same failure, same cause: generation without external verification does not work.

## Component map

| Component | What it does | Model or code? |
|---|---|---|
| Ingestion (Docling, WhisperX) | PDF, audio, video to structured text | Code |
| Chunking | 250-400 token semantic chunks | Code |
| Claim extraction | Papers to typed claim cards | Model (Sonnet primary) |
| Cross-model agreement | Independent re-extraction by Haiku | Model (cross-check) |
| Schema validation | Pydantic type checks | Code |
| Adversarial calibration | Fake claim detection rate | Code |
| Graph construction | Claim cards to typed directed graphs | Code (NetworkX) |
| VF2 subgraph isomorphism | Exact structural matching | Code (deterministic) |
| Maximum common subgraph | Partial structural matching | Code (deterministic) |
| Newman guard | Typed edge constraint with defect veto | Code (deterministic) |
| Equivocation test | Strip shared terms, check structural survival | Code (deterministic) |
| Four-rung grading | Grade with ceiling on what is not licensed | Code (deterministic) |
| Circular provenance detection | Source independence check | Code |
| Decidability check | Instrument capability map lookup | Code (deterministic) |
| Evidence join | ConTraSt database, 761 studies | Code (lookup) |
| Oracle review | Human stamps before public | Human |
| Provenance manifest | Source sentences, model versions, hashes | Code |
| Published rejections | Structural reason for every failed match | Code |

**Every row labelled "deterministic" produces the same output for the same input, verifiable by content hash.** This is the constitutional line: the judge is never a model.

## The five quality gates

Between the model's extraction output and any published verdict, five gates must pass:

1. **Schema validation.** Pydantic enforces that every extracted claim has all required fields with correct types. Malformed output is rejected and retried twice, then flagged.
2. **Cross-model agreement.** A second model independently re-derives entity type, axis and polarity for every claim; in the validated build this is Claude Haiku. A different training family checker is the design target. Structural agreement required. Disagreements flagged for human review, never silently passed.
3. **Adversarial calibration.** The calibration set contains deliberately convincing fakes. The system's detection rate on known fakes is measured and reported.
4. **Human review.** Every claim reviewed by a human before it counts in public output. Approvals stamp the record.
5. **Trust tier labelling.** Every published claim carries a tier label (Tier A signed, Tier B machine-extracted, User-amended). Nothing unlabelled ships.

## What the architecture is NOT

- Not an embedding similarity system (V1 was, it failed)
- Not a fine-tuned model (no LoRA, no domain adapters)
- Not a multi-agent debate system (designed one, shelved it deliberately)
- Not an end-to-end paper-writing system (those multiply unverified output)
- Not a knowledge graph within one domain (those cannot cross vocabulary walls)
- Not a probabilistic system (every judgment is deterministic)

## Determinism guarantee

Same inputs, same judge code version, same ontology version, same capability map version: same output. Content hash verifiable. The CI workflow runs this check on every commit. If determinism breaks, the commit is blocked.

This is not an aspiration. It is an enforced property of the system.
