# Claim Extraction and Typing (Product Side 1)

## What a typed claim card contains

Every scientific claim extracted by the engine becomes a structured object with these fields:

- **Claim kind:** domain-pack-scoped. The consciousness pack uses: locus, temporal_profile, connectivity, substrate_dependence, computability, mechanism, observable_commitment. The physics pack uses: substrate, mechanism, architecture, measurement, location, scale, boundary. Each domain pack defines which kinds are available.
- **Commitment direction:** asserts or denies. Negation is encoded as a polarity field on the claim, not as a separate claim kind. This keeps claim identity stable and makes forks computable as polarity disagreements on the same claim kind.
- **Causal direction:** causes, caused_by, bidirectional, or independent
- **Physical scale:** domain-pack-scoped. The consciousness pack uses quantum through phenomenal (7 levels). The physics pack adds planck and metaphysical (9 levels).
- **Measurability:** measurable now, measurable under assumption, or not measurable
- **Measurable with:** the specific instrument name, when measurable
- **Domain:** the field the source belongs to, used for cross-corpus gating (never match within the same domain)
- **Source sentence:** the exact sentence in the original paper this claim was extracted from
- **Provenance hash:** content hash linking back to the source document, page, and paragraph

## How extraction works

The model (Claude Sonnet) reads a text chunk and produces a JSON object conforming to the typed claim card schema. The output is constrained by the schema: the model cannot invent new claim kinds or leave fields empty. Pydantic validates every card. Malformed output is rejected and retried twice, then flagged for human review.

A second model (Claude Haiku) independently re-extracts the same passage as a cross-check. Structural agreement on the typed fields is required before a claim is match-eligible.

All extraction runs through Anthropic's Batch API at 50% cost. Total model cost for a six-theory corpus: under $15 at mid-2026 API pricing. Adding one new theory costs approximately $2.50 in model spend and 3 to 5 hours of human review.

## What extraction does NOT do

Extraction reads. It does not judge, grade, compare, or match. The model's job ends when the typed claim card is valid. Everything after extraction is deterministic code.

## Cross-model agreement

Every claim card destined for matching is independently re-extracted by a second model of different training lineage. Structural agreement on the typed fields is required before a claim is match-eligible. Disagreements are flagged for human review, never silently passed.

Why different lineage: models from the same training family share systematic blind spots. A claim that two same-family models agree on could reflect a shared bias rather than genuine accuracy. Different lineage makes agreement more meaningful.

## The JSON schema

See `judge/schema/claim_card.json` for the full Pydantic-exported schema.
