txt = input("Write today's journal entry: ")

with open("notes.txt", "w") as file:
    file.write(txt + "\n")

print("Journal saved successfully!")

with open("notes.txt", "") as file:
    journal = file.read()

print("\nYour Saved Journal:")
print(journal)