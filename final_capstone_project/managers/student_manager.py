from models.student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("\nNo students found.")
            return

        print("\n===== STUDENTS =====")
        for i, stu in enumerate(self.students, start=1):
            status = "Pass" if stu.is_passed() else "Fail"
            print(f"{i}. {stu.name} | {stu.age} | {stu.grade} → {status}")

    def search_student(self, name):
        found = False

        for stu in self.students:
            if stu.name.lower() == name.lower():
                print("\nStudent Found:")
                stu.display()
                found = True
                break

        if not found:
            print("Student not found.")

    def delete_student(self, index):
        if 1 <= index <= len(self.students):
            removed = self.students.pop(index - 1)
            print(f"Deleted: {removed.name}")
        else:
            print("Invalid student number.")