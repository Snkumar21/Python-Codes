<<<<<<< HEAD
# Tuples

#Creating tuple
tuple_ds=()
type(tuple_ds)
tuple_ds = (1, 2, 3,4,5) 
print(tuple_ds)
tuple_ds=(12,)
type(tuple_ds)
print(tuple_ds)
#Accessing tuple
tuple_ds = (1, 2, 3,4,5,'tuple_example',5.55) 
print(tuple_ds)
for t in tuple_ds:
    print(t)
print(tuple_ds)
print(tuple_ds[0])
print(tuple_ds[:])
print(tuple_ds[5][4])
#Appending tuple
tuple_ds = (1, 2, 3,4,5,'tuple_example',5.55) 
tuple_ds = tuple_ds + (23, 24, 25) #add elements
print(tuple_ds)
#tuple_ds[2]=100 #you can't change the element in the tuple
print(tuple_ds)
nestuple = (12,14,15, [50, 80, 70], "Good Afternoon")
print(nestuple)
nestuple[3][1] = 100
print(nestuple)
deltuple=(10,20,30,40,50)
print(deltuple)
del deltuple
=======
# Tuples

#Creating tuple
tuple_ds=()
type(tuple_ds)
tuple_ds = (1, 2, 3,4,5) 
print(tuple_ds)
tuple_ds=(12,)
type(tuple_ds)
print(tuple_ds)
#Accessing tuple
tuple_ds = (1, 2, 3,4,5,'tuple_example',5.55) 
print(tuple_ds)
for t in tuple_ds:
    print(t)
print(tuple_ds)
print(tuple_ds[0])
print(tuple_ds[:])
print(tuple_ds[5][4])
#Appending tuple
tuple_ds = (1, 2, 3,4,5,'tuple_example',5.55) 
tuple_ds = tuple_ds + (23, 24, 25) #add elements
print(tuple_ds)
#tuple_ds[2]=100 #you can't change the element in the tuple
print(tuple_ds)
nestuple = (12,14,15, [50, 80, 70], "Good Afternoon")
print(nestuple)
nestuple[3][1] = 100
print(nestuple)
deltuple=(10,20,30,40,50)
print(deltuple)
del deltuple
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
print(deltuple)