# Take an array and sort the array without using pre-defined module.

# Bubble sort function to sort an array
def bubble_sort(arr):
    
    # Defining the length of the array in the variable
    n = len(arr)
    
    # For loop logic of the code
    for i in range(n):
        for j in range(n - i - 1):
            # if array of j is greater than j+1 then j will return j+1 and then j+1 will return array of j.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Array defining
arr = [-1, -2, -9, 100, 9]

# Calling the function
bubble_sort(arr)

# Displaying the result.
print(arr)