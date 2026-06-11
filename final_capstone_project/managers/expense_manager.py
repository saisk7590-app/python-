from models.expense import Expense


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, title, amount):
        expense = Expense(title, amount)
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses found.")
            return

        print("\n===== EXPENSES =====")
        total = 0

        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp.title} - ₹{exp.amount} | {exp.created_at}")
            total += exp.amount

        print(f"\nTotal Spent: ₹{total}")

    def delete_expense(self, index):
        if 1 <= index <= len(self.expenses):
            removed = self.expenses.pop(index - 1)
            print(f"Deleted: {removed.title}")
        else:
            print("Invalid expense number.")