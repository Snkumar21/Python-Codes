myTuple = ()
type(myTuple)
myTuple = (1, 2, 3, 4, 5)
print(myTuple)

myTuple=(12,)
type(myTuple)
print(myTuple)

myTuple1 = (1, 2, 3,4,5,'tuple_example',5.55) 
print(myTuple1)
for t in myTuple1:
    print(t)
print(myTuple1)
print(myTuple1[0])
print(myTuple1[:])
print(myTuple1[5][4])
print(myTuple1[5][4])
print(myTuple1[1 : 2])

tuple_ds = (1, 2, 3,4,5,'tuple_example',5.55) 
tuple_ds = tuple_ds + (23, 24, 25)
print(tuple_ds)

#tuple_ds[2]=100 #you can't change the element in the tuple
print(tuple_ds)