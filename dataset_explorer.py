import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully")
print()

print("Shape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Unique values in each column
print("\nUnique Values:")
print(df.nunique())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Mean
print("\nMean Marks:")
print(df[["Maths", "Science"]].mean())

# Median
print("\nMedian Marks:")
print(df[["Maths", "Science"]].median())

# Minimum marks
print("\nMinimum Marks:")
print(df[["Maths", "Science"]].min())

# Maximum marks
print("\nMaximum Marks:")
print(df[["Maths", "Science"]].max())

# Students with Maths marks greater than 80
print("\nStudents with Maths Marks > 80:")
print(df[df["Maths"] > 80])

# Students from Delhi
print("\nStudents from Delhi:")
print(df[df["City"] == "Delhi"])

# Sort by Maths marks
print("\nStudents Sorted by Maths Marks:")
print(df.sort_values("Maths", ascending=False))

# Sort by Science marks
print("\nStudents Sorted by Science Marks:")
print(df.sort_values("Science", ascending=False))

# Calculate total marks
df["Total"] = df["Maths"] + df["Science"]

print("\nDataset with Total Marks:")
print(df)

# Calculate average marks
df["Average"] = df["Total"] / 2

print("\nDataset with Average Marks:")
print(df)

# Student with highest total marks
print("\nStudent with Highest Total Marks:")
print(df.loc[df["Total"].idxmax()])

# Student with lowest total marks
print("\nStudent with Lowest Total Marks:")
print(df.loc[df["Total"].idxmin()])

# Top 3 students based on Total Marks
print("\nTop 3 Students:")
print(df.nlargest(3, "Total")[["Name", "Total"]])

# Bottom 3 students
print("\nBottom 3 Students:")
print(df.nsmallest(3, "Total")[["Name", "Total"]])

# Average Maths marks
print("\nAverage Maths Marks:")
print(df["Maths"].mean())

# Average Science marks
print("\nAverage Science Marks:")
print(df["Science"].mean())

# Highest Maths marks
print("\nHighest Maths Marks:")
print(df["Maths"].max())

# Highest Science marks
print("\nHighest Science Marks:")
print(df["Science"].max())

# Number of students from each city
print("\nStudents from Each City:")
print(df["City"].value_counts())

# Average marks by city
print("\nAverage Marks by City:")
print(df.groupby("City")[["Maths", "Science", "Total"]].mean())

# Highest total marks from each city
print("\nHighest Total Marks by City:")
print(df.groupby("City")["Total"].max())

# Difference between Maths and Science marks
df["Difference"] = df["Maths"] - df["Science"]

print("\nMaths vs Science Difference:")
print(df[["Name", "Maths", "Science", "Difference"]])

# Students who scored higher in Maths
print("\nStudents who scored higher in Maths:")
print(df[df["Maths"] > df["Science"]][["Name", "Maths", "Science"]])

# Students who scored higher in Science
print("\nStudents who scored higher in Science:")
print(df[df["Science"] > df["Maths"]][["Name", "Maths", "Science"]])

df["Difference"] = df["Maths"] - df["Science"]

# Performance Category

def performance_category(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Good"
    elif average >= 70:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Average"].apply(performance_category)

print("\nPerformance Category:")
print(df[["Name", "Average", "Performance"]])

# Count students in each performance category

print("\nPerformance Category Count:")
print(df["Performance"].value_counts())

# Best student in Maths
best_maths = df.loc[df["Maths"].idxmax()]

print("\nBest Student in Maths:")
print(best_maths[["Name", "Maths"]])

# Best student in Science
best_science = df.loc[df["Science"].idxmax()]

print("\nBest Student in Science:")
print(best_science[["Name", "Science"]])

# Pass/Fail Analysis

passing_marks = 40

df["Maths_Result"] = df["Maths"].apply(
    lambda x: "Pass" if x >= passing_marks else "Fail"
)

df["Science_Result"] = df["Science"].apply(
    lambda x: "Pass" if x >= passing_marks else "Fail"
)

print("\nPass/Fail Analysis:")
print(df[["Name", "Maths", "Maths_Result", "Science", "Science_Result"]])

# Overall Result

df["Overall_Result"] = df.apply(
    lambda row: "Pass"
    if row["Maths"] >= passing_marks and row["Science"] >= passing_marks
    else "Fail",
    axis=1
)

print("\nOverall Result:")
print(df[["Name", "Maths", "Science", "Overall_Result"]])

print("\nOverall Result Count:")
print(df["Overall_Result"].value_counts())

# Subject-wise comparison

subject_averages = df[["Maths", "Science"]].mean()

print("\nSubject-wise Average:")
print(subject_averages)

print("\nBetter Performing Subject:")

if subject_averages["Maths"] > subject_averages["Science"]:
    print("Maths")
elif subject_averages["Science"] > subject_averages["Maths"]:
    print("Science")
else:
    print("Both subjects have the same average")

    # Correlation between Maths and Science

correlation = df["Maths"].corr(df["Science"])

print("\nCorrelation between Maths and Science:")
print(correlation)

# Correlation Matrix

print("\nCorrelation Matrix:")
print(df[["Age", "Maths", "Science", "Total", "Average"]].corr())

# Most consistent student

df["Absolute_Difference"] = df["Difference"].abs()

most_consistent = df.loc[df["Absolute_Difference"].idxmin()]

print("\nMost Consistent Student:")
print(most_consistent[["Name", "Maths", "Science", "Difference"]])

# Students scoring above the overall average

overall_average = df["Average"].mean()

print("\nOverall Average:")
print(overall_average)

print("\nStudents Above Overall Average:")
print(df[df["Average"] > overall_average][["Name", "Average"]])

# Top performing student from each city

top_by_city = df.loc[df.groupby("City")["Total"].idxmax()]

print("\nTop Student from Each City:")
print(top_by_city[["Name", "City", "Total", "Average"]])

# Numerical columns
numerical_columns = df.select_dtypes(include="number").columns

print("\nNumerical Columns:")
print(numerical_columns)

print("\nNumerical Data Summary:")
print(df[numerical_columns].describe())

# Categorical columns
categorical_columns = df.select_dtypes(include="object").columns

print("\nCategorical Columns:")
print(categorical_columns)

print("\nCategorical Data Summary:")
for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts())

    # Age Group Feature Engineering
def age_group(age):
    if age <= 19:
        return "Teen"
    elif age <= 21:
        return "Young Adult"
    else:
        return "Adult"

df["Age_Group"] = df["Age"].apply(age_group)

print("\nAge Group:")
print(df[["Name", "Age", "Age_Group"]])

print("\nAge Group Count:")
print(df["Age_Group"].value_counts())

# Performance Analysis by Age Group

print("\nAverage Marks by Age Group:")
print(
    df.groupby("Age_Group")[["Maths", "Science", "Total", "Average"]].mean()
)

print("\nNumber of Students by Age Group:")
print(df["Age_Group"].value_counts())

# Student Ranking

df["Rank"] = df["Average"].rank(
    ascending=False,
    method="dense"
).astype(int)

print("\nStudent Ranking:")
print(df[["Name", "Average", "Rank"]].sort_values("Rank"))

# Subject-wise Ranking

df["Maths_Rank"] = df["Maths"].rank(
    ascending=False,
    method="dense"
).astype(int)

df["Science_Rank"] = df["Science"].rank(
    ascending=False,
    method="dense"
).astype(int)

print("\nSubject-wise Ranking:")
print(
    df[
        ["Name", "Maths", "Maths_Rank", "Science", "Science_Rank"]
    ].sort_values("Maths_Rank")
)

# Grade Assignment

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)

print("\nStudent Grades:")
print(df[["Name", "Average", "Grade"]])

print("\nGrade Distribution:")
print(df["Grade"].value_counts().sort_index())

# Grade-wise Performance

print("\nAverage Performance by Grade:")
print(
    df.groupby("Grade")[["Maths", "Science", "Total", "Average"]].mean()
)

# Performance Range Analysis

print("\nStudents with Average >= 90:")
print(df[df["Average"] >= 90][["Name", "Average", "Grade"]])

print("\nStudents with Average < 70:")
print(df[df["Average"] < 70][["Name", "Average", "Grade"]])

print("\nHighest Average:")
print(df.loc[df["Average"].idxmax()][["Name", "Average", "Grade"]])

print("\nLowest Average:")
print(df.loc[df["Average"].idxmin()][["Name", "Average", "Grade"]])

# Missing Values Handling

print("\nMissing Values Before Handling:")
print(df.isnull().sum())

# Create a copy to avoid changing the original DataFrame
df_cleaned = df.copy()

# Fill missing numerical values with column mean
numerical_cols = df_cleaned.select_dtypes(include="number").columns

df_cleaned[numerical_cols] = df_cleaned[numerical_cols].fillna(
    df_cleaned[numerical_cols].mean()
)

print("\nMissing Values After Handling:")
print(df_cleaned.isnull().sum())

# Duplicate Rows Handling

print("\nDuplicate Rows Before Cleaning:")
print(df_cleaned.duplicated().sum())

df_deduplicated = df_cleaned.drop_duplicates().copy()

print("\nDuplicate Rows After Cleaning:")
print(df_deduplicated.duplicated().sum())

print("\nShape Before Cleaning:")
print(df_cleaned.shape)

print("\nShape After Cleaning:")
print(df_deduplicated.shape)

# Export Cleaned Dataset

output_file = "cleaned_dataset.csv"

df_deduplicated.to_csv(output_file, index=False)

print("\nCleaned Dataset Exported Successfully!")
print("File Name:", output_file)
print("Rows Exported:", len(df_deduplicated))
print("Columns Exported:", len(df_deduplicated.columns))

# Verify Exported Dataset

df_check = pd.read_csv("cleaned_dataset.csv")

print("\nExport Verification:")
print("File Loaded Successfully")

print("\nExported Dataset Shape:")
print(df_check.shape)

print("\nFirst 5 Rows of Exported Dataset:")
print(df_check.head())

print("\nMissing Values in Exported Dataset:")
print(df_check.isnull().sum().sum())

# Generate Analysis Report

report = f"""
DATASET EXPLORER - ANALYSIS REPORT
=================================

Total Students: {len(df_deduplicated)}

Average Maths Marks: {df_deduplicated["Maths"].mean():.2f}
Average Science Marks: {df_deduplicated["Science"].mean():.2f}

Highest Maths Marks: {df_deduplicated["Maths"].max()}
Highest Science Marks: {df_deduplicated["Science"].max()}

Highest Total Marks: {df_deduplicated["Total"].max()}
Lowest Total Marks: {df_deduplicated["Total"].min()}

Missing Values: {df_deduplicated.isnull().sum().sum()}
Duplicate Rows: {df_deduplicated.duplicated().sum()}
"""

with open("analysis_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nAnalysis Report Generated Successfully!")
print(report)

# City-wise Summary Report

city_report = (
    df_deduplicated
    .groupby("City")
    .agg(
        Student_Count=("Name", "count"),
        Average_Maths=("Maths", "mean"),
        Average_Science=("Science", "mean"),
        Average_Total=("Total", "mean")
    )
    .round(2)
)

print("\nCity-wise Summary Report:")
print(city_report)

city_report.to_csv("city_summary.csv")

print("\nCity Summary Exported Successfully!")

