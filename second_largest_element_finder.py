def second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements."

    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)

    if len(unique_arr) < 2:
        return "No second largest element found."
    
    return unique_arr[1]

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = second_largest(arr)

print("Second largest element:", result)