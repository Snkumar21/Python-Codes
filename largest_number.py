# Example of Largest Number Finder using user-defined value in python...

# Take three numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Check which number is the largest
if num1 > num2 and num1 > num3:
    print(f"The largest number is: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")