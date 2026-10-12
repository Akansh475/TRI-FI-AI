
from src.rescue_ai import generate_rescue_recommendations


def test_high_evidence_gets_high_priority():
    sectors = [
        {"sector": "A", "evidence_score": 0.805, "node_count": 3}
    ]
    result = generate_rescue_recommendations(sectors)

    assert result[0]["priority"] == "HIGH"
    assert result[0]["human_review_required"] is True


def test_medium_evidence_gets_medium_priority():
    sectors = [
        {"sector": "B", "evidence_score": 0.489, "node_count": 3}
    ]
    result = generate_rescue_recommendations(sectors)

    assert result[0]["priority"] == "MEDIUM"


def test_lower_evidence_is_not_ruled_out():
    sectors = [
        {"sector": "C", "evidence_score": 0.314, "node_count": 3}
    ]
    result = generate_rescue_recommendations(sectors)

    assert result[0]["priority"] == "LOWER"
    assert result[0]["human_review_required"] is True
    assert "do not rule it out" in result[0]["recommendation"]
