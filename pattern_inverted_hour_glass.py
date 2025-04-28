N = int(input())
for r in range(2*N + 1):
    i = r if r <= N else 2*N - r
    a = list(range(N, N - i - 1, -1))
    b = a[::-1] if i < N else a[::-1][1:]
    if i < N:
        gap = (2*(N - i) - 1) * 2
        print(' '.join(map(str, a)) + ' ' * gap + ' '.join(map(str, b)))
    else:
        print(' '.join(map(str, a + b)))