import os
import joblib
import numpy as np
from .skill_data import ROLE_SKILLS, LEARNING_RESOURCES

# Load trained sklearn model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "readiness_model.pkl")
model = joblib.load(MODEL_PATH)


def calculate_gap(user_skills: dict, target_role: str):
    """
    user_skills: {"Python": 0.8, "SQL": 0.6, "Docker": 0.5}
    target_role: "ML Engineer"
    """

    if target_role not in ROLE_SKILLS:
        raise ValueError("Invalid target role")

    role_skills = ROLE_SKILLS[target_role]

    matched_skills = []
    missing_skills = []
    total_skills = len(role_skills)

    weighted_sum = 0
    match_count = 0

    for skill, required_weight in role_skills.items():
        if skill in user_skills:
            user_level = user_skills[skill]
            match_count += 1
            weighted_sum += min(user_level, required_weight)
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    coverage_ratio = match_count / total_skills if total_skills > 0 else 0
    avg_weight = (weighted_sum / match_count) if match_count > 0 else 0

    # Predict readiness using sklearn model
    X_new = np.array([[coverage_ratio, avg_weight]])
    readiness = float(model.predict(X_new)[0])

    # Learning resources for missing skills
    learning_path = {}
    for skill in missing_skills:
        if skill in LEARNING_RESOURCES:
            learning_path[skill] = LEARNING_RESOURCES[skill]

    return {
        "readiness_score": round(readiness, 2),
        "coverage_ratio": round(coverage_ratio, 2),
        "avg_weight": round(avg_weight, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "learning_path": learning_path
    }
