from managers.task_manager import TaskManager
from managers.note_manager import NoteManager
from managers.expense_manager import ExpenseManager
from managers.student_manager import StudentManager

from utils.file_handler import (
    load_tasks, load_notes, load_expenses, load_students,
    save_to_file
)

from utils.helpers import print_line, pause


# -------------------------
# FILE PATHS
# -------------------------
TASK_FILE = "storage/tasks.txt"
NOTE_FILE = "storage/notes.txt"
EXPENSE_FILE = "storage/expenses.txt"
STUDENT_FILE = "storage/students.txt"


# -------------------------
# MANAGERS
# -------------------------
task_manager = TaskManager()
note_manager = NoteManager()
expense_manager = ExpenseManager()
student_manager = StudentManager()


# -------------------------
# LOAD DATA AT START
# -------------------------
task_manager.tasks = load_tasks(TASK_FILE)
note_manager.notes = load_notes(NOTE_FILE)
expense_manager.expenses = load_expenses(EXPENSE_FILE)
student_manager.students = load_students(STUDENT_FILE)


# -------------------------
# MAIN LOOP
# -------------------------
while True:
    print("\n===== PERSONAL PRODUCTIVITY HUB =====")
    print("1. Task Manager")
    print("2. Notes Manager")
    print("3. Expense Tracker")
    print("4. Student Records")
    print("5. Save & Exit")

    choice = input("Enter choice: ")

    # ---------------- TASK ----------------
    if choice == "1":
        print("\n--- TASK MANAGER ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")

        sub = input("Enter choice: ")

        if sub == "1":
            title = input("Enter task: ")
            task_manager.add_task(title)

        elif sub == "2":
            task_manager.view_tasks()

        elif sub == "3":
            task_manager.view_tasks()
            i = int(input("Enter task number: "))
            task_manager.complete_task(i)

        elif sub == "4":
            task_manager.view_tasks()
            i = int(input("Enter task number: "))
            task_manager.delete_task(i)

    # ---------------- NOTES ----------------
    elif choice == "2":
        print("\n--- NOTES ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")

        sub = input("Enter choice: ")

        if sub == "1":
            content = input("Enter note: ")
            note_manager.add_note(content)

        elif sub == "2":
            note_manager.view_notes()

        elif sub == "3":
            note_manager.view_notes()
            i = int(input("Enter note number: "))
            note_manager.delete_note(i)

    # ---------------- EXPENSES ----------------
    elif choice == "3":
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")

        sub = input("Enter choice: ")

        if sub == "1":
            title = input("Enter expense title: ")
            amount = float(input("Enter amount: "))
            expense_manager.add_expense(title, amount)

        elif sub == "2":
            expense_manager.view_expenses()

        elif sub == "3":
            expense_manager.view_expenses()
            i = int(input("Enter expense number: "))
            expense_manager.delete_expense(i)

    # ---------------- STUDENTS ----------------
    elif choice == "4":
        print("\n--- STUDENTS ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")

        sub = input("Enter choice: ")

        if sub == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            student_manager.add_student(name, age, grade)

        elif sub == "2":
            student_manager.view_students()

        elif sub == "3":
            name = input("Enter student name: ")
            student_manager.search_student(name)

        elif sub == "4":
            student_manager.view_students()
            i = int(input("Enter student number: "))
            student_manager.delete_student(i)

    # ---------------- SAVE & EXIT ----------------
    elif choice == "5":
        save_to_file(TASK_FILE, task_manager.tasks)
        save_to_file(NOTE_FILE, note_manager.notes)
        save_to_file(EXPENSE_FILE, expense_manager.expenses)
        save_to_file(STUDENT_FILE, student_manager.students)

        print("\nData saved successfully!")
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")