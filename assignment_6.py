import pandas as pd
from io import StringIO
#================================================================
# 1. DATA INITIALIZATION
# Creating structured employee dataset containing department, role, salary,
# and performance metrics.
# ================================================================

raw_csv_data = """
Employee_ID,Name,Department,Role,Salary,Bonus,Performance_Rating,Projects_Completed
101,Alice,Engineering,Developer,85000,12000,4.5,6
102,Bob,Engineering,Developer,78000,10000,3.8,4
103,Charlie,Engineering,Manager,110000,20000,4.8,9
104,David,Sales,Executive,62000,15000,4.2,12
105,Eva,Sales,Executive,58000,11000,3.5,8
106,Frank,Sales,Manager,95000,25000,4.9,15
107,Grace,Marketing,Specialist,65000,8000,4.0,5
108,Hank,Marketing,Specialist,68000,9500,4.1,7
109,Ivy,Marketing,Manager,102000,18000,4.7,8
"""

# Load CSV string into Pandas DataFrame
df = pd.read_csv(StringIO(raw_csv_data.strip()))

print("--- Original Employee Dataset ---")
print(df)
print("\n" + "=" * 80 + "\n")


# ================================================================
# 2. BASIC GROUPING & SINGLE AGGREGATION
# Grouping by a single categorical column ('Department') and calculating average
# metrics across all compatible numerical columns.
# ================================================================

print("--- Concept 1: Basic Grouping (Average Salary & Bonus per Department) ---")

# Group by Department and compute the mean for numerical attributes
dept_means = df.groupby("Department")[["Salary", "Bonus"]].mean()

# dept_means = df.groupby("Department")["Salary"].mean()

# Formatting output values for clarity
dept_means_formatted = dept_means.round(2)

print(dept_means_formatted)
print("\n" + "=" * 80 + "\n")
# ================================================================
# 3. MULTI-COLUMN GROUPING
# Grouping by multiple categorical variables ('Department' and 'Role')
# to analyze metrics at a finer hierarchy level.
# ================================================================

print("--- Concept 2: Multi-Column Grouping (Average Salary by Dept & Role) ---")

# Multi-level grouping
role_hierarchy = (
    df.groupby(["Department", "Role"])[["Salary", "Performance_Rating"]]
    .mean()
    .round(2)
)

print(role_hierarchy)
print("\n" + "=" * 80 + "\n")


# ================================================================
# 4. ADVANCED AGGREGATION USING .agg()
# Applying multiple aggregation functions (sum, mean, max) to different columns
# simultaneously.
# ================================================================
print("--- Concept 3: Advanced Aggregation using .agg() ---")

# Dictionary mapping specific columns to desired statistical operations
agg_operations = {
    "Salary": ["mean", "min", "max"],
    "Bonus": "sum",
    "Projects_Completed": "sum",
    "Performance_Rating": "mean",
}

dept_summary = df.groupby("Department").agg(agg_operations).round(2)

print(dept_summary)
print(dept_summary["Bonus"])

print("\n" + "=" * 80 + "\n")
# ================================================================
# 5. NAMED AGGREGATIONS (CLEAN SINGLE-LEVEL COLUMNS)
# Creating custom, clear column headers in the resulting DataFrame to avoid
# hierarchical MultiIndex column names.
# ================================================================

print("--- Concept 4: Named Aggregation for Flat Data Structure ---")

dept_report = (
    df.groupby("Department")
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Total_Payroll=("Salary", "sum"),
        Average_Salary=("Salary", "mean"),
        Highest_Bonus=("Bonus", "max"),
        Average_Performance=("Performance_Rating", "mean"),
        Total_Projects_Delivered=("Projects_Completed", "sum"),
    )
    .reset_index()
)
# Format numerical fields for presentation
clean_dept_report=dept_report.copy()
clean_dept_report["Average_Salary"] = clean_dept_report[
    "Average_Salary"
].round(2)

clean_dept_report["Average_Performance"] = clean_dept_report[
    "Average_Performance"
].round(2)

print(clean_dept_report.to_string(index=False))
print("\n" + "=" * 80 + "\n")


# ================================================================
# 6. GROUP FILTERING USING .filter()
# Filtering entire groups based on an aggregate condition (similar to SQL HAVING).
# ================================================================

print(
    "--- Concept 5: Group Filtering (Departments with Total Payroll > $200,000) ---"
)
# Keep only department records where the combined team salary exceeds $200k
high_payroll_depts = df.groupby("Department").filter(
    lambda group: group["Salary"].sum() > 200000
)

