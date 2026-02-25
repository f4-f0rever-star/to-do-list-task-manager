class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    def mark_pending(self):
        self.done = False

    def display(self, index):
        status = "DONE" if self.done else "NOT DONE"
        return f"{index}. {self.description} [{status}]"

    def to_file_format(self):
        status = "Done" if self.done else "Pending"
        return f"{self.description}|{status}"

    @classmethod
    def from_file_format(cls, line):
        description, status = line.strip().split("|")
        return cls(description, status == "Done")

    def __str__(self):
        return self.to_file_format()