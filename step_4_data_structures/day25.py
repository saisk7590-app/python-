# -------------------------
# Student Marks System
# -------------------------

# Input marks
marks = []

for i in range(5):
    mark = int(input(f"Enter marks for Student {i + 1}: "))
    marks.append(mark)

# -------------------------
# Display marks
# -------------------------
print("\nStudent Marks:")
for i in range(len(marks)):
    print(f"Student {i + 1}: {marks[i]}")

# -------------------------
# Total calculation
# -------------------------
total = 0
for mark in marks:
    total += mark

# -------------------------
# Average calculation
# -------------------------
average = total / len(marks)

# -------------------------
# Max / Min calculation
# -------------------------
highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

# -------------------------
# Final Output
# -------------------------
print("\n----- RESULT SUMMARY -----")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")