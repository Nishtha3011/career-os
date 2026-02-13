import random
import numpy as np
import pandas as pd
import os

data = []

for _ in range(500):
    total_skills = 6
    matched_skills = random.randint(0, total_skills)
    avg_weight = round(random.uniform(0.4, 0.95), 2)

    coverage_ratio = matched_skills / total_skills

    readiness = coverage_ratio * avg_weight * 100
    readiness += random.uniform(-5, 5)
    readiness = max(0, min(100, round(readiness, 2)))

    data.append([coverage_ratio, avg_weight, readiness])

df = pd.DataFrame(data, columns=["coverage_ratio", "avg_weight", "readiness"])

csv_path = os.path.join(os.path.dirname(__file__), "training_data.csv")
df.to_csv(csv_path, index=False)

print("training_data.csv created successfully ✅")
