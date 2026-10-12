
from src.fusion import fuse_evidence


def test_sectors_are_ranked_by_evidence():
    readings = [
        {
            "node_id": "N1",
            "sector": "A",
            "signal_stability": 0.9,
            "movement_score": 0.8,
            "breathing_periodicity": 0.9,
        },
        {
            "node_id": "N2",
            "sector": "B",
            "signal_stability": 0.3,
            "movement_score": 0.2,
            "breathing_periodicity": 0.1,
        },
    ]

    results = fuse_evidence(readings)

    assert results[0]["sector"] == "A"
    assert results[1]["sector"] == "B"


def test_node_count_is_correct():
    readings = [
        {
            "node_id": "N1",
            "sector": "A",
            "signal_stability": 0.8,
            "movement_score": 0.7,
            "breathing_periodicity": 0.9,
        },
        {
            "node_id": "N2",
            "sector": "A",
            "signal_stability": 0.7,
            "movement_score": 0.6,
            "breathing_periodicity": 0.8,
        },
    ]

    results = fuse_evidence(readings)

    assert results[0]["node_count"] == 2
