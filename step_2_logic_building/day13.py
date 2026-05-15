# ==========================================
# Day 13 — Quiz Game
# Step 2 — Logic Building & Problem Solving
# ==========================================

score = 0
wrong_answers = 0

print("===== QUIZ GAME =====")

# Question 1
answer = input("\n1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    wrong_answers += 1

# Question 2
answer = input("\n2. How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    wrong_answers += 1

# Question 3
answer = input("\n3. What is 5 + 5? ")

if answer == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    wrong_answers += 1

# Question 4
answer = input("\n4. Which language are we learning? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    wrong_answers += 1

# Question 5
answer = input("\n5. What color is the sky on a clear day? ")

if answer.lower() == "blue":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    wrong_answers += 1

# Final Report
print("\n===== QUIZ COMPLETE =====")

print(f"Correct Answers: {score}")
print(f"Wrong Answers: {wrong_answers}")
print(f"Final Score: {score}/5")

# Percentage
percentage = (score / 5) * 100

print(f"Percentage: {percentage}%")

# Grade System
if percentage >= 80:
    print("Grade: A")

elif percentage >= 60:
    print("Grade: B")

elif percentage >= 40:
    print("Grade: C")

else:
    print("Grade: Fail")