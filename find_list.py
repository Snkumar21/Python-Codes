# This is finder code of element from an index.
ls = [20, 39, 28, 19, 328, 4, 74]

# Input the index to retrieve the value
index = int(input("Enter the index: "))

# Check if the index is valid
if 0 <= index < len(ls):
    print(f"The value at index {index} is {ls[index]}.")
else:
    print(f"Index {index} is out of range. The list has indices from 0 to {len(ls) - 1}.")
