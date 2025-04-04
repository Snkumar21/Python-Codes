<<<<<<< HEAD
# Write menu driven python program to implement at least 5 built-in functions of list.
=======
# Example of menu driven python program to implement at least 5 built-in functions of list.

def menu():
    print("\n----- List Operations Menu -----")
    print("1. Append an element")
    print("2. Insert an element at a position")
    print("3. Remove an element")
    print("4. Pop an element")
    print("5. Sort the list")
    print("6. Display the list")
    print("7. Exit")

# Initialize an empty list
my_list = []

while True:
    menu()
    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        element = input("Enter the element to append: ")
        my_list.append(element)
        print("Updated List:", my_list)

    elif choice == 2:
        element = input("Enter the element to insert: ")
        index = int(input("Enter the position (index): "))
        if 0 <= index <= len(my_list):
            my_list.insert(index, element)
            print("Updated List:", my_list)
        else:
            print("Invalid index!")

    elif choice == 3:
        element = input("Enter the element to remove: ")
        if element in my_list:
            my_list.remove(element)
            print("Updated List:", my_list)
        else:
            print("Element not found!")

    elif choice == 4:
        if my_list:
            index = int(input("Enter the index to pop (default -1 for last element): ") or -1)
            if -len(my_list) <= index < len(my_list):
                removed = my_list.pop(index)
                print(f"Removed element: {removed}")
                print("Updated List:", my_list)
            else:
                print("Invalid index!")
        else:
            print("List is empty!")

    elif choice == 5:
        my_list.sort()
        print("Sorted List:", my_list)

    elif choice == 6:
        print("Current List:", my_list)

    elif choice == 7:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select from 1 to 7.")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
