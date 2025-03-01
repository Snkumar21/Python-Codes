# Create a list of 10 elements
my_list = [45, 12, 89, 34, 67, 22, 90, 11, 56, 78]

# 1. Display the first 3 elements
print("First 3 elements:", my_list[:3])

# 2. Display elements excluding the first and the last element
print("Elements excluding the first and last:", my_list[1:-1])

# Sort the list in descending order
my_list.sort(reverse=True)
print("List sorted in descending order:", my_list)