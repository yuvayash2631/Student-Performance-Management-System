import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yuvayash@2631",
    database="student_management"
)
cursor = conn.cursor()


# Function to add student
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    department = entry_department.get()
    marks = entry_marks.get()

    if name == "" or age == "" or department == "" or marks == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute("INSERT INTO students (name, age, gender, department, marks) VALUES (%s, %s, %s, %s, %s)",
                       (name, age, gender, department, marks))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        fetch_students()  # Refresh table
    except:
        messagebox.showerror("Error", "Failed to add student!")


# Function to update student
def update_student():
    selected_item = student_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a student to update!")
        return

    student_id = student_table.item(selected_item, "values")[0]
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    department = entry_department.get()
    marks = entry_marks.get()

    cursor.execute("UPDATE students SET name=%s, age=%s, gender=%s, department=%s, marks=%s WHERE id=%s",
                   (name, age, gender, department, marks, student_id))
    conn.commit()
    messagebox.showinfo("Success", "Student updated successfully!")
    fetch_students()  # Refresh table


# Function to delete student
def delete_student():
    selected_item = student_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a student to delete!")
        return

    student_id = student_table.item(selected_item, "values")[0]
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    messagebox.showinfo("Success", "Student deleted successfully!")
    fetch_students()  # Refresh table


# Function to fetch and display students in table
def fetch_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    student_table.delete(*student_table.get_children())
    for row in rows:
        student_table.insert("", "end", values=row)


# GUI Setup
root = tk.Tk()
root.title("Student Performance Management System")

# Labels and Entry Fields
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Label(root, text="Gender:").grid(row=2, column=0)
tk.Label(root, text="Department:").grid(row=3, column=0)
tk.Label(root, text="Marks:").grid(row=4, column=0)

entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
gender_var = tk.StringVar(value="Male")
gender_menu = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"])
entry_department = tk.Entry(root)
entry_marks = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
gender_menu.grid(row=2, column=1)
entry_department.grid(row=3, column=1)
entry_marks.grid(row=4, column=1)

# Buttons
btn_add = tk.Button(root, text="Add Student", command=add_student)
btn_update = tk.Button(root, text="Update Student", command=update_student)
btn_delete = tk.Button(root, text="Delete Student", command=delete_student)

btn_add.grid(row=5, column=0)
btn_update.grid(row=5, column=1)
btn_delete.grid(row=5, column=2)

# Table to Display Students
columns = ("ID", "Name", "Age", "Gender", "Department", "Marks")
student_table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    student_table.heading(col, text=col)

student_table.grid(row=6, column=0, columnspan=3)
fetch_students()  # Load student data

root.mainloop()
