# This code will remove duplicate element from the list in python.
# Create a list of 10 elements
elements = [int(input(f"Enter element {i+1}: ")) for i in range(10)]

# Remove duplicates by converting the list to a set and back to a list
unique_elements = list(set(elements))

# Display the original and unique lists
print("\nOriginal list with possible duplicates:", elements)
print("List after removing duplicates:", unique_elements)
