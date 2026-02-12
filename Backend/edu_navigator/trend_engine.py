from .skill_data import ROLE_SKILLS

def get_market_demand(role):
    if role not in ROLE_SKILLS:
        return {}

    return {
        skill: round(weight * 100, 1)
        for skill, weight in ROLE_SKILLS[role].items()
    }