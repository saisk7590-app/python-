# -------------------------
# Unique Checker System
# -------------------------

# Create empty set
names = set()

# -------------------------
# Input Names
# -------------------------

for i in range(5):
    user_name = input(f"Enter name {i+1}: ")
    names.add(user_name)

# -------------------------
# Display Unique Names
# -------------------------

print("\n----- UNIQUE NAMES -----")

for name in names:
    print(name)

# -------------------------
# Membership Checking
# -------------------------

search_name = input("\nEnter name to search: ")

if search_name in names:
    print(f"{search_name} found in the set.")
else:
    print(f"{search_name} not found in the set.")

# -------------------------
# Raw Set Output
# -------------------------

print("\nRaw Set:")
print(names)