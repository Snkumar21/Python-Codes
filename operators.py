# Example of operators in python...

# Use of variables
name = "Nitish"
age = 22
print("Name:-", name)
print("Age:-", age)

# Arithmetic operators
num1 = 15
num2 = 20
print("Addition:-", num1 + num2)
print("Subtraction:-", num1 - num2)
print("Multiplication:-", num1 * num2)
print("Division:-", num1 / num2)
print("Modulus:-", num1 % num2)
print("Floor division:-", num1 // num2)
print("Exponent:-", num1 ** num2)

# Assignment operators
a = 2
print("Assignment operator:-", a)
a += 2
print("Add assign:-", a)
a -= 2
print("Subtract assign:-", a)
a *= 2
print("Multiply assign:-" , a)
a /= 2
print("Divide assign:-", a)
a %= 2
print("Modulus assign:-", a)
a //= 2
print("Floor divide assign:-", a)
a **= 2
print("Exponent assign:-", a)

# Comparison operators
num1 = 5
num2 = 12
print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 != num2)
print(num1 >= num2)
print(num1 <= num2)

# Logical operators
num1 = 5
num2 = 12
print(num1 > num2 and num1 < num2)
print(num1 > num2 or num1 < num2)
print(not num1 > num2)
print(num1 and num2) # Find the reason why it is printing 12 instead of True

# Identity operators
num1 = 5
num2 = 12
print(num1 is num2)
print(num1 is not num2)

# Membership operators
h = "Hello World!"
print("'H' in h:-", 'H' in h)
print("'Z' not in h:-", 'Z' not in h)

# Bitwise operators
b = 5  # Binary: 0101
c = 3  # Binary: 0011
print("AND:-", b & c)  # Binary: 0001
print("OR:-", b | c)   # Binary: 0111
print("XOR:-", b ^ c)  # Binary: 0110
print("Left Shift:-", b << 1)  # Binary: 1010
print("Right Shift:-", b >> 1) # Binary: 0010
