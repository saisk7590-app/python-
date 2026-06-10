# reminder_utils.py

from datetime import datetime

def display_reminder(reminder):
    print("\n📌 Reminder")
    print(f"Text: {reminder.text}")
    print(
        f"Created At: "
        f"{reminder.created_at.strftime('%d-%m-%Y %H:%M:%S')}"
    )

def calculate_time_remaining(reminder):
    return reminder.due_date - datetime.now()
