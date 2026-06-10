# file_handler.py

from datetime import datetime
from task import Task


FILE_NAME = "tasks.txt"


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:

        for task in tasks:

            file.write(
                f"{task.title}|"
                f"{task.completed}|"
                f"{task.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )


def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:

                title, completed, created_at = (
                    line.strip().split("|")
                )

                task = Task(
                    title=title,
                    completed=(completed == "True"),
                    created_at=datetime.strptime(
                        created_at,
                        "%Y-%m-%d %H:%M:%S"
                    )
                )

                tasks.append(task)

    except FileNotFoundError:
        pass

    return tasks