from collections import Counter

def count_alphabet_occurrences(s):
    s = s.lower()
    alphabet_counts = Counter(char for char in s if char.isalpha())
    
    for char, count in alphabet_counts.items():
        print(f"{char}: {count}")

# Get user input
input_string = input("Enter a string: ")
count_alphabet_occurrences(input_string)