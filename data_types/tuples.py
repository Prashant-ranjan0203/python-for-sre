# tuple example

my_tuple = (5, 6, 7)

print(f"Tuple:{my_tuple}")

#access element 
print(f"first element :{my_tuple[0]}" )

print(f"last element :{my_tuple[-1]}")

##Slicing
print(f"All elements: {my_tuple[:]}") # includes index 0,1,2
print(f"First 2 elements: {my_tuple[:2]}")  # includes index 0,1
print(f"From index 1 onwards: {my_tuple[1:]}") 
#check len
print(f"Length: {len(my_tuple)}")

#immutability test 

try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error:{e}")

