# Example of pattern printing of normal triangle using '*'.

# Input from the user
n = int(input("Enter the number of rows: "))

# Main logic of the program
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)