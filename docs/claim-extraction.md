# Claim Extraction and Typing (Product Side 1)

## What a typed claim card contains

Every scientific claim extracted by the engine becomes a structured object with these fields:

- **Claim kind:** location, timing, architecture, mechanism, computability, or substrate
- **Commitment direction:** asserts or denies
- **Causal direction:** X causes Y, Y causes X, or bidirectional
- **Physical scale:** quantum, molecular, cellular, neural circuit, whole brain, behavioural, or phenomenal
- **Measurability:** measurable now, measurable under assumption, or not measurable
- **Source sentence:** the exact sentence in the original paper this claim was extracted from
- **Provenance hash:** content hash linking back to the source document, page, and paragraph

## How extraction works

The model (Claude Haiku) reads a text chunk and produces a JSON object conforming to the typed claim card schema. The output is constrained by the schema: the model cannot invent new claim kinds or leave fields empty. Pydantic validates every card. Malformed output is rejected and retried twice, then flagged for human review.

For hard passages, Sonnet escalates. All extraction runs through Anthropic's Batch API at 50% cost.

## What extraction does NOT do

Extraction reads. It does not judge, grade, compare, or match. The model's job ends when the typed claim card is valid. Everything after extraction is deterministic code.

## Cross-model agreement

Every claim card destined for matching is independently re-extracted by a second model of different training lineage. Structural agreement on the typed fields is required before a claim is match-eligible. Disagreements are flagged for human review, never silently passed.

Why different lineage: models from the same training family share systematic blind spots. A claim that two same-family models agree on could reflect a shared bias rather than genuine accuracy. Different lineage makes agreement more meaningful.

## The JSON schema

See `judge/schema/claim_card.json` for the full Pydantic-exported schema.
