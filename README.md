# Employee Performance Analysis – Department Distribution

Email: **24f2005641@ds.study.iitm.ac.in**

This repository contains the Python script and visualization for analyzing employee performance data.  
The goal of this analysis is to help the HR and executive team understand department distribution patterns and identify insights for strategic workforce planning.

## Files Included

### **employee_viz.py**
- Loads employee dataset (either from `employees.csv` or synthetic sample data)
- Calculates the frequency count for the **Finance** department
- Prints frequency counts to the console
- Creates a histogram showing the distribution of departments using Plotly
- Exports an interactive HTML visualization

### **employee_department_distribution.html**
- Interactive histogram visualization  
- Shows number of employees in each department  
- Generated from `employee_viz.py`

## How to Run

Install dependencies:

```bash
pip install pandas plotly matplotlib
