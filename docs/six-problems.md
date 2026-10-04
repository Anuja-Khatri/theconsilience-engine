# The Six Problems the Architecture Had to Solve

Stated in the June 2026 architecture review. Still the correct decomposition. Every component in the engine maps to one or more of these.

## 1. Cross-vocabulary matching

**Problem:** Find that two terms from different fields may point at the same structure when they share no words.

**Example:** "quantum vacuum" in physics and "sunyata" in Buddhist philosophy. No shared vocabulary. Standard embeddings would never pair them. Yet they may describe the same structural commitment about a ground state from which observable phenomena arise.

**What solves it:** Typed claim extraction into a shared schema, followed by structural matching on the schema rather than the words. The vocabulary is stripped. The structure is compared.

**Failure mode without it:** False negatives. Real structural correspondences between fields with different vocabularies are never found.

## 2. Structural guarantees

**Problem:** Distinguish "X causes Y" from "Y causes X." Two theories can use the same concepts with opposite causal arrows.

**Example:** Penrose commits to quantum collapse causing consciousness. Hoffman commits to consciousness causing physics-as-interface. Same concepts. Opposite arrows. An embedding system calls them a match. They are saying opposite things.

**What solves it:** Causal direction as a first-class field on every extracted claim. Typed edge constraints that require direction to match, not just content. One mismatched direction vetoes the correspondence.

**Failure mode without it:** False positives. Theories with opposite causal commitments are reported as corresponding. This is the specific mechanism that killed V1.

## 3. Causal reasoning

**Problem:** Handle interventions and counterfactuals, not just similarity neighbourhoods. "If we intervene on X, does Y change?" is a different question from "are X and Y close in embedding space?"

**What solves it:** Typed graphs with causal edge types (causes, is_substrate_of, is_measured_by) that preserve interventional structure. The matching algorithm tests causal compatibility, not just proximity.

**Failure mode without it:** The system cannot distinguish correlation from causation in the theories it compares.

## 4. Diverse hypothesis generation

**Problem:** Return the plausible space of possible correspondences, not one mode-collapsed answer.

**What solves it:** The fork ledger. Every genuine disagreement is surfaced alongside every correspondence. The output is a map of agreements, disagreements, and untestable questions, not a single verdict. The researcher sees the full landscape and decides.

**Failure mode without it:** The system hides uncertainty behind a single confident answer. This is the ChatGPT failure mode.

## 5. Formal verification

**Problem:** Check that a claimed correspondence actually follows from the structural commitments of both theories.

**What solves it:** Typed subgraph isomorphism (VF2). A correspondence is confirmed only when one theory's typed graph structure maps exactly onto a substructure of the other theory's typed graph, with matching node types and edge types. Partial matches are graded by maximum common subgraph ratio. Nothing is claimed without structural evidence.

**Failure mode without it:** Correspondences are asserted without structural proof. This is what every existing tool does.

## 6. Measured translation accuracy

**Problem:** Know whether the structure survived the translation from one vocabulary to another, not merely whether the cosine score stayed high.

**What solves it:** The equivocation removal test. For any correspondence resting on a shared term, strip the term and re-derive edges from typed graphs alone. If structure survives, the correspondence is real. If it does not, the shared term was doing all the work. This is measured, not guessed.

**Failure mode without it:** Vocabulary coincidences are reported as structural correspondences. This is the most common false positive in cross-domain comparison and the one no other tool catches.
