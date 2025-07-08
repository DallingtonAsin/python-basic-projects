from topics.modules.to_do_list import ToDoList

task_list = []
to_do_list = ToDoList()

while True:
    to_do_list.display_menu()

    try:
        choice = int(input("Enter the choice: "))
        if choice == 1:
            to_do_list.add_tasks(task_list)
        elif choice == 2:
            to_do_list.view_tasks(task_list)
        elif choice == 3:
            to_do_list.save_new_tasks(task_list)
        elif choice == 4:
            to_do_list.load_tasks()
        elif choice == 5:
            to_do_list.mark_task_done(task_list)
        else:
            print("Error: Invalid choice")
            continue
    except ValueError as err:
        print("Error: ", err)
        continue