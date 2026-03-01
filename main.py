from app.auth import Auth
from task_manager import TaskManager


def authenticate():
    while True:
        print("\n=== AUTH MENU ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            user = Auth.login()
            if user:
                return user

        elif choice == "2":
            user = Auth.register()
            if user:
                return user

        elif choice == "3":
            exit()

        else:
            print("Invalid option.")


def main():
    user = authenticate()
    manager = TaskManager(user)

    while True:
        print(f"\n=== TO-DO LIST ({user.username}) ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.mark_done()
        elif choice == "4":
            manager.delete_task()
        elif choice == "5":
            manager.save()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()