# main.py

import calculator
import string_utils
import random_utils

# -------------------
# Calculator Tests
# -------------------
print("CALCULATOR TESTS")
print(calculator.add(10, 20))
print(calculator.subtract(10, 20))
print(calculator.multiply(10, 20))
print(calculator.divide(10, 20))
print(calculator.divide(10, 0))

print("\nSTRING TESTS")

# -------------------
# String Utils Tests
# -------------------
print(string_utils.reverse_string("Hello"))
print(string_utils.is_palindrome("madam"))
print(string_utils.uppercase("hello"))
print(string_utils.lowercase("HELLO"))
print(string_utils.word_count("Hello world from Python"))

print("\nRANDOM TESTS")

# -------------------
# Random Utils Tests
# -------------------
print(random_utils.generate_random_list(5))
print(random_utils.pick_random_item([1, 2, 3, 4, 5]))