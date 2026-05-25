# -------------------------
# Shopping List System
# -------------------------

shopping_list = []

# Add items
for i in range(5):
    item = input("Enter item: ")
    shopping_list.append(item)

# Display items
print("\nYour Shopping List:")

for item in shopping_list:
    print(item)

# List information
print("\nFirst item:", shopping_list[0])
print("Last item:", shopping_list[-1])
print("Total items:", len(shopping_list))

# Search item
search_item = input("\nSearch item: ")

if search_item in shopping_list:
    print("Item found")
else:
    print("Item not found")