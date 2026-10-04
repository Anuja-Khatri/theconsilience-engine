# Phase Zero: Authored Artifacts That Precede Code

The engine cannot be built without three authored artifacts. They were treated as gates rather than documentation. No code was written until all three existed.

## 1. The ontology

The relation types that edges must conform to. Claim kinds (location, timing, architecture, mechanism, computability, substrate). Commitment directions. Physical scales. Measurability classes.

Every relation type was authored by hand to capture real distinctions between scientific commitments. "Causes" is different from "is_substrate_of" is different from "is_measured_by." These distinctions cannot be automated because they are the thing being enforced. A model trained on text would smooth them into similarity. The ontology keeps them sharp.

This is the non-automatable artifact at the core of the system. It is also the primary moat: extending the engine to a new domain means authoring a new domain pack, which takes weeks of expert work per field.

## 2. The calibration set

Deliberately convincing fakes designed to test whether the judge can be fooled. Each fake looks like a real structural correspondence. It uses plausible vocabulary. It has the right shape. But it is structurally wrong: a causal direction is reversed, a substrate is misidentified, a mechanism is attributed to the wrong theory.

The calibration set exists to answer one question: if the system accepts these, it cannot be trusted on real data.

Authored, not generated. A model cannot author fakes that test the model's own blind spots because it shares those blind spots.

## 3. The instrument capability map

Structured data recording which instrument class reaches which physical scale measuring which observable. This is domain expert knowledge encoded as queryable data.

The map is versioned. When instruments improve, the map updates, but old decidability verdicts stay valid under their original version. New verdicts coexist rather than overwrite.

This is the artifact that enables the decidability check: can anyone alive today test this disagreement? Without the map, the question is unanswerable. With the map, it is a deterministic lookup.

## Why these are the moat

All three artifacts are authored, not computed. No shortcut exists. Extending the engine to a new domain (materials science, ecology, condensed matter physics) requires authoring all three for that domain. The code is open. The authored assets are not published. This is the protection line: mechanism is public, authored assets are private.
