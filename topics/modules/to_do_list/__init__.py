
class ToDoList:
    """
      To do list module
    """

    def __init__(self, directory = None, filename = None):
        """
        :param directory:
        :param filename:

        """
        if directory is None:
            directory = "../datasets"
        self.directory = directory
        if filename is None:
            filename = "tasks.txt"
        self.filename = filename
        self.work_directory = f"{self.directory}/{self.filename}"


    def saved_and_unsaved_tasks(self, tasks):
        """

        :param tasks:
        :return:
        """
        file = open(self.work_directory)
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


    def add_tasks(self, tasks):
        """

        :param tasks:
        :return:
        """
        task = input("Enter task description: ")
        tasks.append(task)
        print("Task added successfully")


    def view_tasks(self, tasks):
        """

        :param tasks:
        :return:
        """
        all_tasks = self.saved_and_unsaved_tasks(tasks)
        if not all_tasks:
            print("There are currently no tasks")
        else:
            print("To do list:")
            for i, task in enumerate(all_tasks):
                print(task)


    def save_new_tasks(self, tasks):
        try:
            all_tasks = self.saved_and_unsaved_tasks(tasks)
            file_obj = open(self.work_directory, "w")
            if not tasks:
                print("No tasks to save")
            else:
                for i, task in enumerate(all_tasks):
                    file_obj.write(f"{task}\n")
                print("Tasks saved successfully")
        except FileNotFoundError:
            print("Error: File not Found!")


    def save_tasks(self, tasks):
        """

        :param tasks:
        :return:
        """
        try:
            file_obj = open(self.work_directory, "w")
            if not tasks:
                print("No tasks to save")
            else:
                for i, task in enumerate(tasks):
                    file_obj.write(f"{task}\n")
                print("Tasks saved successfully")
        except FileNotFoundError:
            print("Error: File not Found!")


    def load_tasks(self):
        """

        :return:
        """
        try:
            file_obj = open(self.work_directory)
            tasks = file_obj.readlines()

            if not tasks:
                print("There are no saved tasks!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(task)
        except FileNotFoundError as er:
            print("Error: File not Found!", er)


    def mark_task_done(self, tasks):
        """

        :param tasks:
        :return:
        """
        all_tasks = self.saved_and_unsaved_tasks(tasks)
        if not all_tasks:
            print("There are no tasks in the to-do list yet!")
        else:
            self.view_tasks(tasks)
            number = int(input("Enter the number of the task to mark done: "))
            index = number - 1
            if 0 <= index < len(all_tasks):
                done_task = all_tasks.pop(index)
                new_tasks = all_tasks
                print(f"Task {done_task} has been marked done and removed")
                self.save_tasks(new_tasks)
            else:
                print("Invalid task number")


    def display_menu(self):
        """

        :return:
        """
        print("Menu\n.......\n1. Add task\n2. Display tasks\n3. Save tasks\n4. Load tasks\n5. Mark task done\n6. Exit")