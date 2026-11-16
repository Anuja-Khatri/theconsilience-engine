# The Consilience

**A deterministic verification engine for cross-domain scientific claim comparison.** Part of [The Consilience](https://theconsilience.io), the verification layer for AI-for-science.

> **What this repository is.** The specification, method documentation and papers for the claim-comparison engine. The code in `judge/` is an illustrative reference implementation of the rules, not the production judge. The consolidated judge (one schema, one judge) is in development; the lab-safety and data-validation components that run today live in [lab-gate](https://github.com/Anuja-Khatri/lab-gate) and [consilience-ledger](https://github.com/Anuja-Khatri/consilience-ledger).

[![Determinism](https://github.com/Anuja-Khatri/theconsilience-engine/actions/workflows/determinism.yml/badge.svg)](https://github.com/Anuja-Khatri/theconsilience-engine/actions/workflows/determinism.yml) ![Papers](https://img.shields.io/badge/papers-6%20on%20Zenodo-blue) ![License](https://img.shields.io/badge/license-Apache%202.0-orange)

---

## The problem

Everyone who works across scientific fields performs the same task by hand. They read two literatures. They hold two vocabularies in their head. And they decide whether two claims are the same claim wearing different clothes, whether they genuinely conflict, or whether they simply cannot be compared.

This work takes months. It does not scale. Its output is one person's opinion with a bibliography attached, and it cannot be reproduced, audited, or checked by anyone who was not in the room.

Large language models made generating such connections free, and simultaneously made trusting them impossible. A model will produce a fluent, plausible, uncheckable correspondence on demand. Ask it again tomorrow and it produces a different one.

The bottleneck moved. The question is no longer "can we find a connection." It is "can anyone verify the connection we found."

## The novel goal

**Build the verifier for cross-domain claim comparison.**

Mathematics has proof checkers: AlphaProof works because Lean verifies every step. Code has execution: AlphaEvolve works because candidate programs either run faster or they do not. Comparative theory analysis had nothing. No Lean. No execution. No verifier of any kind.

The Consilience is that verifier.

## Two product sides

**Side 1: Claim Extraction and Experiment Design.** The engine reads scientific papers and extracts typed claims with causal direction, physical scale, and exact source sentence. For each disagreement between two frameworks, it checks whether the disagreement is testable with instruments that exist today and generates discriminating experiment sketches with estimated cost, timeline, and falsification criteria.

**Side 2: Cross-Domain Structural Correspondence.** The engine takes two theories from different fields and compares their structural commitments rather than their vocabulary. Today the comparison runs on typed fields (axis, polarity, value and stated conditions) with a hard veto on mismatched axes and conditions; typed subgraph isomorphism over claim graphs is the design it is moving to. It grades each correspondence on a four-rung ladder with an explicit ceiling on what the match does and does not license. It records every rejection with the structural reason the match failed.

## Architecture

Neurosymbolic. Models extract typed claims under schema constraints. Code does all judgment. Status: **built** = runs in the published results; **in development** = specified, being implemented in the consolidated judge.

- **Typed field comparison** with a hard veto on mismatched axes and conditions (built)
- **Typed subgraph isomorphism** (VF2, 2004) for structural matching (in development)
- **Maximum common subgraph** for partial correspondence (in development)
- **Newman guard**: typed edge constraints where one mismatched relation type vetoes the entire correspondence
- **Equivocation removal test**: strip shared vocabulary, re-derive edges from typed graphs, check if structure survives (in development; a simpler edge-count check runs today)
- **Four-rung grading ladder** with machine-readable ceilings on what each verdict does not license
- **Versioned instrument capability map** for testability assessment
- **Recorded rejections** with structural reasons attached
- **Content hash verification**: same inputs, same output, every time, on any machine

The judge is never a language model. Given the same claim cards, the judge returns the same verdict, verifiable by content hash. Extraction (the model step) is not deterministic: test-retest stability is 0.25 to 0.42, below a 0.70 gate, so a person reviews every claim card.

## Validation

Blind tested against the COGITATE adversarial collaboration's preregistered predictions. The engine recovered 2 of 3 after a disclosed re-review (originally 1 of 3). Against a 1000-key permutation null this is p = 0.075, suggestive only. Full numbers: github.com/Anuja-Khatri/consilience-verification.

Live demo of the cross-theory comparison: [consilience-demo.netlify.app](https://consilience-demo.netlify.app).

## Published papers

| Paper | Title | DOI |
|---|---|---|
| Flagship | A deterministic, auditable engine for cross-theory claim comparison | [10.5281/zenodo.23672883](https://zenodo.org/records/23672883) |
| Lab safety | lab-gate: a plan-checking safety gate for autonomous labs, with a preregistered adversarial evaluation | [10.5281/zenodo.23954617](https://zenodo.org/records/23954617) |
| 1 | Deterministic Verification for Cross-Domain Scientific Claim Comparison (earlier version) | [10.5281/zenodo.23086966](https://zenodo.org/records/23086966) |
| 2 | Per-Instance Lexical Ablation as a Grading Mechanism | [10.5281/zenodo.23119443](https://zenodo.org/records/23119443) |
| 3 | Computational Testability Assessment | [10.5281/zenodo.23119362](https://zenodo.org/records/23119362) |
| 4 | Beyond the Transformer for Scientific Discovery | [10.5281/zenodo.23121190](https://zenodo.org/records/23121190) |

[All papers by Anuja Khatri on Zenodo](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Khatri%2C%20Anuja%22&sort=newest)

## Documentation

Full technical documentation at [docs/](docs/):

- [Mission and novel goal](docs/mission.md)
- [The six problems the architecture solves](docs/six-problems.md)
- [Architecture overview](docs/architecture.md)
- [Full 14-step pipeline](docs/full-pipeline-detail.md)
- [V1 embedding system: how it failed](docs/v1-failure.md)
- [The prediction that preceded the failure](docs/v1-prediction.md)
- [Six research programmes surveyed](docs/six-camps.md)
- [70+ AI-for-science systems studied](docs/ai-science-census.md)
- [Phase zero: authored artifacts that precede code](docs/phase-zero.md)
- [Claim extraction and typing](docs/claim-extraction.md)
- [Structural matching across vocabularies](docs/structural-matching.md)
- [Experiment design and testability](docs/experiment-design.md)
- [Four-rung grading ladder](docs/grading.md)
- [The equivocation test](docs/equivocation-test.md)
- [Structure-directed source acquisition](docs/structure-directed-acquisition.md)
- [Trust tiers](docs/trust-tiers.md)
- [One engine, four config points](docs/one-engine-principle.md)
- [Published rejections](docs/rejections.md)
- [Validation results](docs/validation.md)
- [Historical breakthrough examples](docs/breakthroughs.md)
- [Related systems](docs/adjacents.md)
- [Production infrastructure](docs/infrastructure.md)

## Build provenance

Architecture, ontology, typed schemas, grading rules, ceiling definitions, calibration set design, instrument capability map entries, and every kill decision are human-authored intellectual work. AI tools (Claude Code, Claude API) executed the engineering. The relationship is the same as a physicist using Mathematica to compute integrals while designing the experiment, or a researcher using a calculator while authoring the proof.

Every judgment rule in the `judge/` directory was human-specified. The code implements the rule. The rule is the contribution.

Full statement: [PROVENANCE.md](PROVENANCE.md)

## Product

[theconsilience.io](https://theconsilience.io)

## Author

Anuja Khatri
anuja@theconsilience.io
Bangalore, India

Methods, corrections and null results are published in the open.
