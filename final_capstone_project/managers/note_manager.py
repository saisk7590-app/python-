from models.note import Note


class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, content):
        note = Note(content)
        self.notes.append(note)

    def view_notes(self):
        if not self.notes:
            print("\nNo notes found.")
            return

        print("\n===== NOTES =====")
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note.content} | {note.created_at}")

    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            removed = self.notes.pop(index - 1)
            print(f"Deleted: {removed.content}")
        else:
            print("Invalid note number.")