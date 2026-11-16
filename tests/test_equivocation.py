"""Equivocation check as it runs today: remove nodes carrying a shared
term, then count min(edges left in A, edges left in B)."""
import networkx as nx

from judge.equivocation.lexical_ablation import (
    equivocation_test, find_shared_terms, strip_term_and_check)


def _chain(prefix, terms_per_node):
    g = nx.DiGraph()
    for i, terms in enumerate(terms_per_node):
        g.add_node(f"{prefix}{i}", terms=terms)
    for i in range(len(terms_per_node) - 1):
        g.add_edge(f"{prefix}{i}", f"{prefix}{i+1}")
    return g


def test_no_shared_terms():
    a = _chain("a", [["x"], ["y"]])
    b = _chain("b", [["p"], ["q"]])
    assert equivocation_test(a, b) == {
        "shared_terms": [], "overall_verdict": "no_shared_terms", "results": []}


def test_shared_terms_found():
    a = _chain("a", [["field"], ["y"]])
    b = _chain("b", [["field"], ["q"]])
    assert find_shared_terms(a, b) == {"field"}


def test_structure_survives_when_edges_remain():
    a = _chain("a", [["field"], ["y"], ["z"]])
    b = _chain("b", [["field"], ["q"], ["r"]])
    result = strip_term_and_check(a, b, "field")
    assert result == {"term": "field", "surviving_edges": 1,
                      "verdict": "structurally_supported"}


def test_vocabulary_dependent_when_no_edges_remain():
    a = _chain("a", [["field"], ["y"]])
    b = _chain("b", [["field"], ["q"]])
    out = equivocation_test(a, b)
    assert out["overall_verdict"] == "vocabulary_dependent"
    assert out["results"][0]["surviving_edges"] == 0


def test_term_removal_is_case_insensitive():
    a = _chain("a", [["Field"], ["y"]])
    b = _chain("b", [["field"], ["q"]])
    assert strip_term_and_check(a, b, "FIELD")["surviving_edges"] == 0


def test_shared_terms_and_results_are_sorted():
    a = _chain("a", [["zeta"], ["alpha"], ["mu"], ["x"]])
    b = _chain("b", [["mu"], ["zeta"], ["alpha"], ["y"]])
    out = equivocation_test(a, b)
    assert out["shared_terms"] == ["alpha", "mu", "zeta"]
    assert [r["term"] for r in out["results"]] == ["alpha", "mu", "zeta"]
