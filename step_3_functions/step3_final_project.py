# ==================================
# Step 3 Final Project
# Modular Calculator System
# ==================================


def show_menu():

    print("\n===== CALCULATOR MENU =====")

    print("1. Addition")

    print("2. Subtraction")

    print("3. Multiplication")

    print("4. Division")

    print("5. Exit")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


def main():

    while True:

        show_menu()

        choice = input("Enter Choice: ")


        if choice == "5":

            print("\nExiting Calculator...")

            print("Thank You!")

            break


        elif choice in ["1", "2", "3", "4"]:

            try:

                num1 = float(input("Enter First Number: "))

                num2 = float(input("Enter Second Number: "))

            except ValueError:

                print("Invalid Number Input")

                continue


            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                result = divide(num1, num2)


            print(f"\nResult: {result}")


        else:
            print("Invalid Menu Choice")


# ===== PROGRAM START =====

if __name__ == "__main__":
    main()
