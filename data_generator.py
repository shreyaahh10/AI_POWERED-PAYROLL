import os
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)
os.makedirs("models", exist_ok=True)

import pandas as pd
import numpy as np

def generate_data(records=500):
    np.random.seed(42)
    df = pd.DataFrame({
        "employee_id": [f"E{1000+i}" for i in range(records)],
        "department": np.random.choice(["Engineering","HR","Finance"], records),
        "base_salary": np.random.normal(60000,8000,records).astype(int),
        "overtime_hours": np.random.poisson(8,records),
        "month": np.random.randint(1,13,records),
        "year": 2024
    })

    df.loc[np.random.choice(df.index,10), "base_salary"] *= 2
    df.loc[np.random.choice(df.index,15), "overtime_hours"] *= 8

    df.to_csv("data/raw/payroll_data.csv", index=False)

if __name__ == "__main__":
    generate_data()
