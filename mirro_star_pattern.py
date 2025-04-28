N = int(input())
mid = (N + 1) // 2

# upper half including middle line
for i in range(1, mid + 1):
    indent = '\t' * (mid - i)
    stars = ['*'] * (2 * i - 1)
    print(indent + '\t'.join(stars))

# lower half
for i in range(mid - 1, 0, -1):
    indent = '\t' * (mid - i)
    stars = ['*'] * (2 * i - 1)
    print(indent + '\t'.join(stars))