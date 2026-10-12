
from collections import defaultdict
from typing import Any


def fuse_evidence(
    readings: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Combine simulated sensor evidence by sector."""

    sectors: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for reading in readings:
        sectors[reading["sector"]].append(reading)

    candidates = []

    for sector, nodes in sectors.items():
        node_scores = []

        for node in nodes:
            score = (
                0.35 * node["signal_stability"]
                + 0.25 * node["movement_score"]
                + 0.40 * node["breathing_periodicity"]
            )
            node_scores.append(score)

        average_score = sum(node_scores) / len(node_scores)

        candidates.append({
            "sector": sector,
            "node_count": len(nodes),
            "evidence_score": round(average_score, 3),
            "node_scores": [
                round(score, 3) for score in node_scores
            ],
        })

    return sorted(
        candidates,
        key=lambda candidate: candidate["evidence_score"],
        reverse=True,
    )


if __name__ == "__main__":
    from src.simulator import generate_sensor_data

    readings = generate_sensor_data(seed=42)
    candidates = fuse_evidence(readings)

    print("\n=== SECTOR EVIDENCE RANKING ===")

    for rank, candidate in enumerate(candidates, start=1):
        print(
            f"Priority {rank}: Sector {candidate['sector']} | "
            f"Evidence score: {candidate['evidence_score']} | "
            f"Nodes: {candidate['node_count']}"
        )
