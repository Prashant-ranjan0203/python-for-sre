# cup_size = input("Enter your preferrd cup size from  : 'large', 'medium', 'small' \n").strip().lower()
# if cup_size == 'small':
#     print(f"The price is ${10}")

# elif cup_size == 'medium':
#     print(f"The price is ${15}")

# elif cup_size == 'large':
#     print(f"The price is ${20}")

# else:
#     print(f"Unkown")

# trying with dictionary method 


prices = {
    'small': 10,
    'medium':15,
    'large' :20
    }
cup_size = input("Enter cup size(small,medium,large): ").strip().lower()
if cup_size in prices:
    print(f"The price is ₹{prices[cup_size]}")
else:
    print(f"Unknown cup size")


