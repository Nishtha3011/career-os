from .skill_data import LEARNING_RESOURCES

def generate_roadmap(missing_skills):
    roadmap = {}

    for i, skill in enumerate(missing_skills[:4]):
        roadmap[f"Week {i+1}"] = skill

    learning_plan = {
        skill: LEARNING_RESOURCES.get(skill, ["Resource not available"])
        for skill in missing_skills[:4]
    }

    return roadmap, learning_plan