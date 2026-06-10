# task.py

from datetime import datetime


class Task:
    def __init__(self, title, completed=False, created_at=None):
        self.title = title
        self.completed = completed

        if created_at:
            self.created_at = created_at
        else:
            self.created_at = datetime.now()

    def mark_completed(self):
        self.completed = True

    def display(self):
        status = "✓" if self.completed else " "

        print(
            f"[{status}] {self.title}"
        )

        print(
            f"Created At: "
            f"{self.created_at.strftime('%Y-%m-%d %H:%M')}"
        )