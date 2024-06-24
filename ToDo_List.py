import tkinter as tk
from tkinter import ttk
import os

class TodoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        # Create the main frame
        self.frame = ttk.Frame(master, padding=10)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Create the task entry field
        self.task_entry = ttk.Entry(self.frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        # Create the "Add Task" button
        self.add_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Create the task listbox
        self.task_listbox = tk.Listbox(self.frame, width=30, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Create the "Delete Task" button
        self.delete_button = ttk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5)

        # Create the "Clear All" button
        self.clear_button = ttk.Button(self.frame, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=5, pady=5)

        # Load tasks from file
        self.tasks = self.load_tasks()
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

        # Bind the window closing event
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.tasks.pop(selected[0])
            self.task_listbox.delete(selected[0])
            self.save_tasks()

    def clear_tasks(self):
        self.tasks.clear()
        self.task_listbox.delete(0, tk.END)
        self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

    def on_close(self):
        self.save_tasks()
        self.master.destroy()

root = tk.Tk()
todo_list = TodoList(root)
root.mainloop()
