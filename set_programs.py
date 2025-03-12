# Set
set_ds = {1,1,2,3,3,4,5,6,7,7} 
print(set_ds)
set_ds.add(55)
print(set_ds)
set_ds.remove(55)
print(set_ds)
#Operations
set_ds1 = {10,20,30,40,50}
set_ds2 = {10,20,100,200,300}
print(set_ds1.union(set_ds2))
print(set_ds1.intersection(set_ds2))
print(set_ds2.difference(set_ds1))
set_ds1.clear()
print(set_ds1)