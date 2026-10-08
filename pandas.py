# ============================================================
# PANDAS CRASH COURSE FOR FUNDAMENTALS OF DATA SCIENCE
# ============================================================
#
# Topics Covered:
# 1. Importing Pandas
# 2. Series
# 3. DataFrames
# 4. Creating DataFrames
# 5. Reading and Writing CSV Files
# 6. Inspecting Data
# 7. Selecting Rows and Columns
# 8. Filtering Data
# 9. Adding and Modifying Columns
# 10. Sorting
# 11. Missing Values
# 12. GroupBy
# 13. Aggregation
# 14. Merging DataFrames
# 15. Concatenating DataFrames
# 16. Removing Data
# 17. Apply Function
# 18. Statistical Operations
# 19. Working with Dates
# 20. Mini Data Science Project
#
# ============================================================


import pandas as pd


# ============================================================
# 1. SERIES
# ============================================================

print("\n========== 1. SERIES ==========\n")

marks = pd.Series([85, 90, 76, 95, 88])

print(marks)

print("\nSeries values:")
print(marks.values)

print("\nSeries index:")
print(marks.index)

print("\nFirst value:")
print(marks[0])


# Series with custom index

marks = pd.Series(
    [85, 90, 76, 95],
    index=["Maths", "Physics", "Chemistry", "Computer"]
)

print("\nMarks with custom index:")
print(marks)

print("\nPhysics marks:")
print(marks["Physics"])


# ============================================================
# 2. CREATING A DATAFRAME
# ============================================================

print("\n========== 2. DATAFRAME ==========\n")

data = {
    "Name": ["Rahul", "Priya", "Arjun", "Sneha", "Karan"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 92, 76, 88, 95],
    "Department": ["CSE", "ECE", "CSE", "EEE", "CSE"]
}

df = pd.DataFrame(data)

print(df)


# ============================================================
# 3. BASIC DATAFRAME INFORMATION
# ============================================================

print("\n========== 3. INSPECTING DATA ==========\n")

print("First 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nInformation:")
df.info()

print("\nStatistical summary:")
print(df.describe())


# ============================================================
# 4. SELECTING COLUMNS
# ============================================================

print("\n========== 4. SELECTING COLUMNS ==========\n")

print("Name column:")
print(df["Name"])

print("\nMarks column:")
print(df["Marks"])

print("\nMultiple columns:")
print(df[["Name", "Marks"]])


# ============================================================
# 5. SELECTING ROWS
# ============================================================

print("\n========== 5. SELECTING ROWS ==========\n")

print("First row:")
print(df.iloc[0])

print("\nFirst three rows:")
print(df.iloc[0:3])

print("\nSecond row:")
print(df.iloc[1])


# loc uses labels

print("\nUsing loc:")
print(df.loc[0:2, ["Name", "Marks"]])


# ============================================================
# 6. FILTERING DATA
# ============================================================

print("\n========== 6. FILTERING ==========\n")

print("Students with marks greater than 85:")
print(df[df["Marks"] > 85])

print("\nStudents from CSE:")
print(df[df["Department"] == "CSE"])

print("\nStudents aged 20:")
print(df[df["Age"] == 20])

print("\nCSE students with marks above 80:")
print(
    df[
        (df["Department"] == "CSE") &
        (df["Marks"] > 80)
    ]
)


# ============================================================
# 7. ADDING COLUMNS
# ============================================================

print("\n========== 7. ADDING COLUMNS ==========\n")

df["Passed"] = df["Marks"] >= 40

print(df)

# Creating a calculated column

df["Bonus_Marks"] = df["Marks"] + 5

print("\nAfter adding bonus marks:")
print(df)


# ============================================================
# 8. MODIFYING COLUMNS
# ============================================================

print("\n========== 8. MODIFYING DATA ==========\n")

df["Age"] = df["Age"] + 1

print("After increasing age by 1:")
print(df)


# ============================================================
# 9. SORTING
# ============================================================

print("\n========== 9. SORTING ==========\n")

print("Sorted by marks:")
print(df.sort_values("Marks"))

print("\nSorted by marks descending:")
print(df.sort_values("Marks", ascending=False))

print("\nSorted by age:")
print(df.sort_values("Age"))


# ============================================================
# 10. MISSING VALUES
# ============================================================

print("\n========== 10. MISSING VALUES ==========\n")

student_data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [90, None, 75, None, 88],
    "Attendance": [95, 88, None, 92, 85]
}

students = pd.DataFrame(student_data)

print(students)

print("\nChecking missing values:")
print(students.isnull())

print("\nNumber of missing values:")
print(students.isnull().sum())

# Fill missing values

students["Marks"] = students["Marks"].fillna(
    students["Marks"].mean()
)

students["Attendance"] = students["Attendance"].fillna(
    students["Attendance"].mean()
)

print("\nAfter filling missing values:")
print(students)


# ============================================================
# 11. DROP DATA
# ============================================================

print("\n========== 11. DROPPING DATA ==========\n")

temp_df = df.copy()

print("Original:")
print(temp_df)

# Drop a column

temp_df = temp_df.drop("Bonus_Marks", axis=1)

print("\nAfter dropping Bonus_Marks:")
print(temp_df)

# Drop a row

temp_df = temp_df.drop(0)

print("\nAfter dropping first row:")
print(temp_df)


# ============================================================
# 12. GROUPBY
# ============================================================

print("\n========== 12. GROUPBY ==========\n")

print("Average marks by department:")

print(
    df.groupby("Department")["Marks"].mean()
)

print("\nMaximum marks by department:")

print(
    df.groupby("Department")["Marks"].max()
)

print("\nNumber of students in each department:")

print(
    df.groupby("Department")["Name"].count()
)


# ============================================================
# 13. AGGREGATION
# ============================================================

print("\n========== 13. AGGREGATION ==========\n")

result = df.groupby("Department")["Marks"].agg(
    ["mean", "min", "max", "count"]
)

print(result)


# ============================================================
# 14. APPLY FUNCTION
# ============================================================

print("\n========== 14. APPLY FUNCTION ==========\n")


def grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"


df["Grade"] = df["Marks"].apply(grade)

print(df)


# ============================================================
# 15. MERGING DATAFRAMES
# ============================================================

print("\n========== 15. MERGING ==========\n")

student_info = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Name": ["Rahul", "Priya", "Arjun", "Sneha"]
})

student_marks = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Marks": [85, 92, 76, 88]
})

merged = pd.merge(
    student_info,
    student_marks,
    on="Student_ID"
)

print(merged)


# ============================================================
# 16. CONCATENATING DATAFRAMES
# ============================================================

print("\n========== 16. CONCAT ==========\n")

class_A = pd.DataFrame({
    "Name": ["A", "B"],
    "Marks": [80, 90]
})

class_B = pd.DataFrame({
    "Name": ["C", "D"],
    "Marks": [75, 85]
})

combined = pd.concat(
    [class_A, class_B],
    ignore_index=True
)

print(combined)


# ============================================================
# 17. UNIQUE VALUES
# ============================================================

print("\n========== 17. UNIQUE VALUES ==========\n")

print("Departments:")
print(df["Department"].unique())

print("\nNumber of unique departments:")
print(df["Department"].nunique())

print("\nValue counts:")
print(df["Department"].value_counts())


# ============================================================
# 18. BASIC STATISTICS
# ============================================================

print("\n========== 18. STATISTICS ==========\n")

print("Mean:")
print(df["Marks"].mean())

print("\nMedian:")
print(df["Marks"].median())

print("\nMaximum:")
print(df["Marks"].max())

print("\nMinimum:")
print(df["Marks"].min())

print("\nStandard deviation:")
print(df["Marks"].std())

print("\nSum:")
print(df["Marks"].sum())


# ============================================================
# 19. WORKING WITH DATES
# ============================================================

print("\n========== 19. DATES ==========\n")

dates = pd.DataFrame({
    "Student": ["A", "B", "C"],
    "Join_Date": [
        "2025-01-10",
        "2025-02-15",
        "2025-03-20"
    ]
})

dates["Join_Date"] = pd.to_datetime(
    dates["Join_Date"]
)

print(dates)

print("\nYear:")
print(dates["Join_Date"].dt.year)

print("\nMonth:")
print(dates["Join_Date"].dt.month)

print("\nDay:")
print(dates["Join_Date"].dt.day)


# ============================================================
# 20. READING AND WRITING CSV
# ============================================================

print("\n========== 20. CSV FILES ==========\n")

# Save DataFrame to CSV

df.to_csv(
    "students.csv",
    index=False
)

print("Data saved to students.csv")

# Read CSV

loaded_data = pd.read_csv(
    "students.csv"
)

print("\nData read from CSV:")
print(loaded_data)


# ============================================================
# 21. MINI DATA SCIENCE PROJECT
# ============================================================

print("\n========== 21. MINI DATA SCIENCE PROJECT ==========\n")

sales_data = {
    "Product": [
        "Laptop",
        "Phone",
        "Tablet",
        "Laptop",
        "Phone",
        "Tablet",
        "Laptop",
        "Phone"
    ],

    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics"
    ],

    "Sales": [
        75000,
        50000,
        30000,
        80000,
        45000,
        35000,
        70000,
        55000
    ],

    "Units": [
        3,
        5,
        4,
        4,
        6,
        5,
        3,
        7
    ]
}

sales_df = pd.DataFrame(sales_data)

print("Sales Data:")
print(sales_df)


# ------------------------------------------------------------
# Total sales
# ------------------------------------------------------------

total_sales = sales_df["Sales"].sum()

print("\nTotal Sales:")
print(total_sales)


# ------------------------------------------------------------
# Average sales
# ------------------------------------------------------------

average_sales = sales_df["Sales"].mean()

print("\nAverage Sales:")
print(average_sales)


# ------------------------------------------------------------
# Best selling product by revenue
# ------------------------------------------------------------

best_product = sales_df.loc[
    sales_df["Sales"].idxmax()
]

print("\nHighest Revenue Transaction:")
print(best_product)


# ------------------------------------------------------------
# Total units sold
# ------------------------------------------------------------

total_units = sales_df["Units"].sum()

print("\nTotal Units Sold:")
print(total_units)


# ------------------------------------------------------------
# Sales grouped by product
# ------------------------------------------------------------

product_sales = sales_df.groupby(
    "Product"
)["Sales"].sum()

print("\nSales by Product:")
print(product_sales)


# ------------------------------------------------------------
# Units grouped by product
# ------------------------------------------------------------

product_units = sales_df.groupby(
    "Product"
)["Units"].sum()

print("\nUnits Sold by Product:")
print(product_units)


# ------------------------------------------------------------
# Average sales by product
# ------------------------------------------------------------

average_product_sales = sales_df.groupby(
    "Product"
)["Sales"].mean()

print("\nAverage Sales by Product:")
print(average_product_sales)


# ------------------------------------------------------------
# Sort products by total sales
# ------------------------------------------------------------

print("\nProducts sorted by sales:")

print(
    product_sales.sort_values(
        ascending=False
    )
)


# ============================================================
# 22. QUICK DATA SCIENCE SUMMARY
# ============================================================

print("\n========== FINAL SUMMARY ==========\n")

print("Dataset shape:", sales_df.shape)

print("Columns:")
print(sales_df.columns.tolist())

print("\nData types:")
print(sales_df.dtypes)

print("\nStatistical summary:")
print(sales_df.describe())

print("\nMissing values:")
print(sales_df.isnull().sum())


# ============================================================
# END OF PANDAS CRASH COURSE
# ============================================================

print("\n==========================================")
print("        PANDAS CRASH COURSE COMPLETE")
print("==========================================")