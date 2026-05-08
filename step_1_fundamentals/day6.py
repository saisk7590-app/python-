# --- LOGIN SYSTEM ---
password = "123"
attempt = input("Enter Access PIN: ")

if attempt != password:
    print("Access Denied! ❌")
else:
    print("Access Granted! ✅")
    while True:
        print("\n" + "="*30)
        print("🚀 SMART UTILITY SYSTEM 🚀")
        print("="*30)
        print("1. Profile Generator")
        print("2. Calculator")
        print("3. Multiplication Table")
        print("4. Pattern Printer (Pyramid/Square)")
        print("5. Exit")

        choice = input("\nSelect choice (1-5): ")

        if choice == "1":
            print("\n👤 PROFILE GENERATOR")
            name = input("Name: ")
            age = int(input("Age: "))
            city = input("City: ")
            
            username = name.strip().lower().replace(" ", "_")
            print(f"\n✨ Hello {name}!")
            print(f"🔗 ID: {username} | 📍 {city} | 🎂 Age+5: {age+5}")
            print("Status: 🧔 Adult" if age >= 18 else "Status: 🧒 Minor")

        elif choice == "2":
            print("\n🔢 QUICK CALC")
            a = float(input("First: "))
            b = float(input("Second: "))
            print(f"➕ {a+b} | ➖ {a-b} | ✖️ {a*b}")
            if b != 0: print(f"➗ {a/b}")

        elif choice == "3":
            print("\n📈 TABLE GENERATOR")
            num = int(input("Number: "))
            for i in range(1, 11):
                print(f"🔥 {num} x {i} = {num * i}")

        elif choice == "4":
            print("\n🎨 PATTERN MENU")
            print("A. Triangle Pyramid")
            print("B. Solid Square")
            sub_choice = input("Pick A or B: ").upper()
            rows = int(input("Size: "))
            
            if sub_choice == "A":
                for i in range(1, rows + 1):
                    print(" " * (rows - i) + "* " * i)
            elif sub_choice == "B":
                for i in range(rows):
                    print("⭐ " * rows)

        elif choice == "5":
            print("\nPowering down... 👋")
            break

        else:
            print("\n⚠️ Invalid Entry!")

        # --- REPEAT CONFIRMATION ---
        input("\nPress ENTER to return to menu...")
