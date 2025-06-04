# Example of Pattern Printing of number of 2 multiplication.

# Input from the user
n = int(input("Enter the number of rows: "))
num = 2

# Main logic of the program
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()