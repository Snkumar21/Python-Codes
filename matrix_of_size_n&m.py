def sum_matrix(arr, n, m):
    # Base case: if matrix is empty
    if n == 0:
        return 0
    # Recursive case: sum of last row + sum of rest
    return sum(arr[n-1]) + sum_matrix(arr, n-1, m)

arr = [
    [4, 5, 6, 1],
    [2, 3, 2, 1],
    [1, 3, 6, 7]
]
n = len(arr)
m = len(arr[0]) if arr else 0

print(sum_matrix(arr, n, m))