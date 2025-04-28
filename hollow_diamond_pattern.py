N = int(input())
mid = (N + 1) // 2
for r in range(1, N + 1):
    if r == 1 or r == N:
        print('\t'.join(['*'] * N))
    else:
        side_count = abs(mid - r) + 1
        gap_count = N - 2 * side_count
        left = ['*'] * side_count
        right = ['*'] * side_count
        # Print left cluster, gap tabs, and right cluster
        print('\t'.join(left) + '\t' * (gap_count + 1) + '\t'.join(right))