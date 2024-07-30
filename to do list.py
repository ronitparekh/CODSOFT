import tkinter as tk
from tkinter import messagebox, ttk
import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({'task': task, 'done': False})
        save_tasks()
        list_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task description.")

def list_tasks():
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    for index, task in enumerate(tasks, start=1):
        status = '✓' if task['done'] else '✗'
        status_color = 'green' if task['done'] else 'red'
        text_widget.insert(tk.END, f"{index}. ", 'task_number')
        text_widget.insert(tk.END, status, status_color)
        text_widget.insert(tk.END, f" {task['task']}\n", 'task_text')
    text_widget.config(state=tk.DISABLED)

def mark_task_done():
    try:
        selected_index = int(task_index_entry.get()) - 1
        if 0 <= selected_index < len(tasks):
            tasks[selected_index]['done'] = True
            save_tasks()
            list_tasks()
            task_index_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

def delete_task():
    try:
        selected_index = int(task_index_entry.get()) - 1
        if 0 <= selected_index < len(tasks):
            del tasks[selected_index]
            save_tasks()
            list_tasks()
            task_index_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

def main():
    load_tasks()

    global root, text_widget, task_entry, task_index_entry
    root = tk.Tk()
    root.title("To-Do List Application")
    root.geometry("650x500")
    root.configure(bg='#add8e6')

    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12))
    style.configure('TLabel', font=('Helvetica', 12))

    frame = tk.Frame(root, bg='#add8e6')
    frame.pack(pady=10)

    text_widget = tk.Text(frame, width=70, height=20, font=('Helvetica', 12), state=tk.DISABLED, bg='#f0f8ff')
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, padx=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    text_widget.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_widget.yview)

    text_widget.tag_config('green', foreground='green')
    text_widget.tag_config('red', foreground='red')
    text_widget.tag_config('task_number', font=('Helvetica', 12, 'bold'))
    text_widget.tag_config('task_text', font=('Helvetica', 12))

    task_entry_frame = tk.Frame(root, bg='#add8e6')
    task_entry_frame.pack(pady=10)

    task_entry_label = ttk.Label(task_entry_frame, text="Task Description:", background='#add8e6')
    task_entry_label.grid(row=0, column=0, padx=5)

    task_entry = ttk.Entry(task_entry_frame, width=40, font=('Helvetica', 12))
    task_entry.grid(row=0, column=1, padx=5)

    add_button = ttk.Button(task_entry_frame, text="Add Task", command=add_task)
    add_button.grid(row=0, column=2, padx=5)

    task_index_frame = tk.Frame(root, bg='#add8e6')
    task_index_frame.pack(pady=10)

    task_index_label = ttk.Label(task_index_frame, text="Task Number:", background='#add8e6')
    task_index_label.grid(row=0, column=0, padx=5)

    task_index_entry = ttk.Entry(task_index_frame, width=10, font=('Helvetica', 12))
    task_index_entry.grid(row=0, column=1, padx=5)

    mark_done_button = ttk.Button(task_index_frame, text="Mark Done", command=mark_task_done)
    mark_done_button.grid(row=0, column=2, padx=5)

    delete_button = ttk.Button(task_index_frame, text="Delete Task", command=delete_task)
    delete_button.grid(row=0, column=3, padx=5)

    exit_button = ttk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

    list_tasks()

    root.mainloop()

if __name__ == "__main__":
    main()
