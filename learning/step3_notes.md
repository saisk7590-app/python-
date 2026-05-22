# Day 17 — Function Basics

## What is a Function?

A function is a reusable block of code used to perform a specific task.

Functions help:
- reduce repetition
- organize code
- improve readability
- make programs modular

---

## Function Syntax

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello")
```

---

## Calling a Function

Functions do not execute when defined.

They execute only when called.

```python
greet()
```

---

## Important Concepts

- `def` defines a function
- parentheses `()` are required
- indentation is important
- functions can be reused many times

---

## Common Mistakes

### Forgetting parentheses

Wrong:

```python
greet
```

Correct:

```python
greet()
```

---

### Calling before defining

Wrong:

```python
greet()

def greet():
    print("Hello")
```

---

### Bad indentation

Wrong:

```python
def greet():
print("Hello")
```

---

## Best Practices

- Use meaningful function names
- One function should do one task
- Avoid repeating code
- Keep functions organized
===================================
# Day 18 — Parameters & Arguments

## What Are Parameters?

Parameters are variables that receive values inside functions.

Example:

```python
def greet(name):
    print(name)
```

`name` is a parameter.

---

## What Are Arguments?

Arguments are actual values passed into functions.

Example:

```python
greet("Sai")
```

`"Sai"` is an argument.

---

## Why Parameters Matter

Parameters make functions:
- reusable
- dynamic
- flexible

Without parameters, functions work only for fixed values.

---

## Multiple Parameters

Functions can receive multiple values.

```python
def student(name, age):
    print(name, age)
```

---

## Input and Functions

Best practice:

- take input outside function
- pass values into function

Example:

```python
name = input("Enter name: ")
greet(name)
```

This improves:
- reusability
- modularity
- code organization

---

## Common Mistakes

### Missing arguments

```python
greet()
```

when parameter is required.

---

### Too many arguments

```python
greet("Sai", "Rahul")
```

---

### Forgetting output handling

```python
result = a + b
```

does not display automatically.

Need:

```python
print(result)
```

or:

```python
return result
```

---

## Best Practices

- Use meaningful parameter names
- Avoid repeated input code
- Keep functions reusable
- Separate input logic from function logic
===================================
# 📅 Day 19 — Return Keyword

# 🎯 Goal

Learn how functions send data back using `return`.

This allows:
- reusable calculations
- storing results
- modular systems
- advanced program flow

---

# ✅ What is `return`?

`return` sends a value back from a function.

Example:

```python
def add(a, b):
    return a + b
```

---

# ✅ Difference Between print() and return

## print()

- only displays output
- cannot reuse result easily

Example:

```python
def add(a, b):
    print(a + b)
```

---

## return

- sends value back
- result can be stored
- reusable in other logic

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

---

# ✅ Function Flow

```python
def square(num):
    return num * num

answer = square(5)

print(answer)
```

Flow:

```text
5
↓
goes into function
↓
function processes value
↓
return sends result back
↓
stored in answer
↓
printed
```

---

# ✅ Returning Strings

```python
def full_name(first, last):
    return first + " " + last
```

---

# ✅ Returning Conditions

```python
def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

---

# ✅ Important Concept

`return` immediately stops the function.

Example:

```python
def test():
    print("Start")
    return
    print("End")
```

Output:

```text
Start
```

`print("End")` never runs.

---

# ✅ Common Mistakes

## Forgetting to use returned value

Wrong:

```python
add(10, 20)
```

Better:

```python
result = add(10, 20)
print(result)
```

---

## Confusing print and return

Wrong idea:

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

Because nothing was returned.

---

# ✅ Best Practices

- Use `return` for reusable logic
- Use `print()` mainly for display
- Store returned values properly
- Use meaningful variable names
- Keep function responsibilities clear

---

# ✅ Day 19 Mini Project

Marks Calculator using:
- total calculation
- average calculation
- pass/fail checking
- return chaining
- modular flow

---

# 🧠 Key Learning

Functions are not just for printing.

Functions can:
- process data
- return values
- build reusable systems
- create modular applications
===================================
# 📅 Day 20 — Variable Scope

# 🎯 Goal

Understand:
- local variables
- global variables
- variable visibility
- scope errors

---

# ✅ What is Scope?

Scope means:

> where a variable can be accessed.

---

# ✅ Local Variables

Variables created inside functions are local variables.

Example:

```python
def greet():
    name = "Sai"
    print(name)
```

`name` exists only inside function.

---

# ❌ Local Variable Error

```python
def greet():
    name = "Sai"

print(name)
```

Output:

```text
NameError
```

Because local variables cannot be used outside function.

---

# ✅ Global Variables

Variables created outside functions are global variables.

Example:

```python
course = "Python"

def show_course():
    print(course)
```

Global variables can usually be accessed everywhere.

---

# ✅ Local vs Global Priority

Example:

```python
name = "Global"

def test():
    name = "Local"
    print(name)

test()

print(name)
```

Output:

```text
Local
Global
```

Inside function:
local variable gets priority.

---

# ✅ Best Practices

- Prefer parameters and return values
- Avoid excessive global variables
- Keep functions independent
- Use meaningful variable names

---

# ✅ Common Mistakes

## Using local variable outside function

```python
def test():
    age = 21

print(age)
```

Error happens.

---

## Confusing local and global variables

Variables with same names can behave differently depending on scope.

---

# 🧠 Key Learning

Functions should:
- receive data through parameters
- return values cleanly
- avoid depending heavily on globals
===================================
# 📅 Day 21 — Reusable Systems

# 🎯 Goal

Learn how to combine multiple reusable functions into organized systems.

---

# ✅ What is a Reusable System?

A reusable system is a program built using multiple small reusable functions.

Benefits:
- cleaner code
- easier debugging
- better organization
- easier expansion

---

# ✅ Utility Functions

Utility functions are reusable helper tools.

Example:

```python
def find_square(num):
    return num ** 2
```

---

# ✅ Modular Programming

Large programs should be split into:
- input section
- processing functions
- output section

Example flow:

```text
INPUT
↓
FUNCTION PROCESSING
↓
OUTPUT
```

---

# ✅ One Function = One Responsibility

Good:

```python
find_square()
```

Bad:

```python
do_everything()
```

Functions should focus on one clear task.

---

# ✅ Reusable Thinking

Reusable functions reduce repetition.

Instead of:

```python
print(a + b)
print(x + y)
```

Use:

```python
def add(a, b):
    return a + b
```

---

# ✅ main() Function

`main()` helps organize:
- program execution
- input flow
- output flow

Example:

```python
def main():
    pass
```

---

# ✅ Common Mistakes

- huge messy functions
- repeated logic
- mixing input and processing badly
- unclear function names

---

# ✅ Best Practices

- use meaningful names
- keep functions small
- return values properly
- separate responsibilities
- organize program flow clearly

---

# 🧠 Key Learning

Functions can work together to build complete reusable systems.
===================================
# 📅 Day 22 — Step 3 Final Project
# Modular Calculator System

# 🎯 Goal

Combine all Step 3 concepts into one modular application.

Topics integrated:
- functions
- parameters
- return values
- scope
- reusable systems
- loops
- conditions

---

# ✅ Project Structure

The calculator system was built using multiple reusable functions.

Functions used:
- show_menu()
- add()
- subtract()
- multiply()
- divide()
- main()

---

# ✅ Menu System

Example:

```python
def show_menu():

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
```

Menus help organize user interaction.

---

# ✅ Reusable Calculator Functions

Example:

```python
def add(a, b):
    return a + b
```

Benefits:
- reusable
- clean
- modular
- easier debugging

---

# ✅ Main Program Controller

`main()` controls:
- menu flow
- user input
- function calling
- output display

Example:

```python
def main():
    while True:
        pass
```

---

# ✅ Infinite Loop System

```python
while True:
```

Keeps program running continuously until user exits.

---

# ✅ break Statement

```python
break
```

Stops loop execution.

Without `break`:
- program never exits
- infinite loop continues

---

# ✅ Input Validation

Example:

```python
float(input())
```

Allows decimal number input.

---

# ❌ Common Error — ValueError

Example:

```python
float("hello")
```

Error occurs because:
- "hello" is not a valid number

---

# ✅ Division Safety

```python
if b == 0:
    return "Cannot divide by zero"
```

Prevents runtime errors.

---

# ❌ Common Error — TypeError

Example:

```python
add()
```

Error occurs because:
- required parameters are missing

Correct:

```python
add(10, 20)
```

---

# ✅ Program Architecture

Good program structure:

```text
MENU
↓
INPUT
↓
FUNCTION PROCESSING
↓
OUTPUT
↓
REPEAT
```

---

# ✅ Best Practices Learned

- keep functions small
- one function = one responsibility
- use return values properly
- avoid repeated code
- separate input and processing
- use meaningful names
- build reusable systems

---

# ✅ Step 3 Major Concepts Learned

## Day 17
Function basics

## Day 18
Parameters & arguments

## Day 19
Return keyword

## Day 20
Variable scope

## Day 21
Reusable systems

## Day 22
Full modular integration

---

# 🧠 Final Step 3 Achievement

By the end of Step 3, you can now:
- write reusable functions
- organize larger programs
- reduce repetition
- build modular systems
- use return values properly
- understand scope
- think like a developer

---

# 🎉 Step 3 Completed Successfully
===================================