"""Reference VF2 matcher in judge/matching/vf2_typed.py.

This matcher is reference code. It did not produce the published
COGITATE result (see docs/validation.md). These tests pin what it does
today, including a known defect.
"""
import networkx as nx
import pytest

from judge.matching.vf2_typed import check_subgraph_isomorphism


def _pair(relation_b="causes", kind_b="k2"):
    a = nx.DiGraph()
    a.add_node("x", claim_kind="k", physical_scale="s")
    a.add_node("y", claim_kind="k2", physical_scale="s")
    a.add_edge("x", "y", relation="causes", causal_direction="forward")

    b = nx.DiGraph()
    b.add_node("p", claim_kind="k", physical_scale="s")
    b.add_node("q", claim_kind=kind_b, physical_scale="s")
    b.add_node("r", claim_kind="k3", physical_scale="s")
    b.add_edge("p", "q", relation=relation_b, causal_direction="forward")
    b.add_edge("q", "r", relation="inhibits", causal_direction="forward")
    return a, b


def test_typed_substructure_is_found():
    a, b = _pair()
    result = check_subgraph_isomorphism(a, b)
    assert result["is_isomorphic"] is True
    # The mapping is keyed by graph B's nodes (B -> A).
    assert result["mapping"] == {"p": "x", "q": "y"}


def test_mismatched_edge_type_vetoes_match():
    a, b = _pair(relation_b="inhibits")
    assert check_subgraph_isomorphism(a, b)["is_isomorphic"] is False


def test_mismatched_node_type_vetoes_match():
    a, b = _pair(kind_b="other")
    assert check_subgraph_isomorphism(a, b)["is_isomorphic"] is False


def test_content_hash_is_stable():
    a, b = _pair()
    assert (check_subgraph_isomorphism(a, b)["content_hash"]
            == check_subgraph_isomorphism(a, b)["content_hash"])


@pytest.mark.xfail(strict=True, reason=(
    "Known defect: the mapping is keyed by graph B's nodes but looked up "
    "with graph A's nodes, so matched_edges is always empty."))
def test_matched_edges_are_reported():
    a, b = _pair()
    assert len(check_subgraph_isomorphism(a, b)["matched_edges"]) == 1
