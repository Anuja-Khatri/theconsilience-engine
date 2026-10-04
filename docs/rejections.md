# Published Rejections

## Why rejections matter

Every existing tool shows what it found. None show what they refused. This is the core trust problem: a system that only publishes successes has no accountability for false positives.

The Consilience publishes every rejected match with the specific structural reason it failed.

## What a published rejection contains

- **The pair:** which two claims were compared
- **The rung that would have been assigned** if the match had passed
- **The specific structural defect** that caused the rejection
- **The defect type:** type mismatch (wrong edge type), direction mismatch (opposite causal arrows), vocabulary dependence (equivocation test failure), provenance circularity, or insufficient structural coverage
- **The exact edge or node** where the match broke

## Why this is the trust artifact

A system that publishes its failures is harder to game than one that only publishes its successes.

A researcher looking at Consilience output can check: "this pair was rejected because the causal direction is opposite. Edge 3 in Theory A has 'causes' but the corresponding edge in Theory B has 'is_caused_by.' I can verify this by reading the source sentences."

That is inspectable. That is auditable. That is what no other tool provides.

## The incentive structure

Other tools optimise for recall: show as many connections as possible. Consilience optimises for precision: show only the connections that survive structural verification.

This is a deliberate design decision. Researchers who have been burned by false positives, who need to trust that a claimed correspondence is real before committing years of work to testing it, need precision over recall. Consilience is built for that researcher.

## Published counts

- **Consciousness demo (IIT x GNWT pair):** 21 published rejections
- **Physics workspace (81 sources across 7 domains):** 162 published rejections
