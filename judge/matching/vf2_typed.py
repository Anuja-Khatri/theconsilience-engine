"""
VF2 Subgraph Isomorphism with Typed Edge Constraints

Uses NetworkX's VF2 implementation with custom node and edge matching
functions that enforce type constraints. One mismatched edge type
vetoes the entire correspondence (the Newman guard).

This is the same algorithm family chemists use for molecular
substructure search. Published 2004 (Cordella et al.).
The algorithm is not novel. The typed schema it operates on is.
"""

import hashlib
import json
import networkx as nx
from networkx.algorithms import isomorphism


def node_match(n1_attrs: dict, n2_attrs: dict) -> bool:
    """Nodes match if their claim_kind and physical_scale match."""
    return (
        n1_attrs.get("claim_kind") == n2_attrs.get("claim_kind")
        and n1_attrs.get("physical_scale") == n2_attrs.get("physical_scale")
    )


def edge_match(e1_attrs: dict, e2_attrs: dict) -> bool:
    """
    Edges match if their relation type AND causal direction match.
    One mismatch vetoes the entire correspondence.
    This is the Newman guard.
    """
    return (
        e1_attrs.get("relation") == e2_attrs.get("relation")
        and e1_attrs.get("causal_direction") == e2_attrs.get("causal_direction")
    )


def check_subgraph_isomorphism(
    graph_a: nx.DiGraph, graph_b: nx.DiGraph
) -> dict:
    """
    Check whether graph_a's structure maps onto a substructure of graph_b
    with typed node and edge constraints.

    Returns a dict with:
      - is_isomorphic: bool
      - mapping: dict of node mappings (if isomorphic)
      - matched_edges: list of matched edge pairs
      - content_hash: SHA256 hash of the result (determinism proof)
    """
    matcher = isomorphism.DiGraphMatcher(
        graph_b, graph_a,
        node_match=node_match,
        edge_match=edge_match
    )

    is_iso = matcher.subgraph_is_isomorphic()
    mapping = matcher.mapping if is_iso else {}

    matched_edges = []
    if is_iso:
        for u, v, data in graph_a.edges(data=True):
            mapped_u = mapping.get(u)
            mapped_v = mapping.get(v)
            if mapped_u is not None and mapped_v is not None:
                matched_edges.append({
                    "source_edge": {"from": u, "to": v, **data},
                    "target_edge": {
                        "from": mapped_u,
                        "to": mapped_v,
                        **graph_b.edges[mapped_u, mapped_v]
                    }
                })

    result = {
        "is_isomorphic": is_iso,
        "mapping": {str(k): str(v) for k, v in mapping.items()},
        "matched_edges": matched_edges,
    }

    # Determinism proof: hash the result
    result_json = json.dumps(result, sort_keys=True)
    result["content_hash"] = hashlib.sha256(result_json.encode()).hexdigest()

    return result
