# -------------------------
# Task Manager System
# -------------------------

# Create task list
tasks = []

# -------------------------
# Add Tasks
# -------------------------
tasks.append("buy grocery")
tasks.append("complete assignments")
tasks.append("call mom")

print("After adding tasks:", tasks)

# -------------------------
# Insert Task
# -------------------------
tasks.insert(1, "go to gym")
print("After insert:", tasks)

# -------------------------
# Remove Task
# -------------------------
tasks.remove("go to gym")
print("After remove:", tasks)

# -------------------------
# Pop Last Task
# -------------------------
tasks.pop()
print("After pop:", tasks)

# -------------------------
# Final Output
# -------------------------
print("Final Task List:", tasks)