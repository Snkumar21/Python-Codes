# Example of pass statement in python
import math

#Use of pass statement inside function
def greet():
    pass
print("pass inside a function")

#function with default arguments
def add2(n1=10,n2=33):  
    res2=n1+n2
    print("The addition of two numbers with default values:",res2)

# function call with two arguments
add2(105, 15)
#  function call with one argument
add2(27)
# function call with no arguments
add2()

#use of keyword arguments
def display(fName, lName):
    print('First Name:', fName)
    print('Last Name:', lName)

display(lName = 'Singh', fName = 'Nitish')

# Use of arbitary arguments,program to find sum of multiple numbers 
def add3(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Addition = ", result)

# function call with 3 arguments
add3(11, 22, 33)
# function call with 2 arguments
add3(14, 9)

# sqrt computes the square root
square_root = math.sqrt(16)
print("Square Root of 16 is",square_root)

# pow() comptes the power
power = pow(2, 5)
print("2 to the power 5 is",power)
