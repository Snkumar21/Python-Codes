<<<<<<< HEAD
# Write python program to implement class, object, user defined function to display factorial of a number?

class Factorial:
    def __init__(self, num):
        self.num = num

    def factorial(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact = fact * i
        return fact
    
num = int(input("Enter a number: "))
obj = Factorial(num)
print("Factorial of", num, "is", obj.factorial())
=======
# Example to implement class, object, user defined function to display factorial of a number in python.

class Factorial:
    def __init__(self, num):
        self.num = num

    def factorial(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact = fact * i
        return fact
    
num = int(input("Enter a number: "))
obj = Factorial(num)
print("Factorial of", num, "is", obj.factorial())
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
