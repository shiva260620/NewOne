import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        # Add code to open the main application window or perform other actions after successful login
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Page")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
