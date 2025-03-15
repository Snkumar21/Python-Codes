import itertools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = itertools.permutations(numbers)

for perm in permutations:
    print(perm)