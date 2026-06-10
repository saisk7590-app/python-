# calculator_utils.py

def safe_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def display_result(result):
    print(f"✅ Result: {result}")


def display_error(message):
    print(f"❌ Error: {message}")


def display_menu():
    print("\n=== Safe Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Exit")