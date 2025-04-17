# Example of Odd Even using AND Operator in python.

# Input from the user
num = int(input("Enter a number: "))

# Main logic of the code.
if (num & 1) == 0:
    print("The number is even")
else:
    print("The number is odd")