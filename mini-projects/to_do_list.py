from topics.modules.to_do_list import ToDoList, display_menu, add_tasks

task_list = []
to_do_list = ToDoList()

while True:
    display_menu()

    try:
        choice = int(input("Enter the choice: "))
        if choice == 1:
            add_tasks(task_list)
        elif choice == 2:
            to_do_list.view_tasks(task_list)
        elif choice == 3:
            to_do_list.save_new_tasks(task_list)
        elif choice == 4:
            to_do_list.load_tasks()
        elif choice == 5:
            to_do_list.mark_task_done(task_list)
        elif choice == 6:
            to_do_list.get_word_length()
        elif choice == 7:
            to_do_list.get_character_length()
        elif choice == 8:
            exit(0)
        else:
            print("Error: Invalid choice")
            continue
    except ValueError as err:
        print("Error: ", err)
        continue