# main.py

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulus,
    sqrt
)

from calculator_utils import (
    safe_input,
    display_result,
    display_error,
    display_menu
)


def main():
    print("🧮 Welcome to Safe Calculator!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ")

        if choice == "8":
            print("👋 Thank you for using Safe Calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            display_error("Invalid menu choice.")
            continue

        try:
            num1 = safe_input("Enter first number: ")

            if choice != "7":
                num2 = safe_input("Enter second number: ")

            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                result = divide(num1, num2)

            elif choice == "5":
                result = power(num1, num2)

            elif choice == "6":
                result = modulus(num1, num2)

            elif choice == "7":
                result = sqrt(num1)

            display_result(result)

        except (ZeroDivisionError, ValueError) as error:
            display_error(error)


if __name__ == "__main__":
    main()