# Input
string = 'This is a Simple String'

# Displaying the string
def display_string():
    print(string,"\n")

# Splitting the string into words
def split_string():
    print(string.split(),"\n")

# Concert into Lowercases
def convert_lowercase():
    if any(c.isupper() for c in string):
        print("Lowercase String:", string.lower())
    else:
        print("String is already in lowercase.")

# Count the string
def count_string():
    print("Number of characters in the string:", len(string))

# Menu-driven program
while True:
    print("\nMenu:")
    print("1. Display String")
    print("2. Split String")
    print("3. Convert to Lowercase")
    print("4. Count String")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':
        print("Exiting the program...")
        break
    
    if choice == '1':
        display_string()
    elif choice == '2':
        split_string()
    elif choice == '3':
        convert_lowercase()
    elif choice == '4':
        count_string()