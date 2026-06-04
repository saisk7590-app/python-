while True:
    file_name = input("Enter file name: ").strip()

    try:
        with open(file_name, "r") as file:
            content = file.read()

        print("\n📄 File Content:\n")
        print(content)
        break

    except FileNotFoundError:
        print(f"\n❌ Error: '{file_name}' not found.")

        while True:
            retry = input("Try again? (yes/no): ").strip().lower()

            if retry == "yes":
                break

            elif retry == "no":
                print("🚪 Exiting program. Goodbye!")
                exit()

            else:
                print("⚠ Please enter 'yes' or 'no'.")