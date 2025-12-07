"""
employee_viz.py
Creates a department-frequency histogram and prints the frequency count for the "Finance" department.

Email (for verification): 24f2005641@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import numpy as np
import os

# --- Replace this with loading a CSV if you have one ---
# If an 'employees.csv' exists in the same folder, we'll load it.
# Otherwise we create a sample DataFrame similar to the prompt.
csv_path = "employees.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    # Sample synthetic dataset (100 rows)
    np.random.seed(42)
    data = {
        "employee_id": [f"EMP{str(i+1).zfill(3)}" for i in range(100)],
        "department": [
            "IT","IT","R&D","Sales","IT","Finance","Finance","HR","Sales","Finance",
            "IT","R&D","Sales","Finance","HR","IT","Sales","Finance","R&D","HR"
        ] * 5,  # repeated to reach ~100 rows
        "region": ["Africa","Middle East","Africa","North America","Asia Pacific"] * 20,
        "performance_score": (np.random.rand(100) * 40 + 60).round(2),
        "years_experience": np.random.randint(1, 25, size=100),
        "satisfaction_rating": (np.random.rand(100) * 2 + 3).round(1),
    }
    df = pd.DataFrame(data)

# --- Task 1: Calculate frequency count for "Finance" department and print ---
dept_counts = df["department"].value_counts().sort_index()
finance_count = int(dept_counts.get("Finance", 0))

print("Department frequency counts:")
print(dept_counts.to_string())

print(f"\nFrequency count for the 'Finance' department: {finance_count}")

# --- Task 2: Create histogram (department distribution) ---
fig = px.histogram(
    df,
    x="department",
    color="department",
    category_orders={"department": sorted(df["department"].unique())},
    title="Distribution of Employees by Department",
    labels={"department": "Department", "count": "Number of Employees"},
    template="plotly_white",
)

fig.update_layout(
    showlegend=False,
    xaxis_title="Department",
    yaxis_title="Number of Employees",
    title_x=0.5,
    title_font=dict(size=18, family="Arial"),
)

fig.update_traces(texttemplate="%{y}", textposition="outside", marker_line_width=0.5)

# Save as interactive HTML
output_html = "employee_department_distribution.html"
pio.write_html(fig, file=output_html, auto_open=False, include_plotlyjs="cdn")

print(f"\nInteractive HTML saved to: {output_html}")
print("Upload this HTML file to GitHub and submit the RAW URL.")
