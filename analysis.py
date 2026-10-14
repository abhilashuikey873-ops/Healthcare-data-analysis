#data analysis.py
import pandas as pd

# Load healthcare dataset
df = pd.read_csv("healthcare.csv")

print("HEALTHCARE DATASET")
print(df)

print("\nTotal Patients:", df["Patients"].sum())

print("\nDepartment-wise Patients:")
print(df.groupby("Department")["Patients"].sum())

print("\nAverage Treatment Cost:")
print(df.groupby("Department")["Treatment_Cost"].mean())

print("\nTotal Treatment Cost:")
print(df.groupby("Department")["Treatment_Cost"].sum())

print("\nAverage Hospital Stay:")
print(df.groupby("Department")["Hospital_Stay"].mean())