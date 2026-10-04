# Validation Results

## The benchmark: COGITATE adversarial collaboration

An international adversarial collaboration funded by the Templeton World Charity Foundation. Eleven laboratories. Nineteen months. Roughly $20 million in programme cost. Expert workshops requiring travel, months of reading, manual claim extraction, and negotiation between theory founders.

The collaboration compared two theories: Integrated Information Theory (Tononi) and Global Neuronal Workspace Theory (Dehaene). Expert panels including the founders of both theories spent about a year negotiating three testable predictions between them.

This is the manual process the engine replaces.

## What the engine did

Running blind, with the expert comparisons held out of its corpus, the engine:

1. Read the published theory papers for both IIT and GNW
2. Extracted typed claim cards from each (81 approved claims across the full corpus of six theories)
3. Built typed directed graphs
4. Applied deterministic typed matching with neighbourhood support checks
5. Graded every correspondence and identified every disagreement
6. Checked each disagreement against the instrument capability map
7. Published 21 rejections on the IIT x GNW pair with structural reasons

## The result

The engine recovered two of the three preregistered disagreements exactly, and the third partially. The missing component was a threshold negotiated between scientists in a room, absent from every theory's published text. The partial miss is itself the proof of no training leakage: the engine found what was in the papers, not what was decided in the workshop.

It also surfaced one disagreement the experts could not resolve: a substrate-level divergence that the decidability check correctly ruled untestable and attached the specific structural reason (both theories deny a specific property at the substrate level, so functional experiments cannot separate them at that level).

## The consciousness demo in numbers

| Number | What it is |
|---|---|
| 6 | Theories in the corpus (IIT, GNWT, Orch-OR, NREP, Active Inference, CEMI) |
| 81 | Approved claims across the corpus (extraction + cross-check + human oracle review) |
| 21 | Published rejections on the IIT x GNWT pair, each with structural reason |
| 761 | Studies in the ConTraSt evidence database (Yaron, Melloni, Pitts & Mudrik, 2022) |
| 78 | ConTraSt finding-tags approved for the tag mapping (out of 88; 10 omitted rather than guessed) |
| 36 | Experiment sketches generated |
| 18 | Standing predictions filed against INTREPID before results were published |
| 26 | Automated tests in the suite (graph integrity, grade distributions, holdout absence, fixture stability) |
| 7 | Seconds for full regeneration from results to rendered screens |
| ~$15 | Total model cost for the full corpus at mid-2026 API pricing |

## The physics workspace demo

A second demo was built for a US institution whose research programme spans physics and philosophical traditions. The engine handled 81 sources across unified field theory, Vedantic texts, neuroscience, condensed matter physics, developmental biology, population ecology, and formal language theory.

**Implementation note:** In this demo, matching and audit ran on prompted model agents, not the production deterministic judge. The port to the production VF2 judge is a named next step. The intellectual architecture was identical (extract, match, grade, decidability, experiments, rejections), but the matching step was non-deterministic. The audit discipline was the mitigation: of 62 initial matches, 55 were quarantined or rejected (~89% rejection rate). Only 4 survived the strict 5-criterion quality audit.

A post-build literature audit reclassified most survivors as blind recoveries of known correspondences, keeping two genuinely novel claims. This is published as a correction.

**The physics demo in numbers:**

| Number | What it is |
|---|---|
| 81 | Sources across 7 domains |
| 515 | Typed structural claims extracted (later 615 with supplementary) |
| 62 | Initial matches |
| 55 | Quarantined or rejected (~89%) |
| 4 | Survivors of strict quality audit (~6%) |
| 162 | Published rejections with structural reasons |
| 32 | Experiment paths (19 decidable-now, 13 conditional) |

## What this evaluation is NOT

Most AI-for-science papers evaluate on benchmarks: held-out test sets, accuracy scores, leaderboard positions. This evaluation is different. It tested against a real, preregistered, expert-conducted adversarial collaboration with published results. The experts did not design the evaluation for the engine. The engine was designed to handle the task the experts had already done, blind.

This kind of evaluation is rare. It is also the most honest test available: can the system do what experts do, on the experts' own task, without seeing their answers?
