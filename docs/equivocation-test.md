# The Equivocation Test

## Newman's 1928 vulnerability

M. H. A. Newman showed in 1928 that if relations carry no types, any two systems of the same cardinality share structure trivially. This means structural correspondence claims are vacuous unless the relations are typed. A match that works with any relation type could match anything.

## The standard fix and its limit

Analogical reasoning benchmarks typically filter lexical overlap out of the test set at construction time. The SCAR benchmark, for instance, removes surface-similar examples before evaluation.

This fixes the benchmark but not the real world. In production, you cannot pre-filter the corpus. You need to handle equivocation on each comparison individually.

## The Consilience fix: per-instance lexical ablation at inference time

When a candidate match rests on a shared term (both theories use the word "information," both use "consciousness," both use "energy"), the system:

1. Strips the shared term from both sides
2. Re-derives edges from the typed graphs alone, using only the remaining structural commitments
3. Checks whether any honest edge survives

**If structure survives:** the correspondence is real but capped at Rung 3 (generative analogy) pending resolution. The shared term was not doing all the work.

**If nothing survives:** the match was vocabulary-dependent. The Newman guard vetoes. The item grades as Rung 4 (thematic resonance, quarantined). The shared term was the only thing connecting them.

## Worked example

IIT and GNW both use the word "information." High cosine similarity. The equivocation test strips "information" from both graphs and re-derives edges.

**IIT without "information":** retains edges about integration, exclusion, and intrinsic causal power. The structural commitments survive because they are about a specific mathematical property (phi) that does not depend on the word "information."

**GNW without "information":** retains edges about global broadcasting, prefrontal-parietal networks, and ignition threshold. The structural commitments survive because they are about a specific neural mechanism that does not depend on the word "information."

**Result:** Both theories have structural content beyond the shared term. The correspondence is real at the structural level, not just a vocabulary coincidence. But the specific MEANING of "information" differs between the theories, so the correspondence is capped at Rung 2, not Rung 1.

## Connection to cheminformatics

Molecular substructure search has enforced typed matching for decades. A carbon-carbon double bond must match a carbon-carbon double bond, not any bond. Nobody in cheminformatics would accept an untyped structural match. The Consilience applies the same discipline to scientific claims.

The field just never called it Newman's guard.

## Pseudocode

```
function equivocation_test(pair, shared_terms):
    for term in shared_terms:
        graph_a_stripped = remove_term(pair.graph_a, term)
        graph_b_stripped = remove_term(pair.graph_b, term)
        surviving_edges = re_derive_edges(graph_a_stripped, graph_b_stripped)
        if len(surviving_edges) == 0:
            return VOCABULARY_DEPENDENT  # Newman veto
    return STRUCTURALLY_SUPPORTED  # cap at Rung 3 pending resolution
```
