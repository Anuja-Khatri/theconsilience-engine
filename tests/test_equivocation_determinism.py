"""The equivocation output must be byte-identical across processes.

Python randomises string hashing per process, so iterating a set of
strings gives a different order in each run. The test runs the
equivocation check in two fresh interpreters with different hash seeds
and compares the serialised output byte for byte.
"""
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SCRIPT = r"""
import json
import networkx as nx
from judge.equivocation.lexical_ablation import equivocation_test

a = nx.DiGraph()
b = nx.DiGraph()
terms = ["workspace", "integration", "broadcast", "phi", "access",
         "ignition", "cause", "effect", "posterior", "prefrontal"]
for i, t in enumerate(terms):
    a.add_node(f"a{i}", terms=[t, "shared_" + t])
    b.add_node(f"b{i}", terms=[t])
for i in range(len(terms) - 1):
    a.add_edge(f"a{i}", f"a{i+1}", relation="causes")
    b.add_edge(f"b{i}", f"b{i+1}", relation="causes")

print(json.dumps(equivocation_test(a, b)))
"""


def _run(seed: str) -> bytes:
    env = dict(os.environ, PYTHONHASHSEED=seed)
    return subprocess.run(
        [sys.executable, "-c", SCRIPT],
        cwd=ROOT, env=env, capture_output=True, check=True,
    ).stdout


def test_equivocation_output_is_byte_identical_across_runs():
    outputs = {_run(seed) for seed in ("1", "2", "3", "4", "5")}
    assert len(outputs) == 1, "equivocation output order differs between runs"


def test_two_runs_same_seedless_environment_match():
    # Two default runs (random hash seed each time) must also agree.
    env = {k: v for k, v in os.environ.items() if k != "PYTHONHASHSEED"}
    runs = [
        subprocess.run([sys.executable, "-c", SCRIPT], cwd=ROOT, env=env,
                       capture_output=True, check=True).stdout
        for _ in range(2)
    ]
    assert runs[0] == runs[1]
