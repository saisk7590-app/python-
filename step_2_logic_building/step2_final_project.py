# =========================================================
# STEP 2 FINAL PROJECT — ATM SYSTEM
# File: step2_final_project.py
# =========================================================

# ---------------- LOGIN SYSTEM ----------------

correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:

    print("\n===== ATM LOGIN =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username:

        if password == correct_password:
            print("\n✅ Login Successful!")
            break

        else:
            attempts -= 1
            print(f"\n❌ Wrong Password! Attempts Left: {attempts}")

    else:
        attempts -= 1
        print(f"\n❌ Wrong Username! Attempts Left: {attempts}")

# ---------------- ACCOUNT LOCK ----------------

if attempts == 0:

    print("\n🚫 Account Locked!")
    print("Too many failed attempts.")

else:

    # ---------------- ATM DATA ----------------

    balance = 10000

    transactions = []

    # ---------------- MAIN ATM MENU ----------------

    while True:

        print("\n" + "=" * 40)
        print("🏦 ATM SYSTEM")
        print("=" * 40)

        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        # ---------------- CHECK BALANCE ----------------

        if choice == "1":

            print(f"\n💰 Current Balance: ₹{balance}")

        # ---------------- DEPOSIT MONEY ----------------

        elif choice == "2":

            deposit_amount = float(input("\nEnter deposit amount: ₹"))

            if deposit_amount > 0:

                balance += deposit_amount

                transactions.append(f"Deposited ₹{deposit_amount}")

                print(f"\n✅ ₹{deposit_amount} deposited successfully.")
                print(f"💰 Updated Balance: ₹{balance}")

            else:
                print("\n❌ Deposit amount must be positive.")

        # ---------------- WITHDRAW MONEY ----------------

        elif choice == "3":

            withdraw_amount = float(input("\nEnter withdrawal amount: ₹"))

            if withdraw_amount > 0:

                if withdraw_amount <= balance:

                    balance -= withdraw_amount

                    transactions.append(f"Withdrawn ₹{withdraw_amount}")

                    print(f"\n✅ ₹{withdraw_amount} withdrawn successfully.")
                    print(f"💰 Remaining Balance: ₹{balance}")

                else:
                    print("\n❌ Insufficient Balance.")

            else:
                print("\n❌ Withdrawal amount must be positive.")

        # ---------------- TRANSACTION HISTORY ----------------

        elif choice == "4":

            print("\n===== TRANSACTION HISTORY =====")

            if len(transactions) == 0:
                print("No transactions available.")

            else:

                for transaction in transactions:
                    print(transaction)

        # ---------------- EXIT ----------------

        elif choice == "5":

            print("\n👋 Thank you for using the ATM System.")
            break

        # ---------------- INVALID OPTION ----------------

        else:

            print("\n⚠️ Invalid Choice. Please select between 1 and 5.")