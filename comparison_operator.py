# Example of comparison operator using user-define value.

#User Defined
num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

if num1 == num2:
    print("Both numbers are equal")
elif num1 > num2:
    print("Number", num1, "is greater than", num2)
elif num1 < num2:
    print("Number", num1, "is smaller than", num2)
elif num1 >= num2:
    print("Number", num1, "is greater than or equal to", num2)
elif num1 <= num2:
    print("Number", num1, "is smaller than or equal to", num2)
else:
    print("Number is not equal to")
