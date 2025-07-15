# Read input
n = int(input().strip())

# Generate the pattern
for i in range(1, n + 1):
    if i == 1:
        print("1")
    elif i == 2:
        print("11")
    else:
        num = str(i - 1)
        zeros = "0" * (i - 2)
        print(num + zeros + num)