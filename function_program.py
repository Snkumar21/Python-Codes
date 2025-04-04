def gm(name):#name is called as a parameter
    print("Good Morning",name)

gm("Devyani")#actual value ---argument
gm("AAAA")

#method passing arguments
def add(n1,n2):
    res=n1+n2
    print("Addition of two numbers is",res)

add(10,20)

#use of return value

def add1(n1,n2):
    res1=n1+n2
    return res1

res1=add1(10,12)
print("The addition of two numbers is:",res1)

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

display(lName = 'KKK', fName = 'DDD')

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