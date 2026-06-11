from datetime import datetime


class Expense:
    def __init__(self, title, amount, created_at=None):
        self.title = title
        self.amount = float(amount)
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M")

    def display(self):
        print(f"{self.title} - ₹{self.amount} | {self.created_at}")

    def to_line(self):
        return f"{self.title}|{self.amount}|{self.created_at}"

    @staticmethod
    def from_line(line):
        title, amount, created_at = line.strip().split("|")
        return Expense(title, float(amount), created_at)