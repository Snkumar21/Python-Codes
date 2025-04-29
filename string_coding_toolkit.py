# Example of string to palindrome, reverse the string and vowel and consonants...

class Palindrome:
    def __init__(self, str):
        self.str = str

    def is_palindrome(self):
        return str == str[::-1]

# User input
str = input("Enter the string: ")

# Palindrome calling function
palindrome_obj = Palindrome(str)

# Condition to print the palindrome
if palindrome_obj.is_palindrome():
    print(f"{str} is a Palindrome string.")
else:
    print(f"{str} is NOT a Palindrome string.")

# Reverse the String...
# Original String
print("Original String :",str)

# Reverse Logic
reversed_str = " ".join(str.split()[::-1])

# Displaying the result
print("Reversed String :",reversed_str)

# vowel and consonants...
# Declaration of the Vowels and Consonants
vowels = 'AaEeIiOoUu'
consonants = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'

# Logic of the counting the vowels and consonants
vowels_count = sum(1 for char in str if char in vowels)
consonants_count = sum(1 for char in str if char in consonants)

# Displaying the result...
print("Vowels from the string are : ",vowels_count)
print("Consonants from the string are : ", consonants_count)