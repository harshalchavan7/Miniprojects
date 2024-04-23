class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found!")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")

    def edit_task(self, index, new_task):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print("Task edited successfully!")
        else:
            print("Invalid task number!")

if __name__ == "__main__":
    my_todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Edit Task\n4. Display Tasks\n5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            my_todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            my_todo_list.remove_task(task)
        elif choice == "3":
            index = int(input("Enter the task number to edit: "))
            new_task = input("Enter the new task: ")
            my_todo_list.edit_task(index, new_task)
        elif choice == "4":
            my_todo_list.display_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
