import mysql.connector
import pandas as pd
import numpy as np

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yuvayash@2631",
    database="student_management"
)
cursor = conn.cursor()

# Fetch student data from MySQL
query = "SELECT id, name, age, gender, department, marks FROM students"
cursor.execute(query)
rows = cursor.fetchall()

# Convert data to Pandas DataFrame
columns = ["ID", "Name", "Age", "Gender", "Department", "Marks"]
df = pd.DataFrame(rows, columns=columns)

# Display student data
print("Student Data:\n", df)
# Check if DataFrame is empty
if df.empty:
    print("\n⚠ No student records found! Please add students first.")
else:
    # Calculate Average Marks
    average_marks = df["Marks"].mean()
    print("\n📌 Average Marks of Students:", round(average_marks, 2))

    # Find Highest & Lowest Scorers
    highest_score = df["Marks"].max()
    lowest_score = df["Marks"].min()

    top_students = df[df["Marks"] == highest_score]["Name"].tolist()
    low_students = df[df["Marks"] == lowest_score]["Name"].tolist()

    print("\n🏆 Highest Score:", highest_score, "by", top_students)
    print("\n❌ Lowest Score:", lowest_score, "by", low_students)

    # Assume Pass Mark is 40
    pass_mark = 40

    # Count Passed & Failed Students
    passed_students = df[df["Marks"] >= pass_mark].shape[0]
    failed_students = df[df["Marks"] < pass_mark].shape[0]

    total_students = df.shape[0]

    if total_students > 0:  # Prevent division by zero
        pass_percentage = (passed_students / total_students) * 100
        print("\n✅ Pass Percentage:", round(pass_percentage, 2), "%")
        print("🎓 Students Passed:", passed_students, "❌ Failed:", failed_students)
    else:
        print("\n⚠ No student data available for percentage calculation.")

    # Analyze Department-wise Performance
    dept_performance = df.groupby("Department")["Marks"].mean()
    print("\n📊 Department-wise Average Marks:\n", dept_performance)
