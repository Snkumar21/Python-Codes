dict1 = {}
print(dict1) # Output:- {}

dict2 = {1: "AI", 2: "ML", 3: "Data Science"}
print(dict2) # Output:- {1: 'AI', 2: 'ML', 3: 'Data Science'}
dict2[2] = "Cloud"
print(dict2) # Output:- {1: 'AI', 2: 'Cloud', 3: 'Data Science'}

dict3 = {"First": "Lab DSA", "Second": "Lab JS", "Third": "Lab Python"}
print(dict3) # Output:- {'First': 'Lab DSA', 'Second': 'Lab JS', 'Third': 'Lab Python'}
dict3["Third"] = "Lab Java"
print(dict3) # Output:- {'First': 'Lab DSA', 'Second': 'Lab JS', 'Third': 'Lab Java'}

print(dict3["First"]) # Output:- Lab DSA
print(dict3.get("Second")) # Output:- Lab JS
print(dict3.keys()) # Output:- dict_keys(['First', 'Second', 'Third'])
print(dict3.values()) # Output:- dict_values(['Lab DSA', 'Lab JS', 'Lab Java'])
print(dict3.items()) # Output:- dict_items([('First', 'Lab DSA'), ('Second', 'Lab JS'), ('Third', 'Lab Java')])

popValue = dict3.pop("Third")
print("Value:", popValue) # Output:- 
print("Dictionary:", dict3) # Output:- 

popKeyValue = dict1.popitem()
print("Key, value pair:", popKeyValue) # Output:- 
print("Dictionary", dict3) # Output:- 

dict1.clear()
print("Cleared", dict3) # Output:- 

# Q1)


# Q2)
dictOne = {1: "Facebook", 2: "Amazon", 3: "Apple", 4: "Netflix", 5: "Google"}
dictTwo = {1: "Microsoft", 2: "NVIDIA", 3: "Cisco", 4: "", 5: ""}

# Q3)
