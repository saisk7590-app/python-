===================================
# 🟣 STEP 5 — Day 33 — File Handling (Reading Files)

---

# 📅 Day 33 — Reading Files in Python

# 🎯 What is File Reading?

File reading means accessing stored data from a file into Python.

Instead of typing data every time, Python can load saved information.

---

# 📌 File Opening

## 🔹 Basic Syntax

```python
file = open("data.txt", "r")
```

---

## 🔹 Mode: "r"

| Mode | Meaning                     |
| ---- | --------------------------- |
| r    | Read mode (file must exist) |

✔ Used only for reading data
❌ Cannot modify file

---

# 📖 Methods of Reading Files

---

## 🔹 1. read()

Reads entire file as one string

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

✔ Best for small files
❌ Loads everything into memory

---

## 🔹 2. readline()

Reads file line by line

```python
with open("data.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

    print(line1)
    print(line2)
```

✔ Reads sequentially
✔ Good for step-by-step processing

---

## 🔹 3. readlines()

Reads all lines into a list

```python
with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Output:

```python
["Hello\n", "Python\n", "File Handling\n"]
```

---

# 🧠 File Pointer Concept

Python reads files sequentially using a pointer.

Each read moves pointer forward.

---

# 🔒 Best Practice — with open()

```python
with open("data.txt", "r") as file:
    content = file.read()
```

✔ Auto closes file
✔ Prevents memory leaks
✔ Professional standard

---

# ⚠️ Common Mistakes

## ❌ File Not Found

```python
open("missing.txt", "r")
```

Raises error if file does not exist.

---

## ❌ Wrong Mode

Using `"w"` instead of `"r"` will erase file.

---

## ❌ Not Using with open()

Manual open requires closing file.

---

# 🧪 Practice Concepts Covered

✔ Reading full file
✔ Reading line by line
✔ Reading into list
✔ File pointer behavior
✔ Safe file handling

---

# 🧩 Mini Project — Notes Reader System

## 🎯 Goal

Read notes from file and display them in structured format.

---

## 📌 Features

* Read file "notes.txt"
* Display all notes with numbering
* Filter IMPORTANT / TODO notes
* Show menu options
* Handle missing file safely

---

## 🔄 Program Flow

1. Open file safely
2. Read all lines
3. Check if file is empty
4. Display menu:

   * Show all notes
   * Show important notes
5. Display output based on choice

---

# ⚠️ Key Learning

File handling is the foundation of:

* data storage
* notes apps
* logs
* configuration systems
* real-world applications

---

# 💡 Important Takeaway

👉 File reading = accessing persistent data
👉 Always prefer `with open()`
👉 Think in terms of data flow, not just code

---

# 🚀 End of Day 33

You now understand:

✔ File reading
✔ File modes
✔ read / readline / readlines
✔ Safe file handling
✔ Basic file-based program design

===================================
# 📅 Day 34 — Writing Files in Python

# 🔹 What is File Writing?

File writing means saving data from a Python program into a file permanently.

---

# 🔹 Write Mode ("w")

```python
with open("notes.txt", "w") as file:
```

Used to write data into a file.

---

# 🔹 Important Behavior of "w"

If file does not exist:

✔ Python creates it.

If file already exists:

⚠ Old content is deleted.

Example:

Before:

```text
Apple
Banana
```

After:

```python
file.write("Python")
```

Result:

```text
Python
```

---

# 🔹 write()

Used to save text.

```python
file.write("Hello")
```

---

# 🔹 New Lines

Python does not automatically move to a new line.

Use:

```python
file.write("Line 1\n")
file.write("Line 2\n")
```

---

# 🔹 Best Practice

```python
with open("notes.txt", "w") as file:
```

Benefits:

* auto closes file
* cleaner code
* safer file handling

---

# ⚠ Common Mistakes

## Forgetting that "w" overwrites

```python
with open("notes.txt", "w")
```

Deletes old content.

---

## Forgetting "\n"

Can cause text to appear on one line.

---

## Using wrong mode

```python
open("notes.txt", "r")
```

Cannot be used for writing.

---

# 💡 Real-World Uses

* Journals
* Notes Apps
* Reports
* User Profiles
* Configuration Files

---

# 🧠 Key Concepts Learned

✔ File creation

✔ File writing

✔ write()

✔ New line handling

✔ Data persistence

✔ Overwriting behavior

✔ Reading saved content back

===================================
# 📅 Day 35 — Append Mode in Python

# 🔹 What is Append Mode?

Append mode adds new data to the end of a file.

Mode:

```python
"a"
```

---

# 🔹 Difference Between Write and Append

| Mode | Behavior                 |
| ---- | ------------------------ |
| "w"  | Replaces old content     |
| "a"  | Adds to existing content |

---

# 🔹 Append Syntax

```python
with open("notes.txt", "a") as file:
    file.write("New Entry\n")
```

---

# 🔹 File Creation

If file does not exist:

```python
with open("notes.txt", "a")
```

Python automatically creates it.

---

# 🔹 Why Newlines Matter

Good:

```python
file.write("Coffee - 50\n")
```

Bad:

```python
file.write("Coffee - 50")
```

Without newline, entries can merge together.

---

# 🔹 Real-World Uses

* Expense trackers
* Journals
* Logs
* Attendance systems
* Chat history

---

# ⚠ Common Mistakes

## Using "w" instead of "a"

Can erase all previous data.

---

## Forgetting "\n"

Creates unreadable files.

---

## Assuming append starts from top

Append always writes at the end.

---

# 💡 Key Concepts Learned

✔ append mode

✔ persistent data growth

✔ adding records safely

✔ logging systems

✔ reading appended data

===================================
# 📅 Day 36 — Error Handling Basics

# 🔹 Purpose

Error handling prevents program crashes and improves user experience.

---

# 🔹 try / except

```python id="try"
try:
    risky_code()
except ErrorType:
    handle_error()
```

---

# 🔹 File Not Found Handling

```python id="file"
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

---

# 🔹 Input Validation

```python id="input"
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
```

---

# 🔹 Retry System Pattern

Used for safe programs:

* keeps asking until valid input
* improves UX
* prevents crashes

---

# 🔹 Best Practices

✔ use `.strip()` for inputs
✔ handle specific errors
✔ avoid empty `except:`
✔ give clear messages

---

# 🔹 Real-World Usage

✔ login systems
✔ file readers
✔ APIs
✔ banking apps
✔ dashboards

---

# 🔹 Key Idea

👉 Error handling = making programs crash-proof and user-friendly

===================================
# 🟣 STEP 5 — File Handling

## 🎯 Goal

Learn how to save, load, update, and manage data permanently using files.

---

# 📅 Day 33 — Reading Files

## File Modes

| Mode | Meaning        |
| ---- | -------------- |
| r    | Read mode      |
| r+   | Read and Write |
| rb   | Read Binary    |

## Reading Methods

### read()

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

Reads the entire file.

### readline()

```python
line = file.readline()
```

Reads one line at a time.

### readlines()

```python
lines = file.readlines()
```

Returns a list of lines.

## Best Practice

```python
with open(...)
```

Automatically closes the file.

---

# 📅 Day 34 — Writing Files

## Write Mode

```python
with open("notes.txt", "w") as file:
```

Creates file if missing.

Overwrites file if it exists.

## Writing Data

```python
file.write("Hello")
```

## New Lines

```python
file.write("Line 1\n")
```

---

# 📅 Day 35 — Append Mode

## Append Mode

```python
with open("notes.txt", "a") as file:
```

Adds data to end of file.

Does not delete old content.

## Difference

| Mode | Behavior            |
| ---- | ------------------- |
| w    | Replace old content |
| a    | Add new content     |

---

# 📅 Day 36 — Error Handling

## Basic Structure

```python
try:
    risky_code
except ErrorType:
    handle_error
```

## File Error

```python
except FileNotFoundError:
```

## Input Error

```python
except ValueError:
```

## Zero Division

```python
except ZeroDivisionError:
```

---

# 📅 Day 37 — Notes Manager Project

Concepts Combined:

* Functions
* Menus
* File Reading
* File Writing
* File Appending
* Error Handling
* Persistent Storage

---

# ⚠ Common Mistakes

* Forgetting to close files
* Using w instead of a
* Forgetting \n
* Assuming file exists
* Not handling user input errors

---

# ✅ Best Practices

* Always use with open()
* Handle exceptions
* Use meaningful variable names
* Validate user input
* Keep functions small and focused

---

# 💡 Real-World Uses

* Notes Apps
* Journals
* Expense Trackers
* Attendance Systems
* Logs
* Reports
* Configuration Files

---

# 🎯 Step 5 Outcome

You can now:

✔ Read files confidently

✔ Write files confidently

✔ Append data safely

✔ Store information permanently

✔ Handle missing files safely

✔ Build file-based terminal applications

✔ Understand basic data persistence

===================================
