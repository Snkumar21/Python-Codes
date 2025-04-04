<<<<<<< HEAD
#Dictionary
dict1 = {} 
print(dict1)

dict1 = {1: 'AI', 2: 'Microservices using Java',3:'Cloud Computing'} 
print(dict1)
dict1[3]='Cloud'# change the value
print(dict1)

dict1 = {'First': 'Lab on Python', 'Second': 'Lab on Microservices','Third':'Lab on AI'}
print(dict1)
dict1['Second']='Next Generation Db'
print(dict1)

#Accessing 
print(dict1['First'])
print(dict1.get('Second'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#Deleting 
popedvalue = dict1.pop('Third')
print('Value:', popedvalue)
print('Dictionary:', dict1)
popkeyvalue = dict1.popitem()
print('Key, value pair:', popkeyvalue)
print('Dictionary', dict1)
dict1.clear()
print('ndict', dict1)
=======
# Example of Dictionary in python.
dict1 = {} 
print(dict1)

dict1 = {1: 'AI', 2: 'Microservices using Java',3:'Cloud Computing'} 
print(dict1)
dict1[3]='Cloud'# change the value
print(dict1)

dict1 = {'First': 'Lab on Python', 'Second': 'Lab on Microservices','Third':'Lab on AI'}
print(dict1)
dict1['Second']='Next Generation Db'
print(dict1)

#Accessing 
print(dict1['First'])
print(dict1.get('Second'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#Deleting 
popedvalue = dict1.pop('Third')
print('Value:', popedvalue)
print('Dictionary:', dict1)
popkeyvalue = dict1.popitem()
print('Key, value pair:', popkeyvalue)
print('Dictionary', dict1)
dict1.clear()
print('ndict', dict1)
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
