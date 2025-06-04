# swapping number without using third variable

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

a = a + b
b = a - b
a = a - b

print("a is:", a, "b is:", b)