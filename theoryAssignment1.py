# Q1)
number = 10
if number > 5:
    print("The number is greater than 5.")
    print("This is part of the if block.")

print("This is outside the if block.")

# Q4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 =int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print(f"The largest number is: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")