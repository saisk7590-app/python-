# -------------------------
# Fixed Student Record System
# -------------------------

# Store student records
students = [
    ("Sai", 21, "Python"),
    ("Alex", 22, "Java"),
    ("Maria", 20, "C++")
]

# -------------------------
# Display Student Records
# -------------------------

print("----- STUDENT RECORDS -----\n")

for student in students:
    name, age, course = student

    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Course : {course}")
    print("-" * 25)