#Built in Module in python
import math
import math as ma
from math import pi,factorial
import math
import platform
import time

from math import *

print("The value of pi is:",math.pi)
print("The value of pi is:",ma.pi)
print("The value of pi is :",pi)
print("The value of factorial is :",factorial(5) )

var=platform.system()
print(var)

var1=dir(platform)
print(var1)
print(time.asctime())
print(dir(math))
"""
# Custom Module in python
"""
def lab(labname):
    print("Welcome to "+ labname)

def sum(n1,n2):
    res=n1+n2
    #return res
    print("Sum of two numbers", res)