<<<<<<< HEAD
str = input("Enter a string: ")

vowels = "AaEeIiOoUu"
consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"

vowels_count = sum(1 for char in str if char in vowels)
consonants_count = sum(1 for char in str if char in consonants)

print("Vowels:",vowels_count)
=======
str = input("Enter a string: \n")

vowels = "AaEeIiOoUu"
consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"

vowels_count = sum(1 for char in str if char in vowels)
consonants_count = sum(1 for char in str if char in consonants)

print("Vowels:",vowels_count)
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
print("Consonants:",consonants_count)