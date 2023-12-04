import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        # Add Task Button
        add_task_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 12), bg="green", fg="white")
        add_task_button.pack(pady=10)

        # Task List
        self.task_listbox = tk.Listbox(root, selectbackground="lightblue", selectmode=tk.SINGLE, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Remove Task Button
        remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=("Arial", 12), bg="red", fg="white")
        remove_task_button.pack(pady=10)

        # Initialize tasks
        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{idx}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
