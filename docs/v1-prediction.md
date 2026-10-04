# The Prediction That Preceded the Failure

This is the most important fact in the project's technical history.

## The June 2026 architecture review

One month before V1 was killed, the June 2026 architecture review listed six hard limits of the essence layer. Limit number one reads:

> "X causes Y" and "Y causes X" can embed close together; the system cannot tell that two theories are making opposite directional claims. They look similar in essence-space.

## What happened one month later

That is precisely the mechanism that killed V1, written down a month before it happened.

## Why this matters

**The current architecture is not a reaction to V1's failure. It is the documented recommendation that preceded it.**

The review's top recommendation was: extract a structured claim object alongside the essence, with subject, relation, object, modality, polarity, and causal direction. That is the typed claim card the engine extracts today.

The failure only confirmed a diagnosis already on paper.

This means the architecture was not designed under pressure after a failure. It was designed carefully, from first principles, and the failure validated the design that was already waiting.
