# Create two lists with 5 elements each
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

# Find common elements and store them in a third list
common_elements = [element for element in list1 if element in list2]

# Display the common elements
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common_elements)