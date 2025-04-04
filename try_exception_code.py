<<<<<<< HEAD
# Example of using more than one except block for handling in python...

try:
    ndiv=12/0
    print(ndiv)
    num = [1,2,3,4,5]
    print(num[5])
except ZeroDivisionError:
    print("Denominator cannot be 0")
except IndexError:
=======
# Example of using more than one except block for handling in python...

try:
    ndiv=12/0
    print(ndiv)
    num = [1,2,3,4,5]
    print(num[5])
except ZeroDivisionError:
    print("Denominator cannot be 0")
except IndexError:
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
    print("Index is Out of Bound")