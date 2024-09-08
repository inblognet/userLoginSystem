import tkinter as tk
from tkinter import messagebox
import database
import hashlib
import mysql.connector

# Function to register a new user
def register_user():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not username or not email or not password:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        conn = database.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_password)
        )
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Function to log in an existing user
def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Input Error", "Both username and password are required!")
        return

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        conn = database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",
                       (username, hashed_password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# GUI Setup
app = tk.Tk()
app.title("User Registration and Login")
app.geometry("400x300")

# Username Label and Entry
tk.Label(app, text="Username:").pack(pady=5)
username_entry = tk.Entry(app)
username_entry.pack(pady=5)

# Email Label and Entry (only needed for registration)
tk.Label(app, text="Email:").pack(pady=5)
email_entry = tk.Entry(app)
email_entry.pack(pady=5)

# Password Label and Entry
tk.Label(app, text="Password:").pack(pady=5)
password_entry = tk.Entry(app, show="*")
password_entry.pack(pady=5)

# Register Button
register_button = tk.Button(app, text="Register", command=register_user)
register_button.pack(pady=10)

# Login Button
login_button = tk.Button(app, text="Login", command=login_user)
login_button.pack(pady=10)

# Run the GUI loop
app.mainloop()
