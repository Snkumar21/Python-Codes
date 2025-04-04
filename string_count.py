<<<<<<< HEAD
from collections import Counter

def count_alphabet_occurrences(s):
    s = s.lower()
    alphabet_counts = Counter(char for char in s if char.isalpha())
    
    for char, count in alphabet_counts.items():
        print(f"{char}: {count}")

# Get user input
input_string = input("Enter a string: ")
=======
from collections import Counter

def count_alphabet_occurrences(s):
    s = s.lower()
    alphabet_counts = Counter(char for char in s if char.isalpha())
    
    for char, count in alphabet_counts.items():
        print(f"{char}: {count}")

# Get user input
input_string = input("Enter a string: ")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
count_alphabet_occurrences(input_string)