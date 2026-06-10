# student_utils.py

def display_all_students(students):
    print("\n===== STUDENT DETAILS =====\n")

    for student in students:
        student.display_info()
        print("-" * 25)

    print(f"\nTotal Students: {len(students)}")