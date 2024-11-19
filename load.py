import pandas as pd

file_path = "orders.csv"

if not file_path:
    print("Provide a file path")

print(f"Reading file in path: {file_path}")

df = pd.read_csv(file_path)
globals()["df"] = df

print("Pipeline Starting...")

# Prepare data
exec(open('eda.py').read())