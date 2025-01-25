#This a switch case of all cases of list in python
def display_menu():
    print("\nList Functions Menu:")
    print("1. Add an element")
    print("2. Insert an element at a specific index")
    print("3. Remove an element")
    print("4. Find the index of an element")
    print("5. Count occurrences of an element")
    print("6. Reverse the list")
    print("7. Sort the list")
    print("8. Display the list")
    print("9. Exit")

ls = ['nitish', 9, 10, 'aastha', 83, 10, 'tejaswini', 'keval', 'arvind', 2, 1, 84, 'kunal', 392, 'aaditee', 'arsh', 92, 13, 86]

while True:
    display_menu()
    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        element = input("Enter the element to add: ")
        ls.append(element)
        print(ls)

    elif choice == 2:
        index = int(input("Enter the index to insert at: "))
        element = input("Enter the element to insert: ")
        if 0 <= index <= len(ls):
            ls.insert(index, element)
            print(ls)
        else:
            print("Invalid index!")

    elif choice == 3:
        element = input("Enter the element to remove: ")
        if element in ls:
            ls.remove(element)
            print(f"{element} has been removed from the list.")
        else:
            print(f"{element} is not in the list.")

    elif choice == 4:
        element = input("Enter the element to find the index of: ")
        if element in ls:
            print(f"The index of {element} is {ls.index(element)}.")
        else:
            print(f"{element} is not in the list.")

    elif choice == 5:
        element = input("Enter the element to count: ")
        count = ls.count(element)
        print(f"{element} appears {count} time(s) in the list.")

    elif choice == 6:
        ls.reverse()
        print("The list has been reversed.")

    elif choice == 7:
        try:
            ls.sort()
            print("The list has been sorted in ascending order.")
        except TypeError:
            print("The list contains elements of different types and cannot be sorted.")

    elif choice == 8:
        print(ls)

    elif choice == 9:
        print("Exiting the loop.")
        break

    else:
        print("Invalid choice!")
