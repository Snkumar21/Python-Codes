# Example of pattern printing in shape of square using '*'.

# Input from the user
n = int(input("Enter the number of rows: "))
num = 1

# Main logic of the program
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
