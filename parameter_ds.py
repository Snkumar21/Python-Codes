# Example of passing a parameter in python.

def gm(name):#name is called as a parameter
    print("Good Morning",name)

gm("Nitish")#actual value ---argument
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