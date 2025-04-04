<<<<<<< HEAD
myList = []
print(myList)

myList1 = [2, 9.5, 'A', "College", True]
print(myList1)

myList2 = [1, 2, 3]
print()
myList2.append(4)
print(myList2)
myList2.append([5, 6])
print(myList2)

myList3 = ["TMV", "ADYPU"]
print(myList3)
myList3.extend("MIT")
print(myList3)

# Accessing elements in the list

list_ds = [7, 8, 9, "element", 4.5, 50]
# Syntax:- for <variable name> in <sequence>:
for value in list_ds:
    print(value)
print(list_ds)
print(list_ds[2])
print(list_ds[0:3])
print(list_ds[::-1])

# Deleting elements from the list

list_ds = [7, 8, 9, "element", 4.5, 50]
# del list_ds[5]
# print(list_ds)

# list_ds.remove("element") # removes element with value
# print(list_ds)

poped = list_ds.pop(1)
print("Popped value: ", poped, "Remaining elements: ", list_ds)

list_ds.clear() # empty the list
print(list_ds)
=======
# Example of dataType in list in python.

myList = []
print(myList)

myList1 = [2, 9.5, 'A', "College", True]
print(myList1)

myList2 = [1, 2, 3]
print()
myList2.append(4)
print(myList2)
myList2.append([5, 6])
print(myList2)

myList3 = ["TMV", "ADYPU"]
print(myList3)
myList3.extend("MIT")
print(myList3)

# Accessing elements in the list

list_ds = [7, 8, 9, "element", 4.5, 50]
# Syntax:- for <variable name> in <sequence>:
for value in list_ds:
    print(value)
print(list_ds)
print(list_ds[2])
print(list_ds[0:3])
print(list_ds[::-1])

# Deleting elements from the list

list_ds = [7, 8, 9, "element", 4.5, 50]
# del list_ds[5]
# print(list_ds)

# list_ds.remove("element") # removes element with value
# print(list_ds)

poped = list_ds.pop(1)
print("Popped value: ", poped, "Remaining elements: ", list_ds)

list_ds.clear() # empty the list
print(list_ds)
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
