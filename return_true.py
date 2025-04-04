<<<<<<< HEAD
def has_no_e(word):
    return 'e' not in word.lower()

# List of words
words = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape"]

# Filter words without 'E'
no_e_words = [word for word in words if has_no_e(word)]

# Calculate percentage
percentage = (len(no_e_words) / len(words)) * 100

print("Words without 'E':", no_e_words)
print("Percentage without 'E': {:.2f}%".format(percentage))
=======
# Example of return true in python...

def has_no_e(word):
    return 'e' not in word.lower()

# List of words
words = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape"]

# Filter words without 'E'
no_e_words = [word for word in words if has_no_e(word)]

# Calculate percentage
percentage = (len(no_e_words) / len(words)) * 100

print("Words without 'E':", no_e_words)
print("Percentage without 'E': {:.2f}%".format(percentage))
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
