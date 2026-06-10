# calculator.py

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2


def power(num1, num2):
    return num1 ** num2


def modulus(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
    return num1 % num2


def sqrt(num):
    if num < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return num ** 0.5