arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

merged = [0] * (len(arr1) + len(arr2))

for i in range(len(arr1)):
    merged[i] = arr1[i]

for j in range(len(arr2)):
    merged[len(arr1) + j] = arr2[j]

print(merged)