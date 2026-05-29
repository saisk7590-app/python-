# -------------------------
# Contact Book System
# -------------------------

# Store contacts
contacts = {
    "contact1": {
        "name": "Sai",
        "phone": "9999999999",
        "city": "Hyderabad"
    },

    "contact2": {
        "name": "Ravi",
        "phone": "8888888888",
        "city": "Bangalore"
    },

    "contact3": {
        "name": "Anita",
        "phone": "7777777777",
        "city": "Mumbai"
    }
}

# -------------------------
# Display Contact Book
# -------------------------

print("----- CONTACT BOOK -----\n")

for contact_id, details in contacts.items():
    print(f"Contact ID : {contact_id}")
    print(f"Name       : {details['name']}")
    print(f"Phone      : {details['phone']}")
    print(f"City       : {details['city']}")
    print("-" * 30)

# -------------------------
# Add New Contact
# -------------------------

contacts["contact4"] = {
    "name": "Priya",
    "phone": "6666666666",
    "city": "Chennai"
}

# -------------------------
# Update Contact
# -------------------------

contacts["contact2"]["phone"] = "9999999999"

# -------------------------
# Final Updated Contact Book
# -------------------------

print("\n----- UPDATED CONTACT BOOK -----\n")

for contact_id, details in contacts.items():
    print(f"Contact ID : {contact_id}")
    print(f"Name       : {details['name']}")
    print(f"Phone      : {details['phone']}")
    print(f"City       : {details['city']}")
    print("-" * 30)