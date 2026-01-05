from river import drift
import pandas as pd

df = pd.read_csv("data/processed/payroll_features.csv")
adwin = drift.ADWIN()

for v in df["salary_scaled"]:
    adwin.update(v)
    if adwin.drift_detected:
        print("Concept drift detected")
        break
