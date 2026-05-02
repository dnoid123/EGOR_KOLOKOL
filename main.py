import random
import json
import os
from tkinter import *
from tkinter import messagebox

tasks_list = [
    ("Прочитать статью", "учёба"),
    ("Сделать зарядку", "спорт"),
    ("Написать отчёт", "работа"),
    ("Сделать домашнее задание", "учёба"),
    ("Отжаться 20 раз", "спорт"),
    ("Ответить на письма", "работа"),
    ("Посмотреть лекцию", "учёба"),
    ("Пробежать 1 км", "спорт"),
    ("Создать презентацию", "работа"),
    ("Решить 5 задач", "учёба"),
    ("Сделать план на день", "работа")
]

history = [] 
file_name = "history.json" 


def load_history():
    global history
    if os.path.exists(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                history = json.load(f)
            update_history_list()
        except:
            history = []


def save_history():
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def update_history_list():
    listbox_history.delete(0, END)
    filter_type = filter_var.get()
    
    for item in history:
        task_text = item["task"]
        task_type = item["type"]
        
        if filter_type == "Все" or filter_type == task_type:
            listbox_history.insert(END, f"{task_text} ({task_type})")


def generate_task():
    if not tasks_list:
        messagebox.showwarning("Внимание", "Список задач пуст!")
        return
    
    task_name, task_type = random.choice(tasks_list)
    
    history_item = {
        "task": task_name,
        "type": task_type
    }
    history.append(history_item)
    save_history()
    update_history_list()
    
    label_result.config(text=f"Задача: {task_name}")
    label_type_info.config(text=f"Тип: {task_type}")

root = Tk()
root.title("Random Task Generator")
root.geometry("600x500")
root.resizable(False, False)

label_result = Label(root, text="Нажмите кнопку", font=("Arial", 14))
label_result.pack(pady=20)

label_type_info = Label(root, text="", font=("Arial", 11))
label_type_info.pack()

btn_generate = Button(root, text="Сгенерировать задачу", font=("Arial", 12),
                      bg="lightblue", command=generate_task, width=25, height=2)
btn_generate.pack(pady=20)

Label(root, text="История задач", font=("Arial", 12, "bold")).pack(pady=(15, 5))

frame_filter = Frame(root)
frame_filter.pack(pady=5)

Label(frame_filter, text="Фильтр по типу:", font=("Arial", 10)).pack(side=LEFT, padx=5)

filter_var = StringVar(value="Все")
filter_options = ["Все", "учёба", "спорт", "работа"]
filter_menu = OptionMenu(frame_filter, filter_var, *filter_options, command=lambda x: update_history_list())
filter_menu.config(width=10)
filter_menu.pack(side=LEFT, padx=5)

frame_list = Frame(root)
frame_list.pack(pady=5, fill=BOTH, expand=True, padx=10)

scrollbar = Scrollbar(frame_list)
scrollbar.pack(side=RIGHT, fill=Y)

listbox_history = Listbox(frame_list, yscrollcommand=scrollbar.set, height=12, font=("Arial", 10))
listbox_history.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=listbox_history.yview)

load_history()

root.mainloop()
