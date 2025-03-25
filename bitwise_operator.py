# Example of bitwise operator in python.

#User Defined
num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

print("Bitwise Operations on num1 =", num1, "and num2 =", num2)

# Bitwise AND
result = num1 & num2  # Binary: 111100 & 001101 = 001100
print("num1 & num2 =", result)

# Bitwise OR
result = num1 | num2  # Binary: 111100 | 001101 = 111101
print("num1 | num2 =", result)

# Bitwise XOR
result = num1 ^ num2  # Binary: 111100 ^ 001101 = 110001
print("num1 ^ num2 =", result)

# Bitwise NOT
result = ~num1  # Inverts bits: ~111100 = -111101
print("~num1 =", result)

# Left Shift
shift = 2
result = num1 << shift  # Binary: 111100 << 2 = 11110000
print("num1 <<", shift, "=", result)

# Right Shift
result = num1 >> shift  # Binary: 111100 >> 2 = 001111
print("num1 >>", shift, "=", result)
