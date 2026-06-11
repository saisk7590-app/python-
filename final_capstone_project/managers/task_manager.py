from models.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    # -------------------------
    # ADD TASK
    # -------------------------
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    # -------------------------
    # VIEW TASKS
    # -------------------------
    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return

        print("\n===== TASK LIST =====")
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else " "
            print(f"{i}. [{status}] {task.title} | {task.created_at}")

    # -------------------------
    # COMPLETE TASK
    # -------------------------
    def complete_task(self, index):
        try:
            if 1 <= index <= len(self.tasks):
                self.tasks[index - 1].mark_done()
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except Exception as e:
            print("Error:", e)

    # -------------------------
    # DELETE TASK
    # -------------------------
    def delete_task(self, index):
        try:
            if 1 <= index <= len(self.tasks):
                removed = self.tasks.pop(index - 1)
                print(f"Deleted: {removed.title}")
            else:
                print("Invalid task number.")
        except Exception as e:
            print("Error:", e)

    # -------------------------
    # LOAD TASKS (from file integration later)
    # -------------------------
    def load_tasks(self, task_list):
        self.tasks = task_list