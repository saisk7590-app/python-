class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = grade.upper()

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def is_passed(self):
        return self.grade in ["A", "B", "C"]

    def to_line(self):
        return f"{self.name}|{self.age}|{self.grade}"

    @staticmethod
    def from_line(line):
        name, age, grade = line.strip().split("|")
        return Student(name, int(age), grade)