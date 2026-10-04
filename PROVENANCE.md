# Build Provenance

## What is human intellectual work

Every design decision in this system was made by a human. Specifically:

**Architecture decisions:**
- The decision to kill V1 (three-level embedding, 6,341 false positives) and rebuild on neurosymbolic verification
- The choice of typed subgraph isomorphism over embedding similarity for structural matching
- The four-rung grading ladder design, including the ceiling statements that define what each rung does not license
- The equivocation removal test mechanism (per-instance lexical ablation at inference time)
- The Newman guard (typed edge constraint with single-defect veto)
- The decision that the judge is never a language model
- The five quality gates between extraction and verdict
- The cross-model agreement gate using a model of different training lineage
- Content hash verification as a determinism guarantee

**Authored artifacts (the moat):**
- The ontology: relation types, claim kinds, typed edge vocabulary. Every relation type was authored by hand to capture real distinctions between scientific commitments.
- The calibration set: deliberately convincing fakes designed to test whether the judge can be fooled. These were authored, not generated.
- The instrument capability map: which instrument class reaches which physical scale measuring which observable. This is domain expert knowledge encoded as structured data.
- The extraction prompts: ontology relation types embedded in the prompt, constraining what the model can extract. Authored, not default.

**Kill decisions:**
- V1 embedding architecture killed after structural audit (July 2026)
- BioDisco reference removed (unverifiable)
- FAME reference removed (hallucinated)
- Six hallucinated or wrong citations found and corrected across four papers before publication
- Multi-agent co-scientist loop designed, scheduled, then deliberately shelved (wrong shape for verification)
- LoRA fine-tuning deferred (insufficient training data, wrong feedback loop)
- General first-order logic layer deferred (too expensive at scale)

**Adoption and deferral decisions documented in Paper 4:**
- Six research programmes evaluated (Marcus, Kambhampati, Chollet, LeCun, Bengio, Scholkopf)
- Three adopted, three deferred, each with documented reasoning
- Seventy-plus AI-for-science systems censused, each evaluated against the six problems

## What AI tools did

- **Claude Code** executed engineering tasks from human specifications: function implementations, API integrations, frontend components, database migrations, deployment configuration
- **Claude API (Haiku and Sonnet)** runs the extraction pipeline: reading papers and producing typed claim cards under schema constraints. This is the neural half of the neurosymbolic architecture. The model reads. The code judges.
- **Claude (chat)** assisted with research, writing, editing, and drafting. Every paper, email, and document was reviewed and edited by the author.

## The distinction

A physicist uses Mathematica to compute integrals but designs the experiment. A chemist uses lab instruments to measure but designs the protocol. A researcher uses a calculator to verify arithmetic but authors the proof.

The Consilience uses AI tools for engineering execution and text processing. The architecture, the ontology, the grading rules, the evaluation design, and every decision about what to build, what to kill, and what to defer are human intellectual work.

The code in the `judge/` directory implements human-specified rules. The rules are the contribution. The code is the implementation.

## How to verify

Every judgment in this system is deterministic. Run the same inputs through the same judge code and you get the same output, verifiable by content hash. The CI workflow in `.github/workflows/determinism.yml` runs this check on every commit. The green badge on the README means it passed.

No other AI-for-science research tool can show this badge. That is the point.
