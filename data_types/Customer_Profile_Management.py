# Step 1: Create dictionary
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}

# Step 2: Print dictionary
print("Initial customer:", customer)

# Step 3: Add email and phone
customer["email"] = "john.doe@example.com"
customer["phone"] = "123-456-7890"

# Step 4: Print updated dictionary
print("\nAfter adding email & phone:", customer)

# Step 5: Print specific values
print("\nName:", customer["name"])
print("City:", customer["city"])

# Step 6: Check if 'email' exists
print("\nDoes 'email' exist?", "email" in customer)

# Step 7: Delete 'age'
del customer["age"]

# Step 8: Print updated dictionary
print("\nAfter deleting age:", customer)

# Step 9: Print keys, values, items
print("\nKeys:", customer.keys())
print("Values:", customer.values())
print("Items:", customer.items())

# Step 10: Remove last inserted item
last_item = customer.popitem()
print("\nRemoved last item:", last_item)

# Step 11: Use .get() for missing key
membership = customer.get("membership")
print("\nMembership value:", membership)

# Step 12: Update dictionary
customer["address"] = "221B Baker Street"

# Step 13: Final dictionary
print("\nFinal customer data:", customer)