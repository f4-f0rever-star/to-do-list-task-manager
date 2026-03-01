from app.storage import Storage
from app.task import Task


class TaskManager:
    def __init__(self, user):
        self.user = user
        self.tasks = Storage.load_tasks(user.username)

    def add_task(self):
        description = input("Enter task: ")
        self.tasks.append(Task(description))
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(task.display(i))

    def mark_done(self):
        self.view_tasks()
        try:
            num = int(input("Task number to mark done: "))
            self.tasks[num - 1].mark_done()
            print("Task completed!")
        except:
            print("Invalid choice.")

    def delete_task(self):
        self.view_tasks()
        try:
            num = int(input("Task number to delete: "))
            self.tasks.pop(num - 1)
            print("Task deleted!")
        except:
            print("Invalid choice.")

    def save(self):
        Storage.save_tasks(self.user.username, self.tasks)