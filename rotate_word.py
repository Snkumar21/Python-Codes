def rotate_word(word, shift):
    rotated_word = ""
    
    for char in word:
        if char.isalpha():  # Check if character is a letter
            start = ord('A') if char.isupper() else ord('a')
            rotated_word += chr(start + (ord(char) - start + shift) % 26)
        else:
            rotated_word += char  # Keep non-alphabet characters unchanged
    
    return rotated_word

# Example Usage
word = input("Enter a word: ").upper()
shift = int(input("Enter shift value: "))
print("Rotated Word:", rotate_word(word, shift))