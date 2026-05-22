# ==============================
# Day 21 — Utility Toolkit
# ==============================

def find_square(num):
    return num ** 2


def find_cube(num):
    return num ** 3


def check_even_odd(num):

    if num % 2 == 0:
        return "Even"

    else:
        return "Odd"


def find_largest(a, b):

    if a > b:
        return a

    else:
        return b


def main():

    # ===== INPUT SECTION =====

    num1 = int(input("Enter First Number: "))

    num2 = int(input("Enter Second Number: "))


    # ===== PROCESSING SECTION =====

    square_result = find_square(num1)

    cube_result = find_cube(num1)

    largest_result = find_largest(num1, num2)

    even_odd1 = check_even_odd(num1)

    even_odd2 = check_even_odd(num2)


    # ===== OUTPUT SECTION =====

    print("\n===== UTILITY TOOLKIT =====")

    print(f"Square of {num1}: {square_result}")

    print(f"Cube of {num1}: {cube_result}")

    print(f"{num1} is {even_odd1}")

    print(f"{num2} is {even_odd2}")

    print(f"Largest Number: {largest_result}")


# ===== PROGRAM START =====

if __name__ == "__main__":
    main()