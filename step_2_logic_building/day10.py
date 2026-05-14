# ==========================================
# Day 10 — Pattern Suite Mini Project
# Step 2 — Logic Building & Problem Solving
# ==========================================

while True:

    # ===== MENU =====
    print("\n===== PATTERN SUITE =====")
    print("1. Square Pattern")
    print("2. Triangle Pattern")
    print("3. Number Triangle")
    print("4. Reverse Triangle")
    print("5. Equilateral Triangle")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # ===== 1. Square Pattern =====
    if choice == "1":

        print("\nSquare Pattern:\n")

        for row in range(4):
            for col in range(4):
                print("*", end=" ")
            print()

    # ===== 2. Triangle Pattern =====
    elif choice == "2":

        print("\nTriangle Pattern:\n")

        for row in range(1, 5):
            for col in range(row):
                print("*", end=" ")
            print()

    # ===== 3. Number Triangle =====
    elif choice == "3":

        print("\nNumber Triangle:\n")

        for row in range(1, 5):
            for number in range(1, row + 1):
                print(number, end=" ")
            print()

    # ===== 4. Reverse Triangle =====
    elif choice == "4":

        print("\nReverse Triangle:\n")

        for row in range(4, 0, -1):
            for col in range(row):
                print("*", end=" ")
            print()

    # ===== 5. Equilateral Triangle =====
    elif choice == "5":

        print("\nEquilateral Triangle:\n")

        for row in range(1, 5):

            # Print spaces
            for space in range(4 - row):
                print(" ", end="")

            # Print stars
            for star in range(row):
                print("*", end=" ")

            print()

    # ===== 6. Exit =====
    elif choice == "6":

        print("\nExiting Pattern Suite...")
        print("Goodbye!")
        break

    # ===== Invalid Choice =====
    else:
        print("Invalid choice. Please select between 1 and 6.")