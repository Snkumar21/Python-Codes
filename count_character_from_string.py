def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

string = input("Enter a string: ")

result = count_characters(string)

print("Character frequencies:", result)