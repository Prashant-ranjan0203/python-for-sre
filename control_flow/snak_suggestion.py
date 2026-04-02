snack = input("Enter your preferred snack:").strip().lower()
#strip() is a string cleanup method in Python.It removes extra unwanted characters from the beginning and end of a string.
if snack == "cookies" or snack == "samosa":
    print(f"Great choice ! we will serve you {snack}")

else:
    print(f"sorry, we only serve cookies or samosa with tea")


