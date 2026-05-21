# =========================
# Day 20 — Login Validator
# =========================

stored_username = "admin"
stored_password = "1234"


def login(username, password):

    if username == stored_username and password == stored_password:
        return "✅ Login Successful"

    else:
        return "❌ Invalid Credentials"


# ===== INPUT SECTION =====

input_username = input("Enter Username: ")

input_password = input("Enter Password: ")


# ===== PROCESSING SECTION =====

login_result = login(input_username, input_password)


# ===== OUTPUT SECTION =====

print("\n===== LOGIN STATUS =====")

print(login_result)