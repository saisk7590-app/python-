correct_username = "admin"
correct_password = "1234"

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    print(f"\nAttempt {attempts + 1} of {max_attempts}")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username:

        if password == correct_password:
            print("\nLogin successful.")
            print(f"Welcome, {username}!")
            break

        else:
            print("Wrong password.")

    else:
        print("Wrong username.")

    attempts += 1

    remaining_attempts = max_attempts - attempts

    if remaining_attempts > 0:
        print(f"Remaining attempts: {remaining_attempts}")

else:
    print("\nAccount locked due to 3 failed attempts.")