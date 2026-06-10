# main.py

from student import Student
from student_utils import display_all_students


def main():
    students = []

    print("===== Student Management System =====")

    for i in range(3):
        print(f"\nEnter Details for Student {i + 1}")

        name = input("Enter name: ")

        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError:
                print("Please enter a valid age.")

        grade = input("Enter grade (A/B/C/D/F): ").upper()

        student = Student(name, age, grade)
        students.append(student)

    display_all_students(students)

    print("\n===== INTRODUCTIONS =====\n")

    for student in students:
        student.introduce()

    print("\n===== RESULTS =====\n")

    for student in students:
        status = "Passed" if student.is_passed() else "Failed"
        print(f"{student.name} - {status}")


if __name__ == "__main__":
    main()