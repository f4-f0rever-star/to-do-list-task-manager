from task import Task


class Storage:

    @staticmethod
    def load_tasks(username):
        tasks = []
        filename = f"{username}_tasks.txt"

        try:
            with open(filename, "r") as file:
                for line in file:
                    tasks.append(Task.from_file_format(line))
        except FileNotFoundError:
            pass

        return tasks

    @staticmethod
    def save_tasks(username, tasks):
        filename = f"{username}_tasks.txt"

        with open(filename, "w") as file:
            for task in tasks:
                file.write(task.to_file_format() + "\n")