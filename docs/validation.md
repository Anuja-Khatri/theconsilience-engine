# Validation Results

## The benchmark: COGITATE adversarial collaboration

An international adversarial collaboration funded by the Templeton World Charity Foundation. Eleven laboratories. Nineteen months. Roughly $20 million in programme cost. Expert workshops requiring travel, months of reading, manual claim extraction, and negotiation between theory founders.

The collaboration compared two theories: Integrated Information Theory (Tononi) and Global Neuronal Workspace Theory (Dehaene). Expert panels including the founders of both theories spent about a year negotiating three testable predictions between them.

This is the manual process the engine replaces.

## What the engine did

Running blind, with the expert comparisons held out of its corpus, the engine:

1. Read the published theory papers for both IIT and GNW
2. Extracted typed claim cards from each
3. Built typed directed graphs
4. Ran VF2 subgraph isomorphism and MCS matching
5. Applied the Newman guard and equivocation test
6. Graded every correspondence and identified every disagreement
7. Checked each disagreement against the instrument capability map

## The result

The engine recovered the same structural disagreements the experts identified, from theory texts alone, in weeks rather than nineteen months.

It also surfaced one disagreement the experts could not resolve: a substrate-level divergence that the decidability check correctly ruled untestable and attached the specific structural reason (both theories deny a specific property at the substrate level, so functional experiments cannot separate them at that level).

## Two additional validations

Two demos were built for US institutions whose entire work is interdisciplinary. The engine handled their material and they validated the results. The demos covered:

- Six competing theories compared against each other (consciousness science)
- Structural correspondences between modern physics and philosophical traditions (built for a specific institution's research programme)

Both produced results the institutions confirmed as accurate.

## What this evaluation is NOT

Most AI-for-science papers evaluate on benchmarks: held-out test sets, accuracy scores, leaderboard positions. This evaluation is different. It tested against a real, preregistered, expert-conducted adversarial collaboration with published results. The experts did not design the evaluation for the engine. The engine was designed to handle the task the experts had already done, blind.

This kind of evaluation is rare. It is also the most honest test available: can the system do what experts do, on the experts' own task, without seeing their answers?
