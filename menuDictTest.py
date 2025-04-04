<<<<<<< HEAD
# Write menu driven python program to implement at least 5 built-in functions of dictionary.

def display_menu():
    print("1. Add a key-value pair")
    print("2. Remove a key-value pair")
    print("3. Update a value")
    print("4. Check if a key exists")
    print("5. Clear the dictionary")
    print("6. Exit")

my_dict = {}

while True:
    display_menu()
    choice = int(input("Enter your choice (1-9): "))
        
    if choice == 1:
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            my_dict[key] = value
            print(key, value)
            print("Current dictionary:", my_dict)

    elif choice == 2:
            key = input("Enter the key to remove: ")
            if key in my_dict:
                my_dict.pop(key)
                print(f"Removed key: ", key)
            else:
                print("Key not found")
            print("Current dictionary:", my_dict)

    elif choice == 3:
            key = input("Enter the key to update: ")
            if key in my_dict:
                value = input("Enter the new value: ")
                my_dict[key] = value
                print(key, value)
            else:
                print("Key not found")
            print("Current dictionary:", my_dict)

    elif choice == 4:
            key = input("Enter the key to check: ")
            if key in my_dict:
                print(f"Key '{key}' exists with value: ", my_dict[key])
            else:
                print(f"Key does not exist.", key)

    elif choice == 5:
            my_dict.clear()
            print("Dictionary cleared")
            print("Current dictionary:", my_dict)

    elif choice == 6:
            print("Exit")
            break

    else:
            print("Incorrect choice, please select a number between 1 and 9.")
=======
# Example of menu driven python program to implement at least 5 built-in functions of dictionary.

def display_menu():
    print("1. Add a key-value pair")
    print("2. Remove a key-value pair")
    print("3. Update a value")
    print("4. Check if a key exists")
    print("5. Clear the dictionary")
    print("6. Exit")

my_dict = {}

while True:
    display_menu()
    choice = int(input("Enter your choice (1-9): "))
        
    if choice == 1:
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            my_dict[key] = value
            print(key, value)
            print("Current dictionary:", my_dict)

    elif choice == 2:
            key = input("Enter the key to remove: ")
            if key in my_dict:
                my_dict.pop(key)
                print(f"Removed key: ", key)
            else:
                print("Key not found")
            print("Current dictionary:", my_dict)

    elif choice == 3:
            key = input("Enter the key to update: ")
            if key in my_dict:
                value = input("Enter the new value: ")
                my_dict[key] = value
                print(key, value)
            else:
                print("Key not found")
            print("Current dictionary:", my_dict)

    elif choice == 4:
            key = input("Enter the key to check: ")
            if key in my_dict:
                print(f"Key '{key}' exists with value: ", my_dict[key])
            else:
                print(f"Key does not exist.", key)

    elif choice == 5:
            my_dict.clear()
            print("Dictionary cleared")
            print("Current dictionary:", my_dict)

    elif choice == 6:
            print("Exit")
            break

    else:
            print("Incorrect choice, please select a number between 1 and 9.")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
