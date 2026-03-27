## List basics 

my_list = [10,20,30,40]
print(f"List: {my_list}")


## Access elements 

print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")
print(f"Every 2nd element from index 1: {my_list[1::2]}")
## [start : end : step] slicing works 

## Update elements 

my_list[0] = 100 #Lists are mutable → you can change values
print(f"New list : {my_list}")

## Appened elements, append() → add at end
my_list.append(50)
print(f"After append : {my_list}")

## Insert elements , insert() → add at specific position
my_list.insert(1, 60)
print(f"Afer insert: {my_list}")

## Extend elements , add multiple elements
my_list.extend([80, 90])
print(f"After extend: {my_list}")