n = int(input())

for i in range(1, 2 * n):
    if i <= n:
        row = i
    else:
        row = 2 * n - i

    # Print leading tabs
    print("\t" * (n - row), end="")

    # Calculate starting number
    start = row
    count = 2 * row - 1

    # Print increasing then decreasing numbers
    for j in range(1, count + 1):
        if j <= row:
            print(start, end="\t")
            start += 1
        else:
            start -= 1
            print(start, end="\t")

    print()