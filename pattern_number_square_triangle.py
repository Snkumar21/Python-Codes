# Read input
N = int(input().strip())

# Generate the pattern
for i in range(1, N + 1):
    row = [str(j ** 2) for j in range(1, i + 1)]
    print(" ".join(row))