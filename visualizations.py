import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Maths vs Science Bar Chart
plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Maths"], label="Maths")
plt.bar(
    df["Name"],
    df["Science"],
    bottom=df["Maths"],
    label="Science"
)

plt.title("Student Marks: Maths + Science")
plt.xlabel("Student")
plt.ylabel("Combined Marks")
plt.legend()

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Compare Maths and Science
plt.figure(figsize=(9, 5))

x = range(len(df))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    df["Maths"],
    width=width,
    label="Maths"
)

plt.bar(
    [i + width / 2 for i in x],
    df["Science"],
    width=width,
    label="Science"
)

plt.title("Maths vs Science Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(list(x), df["Name"])
plt.legend()

plt.tight_layout()
plt.show()


# City-wise Average Marks

city_avg = df.groupby("City")[["Maths", "Science"]].mean()

plt.figure(figsize=(8, 5))

city_avg.plot(kind="bar", width=0.8)

plt.title("City-wise Average Marks")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.legend(title="Subject")

plt.tight_layout()
plt.show()


# Student Total Marks Bar Chart

df["Total"] = df["Maths"] + df["Science"]

plt.figure(figsize=(9, 5))

plt.bar(df["Name"], df["Total"])

plt.title("Student Total Marks")
plt.xlabel("Student")
plt.ylabel("Total Marks")

plt.tight_layout()
plt.show()


# Marks Distribution Histogram

plt.figure(figsize=(8, 5))

plt.hist(df["Maths"], bins=5, edgecolor="black")

plt.title("Distribution of Maths Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()


# Science Marks Distribution

plt.figure(figsize=(8, 5))

plt.hist(df["Science"], bins=5, edgecolor="black")

plt.title("Distribution of Science Marks")
plt.xlabel("Science Marks")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()


# Subject-wise Average Marks

subjects = ["Maths", "Science"]
averages = [df["Maths"].mean(), df["Science"].mean()]

plt.figure(figsize=(7, 5))

plt.bar(subjects, averages, edgecolor="black")

plt.title("Average Marks: Maths vs Science")
plt.xlabel("Subject")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.show()


# Number of Students in Each City

city_counts = df["City"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(city_counts.index, city_counts.values, edgecolor="black")

plt.title("Number of Students in Each City")
plt.xlabel("City")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()


# Maths vs Science Scatter Plot

plt.figure(figsize=(8, 5))

plt.scatter(df["Maths"], df["Science"])

plt.title("Maths vs Science: Student Performance")
plt.xlabel("Maths Marks")
plt.ylabel("Science Marks")

plt.tight_layout()
plt.show()


# Correlation Heatmap

correlation = df[["Maths", "Science"]].corr()

plt.figure(figsize=(6, 5))

plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)

plt.colorbar(label="Correlation")

plt.xticks([0, 1], correlation.columns)
plt.yticks([0, 1], correlation.index)

for i in range(2):
    for j in range(2):
        plt.text(
            j, i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Maths vs Science Correlation")
plt.tight_layout()
plt.show()


# Top 3 Students by Total Marks

top_students = df.nlargest(3, "Total")

plt.figure(figsize=(7, 5))

plt.bar(top_students["Name"], top_students["Total"])

plt.title("Top 3 Students by Total Marks")
plt.xlabel("Student")
plt.ylabel("Total Marks")

plt.tight_layout()
plt.show()


# Top 3 Students by Maths Marks

top_maths = df.nlargest(3, "Maths")

plt.figure(figsize=(7, 5))

plt.bar(top_maths["Name"], top_maths["Maths"])

plt.title("Top 3 Students in Maths")
plt.xlabel("Student")
plt.ylabel("Maths Marks")

plt.tight_layout()
plt.show()


# Top 3 Students in Science

top_science = df.nlargest(3, "Science")

plt.figure(figsize=(7, 5))

plt.bar(top_science["Name"], top_science["Science"])

plt.title("Top 3 Students in Science")
plt.xlabel("Student")
plt.ylabel("Science Marks")

plt.tight_layout()
plt.show()


# Maths and Science Box Plot

plt.figure(figsize=(7, 5))

plt.boxplot(
    [df["Maths"], df["Science"]],
    tick_labels=["Maths", "Science"]
)

plt.title("Marks Distribution: Maths vs Science")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()


# Maths vs Science Line Chart

plt.figure(figsize=(9, 5))

plt.plot(
    df["Name"],
    df["Maths"],
    marker="o",
    label="Maths"
)

plt.plot(
    df["Name"],
    df["Science"],
    marker="o",
    label="Science"
)

plt.title("Maths vs Science Marks by Student")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.legend()

plt.tight_layout()
plt.show()


# Mini Dashboard: 4 Charts in One Window

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. Total marks by student
axes[0, 0].bar(df["Name"], df["Total"])
axes[0, 0].set_title("Total Marks by Student")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Maths vs Science
axes[0, 1].bar(df["Name"], df["Maths"], label="Maths")
axes[0, 1].bar(
    df["Name"],
    df["Science"],
    bottom=df["Maths"],
    label="Science"
)
axes[0, 1].set_title("Maths + Science")
axes[0, 1].legend()
axes[0, 1].tick_params(axis="x", rotation=45)

# 3. Average marks by city
city_avg.plot(kind="bar", ax=axes[1, 0])
axes[1, 0].set_title("City-wise Average Marks")
axes[1, 0].tick_params(axis="x", rotation=0)

# 4. Maths vs Science scatter plot
axes[1, 1].scatter(df["Maths"], df["Science"])
axes[1, 1].set_title("Maths vs Science Relationship")
axes[1, 1].set_xlabel("Maths")
axes[1, 1].set_ylabel("Science")

fig.suptitle("Dataset Explorer Dashboard")
plt.tight_layout()
plt.savefig("dataset_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()

