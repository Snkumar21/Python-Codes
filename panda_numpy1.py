import numpy as np
# create a list named list1
list1 = [22, 43, 64, 85]
# create numpy array using list1
arrayvar = np.array(list1)
print(arrayvar)

arrayvar1=np.array([22, 43, 64, 85])
print(arrayvar1)
# create an array with 5 elements filled with zeros
array1 = np.zeros(5)
print(array1)


# create an array with values from 0 to 4
array1 = np.arange(5)
print("Using np.arange(5):", array1)
# create an array with values from 1 to 8 with a step of 2
array2 = np.arange(1, 9, 2)
print("Using np.arange(1, 9, 2):",array2)

# generate an array of 5 random numbers
array1 = np.random.rand(5)
print(array1)

# create an empty array of length 4
array1 = np.empty(4)
print(array1)

# create a 2D array with 2 rows and 4 columns
array1 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8]])
print(array1)