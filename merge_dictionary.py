# Creating two dictionaries
dict1 = {'name': 'Nitish', 'age': 22, 'city': 'Pune', 'gender': 'Male', 'country': 'India'}
dict2 = {'profession': 'Technologist', 'salary': 1500000, 'company': 'Tech Brain', 'experience': 5, 'married': False}

# Merging both dictionaries into a third dictionary
merged_dict = {**dict1, **dict2}  # Using dictionary unpacking

# Displaying the merged dictionary
print("Merged Dictionary:", merged_dict)