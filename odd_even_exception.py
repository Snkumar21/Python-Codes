# Example of print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 1
except:
    print("The entered number is even")
else:
    print("The entered number is odd")