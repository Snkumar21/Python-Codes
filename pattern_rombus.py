N = int(input())
# Upper half including middle row
for i in range(1, N + 1):
    indent = '\t' * (N - i)
    inc = [str(i + j) for j in range(i)]
    dec = [str(i + j) for j in range(i - 2, -1, -1)]
    print(indent + '\t'.join(inc + dec))
# Lower half
for i in range(N - 1, 0, -1):
    indent = '\t' * (N - i)
    inc = [str(i + j) for j in range(i)]
    dec = [str(i + j) for j in range(i - 2, -1, -1)]
    print(indent + '\t'.join(inc + dec))