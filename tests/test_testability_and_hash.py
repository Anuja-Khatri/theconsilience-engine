"""Instrument capability lookup and verdict hashing."""
from judge.hash.determinism_check import compute_verdict_hash, verify_determinism
from judge.testability.capability_map_lookup import check_testability

MAP = [
    {"instrument_class": "fMRI", "physical_scale": "macro",
     "observable": "BOLD signal", "resolution": "2 mm"},
    {"instrument_class": "EEG", "physical_scale": "macro",
     "observable": "scalp potential"},
]


def test_testable_now():
    r = check_testability({"physical_scale": "macro", "observable": "bold"},
                          MAP, "v1")
    assert r["verdict"] == "testable_now"
    assert r["instrument"] == "fMRI"
    assert r["map_version"] == "v1"


def test_testable_under_assumption_names_instruments():
    r = check_testability({"physical_scale": "macro", "observable": "phi"},
                          MAP, "v1")
    assert r["verdict"] == "testable_under_assumption"
    assert r["available_instruments"] == ["fMRI", "EEG"]


def test_not_testable_names_reason_and_version():
    r = check_testability({"physical_scale": "quantum", "observable": "phi"},
                          MAP, "v2")
    assert r["verdict"] == "not_testable"
    assert "v2" in r["reason"] and "quantum" in r["reason"]


def test_hash_ignores_key_order():
    assert compute_verdict_hash({"a": 1, "b": 2}) == compute_verdict_hash({"b": 2, "a": 1})


def test_verify_determinism_detects_difference():
    assert verify_determinism({"rung": 2}, {"rung": 2})["match"] is True
    assert verify_determinism({"rung": 2}, {"rung": 3})["match"] is False
