# task_manager.py

from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))
        print("✅ Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n===== TASKS =====")

        for index, task in enumerate(self.tasks, start=1):
            print(f"\nTask {index}")
            task.display()

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):

            task = self.tasks[task_number - 1]

            task.mark_completed()

            print(
                f"✅ '{task.title}' marked as completed."
            )

        else:
            print("❌ Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):

            removed_task = self.tasks.pop(
                task_number - 1
            )

            print(
                f"🗑️ '{removed_task.title}' deleted."
            )

        else:
            print("❌ Invalid task number.")

    def show_statistics(self):
        total = len(self.tasks)

        completed = sum(
            task.completed
            for task in self.tasks
        )

        pending = total - completed

        print("\n===== STATISTICS =====")
        print(f"Total Tasks : {total}")
        print(f"Completed   : {completed}")
        print(f"Pending     : {pending}")