# Example of using more than one except block for handling in python...

try:
    ndiv=12/0
    print(ndiv)
    num = [1,2,3,4,5]
    print(num[5])
except ZeroDivisionError:
    print("Denominator cannot be 0")
except IndexError:
    print("Index is Out of Bound")