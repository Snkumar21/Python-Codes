# Example of replace element in the list in python...

# Consider the list with following elements: -
# ls = 20, 30, 40, 20, 50
# Find and replace the first occurrence of 20 with 10.

ls = [20, 30, 40, 20, 50]

if 20 in ls:
    index = ls.index(20)
    ls[index] = 10
    
print(ls)