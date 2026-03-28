# Shopping List Operations

# Initial list
my_cart = ["apples", "bananas", "milk"]
print("Initial cart:", my_cart)

# Add item
my_cart.append("bread")
print("After adding bread:", my_cart)

# Insert item
my_cart.insert(0, "ketchup")
print("After inserting ketchup:", my_cart)

# Remove item
my_cart.remove("bananas")
print("After removing bananas:", my_cart)

# Pop last item
removed_item = my_cart.pop()
print("Removed item:", removed_item)
print("After pop:", my_cart)

# Extend list
my_cart.extend(["rice", "butter"])
print("After extending:", my_cart)

# Sort list
my_cart.sort()
print("Sorted cart:", my_cart)

# Reverse list
my_cart.reverse()
print("Reversed cart:", my_cart)

# Concatenate lists
new_list = ["juice", "jam"]
updated_list = my_cart + new_list
print("Concatenated list:", updated_list)

# Duplicate list
duplicate = my_cart * 2
print("Duplicated list:", duplicate)

# String to list
veggies = "tomato cucumber spinach"
veggie_list = veggies.split()
print("Vegetable list:", veggie_list)