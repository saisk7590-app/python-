# Day 1: Get inputs and store them in variables
print("Welcome to the Bill Splitter!")
total_bill_str = input("What was the total bill? $")
tip_percentage_str = input("How much tip would you like to give? (e.g., 10, 12, or 15) ")
people_str = input("How many people are splitting the bill? ")

# Day 2: Type conversion and calculations
# We use float() for money because it has decimals
total_bill = float(total_bill_str)
tip_percent = int(tip_percentage_str)
people = int(people_str)

# Calculate total with tip
tip_amount = total_bill * (tip_percent / 100)
final_total = total_bill + tip_amount
amount_per_person = final_total / people

# Day 3: String formatting (f-strings)
# :.2f forces the number to show exactly 2 decimal places (like $15.50)
message = f"Each person should pay: ${amount_per_person:.2f}"
print(message)
