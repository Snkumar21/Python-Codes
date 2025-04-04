def display_menu():
    print("\nDictionary Operations Menu:")
    print("1. Create a Dictionary")
    print("2. Add a Key-Value Pair")
    print("3. Remove a Key")
    print("4. Update a Value")
    print("5. Display Dictionary")
    print("6. Get Value by Key")
    print("7. Get All Keys")
    print("8. Get All Values")
    print("9. Get All Key-Value Pairs")
    print("10. Clear Dictionary")
    print("11. Exit")

# Initialize an empty dictionary
dictionary = {}

while True:
    display_menu()
    choice = input("Enter your choice (1-11): ")

    if choice == '1':
        dictionary = eval(input("Enter dictionary in key-value pairs (e.g., {'name': 'Alice', 'age': 25}): "))
        print("Dictionary created successfully!")

    elif choice == '2':
        key = input("Enter key: ")
        value = input("Enter value: ")
        dictionary[key] = value
        print("Key-Value pair added.") 

    elif choice == '3':
        key = input("Enter key to remove: ")
        if key in dictionary:
            dictionary.pop(key)
            print(f"Key '{key}' removed.")
        else:
            print("Key not found.")

    elif choice == '4':
        key = input("Enter key to update: ")
        if key in dictionary:
            value = input("Enter new value: ")
            dictionary[key] = value
            print(f"Key '{key}' updated.")
        else:
            print("Key not found.")

    elif choice == '5':
        print("Current Dictionary:", dictionary, "\n")

    elif choice == '6':
        key = input("Enter key to fetch value: ")
        print(f"Value: {dictionary.get(key, 'Key not found')}")

    elif choice == '7':
        print("All Keys:", list(dictionary.keys()))

    elif choice == '8':
        print("All Values:", list(dictionary.values()))

    elif choice == '9':
        print("All Key-Value Pairs:", list(dictionary.items()))

    elif choice == '10':
        dictionary.clear()
        print("Dictionary cleared.")
        
    elif choice == '11':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a valid option (1-11).")