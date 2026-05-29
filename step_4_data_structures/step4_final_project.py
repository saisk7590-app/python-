students = {}
courses = set()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Unique Courses")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # -------------------------
    # Add Student
    # -------------------------

    if choice == "1":

        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))

        students[student_id] = {
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }

        courses.add(course)

        print("Student added successfully.")

    # -------------------------
    # View Students
    # -------------------------

    elif choice == "2":

        if not students:
            print("No students found.")

        else:

            for student_id, details in students.items():

                print("\n----------------------")
                print(f"Student ID : {student_id}")
                print(f"Name       : {details['name']}")
                print(f"Age        : {details['age']}")
                print(f"Course     : {details['course']}")
                print(f"Marks      : {details['marks']}")

    # -------------------------
    # Search Student
    # -------------------------

    elif choice == "3":

        student_id = input("Enter student ID to search: ")

        if student_id in students:

            details = students[student_id]

            print("\nStudent Found")
            print(f"Name   : {details['name']}")
            print(f"Age    : {details['age']}")
            print(f"Course : {details['course']}")
            print(f"Marks  : {details['marks']}")

        else:
            print("Student not found.")

    # -------------------------
    # Update Student
    # -------------------------

    elif choice == "4":

        student_id = input("Enter student ID to update: ")

        if student_id in students:

            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            marks = int(input("Enter new marks: "))

            students[student_id]["age"] = age
            students[student_id]["course"] = course
            students[student_id]["marks"] = marks

            courses.add(course)

            print("Student updated successfully.")

        else:
            print("Student not found.")

    # -------------------------
    # Delete Student
    # -------------------------

    elif choice == "5":

        student_id = input("Enter student ID to delete: ")

        if student_id in students:

            students.pop(student_id)

            print("Student deleted successfully.")

        else:
            print("Student not found.")

    # -------------------------
    # Show Unique Courses
    # -------------------------

    elif choice == "6":

        if not courses:
            print("No courses found.")

        else:

            print("\nUnique Courses:")

            for course in courses:
                print(course)

    # -------------------------
    # Exit
    # -------------------------

    elif choice == "7":

        print("Exiting program...")
        break

    # -------------------------
    # Invalid Choice
    # -------------------------

    else:
        print("Invalid choice.")