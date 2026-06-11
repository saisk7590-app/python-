from datetime import datetime


class Task:
    def __init__(self, title, created_at=None, completed=False):
        self.title = title
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M")
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def display(self):
        status = "✓" if self.completed else " "
        print(f"[{status}] {self.title} | Created: {self.created_at}")

    def to_line(self):
        return f"{self.title}|{self.created_at}|{self.completed}"

    @staticmethod
    def from_line(line):
        title, created_at, completed = line.strip().split("|")
        return Task(title, created_at, completed == "True")