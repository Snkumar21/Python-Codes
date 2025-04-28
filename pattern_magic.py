# Read input (odd N >= 5)
N = int(input().strip())
width = 2 * N - 1

for i in range(1, width + 1):
    # Map to effective row index r
    r = i if i <= N else 2 * N - i

    stars_per_side = N - r + 1
    spaces_middle = width - 2 * stars_per_side

    if spaces_middle < 0:
        # First or last row: full line of stars
        print('*' * width)
    else:
        # Hollow row: stars at the sides, spaces in the middle
        print(
            '*' * stars_per_side
            + ' ' * spaces_middle
            + '*' * stars_per_side
        )