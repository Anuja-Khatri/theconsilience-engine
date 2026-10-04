# Experiment Design and Testability

## The decidability question

For every genuine disagreement the engine surfaces, it asks: can anyone alive today test this?

## The instrument capability map

A versioned structured data asset recording:
- Which instrument class exists (fMRI, EEG, MEG, TMS, optogenetics, calcium imaging, etc.)
- Which physical scale each instrument reaches (quantum, molecular, cellular, neural circuit, whole brain)
- Which observable each instrument measures (electrical activity, blood oxygenation, neurotransmitter concentration, etc.)
- The resolution limits of each instrument class

## Three possible outputs

**Testable now.** The instrument is named. The observable is named. The predicted split between the two theories is stated. An experiment sketch is generated: manipulated variable, discriminating observable, predicted outcome under each theory, estimated cost, estimated timeline, which type of lab can run it.

**Testable under a stated assumption.** The assumption is named explicitly. "If [assumption] holds, then [instrument] can discriminate by measuring [observable]." The assumption is not hidden.

**Not testable with current technology.** The specific structural reason is named. For example: "Both theories deny that [property] is substrate-level, so functional experiments measuring [property] at the [scale] level cannot separate them. The disagreement is about substrate, and no current instrument reads substrate at this scale."

## Version pinning

The instrument capability map is versioned. When instruments improve (new resolution, new instrument class), the map updates. Old verdicts stay valid under their original version. New verdicts use the updated map. Both coexist.

This means a decidability verdict from 2026 remains citable in 2030, even if a new instrument has since made the disagreement testable. The new verdict says "testable as of map version 2030-01." The old verdict says "not testable as of map version 2026-09." Both are true.

## Experiment sketch generation

For each testable disagreement, the engine generates:
- **Manipulated variable:** what the experiment changes
- **Discriminating observable:** what the experiment measures
- **Predicted split:** what each theory predicts the measurement will show
- **Falsification criteria:** what result would disprove each theory
- **Estimated cost:** order of magnitude
- **Estimated timeline:** weeks, months, or years
- **Lab requirements:** what kind of facility can run it
