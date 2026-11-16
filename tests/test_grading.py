"""Four-rung grading ladder: rule table and ceilings."""
import pytest

from judge.grading.four_rung_ladder import CEILINGS, assign_rung


@pytest.mark.parametrize("iso, mcs, survived, defect, rung", [
    (True, 1.0, True, False, 1),   # full match, survives ablation
    (False, 0.75, True, False, 2),  # partial match at or above 0.5
    (False, 0.5, True, False, 2),   # boundary is inclusive
    (False, 0.49, True, False, 3),  # below 0.5: generative only
    (True, 1.0, False, False, 4),   # vocabulary-dependent: quarantined
    (True, 1.0, True, True, 3),     # defect edge caps at rung 3
    (True, 1.0, False, True, 4),    # defect edge and vocabulary-dependent
])
def test_rung_assignment(iso, mcs, survived, defect, rung):
    result = assign_rung(iso, mcs, survived, defect)
    assert result["rung"] == rung
    assert result["ceiling"] == CEILINGS[rung]


def test_every_ceiling_states_what_it_does_not_license():
    for rung in (1, 2, 3, 4):
        assert "does not license" in CEILINGS[rung].lower()
