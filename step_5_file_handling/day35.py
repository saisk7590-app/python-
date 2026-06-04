expense_name = input("Enter expense name: ")
amount = float(input("Enter amount: "))

with open("notes.txt", "a") as file:
    file.write(f"{expense_name} - {amount}\n")

print("Expense saved successfully!")

print("\nAll Expenses:")

with open("notes.txt", "r") as file:
    for expense in file:
        print(expense.strip())