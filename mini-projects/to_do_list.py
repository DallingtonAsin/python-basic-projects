directory = "../datasets"

def saved_and_unsaved_tasks(tasks):
    file = open(f"{directory}/tasks.txt")
    to_do = file.readlines()
    all_tasks = []

    if to_do:
        for t in to_do:
            t = t.strip("\n")
            all_tasks.append(t)
    if tasks:
        for i, task in enumerate(tasks, start=len(all_tasks)):
            all_tasks.append(f"{i + 1}. {task}")

    return all_tasks


def add_tasks(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully")


def view_tasks(tasks):

    all_tasks = saved_and_unsaved_tasks(tasks)
    if not all_tasks:
        print("There are currently no tasks")
    else:
        print("To do list:")
        for i, task in enumerate(all_tasks):
            print(task)


def save_new_tasks(tasks):
    try:
        all_tasks = saved_and_unsaved_tasks(tasks)
        file_obj = open(f"{directory}/tasks.txt", "w")
        if not tasks:
            print("No tasks to save")
        else:
            for i, task in enumerate(all_tasks):
                file_obj.write(f"{task}\n")
            print("Tasks saved successfully")
    except FileNotFoundError:
        print("Error: File not Found!")

def save_tasks(tasks):
    try:
        file_obj = open(f"{directory}/tasks.txt", "w")
        if not tasks:
            print("No tasks to save")
        else:
            for i, task in enumerate(tasks):
                file_obj.write(f"{task}\n")
            print("Tasks saved successfully")
    except FileNotFoundError:
        print("Error: File not Found!")

def load_tasks():
    try:
        file_obj = open(f"{directory}/tasks.txt")
        tasks = file_obj.readlines()

        if not tasks:
            print("There are no saved tasks!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(task)
    except FileNotFoundError as er:
        print("Error: File not Found!", er)


def mark_task_done(tasks):
    all_tasks = saved_and_unsaved_tasks(tasks)
    if not all_tasks:
        print("There are no tasks in the to-do list yet!")
    else:
        view_tasks(tasks)
        number = int(input("Enter the number of the task to mark done: "))
        index = number - 1
        if 0 <= index < len(all_tasks):
            done_task = all_tasks.pop(index)
            new_tasks = all_tasks
            print(f"Task {done_task} has been marked done and removed")
            save_tasks(new_tasks)
        else:
            print("Invalid task number")


def display_menu():
    print("Menu\n.......\n1. Add task\n2. Display tasks\n3. Save tasks\n4. Load tasks\n5. Mark task done\n6. Exit")

task_list = []

while True:
    display_menu()

    try:
        choice = int(input("Enter the choice: "))
        if choice == 1:
            add_tasks(task_list)
        elif choice == 2:
            view_tasks(task_list)
        elif choice == 3:
            save_new_tasks(task_list)
        elif choice == 4:
            load_tasks()
        elif choice == 5:
            mark_task_done(task_list)
        else:
            print("Error: Invalid choice")
            continue
    except ValueError as err:
        print("Error: ", err)
        continue