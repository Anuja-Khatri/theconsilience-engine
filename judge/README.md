# The Deterministic Judge

This directory contains reference code for the judge: the deterministic layer that grades, runs the equivocation check and assesses testability. No model touches this code's output. It is not the matcher that produced the published COGITATE result (a rule-based typed matcher, not in this repository). Tests are in `../tests/`.

## Components

- `schema/` — JSON schemas for typed claim cards, correspondences, rejections, and instrument entries
- `matching/` — reference VF2 subgraph isomorphism with typed node and edge constraints (in development: it does not yet report matched edges; maximum common subgraph is not implemented)
- `grading/` — Four-rung grading ladder with ceiling statements
- `equivocation/` — Lexical ablation check: remove nodes carrying each shared term and count the edges left (re-deriving edges after stripping is in development). Output order is sorted, so it is byte-identical across runs
- `testability/` — Versioned instrument capability map lookup
- `hash/` — Content hash verification (run twice, compare hashes)

## What is included

The mechanism code: how matching, grading, equivocation testing, and testability checking work. These implement human-specified rules as deterministic functions.

## What is NOT included

The authored assets: ontology entries (relation types, claim kinds), calibration set (the fakes), instrument capability map data (specific instruments and scales), and extraction prompts. These are the moat. The mechanism is open. The data the mechanism operates on is not published.

## Running the determinism demo

From the repository root:

```bash
pip install -r requirements.txt
python examples/determinism-demo/run_demo.py
python -m pytest -q tests
```

The demo grades one input twice in one process and compares hashes. The test suite also checks the equivocation output across separate processes.
