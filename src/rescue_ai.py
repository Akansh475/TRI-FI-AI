
def generate_rescue_recommendations(ranked_sectors):
    """
    Convert fused sensor evidence into explainable rescue recommendations.

    Evidence scores are synthetic ranking signals, not probabilities
    that a survivor is present.
    """
    recommendations = []

    for sector in ranked_sectors:
        score = sector["evidence_score"]
        node_count = sector["node_count"]

        if score >= 0.70:
            priority = "HIGH"
            action = (
                "Request prompt human review and consider "
                "a targeted follow-up search."
            )
        elif score >= 0.40:
            priority = "MEDIUM"
            action = (
                "Review the available evidence and consider "
                "additional sensor measurements."
            )
        else:
            priority = "LOWER"
            action = (
                "Keep this sector in the assessment; do not "
                "rule it out based on this score alone."
            )

        recommendations.append({
            "sector": sector["sector"],
            "evidence_score": round(score, 3),
            "node_count": node_count,
            "priority": priority,
            "recommendation": action,
            "human_review_required": True,
        })

    return recommendations
