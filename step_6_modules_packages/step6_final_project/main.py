# main.py

from task_manager import TaskManager
from file_handler import (
    save_tasks,
    load_tasks
)
from utils import (
    display_menu,
    safe_input
)


def main():

    manager = TaskManager()

    manager.tasks = load_tasks()

    while True:

        display_menu()

        choice = safe_input(
            "Enter choice: "
        )

        if choice == "1":

            title = safe_input(
                "Enter task: "
            )

            manager.add_task(title)

            save_tasks(manager.tasks)

        elif choice == "2":

            manager.view_tasks()

        elif choice == "3":

            try:

                task_number = int(
                    safe_input(
                        "Enter task number: "
                    )
                )

                manager.complete_task(
                    task_number
                )

                save_tasks(
                    manager.tasks
                )

            except ValueError:

                print(
                    "❌ Please enter a valid number."
                )

        elif choice == "4":

            try:

                task_number = int(
                    safe_input(
                        "Enter task number to delete: "
                    )
                )

                manager.delete_task(
                    task_number
                )

                save_tasks(
                    manager.tasks
                )

            except ValueError:

                print(
                    "❌ Please enter a valid number."
                )

        elif choice == "5":

            manager.show_statistics()

        elif choice == "6":

            save_tasks(manager.tasks)

            print(
                "✅ Tasks saved successfully."
            )

        elif choice == "7":

            save_tasks(manager.tasks)

            print(
                "👋 Goodbye!"
            )

            break

        else:

            print(
                "❌ Invalid choice."
            )


if __name__ == "__main__":
    main()