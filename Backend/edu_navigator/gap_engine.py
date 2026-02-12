import math
from .skill_data import ROLE_SKILLS


def calculate_gap(user_skills, role):
    role_skills = ROLE_SKILLS.get(role, {})

    if not role_skills:
        return 0, []

    user_vector = []
    role_vector = []
    missing_skills = []

    # Build vectors
    for skill, weight in role_skills.items():
        role_vector.append(weight)

        if skill.lower() in [s.lower() for s in user_skills]:
            user_vector.append(1)
        else:
            user_vector.append(0)
            missing_skills.append((skill, weight))

    # Dot product
    dot_product = sum(u * r for u, r in zip(user_vector, role_vector))

    # Magnitudes
    user_magnitude = math.sqrt(sum(u ** 2 for u in user_vector))
    role_magnitude = math.sqrt(sum(r ** 2 for r in role_vector))

    # Avoid division by zero
    if user_magnitude == 0 or role_magnitude == 0:
        similarity = 0
    else:
        similarity = dot_product / (user_magnitude * role_magnitude)

    readiness_percent = round(similarity * 100, 2)

    # Sort missing skills by importance
    missing_skills.sort(key=lambda x: x[1], reverse=True)

    return readiness_percent, [skill for skill, _ in missing_skills]