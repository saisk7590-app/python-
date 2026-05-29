# -------------------------
# Student Database System
# -------------------------

# Create student dictionary
student = {}

# -------------------------
# Input Student Details
# -------------------------

student["name"] = input("Enter student's name: ")
student["age"] = int(input("Enter student's age: "))
student["course"] = input("Enter student's course: ")
student["marks"] = int(input("Enter student's marks: "))

# -------------------------
# Display Student Details
# -------------------------

print("\n----- STUDENT DETAILS -----")

for key, value in student.items():
    print(f"{key.capitalize()} : {value}")

# -------------------------
# Update Student Age
# -------------------------

student["age"] = int(input("\nEnter updated age: "))

# -------------------------
# Add New Field
# -------------------------

student["city"] = input("Enter student's city: ")

# -------------------------
# Remove Field
# -------------------------

student.pop("course")

# -------------------------
# Final Updated Database
# -------------------------

print("\n----- FINAL STUDENT DATABASE -----")

for key, value in student.items():
    print(f"{key.capitalize()} : {value}")

# -------------------------
# Raw Dictionary View
# -------------------------

print("\nRaw Dictionary:")
print(student)