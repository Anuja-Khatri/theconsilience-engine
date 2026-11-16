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

**Side 1: Claim Extraction and Experiment Design.** Typed claims (causal direction, physical scale, exact source sentence) are drafted from scientific papers by a model and reviewed by a person before the judge sees them. No extraction code is in this repository. For each disagreement between two frameworks, the judge checks whether the disagreement is testable with instruments that exist today; the published demo also produced experiment sketches with estimated cost, timeline and falsification criteria.

**Side 2: Cross-Domain Structural Correspondence.** The engine takes two theories from different fields and compares their structural commitments rather than their vocabulary. Today the comparison runs on typed fields (axis, polarity, value and stated conditions) with a hard veto on mismatched axes and conditions; typed subgraph isomorphism over claim graphs is the design it is moving to. It grades each correspondence on a four-rung ladder with an explicit ceiling on what the match does and does not license. It records every rejection with the structural reason the match failed.

## Architecture

Neurosymbolic. Models draft typed claims under schema constraints; a person reviews them; code does all judgment. Status: **built** = runs in the published results; **reference code** = in `judge/` here, tested, but not what produced the published results; **in development** = specified, not yet implemented.

- **Rule-based typed matcher** over typed claim fields (axis, polarity, value, stated conditions) with a hard veto on mismatched axes and conditions (built; this is the matcher behind the COGITATE result; it is not in this repository — a public version of the field comparison is in [consilience-ledger](https://github.com/Anuja-Khatri/consilience-ledger))
- **Four-rung grading ladder** with a ceiling statement on what each rung does not license (reference code: `judge/grading/`)
- **Equivocation check**: remove the nodes that carry a shared term from both graphs and count the edges left; zero edges on either side marks the correspondence vocabulary-dependent (reference code: `judge/equivocation/`). Re-deriving edges from the typed graphs after stripping is in development
- **Versioned instrument capability map lookup** for testability: testable now, testable under a named assumption, or not testable with a reason (reference code: `judge/testability/`)
- **Content hash** over each verdict, so two runs can be compared (reference code: `judge/hash/`)
- **Typed subgraph isomorphism** (VF2, 2004) with typed node and edge constraints, where one mismatched relation type vetoes the match (the Newman guard) (in development; a reference matcher is in `judge/matching/`, but it does not yet report matched edges, a known defect pinned in the tests)
- **Maximum common subgraph** for partial correspondence (in development; no code yet. The grading ladder takes an `mcs_ratio` argument, but nothing here computes it)
- **Recorded rejections** with structural reasons attached (built in the published demo; not in this repository)

The judge is never a language model. Given the same claim cards, the judge is designed to return the same verdict, checkable by content hash; the tests run the reference code in separate processes and compare the output byte for byte. Extraction (the model step) is not deterministic: test-retest stability is 0.25 to 0.42, below a 0.70 gate, so a person reviews every claim card.

## Validation

Blind tested against the COGITATE adversarial collaboration's preregistered predictions, using the rule-based typed matcher (not the reference VF2 code in `judge/`). The engine recovered 2 of 3 preregistered disagreements after a disclosed re-review (originally 1 of 3). Against a 1,000-key permutation null this is p = 0.075, suggestive only. Method and full numbers: the flagship paper, [10.5281/zenodo.23672883](https://zenodo.org/records/23672883), and [docs/validation.md](docs/validation.md).

Live demo of the cross-theory comparison: [consilience-demo.netlify.app](https://consilience-demo.netlify.app).

## Running the tests

Needs Python 3.10 or later.

```bash
git clone https://github.com/Anuja-Khatri/theconsilience-engine.git
cd theconsilience-engine
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q tests
python examples/determinism-demo/run_demo.py
```

The suite covers the reference judge code in `judge/`: the grading ladder, the equivocation check (including a byte-identical output check across processes), the reference VF2 matcher, the capability-map lookup and the verdict hash. It does not reproduce the COGITATE result; that ran on the rule-based matcher described above.

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
