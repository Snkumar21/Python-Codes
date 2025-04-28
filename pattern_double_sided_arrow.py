n = int(input())

mid = (n + 1) // 2

for i in range(1, n + 1):
    # Decide which row
    if i <= mid:
        row = i
    else:
        row = n - i + 1

    # Print leading tabs
    print("\t" * (mid - row), end="")

    # Print decreasing numbers
    for num in range(row, 0, -1):
        print(num, end="\t")

    # Middle tabs
    if i == 1 or i == n:
        pass
    else:
        spaces = (row * 2 - 1)
        print("\t" * spaces, end="")

    # Print increasing numbers
    if i != 1 and i != n:
        for num in range(1, row + 1):
            print(num, end="\t")

    print()