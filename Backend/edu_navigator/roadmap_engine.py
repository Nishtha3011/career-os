def generate_roadmap(missing_skills):

    roadmap = {}
    learning_resources = {}

    for i, skill in enumerate(missing_skills[:4]):  # top 4 missing
        roadmap[f"Week {i+1}"] = skill

        learning_resources[skill] = [
            f"Official Documentation for {skill}",
            f"YouTube Advanced {skill} Tutorial",
            f"Hands-on Project on {skill}"
        ]

    return roadmap, learning_resources