def governance_check(jurisdiction, explainability_score, bias_detected):

    if jurisdiction == "EU":
        if explainability_score < 0.6:
            return "HUMAN_REVIEW_REQUIRED"

    if bias_detected:
        return "FAIR_LENDING_ALERT"

    return "COMPLIANT"
