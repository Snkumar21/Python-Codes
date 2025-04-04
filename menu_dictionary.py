<<<<<<< HEAD
def display_menu():
    print("1. Add a key-value pair")
    print("2. Remove a key-value pair")
    print("3. Update a value")
    print("4. Check if a key exists")
    print("5. Display all keys")
    print("6. Display all values")
    print("7. Display all key-value pairs")
    print("8. Clear the dictionary")
    print("9. Exit")

my_dict = {}

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-9): "))
        
        if choice == 1:
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            my_dict[key] = value
            print(f"Added: ", key, value)
            print("Current Dictionary:", my_dict)

        elif choice == 2:
            key = input("Enter the key to remove: ")
            if key in my_dict:
                my_dict.pop(key)
                print(f"Removed key: ", key)
            else:
                print("Key not found!")
            print("Current Dictionary:", my_dict)

        elif choice == 3:
            key = input("Enter the key to update: ")
            if key in my_dict:
                value = input("Enter the new value: ")
                my_dict[key] = value
                print(f"Updated: ", key, value)
            else:
                print("Key not found!")
            print("Current Dictionary:", my_dict)

        elif choice == 4:
            key = input("Enter the key to check: ")
            if key in my_dict:
                print(f"Key '{key}' exists with value: ", my_dict[key])
            else:
                print(f"Key does not exist.", key)

        elif choice == 5:
            print("Keys:", list(my_dict.keys()))

        elif choice == 6:
            print("Values:", list(my_dict.values()))

        elif choice == 7:
            print("Current Dictionary:", my_dict)

        elif choice == 8:
            my_dict.clear()
            print("Dictionary cleared!")
            print("Current Dictionary:", my_dict)

        elif choice == 9:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 9.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
=======
# Example of menu driven program of dictionary in python...

def display_menu():
    print("1. Add a key-value pair")
    print("2. Remove a key-value pair")
    print("3. Update a value")
    print("4. Check if a key exists")
    print("5. Display all keys")
    print("6. Display all values")
    print("7. Display all key-value pairs")
    print("8. Clear the dictionary")
    print("9. Exit")

my_dict = {}

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-9): "))
        
        if choice == 1:
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            my_dict[key] = value
            print(f"Added: ", key, value)
            print("Current Dictionary:", my_dict)

        elif choice == 2:
            key = input("Enter the key to remove: ")
            if key in my_dict:
                my_dict.pop(key)
                print(f"Removed key: ", key)
            else:
                print("Key not found!")
            print("Current Dictionary:", my_dict)

        elif choice == 3:
            key = input("Enter the key to update: ")
            if key in my_dict:
                value = input("Enter the new value: ")
                my_dict[key] = value
                print(f"Updated: ", key, value)
            else:
                print("Key not found!")
            print("Current Dictionary:", my_dict)

        elif choice == 4:
            key = input("Enter the key to check: ")
            if key in my_dict:
                print(f"Key '{key}' exists with value: ", my_dict[key])
            else:
                print(f"Key does not exist.", key)

        elif choice == 5:
            print("Keys:", list(my_dict.keys()))

        elif choice == 6:
            print("Values:", list(my_dict.values()))

        elif choice == 7:
            print("Current Dictionary:", my_dict)

        elif choice == 8:
            my_dict.clear()
            print("Dictionary cleared!")
            print("Current Dictionary:", my_dict)

        elif choice == 9:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 9.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
