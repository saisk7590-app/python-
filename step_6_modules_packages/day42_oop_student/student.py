# student.py

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade.upper()

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Grade: {self.grade}")

    def introduce(self):
        print(f"Hi, I am {self.name}.")

    def is_passed(self):
        return self.grade in ["A", "B", "C"]