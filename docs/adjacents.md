# Related Systems

Technical notes on adjacent tools and where Consilience sits relative to them.

| System | What it does | Scope | Consilience's approach |
|---|---|---|---|
| **Semantic Scholar** | Finds and ranks papers by citation graph | Does not compare claim structures | Consilience compares structural commitments, not documents |
| **Elicit** | Extracts claims from papers, answers questions | Does not grade structural correspondence | Consilience grades with ceilings and publishes rejections |
| **Consensus** | Finds scientific consensus from papers | Does not handle cross-domain vocabulary walls | Consilience strips vocabulary and matches structure |
| **NotebookLM** | Summarises uploaded documents | Ungraded, non-reproducible, changes every run | Consilience is deterministic and hash-verifiable |
| **ChatGPT / Claude** | Generates plausible comparisons | Changes every time, no structural proof | Consilience is deterministic and records the structural basis of each verdict |
| **ClaimFlow** | Tracks claim evolution within NLP through citation chains | Within-field only, not cross-domain | Consilience matches across fields with different vocabularies |
| **SciAgents** | Multi-agent graph reasoning for discovery in materials science | Single domain, model has last word | Consilience crosses domains, code has last word |
| **Co-Scientist** | Seven-agent hypothesis generation | Relies on model self-evaluation | Consilience uses external verification, not self-evaluation |
| **AlphaProof** | Model generates, Lean verifies (mathematics) | Total verifier: mathematics has proof checkers | Consilience builds a partial verifier for empirical science (no Lean exists here) |
| **Matter-of-Fact** | Single claim feasibility in materials science | Individual claims within one field | Consilience checks cross-domain disagreement testability |

## Where Consilience sits

The systems above fall broadly into retrieval tools (finding documents), generation tools (producing hypotheses), and within-domain tools (working inside one field).

Consilience works in the layer between retrieval and expert judgment: comparing structural commitments across domains, with deterministic grading and published rejections. It is complementary to these systems rather than a replacement for them.
