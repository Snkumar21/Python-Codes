# Example of permutation in python...

import itertools

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myList)
p = itertools.permutations(myList)
for l in p:
    print(l)
print(myList)
