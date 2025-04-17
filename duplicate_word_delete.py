# This delete duplicate word from the given string.
string = input("Enter the string : ")

value = string.split()
unique = " ".join(dict.fromkeys(value))

print(unique)