# This is a factorial display using class in python.
class FactorialCalculator:
    def __init__(self, num):
        self.num = num

    def calculate_factorial(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact *= i
        return fact

# Getting an input
num = int(input("Enter a number: "))

# Calling the class
factorial_obj = FactorialCalculator(num)

# Displaying the output
print(f"The factorial of {num} is: {factorial_obj.calculate_factorial()}")