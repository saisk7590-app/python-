from datetime import datetime


class Note:
    def __init__(self, content, created_at=None):
        self.content = content
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M")

    def display(self):
        print(f"- {self.content} | {self.created_at}")

    def to_line(self):
        return f"{self.content}|{self.created_at}"

    @staticmethod
    def from_line(line):
        content, created_at = line.strip().split("|")
        return Note(content, created_at)