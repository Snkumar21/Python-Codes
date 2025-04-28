# Read input
N = int(input())

# Upper half (0 to N)
for i in range(N + 1):
    # Indentation grows by 2 spaces per level
    indent = ' ' * (2 * i)
    # Build descending and ascending sequences
    left = list(range(N - i, -1, -1))
    right = list(range(1, N - i + 1))
    nums = left + right
    # Print line
    print(indent + ' '.join(map(str, nums)))

# Lower half (N-1 down to 0)
for i in range(N - 1, -1, -1):
    indent = ' ' * (2 * i)
    left = list(range(N - i, -1, -1))
    right = list(range(1, N - i + 1))
    nums = left + right
    print(indent + ' '.join(map(str, nums)))