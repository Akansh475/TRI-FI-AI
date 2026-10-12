
import random
from typing import Any


def generate_sensor_data(seed: int | None = None) -> list[dict[str, Any]]:
    """
    Generate synthetic RF sensing features for development.

    These are simulated values, not real sensor measurements
    or validated indicators of human presence.
    """
    rng = random.Random(seed)

    sector_profiles = {
        "A": {
            "signal_stability": 0.90,
            "movement_score": 0.70,
            "breathing_periodicity": 0.82,
        },
        "B": {
            "signal_stability": 0.65,
            "movement_score": 0.42,
            "breathing_periodicity": 0.35,
        },
        "C": {
            "signal_stability": 0.48,
            "movement_score": 0.25,
            "breathing_periodicity": 0.20,
        },
    }

    readings = []

    for sector, profile in sector_profiles.items():
        for node_number in range(1, 4):
            reading = {
                "node_id": f"NODE_{node_number}",
                "sector": sector,
                "signal_stability": round(
                    min(1.0, max(0.0,
                        rng.gauss(profile["signal_stability"], 0.05)
                    )), 3
                ),
                "movement_score": round(
                    min(1.0, max(0.0,
                        rng.gauss(profile["movement_score"], 0.08)
                    )), 3
                ),
                "breathing_periodicity": round(
                    min(1.0, max(0.0,
                        rng.gauss(
                            profile["breathing_periodicity"], 0.06
                        )
                    )), 3
                ),
            }

            readings.append(reading)

    return readings


if __name__ == "__main__":
    for item in generate_sensor_data(seed=42):
        print(item)
