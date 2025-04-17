# Example of Pattern Printing of star '*' from left-side of floyd shape triangle.

# Input from the user
n = int(input("Enter the number of rows: "))
num = 1

# Main logic of the program
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()