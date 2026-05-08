# 🟢 STEP 1 — Python Fundamentals

## 🎯 Goal
Learn Python basics and build simple terminal applications.

---

# 📅 Day 1 — Basics

## Topics
- print()
- variables
- input()

## Example

```python
name = input("Enter name: ")
print(f"Hello {name}")
```

## Key Learning
- Input → Processing → Output
- Variables store data

---

# 📅 Day 2 — Type Conversion & Operators

## Topics
- int()
- float()
- operators

## Operators
| Operator | Meaning |
|---|---|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Remainder |

## Example

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(a + b)
```

## Key Learning
- User input is string by default
- Convert using int() or float()

---

# 📅 Day 3 — Strings

## Topics
- lower()
- upper()
- strip()
- replace()
- slicing

## Example

```python
name = " Sai Kiran "

username = name.strip().lower().replace(" ", "_")

print(username)
```

## Key Learning
- Strings are used everywhere
- Formatting makes apps cleaner

---

# 📅 Day 4 — Conditions

## Topics
- if
- else
- elif
- comparison operators

## Example

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## Key Learning
- Conditions help programs make decisions

---

# 📅 Day 5 — Loops

## Topics
- for loop
- while loop
- range()

## Example

```python
for i in range(5):
    print(i)
```

## Key Learning
- Loops automate repetition

---

# 📅 Day 6 — Nested Loops & Patterns

## Topics
- nested loops
- patterns

## Example

```python
for i in range(5):

    for j in range(5):
        print("*", end=" ")

    print()
```

## Key Learning
- Nested loops control rows and columns

---

# 🔥 Final Step 1 Project

## Features
- Login system
- Calculator
- Profile generator
- Multiplication table
- Pattern printer

## Concepts Used
- input/output
- strings
- conditions
- loops
- nested loops

---

# 🧠 Final Understanding

After Step 1, I can:
- write Python basics confidently
- build terminal applications
- use loops and conditions
- understand program flow