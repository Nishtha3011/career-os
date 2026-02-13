import joblib
import os
import numpy as np

model_path = os.path.join(os.path.dirname(__file__), "readiness_model.pkl")
model = joblib.load(model_path)

# Example input
coverage_ratio = 0.67
avg_weight = 0.75

predicted_readiness = model.predict([[coverage_ratio, avg_weight]])

print("Predicted Readiness:", round(predicted_readiness[0], 2), "%")
