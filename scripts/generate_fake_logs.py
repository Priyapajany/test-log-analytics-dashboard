import pandas as pd
import random
from datetime import datetime, timedelta
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)  # make sure /data exists

file_path = os.path.join(DATA_DIR, "fake_test_logs.csv")

# Sample values
test_names = [f"Test_{i}" for i in range(1, 21)]
statuses = ["PASS", "FAIL", "SKIP"]
environments = ["QA", "Staging", "Prod"]
executors = ["Jenkins", "GitHub Actions", "Local"]

# Generate fake logs
logs = []
start_date = datetime(2025, 1, 1)

for i in range(100):  # 100 rows
    log = {
        "TestID": i + 1,
        "TestName": random.choice(test_names),
        "Status": random.choices(statuses, weights=[0.6, 0.3, 0.1])[0],
        "ExecutionTime_sec": round(random.uniform(0.5, 10.0), 2),
        "ExecutedBy": random.choice(executors),
        "Environment": random.choice(environments),
        "ExecutionDate": (start_date + timedelta(days=random.randint(0, 60))).strftime("%Y-%m-%d")
    }
    logs.append(log)

# Convert to DataFrame
df = pd.DataFrame(logs)

# Save as CSV
df.to_csv(file_path, index=False)
print(f"✅ Fake dataset created at: {file_path}")