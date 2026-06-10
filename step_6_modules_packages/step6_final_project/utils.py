# utils.py

def display_menu():

    print("\n===== STUDENT TASK MANAGER =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Statistics")
    print("6. Save Tasks")
    print("7. Exit")


def safe_input(message):
    return input(message).strip()