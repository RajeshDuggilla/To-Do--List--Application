import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")

def add_task():
    task = task_entry.get()
    if task:
        tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        task_index = tasks.curselection()[0]
        tasks.delete(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def mark_task():
    try:
        task_index = tasks.curselection()[0]
        task = tasks.get(task_index)
        tasks.delete(task_index)
        tasks.insert(tk.END, task + " (Done)")
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")

tasks = tk.Listbox(root, width=50, height=10)
tasks.pack(pady=10)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as Done", command=mark_task)
mark_button.pack(pady=5)

root.mainloop()
