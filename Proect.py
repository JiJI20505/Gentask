import tkinter as tk
from tkinter import messagebox
import random
import json
import os


DEFAULT_TASKS = []
TIMES = ["5 мин", "10 мин", "15 мин", "20 мин", "30 мин"]

def load_tasks():
    return json.load(open("tasks.json", "r")) if os.path.exists("tasks.json") else []

def save_tasks(tasks):
    json.dump(tasks, open("tasks.json", "w"), ensure_ascii=False, indent=2)

root = tk.Tk()
root.title("Gentask")
root.geometry("520x620")
root.configure(bg="#2c3e50")

user_tasks = load_tasks()

def update_list():
    listbox.delete(0, tk.END)
    for t in DEFAULT_TASKS:
        listbox.insert(tk.END, f"🔹 {t}")
    for t in user_tasks:
        listbox.insert(tk.END, f"➕ {t}")

def generate():
    all_tasks = DEFAULT_TASKS + user_tasks
    if all_tasks:
        task_label.config(text=random.choice(all_tasks))
        time_label.config(text=f"⏱️ {random.choice(TIMES)}")
        emoji_label.config(text=random.choice(["✨", "🎯", "📚", "💪","🏅","🎁"]))

def add():
    task = entry.get().strip()
    if task and task not in user_tasks and task not in DEFAULT_TASKS:
        user_tasks.append(task)
        save_tasks(user_tasks)
        update_list()
        entry.delete(0, tk.END)
        messagebox.showinfo("✅", "Задача добавлена!")

def delete():
    sel = listbox.curselection()
    if sel:
        task = listbox.get(sel[0])[2:]
        if task in user_tasks:
            user_tasks.remove(task)
            save_tasks(user_tasks)
            update_list()
            messagebox.showinfo("🗑️", "Задача удалена!")

tk.Label(root, text=" ГЕНЕРАТОР ДЕЛ", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white").pack(pady=15)

tk.Button(root, text=" СЛУЧАЙНОЕ ДЕЛО", font=("Arial", 12, "bold"), bg="#e67e22", fg="white",
          command=generate, padx=20, pady=10).pack(pady=10)

frame = tk.Frame(root, bg="white", relief=tk.RAISED, bd=2)
frame.pack(pady=10, padx=20, fill=tk.X)

emoji_label = tk.Label(frame, text="✨", font=("Arial", 36), bg="white")
emoji_label.pack(pady=5)

task_label = tk.Label(frame, text="Нажми кнопку!", font=("Arial", 12), bg="white", wraplength=350)
task_label.pack(pady=5)

time_label = tk.Label(frame, text="⏱️ --", font=("Arial", 10), bg="white")
time_label.pack(pady=5)

add_frame = tk.Frame(root, bg="#2c3e50")
add_frame.pack(pady=10, padx=20, fill=tk.X)

entry = tk.Entry(add_frame, font=("Arial", 11))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

tk.Button(add_frame, text="➕", font=("Arial", 10), bg="#27ae60", fg="white", command=add, width=3).pack(side=tk.RIGHT)

tk.Label(root, text=" МОИ ЗАДАЧИ - ДОБАВЬТЕ НОВУЮ ЗАДАЧУ⏫", font=("Arial", 10, "bold"), bg="#2c3e50", fg="white").pack()

listbox = tk.Listbox(root, height=8, font=("Arial", 10))
listbox.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

tk.Button(root, text="✖ Удалить выбранную задачу", font=("Arial", 10), bg="#c0392b", fg="white",
          command=delete).pack(pady=5)

update_list()
root.mainloop()