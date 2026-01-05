import pandas as pd
import joblib

X = pd.read_csv("data/processed/payroll_features.csv")
model = joblib.load("models/isolation_forest.pkl")

X["anomaly"] = model.predict(X)
print(X[X.anomaly==-1].head())
