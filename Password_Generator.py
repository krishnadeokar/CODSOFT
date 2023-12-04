import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Apply themed style
style = ttk.Style()
style.theme_use("clam")  # You can experiment with different themes

# Configure additional style options
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Create and place widgets with updated styles
label_style = "TLabel" if ttk.Style().theme_use() == "clam" else "Label"
ttk.Label(root, text="Enter Password Length:", style=label_style).pack(pady=10)

entry_style = "TEntry" if ttk.Style().theme_use() == "clam" else "Entry"
length_entry = ttk.Entry(root, width=30, style=entry_style)
length_entry.pack(pady=10)

button_style = "TButton" if ttk.Style().theme_use() == "clam" else "Button"
generate_button = ttk.Button(root, text="Generate Password", command=generate_and_display_password, style=button_style)
generate_button.pack(pady=20)

result_label = ttk.Label(root, text="", style=label_style)
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
