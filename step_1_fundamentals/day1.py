# --- Input ---
print("\n--- Input ---")
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
college = input("Enter college: ")
favorite_food = input("Enter favorite food: ")

# --- Processing ---
username = name.lower().replace(" ", "_")
future_age = age + 1

# --- Output ---
print("\n--- PROFILE ---")
print(f"Generated Username: {username}")
print(f"Hello {name}, next year you will be {future_age}")
print(f"You live in {city} and study at {college}")
print(f"Your favorite food is {favorite_food}")

# --- Extra Logic (Optional) ---
if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")