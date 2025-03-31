import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yuvayash@2631",
    database="student_management"
)
cursor = conn.cursor()


# Function to sign up a new user
def signup():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Signup successful! Please login.")
    except:
        messagebox.showerror("Error", "Username already exists!")


# Function to log in
def login():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()  # Close login window and proceed to the main app
    else:
        messagebox.showerror("Error", "Invalid username or password!")


# GUI Setup
root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username:").grid(row=0, column=0)
tk.Label(root, text="Password:").grid(row=1, column=0)

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Hide password input
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

btn_signup = tk.Button(root, text="Sign Up", command=signup)
btn_login = tk.Button(root, text="Login", command=login)
btn_signup.grid(row=2, column=0)
btn_login.grid(row=2, column=1)

root.mainloop()
