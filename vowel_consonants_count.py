str = input("Enter a string: ")

vowels = "AaEeIiOoUu"
consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"

vowels_count = sum(1 for char in str if char in vowels)
consonants_count = sum(1 for char in str if char in consonants)

print("Vowels:",vowels_count)
print("Consonants:",consonants_count)