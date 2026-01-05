import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")

import pandas as pd
import joblib
import time

model = joblib.load("models/isolation_forest.pkl")
df = pd.read_csv("data/processed/payroll_features.csv")

for _, row in df.iterrows():
    if model.predict([row])[0] == -1:
        print("Real-time anomaly:", row.to_dict())
    time.sleep(0.05)
