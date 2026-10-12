
from src.simulator import generate_sensor_data
from src.fusion import fuse_evidence
from src.rescue_ai import generate_rescue_recommendations


def main():
    print("\n=== TRI-FI RESCUE ===")
    print("Disaster Rescue Decision-Support Prototype\n")

    # Step 1: Generate simulated sensor readings
    readings = generate_sensor_data(seed=42)
    print(f"[1] Sensor readings collected: {len(readings)}")

    # Step 2: Fuse evidence and rank sectors
    ranked_sectors = fuse_evidence(readings)
    print("[2] Evidence fusion completed")

    # Step 3: Generate explainable recommendations
    recommendations = generate_rescue_recommendations(ranked_sectors)
    print("[3] Rescue recommendations generated\n")

    # Display results
    print("=== RESCUE ASSESSMENT ===")

    for item in recommendations:
        print(f"\nSector: {item['sector']}")
        print(f"Priority: {item['priority']}")
        print(f"Evidence score: {item['evidence_score']:.3f}")
        print(f"Sensor nodes: {item['node_count']}")
        print(f"Recommendation: {item['recommendation']}")
        print(f"Human review required: {item['human_review_required']}")

    print("\nNote: This prototype uses simulated sensor data.")
    print("Scores are not survivor probabilities.")
    print("All recommendations require human assessment.")


if __name__ == "__main__":
    main()
