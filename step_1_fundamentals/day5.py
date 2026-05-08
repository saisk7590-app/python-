while True:
    print("\n--- Quick Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Miles to Kilometers")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        # Formula: (Celsius * 9/5) + 32
        print(f"Result: {c}°C is {(c * 9/5) + 32:.2f}°F")

    elif choice == "2":
        miles = float(input("Enter Miles: "))
        # Formula: Miles * 1.60934
        print(f"Result: {miles} miles is {miles * 1.60934:.2f} km")

    elif choice == "3":
        print("Closing converter. Bye!")
        break

    else:
        print("Please pick 1, 2, or 3")
