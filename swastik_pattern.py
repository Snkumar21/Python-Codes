# Read input (odd N ≥ 5)
N = int(input().strip())
mid = N // 2

for i in range(N):
    for j in range(N):
        if i < mid:
            # Top half: left arm, vertical drop, and top arm
            if j == 0 or j == mid or (i == 0 and j > mid):
                print('*', end='')
            else:
                print(' ', end='')
        elif i == mid:
            # Middle crossbar
            print('*', end='')
        else:
            # Bottom half: right arm and bottom arm
            if j == mid or j == N - 1 or (i == N - 1 and j <= mid):
                print('*', end='')
            else:
                print(' ', end='')
    print()