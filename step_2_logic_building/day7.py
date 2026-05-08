# ==========================================
# Day 7 — ATM Menu Mini Project (Improved)
# Step 2 — Logic Building & Problem Solving
# ==========================================

# Initial ATM Balance
balance = 10000

# Infinite loop to keep ATM running
while True:

    # ===== ATM MENU =====
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    # User choice
    choice = input("Enter your choice (1-4): ")

    # ===== CHECK BALANCE =====
    if choice == "1":
        print(f"\nCurrent Balance: ₹{balance}")

    # ===== DEPOSIT MONEY =====
    elif choice == "2":

        deposit_amount = int(input("Enter deposit amount: ₹"))

        # Validation
        if deposit_amount <= 0:
            print("Invalid deposit amount.")

        else:
            balance += deposit_amount

            print(f"\n₹{deposit_amount} deposited successfully.")
            print(f"Updated Balance: ₹{balance}")

    # ===== WITHDRAW MONEY =====
    elif choice == "3":

        withdraw_amount = int(input("Enter withdrawal amount: ₹"))

        # Validation
        if withdraw_amount <= 0:
            print("Invalid withdrawal amount.")

        # Insufficient balance check
        elif withdraw_amount > balance:
            print("Insufficient balance.")

        # Successful withdrawal
        else:
            balance -= withdraw_amount

            print(f"\n₹{withdraw_amount} withdrawn successfully.")
            print(f"Remaining Balance: ₹{balance}")

    # ===== EXIT ATM =====
    elif choice == "4":
        print("\nThank you for using the ATM.")
        print("Goodbye!")
        break

    # ===== INVALID MENU OPTION =====
    else:
        print("Invalid choice. Please select between 1 and 4.")