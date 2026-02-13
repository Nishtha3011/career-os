import pandas as pd
import joblib
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load CSV
csv_path = os.path.join(os.path.dirname(__file__), "training_data.csv")
df = pd.read_csv(csv_path)

X = df[["coverage_ratio", "avg_weight"]]
y = df["readiness"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save model
model_path = os.path.join(os.path.dirname(__file__), "readiness_model.pkl")
joblib.dump(model, model_path)

print("Model trained & saved successfully 🚀")
print("MSE:", round(mse, 2))
print("R2 Score:", round(r2, 3))
