# Example of identity operators in python...

print("Identity Operators")
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x =", x)
print("y =", y)
print("z =", z)

# is operator
print("Does x is z? ->", x is z)  # True, because z is a reference to x
print("Does x is y? ->", x is y)  # False, different objects with the same values

# is not operator
print("Does x is not y? ->", x is not y)  # True, x and y are not the same object
print("Does x is not z? ->", x is not z)  # False, x and z are the same object

print()