# =====================================
# SMART PROFILE LOGIN SYSTEM
# =====================================

# -------- USER REGISTRATION --------
print("\n===== CREATE ACCOUNT =====")

full_name = input("Enter your full name: ").strip()
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip()
password = input("Create password: ").strip()

# -------- STRING PROCESSING --------
username = full_name.lower().replace(" ", "_")

# -------- CALCULATIONS --------
future_age = age + 5

# -------- ACCOUNT SUMMARY --------
print("\n===== ACCOUNT CREATED =====")
print(f"Generated Username: {username}")

# -------- LOGIN SYSTEM --------
print("\n===== LOGIN =====")

login_username = input("Enter username: ").strip().lower()
login_password = input("Enter password: ").strip()

# -------- AUTHENTICATION --------
if login_username == username and login_password == password:

    print("\n✅ Login Successful")

    # -------- PROFILE SECTION --------
    print("\n========== PROFILE ==========")

    print(f"Name            : {full_name.title()}")
    print(f"Username        : {username}")
    print(f"City            : {city.title()}")
    print(f"Current Age     : {age}")
    print(f"Age After 5 Years : {future_age}")

    # -------- AGE STATUS --------
    if age >= 18:
        print("Status          : Adult")
    else:
        print("Status          : Minor")

    print("================================")

else:
    print("\n❌ Invalid Username or Password")