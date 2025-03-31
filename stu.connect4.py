import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample DataFrame creation (you would typically load this from a file)
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Marks': [85, 58, 90, 45, 76],
    'Department': ['Science', 'Commerce', 'Science', 'Arts', 'Commerce']
}

# Create DataFrame
df = pd.DataFrame(data)

# Ensure there are no missing marks
df = df.dropna(subset=['Marks'])

# Check if DataFrame is empty
if df.empty:
    print("\n⚠ No student records found! Please add students first.")
else:
    # 1. Plot Marks Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Marks"], bins=10, kde=True, color="blue")
    plt.title("Marks Distribution of Students")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.show()

    # 2. Plot Pass vs Fail Students
    # Defining the pass/fail criteria (e.g., passing marks >= 50)
    passed_students = df[df["Marks"] >= 50].shape[0]
    failed_students = df[df["Marks"] < 50].shape[0]

    labels = ["Passed", "Failed"]
    values = [passed_students, failed_students]
    colors = ["green", "red"]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
    plt.title("Pass vs Fail Percentage")
    plt.show()

    # 3. Plot Department-wise Average Marks
    # Calculate average marks per department
    dept_performance = df.groupby('Department')['Marks'].mean()

    plt.figure(figsize=(8, 5))
    sns.barplot(x=dept_performance.index, y=dept_performance.values, palette="viridis")
    plt.title("Department-wise Average Marks")
    plt.xlabel("Department")
    plt.ylabel("Average Marks")
    plt.xticks(rotation=45)
    plt.show()
