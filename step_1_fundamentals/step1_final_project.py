# ---------------- LOGIN SYSTEM ----------------

system_password = "python123"

while True:

    entered_password = input("Enter System Password: ")

    if entered_password == system_password:
        print("\n✅ Access Granted!")
        break

    else:
        print("❌ Wrong Password. Try Again.")


# ---------------- MAIN MENU ----------------

while True:

    print("\n" + "=" * 40)
    print("🚀 SMART STUDENT UTILITY SYSTEM")
    print("=" * 40)

    print("1. Student Profile")
    print("2. Calculator")
    print("3. Grade Checker")
    print("4. Multiplication Table")
    print("5. Pattern Generator")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # ---------------- PROFILE ----------------

    if choice == "1":

        print("\n--- STUDENT PROFILE ---")

        name = input("Enter full name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        college = input("Enter college: ")

        username = name.strip().lower().replace(" ", "_")
        future_age = age + 5

        print("\n--- PROFILE DETAILS ---")
        print(f"Username: {username}")
        print(f"City: {city}")
        print(f"College: {college}")
        print(f"Age after 5 years: {future_age}")

        if age >= 18:
            print("Status: Adult")
        else:
            print("Status: Minor")

    # ---------------- CALCULATOR ----------------

    elif choice == "2":

        print("\n--- CALCULATOR ---")

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        print(f"Addition: {first_number + second_number}")
        print(f"Subtraction: {first_number - second_number}")
        print(f"Multiplication: {first_number * second_number}")

        if second_number != 0:
            print(f"Division: {first_number / second_number}")
        else:
            print("Cannot divide by zero")

    # ---------------- GRADE CHECKER ----------------

    elif choice == "3":

        print("\n--- GRADE CHECKER ---")

        marks = int(input("Enter marks: "))

        if marks >= 90:
            print("Grade: A")

        elif marks >= 70:
            print("Grade: B")

        elif marks >= 50:
            print("Grade: C")

        else:
            print("Grade: Fail")

    # ---------------- MULTIPLICATION TABLE ----------------

    elif choice == "4":

        print("\n--- MULTIPLICATION TABLE ---")

        number = int(input("Enter a number: "))

        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")

    # ---------------- PATTERN GENERATOR ----------------

    elif choice == "5":

        print("\n--- PATTERN GENERATOR ---")

        rows = int(input("Enter number of rows: "))

        print("\nTriangle Pattern:\n")

        for i in range(1, rows + 1):

            for j in range(i):
                print("*", end=" ")

            print()

        print("\nSquare Pattern:\n")

        for i in range(rows):

            for j in range(rows):
                print("#", end=" ")

            print()

    # ---------------- EXIT ----------------

    elif choice == "6":

        print("\n👋 Exiting System...")
        break

    # ---------------- INVALID OPTION ----------------

    else:
        print("\n⚠️ Invalid choice. Please try again.")

    input("\nPress ENTER to continue...")