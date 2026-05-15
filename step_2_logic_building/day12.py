total_expense = 0

largest_expense = 0
smallest_expense = None

for i in range(5):

    amount = int(input("Enter expense amount: "))

    total_expense += amount

    # Largest Expense Tracking
    if amount > largest_expense:
        largest_expense = amount

    # Smallest Expense Tracking
    if smallest_expense is None or amount < smallest_expense:
        smallest_expense = amount

average = total_expense / 5

print("\n===== Expense Report =====")

print(f"Total Expense: {total_expense}")
print(f"Largest Expense: {largest_expense}")
print(f"Smallest Expense: {smallest_expense}")
print(f"Average Expense: {average}")