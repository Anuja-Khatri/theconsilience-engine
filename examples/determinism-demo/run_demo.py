"""
Determinism Demo

Run the same comparison twice and verify the hashes match.
This is the proof that the judge is deterministic.
"""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from judge.hash.determinism_check import compute_verdict_hash, verify_determinism
from judge.grading.four_rung_ladder import assign_rung

# Example: two theories with a partial structural match
# Run the grading twice with identical inputs

inputs = {
    "is_isomorphic": False,
    "mcs_ratio": 0.75,
    "equivocation_survived": True,
    "has_defect_edge": False
}

# Run 1
verdict_1 = assign_rung(**inputs)
verdict_1["inputs"] = inputs

# Run 2 (identical)
verdict_2 = assign_rung(**inputs)
verdict_2["inputs"] = inputs

# Verify
result = verify_determinism(verdict_1, verdict_2)

print("=" * 60)
print("DETERMINISM DEMO")
print("=" * 60)
print(f"Run 1 result: Rung {verdict_1['rung']}")
print(f"Run 1 hash:   {result['hash_1']}")
print(f"Run 2 result: Rung {verdict_2['rung']}")
print(f"Run 2 hash:   {result['hash_2']}")
print(f"Match:        {result['match']}")
print(f"Message:      {result['message']}")
print("=" * 60)

if not result["match"]:
    sys.exit(1)
