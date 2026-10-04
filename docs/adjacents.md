# Related Systems

Technical notes on adjacent tools and where Consilience sits relative to them.

| System | What it does | What it does not do | Where Consilience differs |
|---|---|---|---|
| **Semantic Scholar** | Finds and ranks papers by citation graph | Does not compare claim structures | Consilience compares structural commitments, not documents |
| **Elicit** | Extracts claims from papers, answers questions | Does not grade structural correspondence | Consilience grades with ceilings and publishes rejections |
| **Consensus** | Finds scientific consensus from papers | Does not handle cross-domain vocabulary walls | Consilience strips vocabulary and matches structure |
| **NotebookLM** | Summarises uploaded documents | Ungraded, non-reproducible, changes every run | Consilience is deterministic and hash-verifiable |
| **ChatGPT / Claude** | Generates plausible comparisons | Changes every time, no structural proof | Consilience gives same answer every time with structural receipts |
| **ClaimFlow** | Tracks claim evolution within NLP through citation chains | Within-field only, not cross-domain | Consilience matches across fields with different vocabularies |
| **SciAgents** | Multi-agent graph reasoning for discovery in materials science | Single domain, model has last word | Consilience crosses domains, code has last word |
| **Co-Scientist** | Seven-agent hypothesis generation | Self-evaluation unreliable (their own admission) | Consilience uses external verification, not self-evaluation |
| **AlphaProof** | Model generates, Lean verifies (mathematics) | Total verifier: mathematics has proof checkers | Consilience builds a partial verifier for empirical science (no Lean exists here) |
| **Matter-of-Fact** | Single claim feasibility in materials science | Individual claims within one field | Consilience checks cross-domain disagreement testability |

## The gap Consilience occupies

Every system above is either a retrieval tool (finds documents), a generation tool (produces hypotheses), or a within-domain tool (works inside one field).

Nobody occupies the layer between retrieval and expert judgment for cross-domain structural comparison. That is where Consilience sits.
