# reminder.py

from datetime import datetime, timedelta

class Reminder:
    def __init__(self, text, days=1):
        self.text = text
        self.created_at = datetime.now()
        self.due_date = self.created_at + timedelta(days=days)