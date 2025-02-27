# Example of pattern program using star.

# Input
n = int(input("Enter the number of rows: "))

# Logic and Display
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
