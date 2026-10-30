
# TRI-FI RESCUE

### AI-Assisted Disaster Rescue Decision-Support Prototype

TRI-FI RESCUE is a disaster-response decision-support prototype designed to help rescue teams prioritize areas for further assessment using simulated multi-node sensor evidence.

## Current Features

- Synthetic sensor data generation across multiple sectors.
- Evidence fusion from multiple sensor nodes.
- Sector ranking based on a weighted evidence score.
- Explainable rescue-priority recommendations.
- Human review required for every recommendation.
- Automated tests for fusion and recommendation .

## System Pipeline

Sensor Simulator → Evidence Fusion → Sector Ranking → Rescue Recommendations → Human Review

## Technology Stack

- Python
- NumPy
- pytest
- Nebius Token Factory integration planned

## Run Locally

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the prototype:

```bash
python -m src.main
```

Run tests:

```bash
python -m pytest -v
```

## Important Limitations

The current prototype uses simulated sensor readings. Its evidence scores are ranking signals, not calibrated probabilities of survivor presence. It has not yet been validated using real disaster-site sensor data.

Recommendations are intended to support human assessment, not replace trained rescue personnel.

## Development Status

- [x] Sensor simulator
- [x] Evidence fusion
- [x] Rescue decision engine
- [x] Automated tests
- [ ] Nebius Token Factory integration
- [ ] Real sensor data integration
- [ ] Rescue dashboard
