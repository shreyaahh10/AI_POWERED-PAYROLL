import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/raw/payroll_data.csv")
scaler = StandardScaler()
scaled = scaler.fit_transform(df[["base_salary","overtime_hours"]])

pd.DataFrame(scaled, columns=["salary_scaled","overtime_scaled"]).to_csv(
    "data/processed/payroll_features.csv", index=False)
