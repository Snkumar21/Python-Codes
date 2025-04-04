# Write a menu driven program for the given string input: "This is a Simple String"
# i) To display length 
# ii) To display the count of characters 
# iii) To split the string 
# iv) If the given string has capital letters, then convert it to lower case letters 

def stringMenu():
    print("1. Display length")
    print("2. Display count of characters")
    print("3. Split the string")
    print("4. Convert to lower case")

str1 = "This is a Simple String"
while(True):
    stringMenu()
    select = int(input("Select an option:"))
    if select == 1:
        print("Length of the string is:", len(str1)) # Output:- Length of the string is: 23
    elif select == 2:
        print("Count of characters in the string is:", len(str1)) # Output:- Count of characters in the string is: 23
    elif select == 3:
        print("Split the string:", str1.split()) # Output:- Split the string: ['This', 'is', 'a', 'Simple', 'String']
    elif select == 4:
        print("Convert to lower case:", str1.lower()) # Output:- Convert to lower case: this is a simple string
    else:
        print("Invalid option")
