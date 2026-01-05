import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

X = pd.read_csv("data/processed/payroll_features.csv")
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)
joblib.dump(model,"models/isolation_forest.pkl")
