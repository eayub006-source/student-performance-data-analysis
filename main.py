"""Simple student data analysis script."""

import os
import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv("student_data.csv")
os.makedirs("output", exist_ok=True)

# Basic output in terminal
print("First 5 rows:")
print(df.head())
print()

print("Average age:", df["age"].mean())
print()

print("Average final grade by gender:")
print(df.groupby("sex")["G3"].mean())
print()

# Graph 1: final grade distribution
df["G3"].hist(bins=20)
plt.title("Distribution of Final Grades")
plt.xlabel("Final grade (G3)")
plt.ylabel("Count")
plt.savefig("output/g3_distribution.png")
plt.close()

# Graph 2: average age by gender
df.groupby("sex")["age"].mean().plot(kind="bar")
plt.title("Average Age by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Age")
plt.savefig("output/avg_age_by_sex.png")
plt.close()
