# Get input string from user
text = input("Enter a string: ")

# First part: print by building up the string
for i in range(len(text)):
    print(text[:i+1])

# Second part: print substrings starting from each position
for i in range(1, len(text)-1):
    for j in range(i, len(text)):
        print(text[i:j+1]) 