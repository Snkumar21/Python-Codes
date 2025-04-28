N = int(input())
m = (N + 1) // 2
L = list(range(1, m)) + [m] + list(range(m-1, 0, -1))

for i in L:
    s = ' ' * (m - i) * 4
    a = ' '.join(map(str, range(i, 0, -1)))
    b = ' '.join(map(str, range(1, i + 1))) if i > 1 else ''
    g = ' ' * (4 * (i - 1) - 1) if i > 1 else ''
    print(s + a + g + b)