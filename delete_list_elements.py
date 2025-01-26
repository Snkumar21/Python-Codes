#Delete list element from using Index value from the List in Python.

list_ds = [5, 6, 7, 'access-the-elements', 4.55, 20, 50]

del list_ds[5] #delete element at index 5
print(list_ds) #output

list_ds.remove('access-the-elements') #remove
print(list_ds)

poped = list_ds.pop(1) #pop
print("Popped value:", poped, "Remaining elements:", list_ds) #output

list_ds.clear() #empty the list
print(list_ds) #output
