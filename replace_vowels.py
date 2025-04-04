def replace_vowels(text):
    vowels = "AaEeIiOoUu"
    result = "".join("*" if char in vowels else char for char in text)
    return result

user_input = input("Enter a string: ")
modified_string = replace_vowels(user_input)

print(modified_string)