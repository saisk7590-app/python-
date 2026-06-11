from models.task import Task
from models.note import Note
from models.expense import Expense
from models.student import Student


# -------------------------
# GENERIC SAVE FUNCTION
# -------------------------
def save_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item.to_line() + "\n")


# -------------------------
# TASKS LOAD
# -------------------------
def load_tasks(filename):
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                tasks.append(Task.from_line(line))
    except FileNotFoundError:
        pass

    return tasks


# -------------------------
# NOTES LOAD
# -------------------------
def load_notes(filename):
    notes = []

    try:
        with open(filename, "r") as file:
            for line in file:
                notes.append(Note.from_line(line))
    except FileNotFoundError:
        pass

    return notes


# -------------------------
# EXPENSES LOAD
# -------------------------
def load_expenses(filename):
    expenses = []

    try:
        with open(filename, "r") as file:
            for line in file:
                expenses.append(Expense.from_line(line))
    except FileNotFoundError:
        pass

    return expenses


# -------------------------
# STUDENTS LOAD
# -------------------------
def load_students(filename):
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                students.append(Student.from_line(line))
    except FileNotFoundError:
        pass

    return students