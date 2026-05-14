total_sum = 0

even_count = 0
odd_count = 0

positive_count = 0
negative_count = 0

print("===== Number Analyzer =====")

for i in range(5):

    number = int(input("Enter a number: "))

    total_sum += number

    # Even / Odd Check
    if number % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

    # Positive / Negative Check
    if number > 0:
        positive_count += 1

    elif number < 0:
        negative_count += 1

print("\n===== REPORT =====")

print(f"Total Sum: {total_sum}")
print(f"Even Numbers: {even_count}")
print(f"Odd Numbers: {odd_count}")
print(f"Positive Numbers: {positive_count}")
print(f"Negative Numbers: {negative_count}")