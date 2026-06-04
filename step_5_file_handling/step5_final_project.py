def main():
    while True:
        print("\n===== NOTES MANAGER =====")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Overwrite Notes")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_notes()

        elif choice == "2":
            add_note()

        elif choice == "3":
            overwrite_notes()

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()

            if notes.strip():
                print("\n📄 Your Notes:")
                print(notes)
            else:
                print("\n📭 Notes file is empty.")

    except FileNotFoundError:
        print("\n📭 No notes found.")


def add_note():
    note = input("\nEnter note: ").strip()

    if note:
        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("✅ Note added successfully.")

    else:
        print("⚠ Empty note not saved.")


def overwrite_notes():
    note = input("\nEnter new note: ").strip()

    if note:
        with open("notes.txt", "w") as file:
            file.write(note + "\n")

        print("✅ Notes overwritten successfully.")

    else:
        print("⚠ Empty note not saved.")


if __name__ == "__main__":
    main()