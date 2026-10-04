# Six Research Programmes Surveyed

Six serious research programmes argue that language models alone cannot do reliable scientific reasoning. Each proposes something different. We surveyed all six and built a production system on top of three of them. Paper 4 documents every adoption and deferral decision.

## 1. Gary Marcus: the neurosymbolic thesis

**Argument:** LLMs are pattern recognisers, not reasoners. Scaling will not fix this. The future is hybrid: neural networks for perception, symbolic systems for reasoning.

**Verdict: ACCEPTED.** This IS the architecture family. Consilience is neurosymbolic in the strict sense: neural reading, symbolic judgment. Naming it correctly matters because it is a recognised family rather than a workaround.

## 2. Subbarao Kambhampati: LLM Modulo and external verifiers

**Argument:** LLMs are non-veridical memory systems with no internal world model. Keep the LLM for language and retrieval. Pair it always with an external verifier. The LLM proposes; a classical solver disposes. No output reaches the user without passing a non-LLM check. His data: autonomous LLM plans are correct roughly 12% of the time.

**Verdict: ACCEPTED as the governing pattern.** The single most load-bearing idea in the system. Everything downstream, the deterministic judge, the cross-model agreement gate, the five quality gates, is LLM Modulo applied to claim comparison.

## 3. Yoshua Bengio: the generator-estimator split

**Argument:** Imitation-trained models treat all text as truth. The alternative: a generator proposes, a neutral estimator scores, and they cannot be the same network. Output as Bayesian posteriors with externalised reasoning.

**Verdict: ACCEPTED in principle, adapted in implementation.** The generator-estimator separation is the same commitment as LLM Modulo, arrived at from a different direction. What was NOT adopted: the estimator as a neural network producing posteriors. Our estimator is deterministic code producing a grade, because a probabilistic estimator still drifts across runs.

## 4. François Chollet: program synthesis

**Argument:** Intelligence is the efficiency of acquiring new skills from few examples. LLMs have enormous skill and minimal fluid intelligence. Deep-learning-guided program synthesis is the alternative.

**Verdict: DEFERRED.** Relevant to generation (sampling the space of candidate correspondences), not verification. Held as a Phase 2 option. Never built because the project's identity settled on verification, and because Ndea (Chollet's company) is pre-product with a three-to-five-year research horizon.

## 5. Yann LeCun: JEPA and world models

**Argument:** LLMs cannot reach advanced intelligence because they are trained on text, which is a serialisation of reasoning rather than reasoning itself. Real understanding requires world models that predict in latent space. The variant that mattered most: Meta's Large Concept Models (LCMs), which process sentence embeddings rather than tokens.

**Verdict: STUDIED, NOT ADOPTED.** Two reasons. First, buildability: LCMs operate in a trained latent space and closing that gap means training a foundation model, not a solo-founder project. Second, and decisive: JEPA changes how a model reads. It does not change who judges. Even if JEPA replaced transformers entirely tomorrow, the system would swap its reader and keep its judge.

## 6. Bernhard Scholkopf: causal representation learning

**Argument:** Observations are generated from low-dimensional causal variables projected into high-dimensional data. Current ML learns the projection and not the generators. Three principles: independent causal mechanisms, disentanglement, and invariance across environments.

**Verdict: ADOPTED as the framing and evaluation standard, not as machinery.** No formal disentanglement implemented. No identifiability proof attempted. What was adopted: the standard that the structural representation of a passage should be the same whether expressed in physics, Vedanta, or phenomenology. The calibration set tests exactly this, that fakes fail and genuine cross-vocabulary correspondences pass. Invariance across traditions is the evaluation criterion.

---

## Summary

| Programme | Verdict | What was adopted |
|---|---|---|
| Marcus (neurosymbolic) | ACCEPTED | Architecture family identity |
| Kambhampati (LLM Modulo) | ACCEPTED | Governing pattern: models extract, code judges |
| Bengio (generator-estimator) | ACCEPTED (adapted) | Separation principle; estimator is code not neural network |
| Chollet (program synthesis) | DEFERRED | Held as Phase 2 option for generation |
| LeCun (JEPA/world models) | STUDIED, NOT ADOPTED | Changes reader not judge; not buildable solo |
| Scholkopf (causal representation) | ADOPTED (framing only) | Evaluation standard: invariance across traditions |
