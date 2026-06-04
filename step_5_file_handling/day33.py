try:
    with open("notes.txt", "r") as file:
        notes = file.readlines()
except FileNotFoundError:
    print("No notes found")
    notes = []

def display(notes_list):
    for idx, note in enumerate(notes_list, start=1):
        print(f"{idx}. {note.strip()}")

if not notes:
    print("No notes available in file.")
else:
    print("All Notes:")
    display(notes)

    important_notes = [
        note for note in notes
        if "IMPORTANT" in note.upper() or "TODO" in note.upper()
    ]

    print("\nMenu:")
    print("1. Show all notes")
    print("2. Show important notes")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nAll Notes:")
        display(notes)

    elif choice == "2":
        if important_notes:
            print("\nImportant Notes:")
            display(important_notes)
        else:
            print("No important notes found.")

    else:
        print("Invalid choice.")