import tkinter
from tkinter import *
import re

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def submit():
    name = name_entry.get()
    email = email_entry.get()
    
    if not name or not email:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format.")
        return
    
    user = User(name, email)
    messagebox.showinfo("Success", f"User {user.name} added with email {user.email}!")
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Create the main window
root = Tk()
root.title("User Registration")
root.geometry("300x200")

# Create and place the labels and entries
tk.Label(root, text="Name").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
