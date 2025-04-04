#Strings
# create a string using double quotes
string1 = "Python programming"
# create a string using single quotes
string1 = 'Python programming'
# create string type variables
name = "Python"
print(name)
message = "I love Python."
print(message)
#Access String Characters in Python
#1. Indexing
message = 'hello'
# access 1st index element
print(message[1]) # "e"
#2. Use of negative index
message = 'hello'
# access 4th last element
print(message[-4]) # "e"
#3.Slicing
message = 'Hello'
# access character from 1st index to 3rd index
print(message[1:4])  # "ell"

#Strings are immutable
message = 'Hello Everyone'
# message[0] = 'M'
print(message)

#We can use variable name
message = 'Good Morning'
# assign new string to message variable
message = 'Hello Everyone'
print(message); # prints "Hello Everyone"

# multiline string 
message = """
Basics is very important
It forms the foundation for placement
"""
print(message)

#Operations on string---Compare two strings
str1 = "Hello, world"
str2 = "I love Python."
str3 = "Hello, world!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)
# split()
txt = "welcome to the jungle"
x = txt.split()
print(x)
# strip()
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")