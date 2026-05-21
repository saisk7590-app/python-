# ==============================
# Day 19 — Marks Calculator
# ==============================

def calculate_total(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    return total


def calculate_average(total_marks):
    average = total_marks / 3
    return average


def check_result(average_marks):
    if average_marks >= 35:
        return "Pass"
    else:
        return "Fail"


# ===== INPUT SECTION =====

mark1 = float(input("Enter Mark 1: "))
mark2 = float(input("Enter Mark 2: "))
mark3 = float(input("Enter Mark 3: "))


# ===== PROCESSING SECTION =====

total_marks = calculate_total(mark1, mark2, mark3)

average_marks = calculate_average(total_marks)

final_result = check_result(average_marks)


# ===== OUTPUT SECTION =====

print("\n===== STUDENT REPORT =====")

print("Total Marks :", total_marks)

print("Average Marks :", average_marks)

print("Final Result :", final_result)