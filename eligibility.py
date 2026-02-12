def calculate_eligibility_score(education, funds, travel_history):

    score = 0
    feedback = []

    # Education scoring
    education_scores = {
        "High School": 10,
        "Bachelor": 25,
        "Master": 35,
        "PhD": 40
    }

    score += education_scores.get(education, 0)

    # Financial scoring
    if funds > 20000:
        score += 30
    elif funds > 10000:
        score += 20
    elif funds > 5000:
        score += 10
    else:
        feedback.append("Increase financial proof documents.")

    # Travel history scoring
    if travel_history == "Frequent":
        score += 20
    elif travel_history == "Some":
        score += 10
    else:
        feedback.append("Limited travel history may affect approval.")

    # Cap at 100
    score = min(score, 100)

    if score >= 75:
        status = "Strong Profile ✅"
    elif score >= 50:
        status = "Moderate Profile ⚠️"
    else:
        status = "Weak Profile ❌"

    feedback.insert(0, f"Profile Assessment: {status}")

    return score, feedback
